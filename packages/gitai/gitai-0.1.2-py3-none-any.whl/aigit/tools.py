from langchain.tools import BaseTool, tool
from typing import Union, Dict, Tuple
import subprocess


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


class CommitDetailsTool(BaseTool):
	name = "Commit-Details-Tool"
	description = "Get detailed information to help you write a commit message."

	def _to_args_and_kwargs(self, tool_input: Union[str, Dict]) -> Tuple[Tuple, Dict]:
		return (), {}

	def _run(self):
		cached = True
		additional_notes = ""
		last_commit_messages = get_last_commit_messages()
		files_changed_summary = get_files_changed_summary()
		detailed_diff = get_detailed_diff(cached)
		detailed_context = DETAILED_CONTEXT_TEMPLATE.format(
			last_commit_messages=last_commit_messages,
			files_changed_summary=files_changed_summary,
			detailed_diff=detailed_diff,
			additional_notes=additional_notes,
		)
		return detailed_context
	
	async def _arun(self):
		return self._run()


class PRDetailsTool(BaseTool):
	name = "PR-Details-Tool"
	description = "Get detailed information to help you write a pull request message."

	def _to_args_and_kwargs(self, tool_input: Union[str, Dict]) -> Tuple[Tuple, Dict]:
		return (), {}

	def _run(self):
		cached = False
		additional_notes = get_additional_notes()
		last_commit_messages = get_last_commit_messages()
		files_changed_summary = get_files_changed_summary()
		detailed_diff = get_detailed_diff(cached)
		detailed_context = DETAILED_CONTEXT_TEMPLATE.format(
			last_commit_messages=last_commit_messages,
			files_changed_summary=files_changed_summary,
			detailed_diff=detailed_diff,
			additional_notes=additional_notes,
		)
		return detailed_context
	
	async def _arun(self):
		return self._run()


class CreateCommitTool(BaseTool):
	name = "Create-Commit-Tool"
	description = "Create a commit with the given message."

	def _run(self, message: str):
		subprocess.run(['git', 'add', '.'])
		subprocess.run(['git', 'commit', '-m', message])
		return f"Committed changes with message: {message}"
	
	async def _arun(self, message: str):
		return self._run(message)

class CreatePRTool(BaseTool):
	name = "Create-PR-Tool"
	description = "Create a pull request with the given message."

	def _run(self, message: str):
		subprocess.run(['hub', 'pull-request', '-m', message])
		return f"Created PR with message: {message}"
	
	async def _arun(self, message: str):
		return self._run(message)


@tool
def get_details_for_commit_message() -> str:
	"""Get detailed information to help you write a commit message."""
	cached = True
	additional_notes = ""
	last_commit_messages = get_last_commit_messages()
	files_changed_summary = get_files_changed_summary()
	detailed_diff = get_detailed_diff(cached)
	detailed_context = DETAILED_CONTEXT_TEMPLATE.format(
    	last_commit_messages=last_commit_messages,
    	files_changed_summary=files_changed_summary,
    	detailed_diff=detailed_diff,
		additional_notes=additional_notes,
    )
	return detailed_context


@tool
def get_details_for_pr_message() -> str:
	"""Get detailed information to help you write a pull request message."""
	cached = False
	additional_notes = get_additional_notes()
	last_commit_messages = get_last_commit_messages()
	files_changed_summary = get_files_changed_summary()
	detailed_diff = get_detailed_diff(cached)
	detailed_context = DETAILED_CONTEXT_TEMPLATE.format(
		last_commit_messages=last_commit_messages,
		files_changed_summary=files_changed_summary,
		detailed_diff=detailed_diff,
		additional_notes=additional_notes,
	)
	return detailed_context


@tool
def create_commit(message: str) -> str:
	"""Create a commit with the given message."""
	subprocess.run(['git', 'add', '.'])
	subprocess.run(['git', 'commit', '-m', message])
	return f"Committed changes with message: {message}"

@tool
def create_pr(message: str) -> str:
	"""Create a pull request with the given message."""
	subprocess.run(['hub', 'pull-request', '-m', message])
	return f"Created PR with message: {message}"