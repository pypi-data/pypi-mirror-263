import time
import regex
from typing import Annotated, Optional

import httpx
import typer

from gitoptim.schemas.workflows import AnalyseLogsSchema
from gitoptim.services.gitlab import GitlabAPI
from gitoptim.utils.cli import console, error_console
from gitoptim.utils.tag import EndTag, StartTag, TagFactory

PROMPT_TEMPLATE = (
    "{input}\n\nAbove are displayed logs from Gitlab CI/CD job. Analyse them. If there are no errors and warning "
    "don't do anything. If there are any errors or warning summarize them. If you know how to fix some "
    "errors/warnings or fix is described in the logs include it in your answer. Group errors, warnings and fixes by "
    "command. Commands are prefixed with $ sign.")


def extract_relevant_logs(api: GitlabAPI, after_last_command: bool, last_tag: bool, tag_name: str):
    retries = 0
    logs = api.get_job_logs()
    start_tag = TagFactory.create_start_tag()
    start_tag_index = logs.rfind(str(start_tag))

    while start_tag_index == -1:
        retries += 1

        if retries > 18:
            error_console.print("Cannot synchronize with Gitlab logs")
            raise typer.Exit(code=1)

        time.sleep(10)
        logs = api.get_job_logs()
        start_tag_index = logs.rfind(str(start_tag))

    logs_before_command = logs[:start_tag_index]
    command_echo_index = logs_before_command.rfind("$ gitoptim")

    if command_echo_index != -1:
        logs_before_command = logs_before_command[:command_echo_index]

    if after_last_command:
        return extract_after_last_command(logs_before_command)
    elif last_tag:
        return extract_tagged(logs_before_command)
    elif tag_name is not None:
        return extract_tagged(logs_before_command, tag_name)

    return logs_before_command


def extract_tagged(logs: str, name: Optional[str] = None):
    pattern = regex.compile(StartTag.generate_regex_pattern(name), regex.REVERSE)
    match = pattern.search(logs)

    if match is None:
        error_console.print(f"Tag with name: {name} not found." if name is not None else "No tags found.")
        raise typer.Exit(code=1)

    start_index = match.end()

    pattern = regex.compile(EndTag.generate_regex_pattern(name), regex.REVERSE)
    match = pattern.search(logs)
    end_index = match.end() if match is not None else len(logs)

    return logs[start_index:end_index]


def extract_after_last_command(logs):
    pattern = regex.compile(EndTag.generate_regex_pattern(), regex.REVERSE)
    match = pattern.search(logs)
    return logs if match is None else logs[match.end():]


def run_workflow_task(logs: str):
    headers = {'Authorization': "Basic MjkzOllyV1NZd0NQZEotQTJNYXRpNUFZc25xWDJsVGxoSlE0"}
    timeout = httpx.Timeout(None, connect=None, read=None, write=None)

    data = AnalyseLogsSchema(input=PROMPT_TEMPLATE.format(input=logs))

    r = httpx.post(
        "https://autumn8functions.default.aws.autumn8.ai/inference/4373e4e3-2502-4f28-b96a-125c2bc6faeb%2B293"
        "%2Bq5k6v6egxqi65gt1ojg9%2Bg5-2xlarge%2Bmar",
        json=data.model_dump(), headers=headers, timeout=timeout)

    console.print(r.json()["message"]["output"])


def validate_name(name: Optional[str]):
    if name is not None and len(name) == 0:
        error_console.print("Name cannot be empty.")
        raise typer.Exit(code=1)

    elif name is not None and name.isalnum() is False:
        error_console.print("Name can only contain letters and numbers.")
        raise typer.Exit(code=1)

    return name


def validate(after_last_command, last_tag, name):
    if [after_last_command is True, last_tag is True, name is not None].count(True) > 1:
        error_console.print("Options to this command are mutually exclusive.")
        raise typer.Exit(code=1)


def command(
        after_last_command: Annotated[
            bool, typer.Option("--after-last-command",
                               help="Include only the logs that appear after the last execution of any `gitoptim` "
                                    "command. Includes all logs if `gitoptim tag` was never used.")] = False,
        last_tag: Annotated[
            bool, typer.Option("--last-tag",
                               help="Include only the logs that appear after the last execution of any `gitoptim` "
                                    "command. Includes all logs if `gitoptim tag` was never used.")] = False,
        name: Annotated[str, typer.Option(help="name", callback=validate_name)] = None,
        # analyse_logs_trigger_id: Annotated[
        #     int, typer.Option(help="Needs to be provided if not set in environment variables.")] = None,
):
    """
    Analyse logs from the current job.

    Includes only the logs that appear before execution of this command.

    Example:
    $ npm install
    $ gitoptim analyse
    $ npm run test
    $ gitoptim analyse logs --after-last-command
    $ gitoptim analyse

    In the example above first `gitoptim` command will analyse logs from `npm install`. Second `gitoptim` command will
    analyse only the logs from `npm run test`. Last command will analyse all the logs.

    See:
    `gitoptim tag`
    """

    validate(after_last_command, last_tag, name)

    console.print("Running job logs analysis command")
    gitlab_api = GitlabAPI()

    console.print("Synchronizing with Gitlab logs... (it may take up to 3 minutes)")
    relevant_logs = extract_relevant_logs(gitlab_api, after_last_command, last_tag, name)
    console.print(relevant_logs)

    # console.print("Starting analysis...")
    # run_workflow_task(relevant_logs)
    #
    # console.print("Logs analysis started. See [url] for more details.")
