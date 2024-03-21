import os
import subprocess
import json
import click
import fnmatch
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts.chat import (
	ChatPromptTemplate,
	HumanMessagePromptTemplate,
	SystemMessagePromptTemplate,
)
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
import tiktoken
from langchain.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveJsonSplitter, CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.chains import RefineDocumentsChain, LLMChain
from langchain_core.prompts import PromptTemplate
import sys
from datetime import datetime
from langchain_core.callbacks import BaseCallbackHandler
from typing import Any, Union
import time

load_dotenv()



COMMIT_MESSAGE_TEMPLATE = """
You are a software developer. You have made some changes to the codebase. Please provide a commit message for the following changes (Before running any tools, make sure to ask the user for permission to run them):
"""

PR_MESSAGE_TEMPLATE = """
You are a software developer. You have made some changes to the codebase and are preparing to merge them into the main branch. Please provide a detailed pull request message for the following changes (Before running any tools, make sure to ask the user for permission to run them):
"""

README_TEMPLATE = """
You are a software developer. You have made some changes to the codebase. Please review the provided files (including the current version of the README) and generate a comprehensive and updated README file. (Before running any tools, make sure to ask the user for permission to run them):
"""

README_CONTEXT_TEMPLATE = """

Project files:
{project_files}
"""

DETAILED_CONTEXT_TEMPLATE = """
Last few commit messages:
{last_commit_messages}

Files changed (summary):
{files_changed_summary}

Detailed diff of changes:
{detailed_diff}

Additional notes:
{additional_notes}
"""

class CreateCommitMessage(BaseModel):
	commit_message: str = Field(
		..., description="The commit message for the changes made."
	)

class CreatePRMessage(BaseModel):
	pr_message: str = Field(
		..., description="The pull request message for the changes made."
	)

def get_last_commit_messages(n=3):
	return subprocess.run(['git', 'log', f'-{n}', '--pretty=%B'], capture_output=True, text=True).stdout.strip()

def get_files_changed_summary():
	return subprocess.run(['git', 'diff', '--cached', '--stat'], capture_output=True, text=True).stdout.strip()

def get_detailed_diff(cached=True):
	cmd = ['git', 'diff', '--cached'] if cached else ['git', 'diff']
	return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()

def get_additional_notes():
	# Placeholder for any additional notes you might want to include for PRs
	return ""

def get_current_readme():
	with open('README.md', 'r') as f:
		return f.read()

def parse_gitignore(gitignore_path):
	"""Parse .gitignore and return a list of patterns to ignore."""
	ignore_patterns = []
	if os.path.exists(gitignore_path):
		with open(gitignore_path, 'r') as f:
			for line in f:
				stripped_line = line.strip()
				if stripped_line and not stripped_line.startswith('#'):
					ignore_patterns.append(stripped_line)
	return ignore_patterns

def should_ignore(path, ignore_patterns):
	"""Determine if the file should be ignored based on .gitignore patterns."""
	for pattern in ignore_patterns:
		if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
			return True
	return False

def generate_files_dict(start_path):
	"""Generate the dictionary of file paths and contents."""
	files_dict = {}
	files_under_source_control = subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.strip().split('\n')
	for file in files_under_source_control:
		try:
			with open(file, 'r') as f:
				files_dict[file] = f.read()
		except UnicodeDecodeError:
			pass
	return files_dict
	# gitignore_path = os.path.join(start_path, '.gitignore')
	# ignore_patterns = parse_gitignore(gitignore_path)

	# files_dict = {}
	# for root, dirs, files in os.walk(start_path):
	# 	# Filter out ignored directories
	# 	dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]
	# 	for file in files:
	# 		relative_path = os.path.relpath(os.path.join(root, file), start_path)
	# 		if relative_path.startswith('.'):
	# 			continue
	# 		if not should_ignore(relative_path, ignore_patterns):
	# 			try:
	# 				with open(os.path.join(root, file), 'r') as f:
	# 					files_dict[relative_path] = f.read()
	# 			except UnicodeDecodeError:
	# 				pass
	# return files_dict

def get_project_files():
	return json.dumps(generate_files_dict(os.getcwd()))


def get_llm(llm):
	if llm == 'openai':
		return ChatOpenAI(model="gpt-4-0125-preview")
	else:
		raise ValueError("Language model not supported.")

def get_refine_chain(llm):
	# document_prompt = PromptTemplate(
	# 	input_variables=["page_content"],
	# 	template="{page_content}"
	# )
	# document_variable_name = "context"
	# # The prompt here should take as an input variable the
	# # `document_variable_name`
	# prompt = PromptTemplate.from_template(
	# 	"Summarize this content: {context}"
	# )
	# initial_llm_chain = LLMChain(llm=llm, prompt=prompt)
	# initial_response_name = "prev_response"
	# # The prompt here should take as an input variable the
	# # `document_variable_name` as well as `initial_response_name`
	# prompt_refine = PromptTemplate.from_template(
	# 	"Here's your first summary: {prev_response}. "
	# 	"Now add to it based on the following context: {context}"
	# )
	# refine_llm_chain = LLMChain(llm=llm, prompt=prompt_refine)
	# chain = RefineDocumentsChain(
	# 	initial_llm_chain=initial_llm_chain,
	# 	refine_llm_chain=refine_llm_chain,
	# 	document_prompt=document_prompt,
	# 	document_variable_name=document_variable_name,
	# 	initial_response_name=initial_response_name,
	# )
	prompt_template = """Write a concise summary of the following:
	{text}
	CONCISE SUMMARY:"""
	prompt = PromptTemplate.from_template(prompt_template)

	refine_template = (
		"Your job is to produce a final summary\n"
		"We have provided an existing summary up to a certain point: {existing_answer}\n"
		"We have the opportunity to refine the existing summary"
		"(only if needed) with some more context below.\n"
		"------------\n"
		"{text}\n"
		"------------\n"
		"Given the new context, refine the original summary in Italian"
		"If the context isn't useful, return the original summary."
	)
	refine_prompt = PromptTemplate.from_template(refine_template)
	class MyCustomHandler(BaseCallbackHandler):
		def on_chain_error(
			self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
		) -> Any:
			# sleep for a minute to avoid rate limiting
			time.sleep(60)
			print("Sleeping for a minute to avoid rate limiting")
			# pick up where we left off
			return True
	
	chain = load_summarize_chain(
		llm=llm,
		chain_type="refine",
		question_prompt=prompt,
		refine_prompt=refine_prompt,
		return_intermediate_steps=True,
		input_key="input_documents",
		output_key="output_text",
		callbacks=[MyCustomHandler()],
	)

	return chain

def get_split_text_as_docs(text):
	text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
		encoding_name="cl100k_base", chunk_size=80000, chunk_overlap=0
	)
	return text_splitter.create_documents([text])

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
	"""Returns the number of tokens in a text string."""
	encoding = tiktoken.get_encoding(encoding_name)
	num_tokens = len(encoding.encode(string))
	return num_tokens


@click.command()
@click.option('--mode', type=click.Choice(['commit', 'pr', 'readme']), default='commit', required=True)
@click.option('--llm', default='openai', help='Which language model to use. Default is openai.')
def main(mode, llm):
	llm = get_llm(llm)
	if mode == 'readme':
		project_files_content = README_CONTEXT_TEMPLATE.format(
			project_files=get_project_files(),
		)
		# replace curly braces with double curly braces to escape them
		project_files_content = project_files_content.replace("{", "{{").replace("}", "}}")
		refine_chain = get_refine_chain(llm)
		split_docs = get_split_text_as_docs(project_files_content)
		final_content = refine_chain.invoke(
			{"input_documents": split_docs},
			return_only_outputs=True
		)
		final_content = final_content["output_text"]

		chat_prompt = ChatPromptTemplate.from_messages(
			[
				("system", README_TEMPLATE),
				("human", final_content),
			]
		)
		print()
		response = llm.invoke(
			chat_prompt.format_prompt(
				text=project_files_content
			).to_messages()
		)
		print(response.content)
		return

	# llm_with_tools = llm.bind_tools(
	# 	[CreateCommitMessage, CreatePRMessage],
	# )
	additional_notes = ""
	cached = True if mode == 'commit' else False

	# Gather detailed information
	last_commit_messages = get_last_commit_messages()
	files_changed_summary = get_files_changed_summary()
	detailed_diff = get_detailed_diff(cached)
    
	if mode == 'pr':
		additional_notes = get_additional_notes()
    
    # Prepare the detailed context
	detailed_context = DETAILED_CONTEXT_TEMPLATE.format(
    	last_commit_messages=last_commit_messages,
    	files_changed_summary=files_changed_summary,
    	detailed_diff=detailed_diff,
		additional_notes=additional_notes,
    )
	# replace curly braces with double curly braces to escape them
	detailed_context = detailed_context.replace("{", "{{").replace("}", "}}")
    
	template = COMMIT_MESSAGE_TEMPLATE if mode == 'commit' else PR_MESSAGE_TEMPLATE

	refine_chain = get_refine_chain(llm)
	split_docs = get_split_text_as_docs(detailed_context)
	final_content = refine_chain.invoke(
		{"input_documents": split_docs},
		return_only_outputs=True
	)
	final_content = final_content["output_text"]
	chat_prompt = ChatPromptTemplate.from_messages(
    	[
        	("system", template),
        	("human", final_content),
    	]
    )
    
	response = llm.invoke(
		chat_prompt.format_prompt(
			text=final_content
		).to_messages()
	)
	print(response.content)


if __name__ == '__main__':
	main()
