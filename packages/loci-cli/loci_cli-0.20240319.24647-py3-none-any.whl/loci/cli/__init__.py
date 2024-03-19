import click
import rich
import requests
from rich.console import Console

from loci import (
    WORKING_FUNC,
    CURRENT_SUPPORTED_SERVER_VERSION,
    PAST_CLI_SUPPORT_MAP,
    LOCI_SERVER_GITLAB_PROJECT_ID,
    LOCI_CLI_GITLAB_PROJECT_ID,
)
from loci.errors import LociError
from loci.utils import loci_api_req_raw, get_env
from ..version import __version__

console = Console()


def _print_line(header, msg):
    rich.print(header, msg)


def print_info(msg):
    _print_line("[[bold blue]INFO[/bold blue]]", msg)


def print_success(msg):
    _print_line("[[bold green]SUCCESS[/bold green]]", msg)


def print_warning(msg):
    _print_line("[[bold yellow]WARNING[/bold yellow]]", msg)


def print_error(msg, fatal=True):
    _print_line("[[bold red]ERROR[/bold red]]", msg)

    if fatal:
        quit(-1)


def print_version(prog_name, version):
    rich.print("[bold]%s[/bold] v%s" % (prog_name, version))


def working():
    return console.status("Working...")


def print_loci_error_msg(exception: LociError, fatal: bool = True):
    if not isinstance(exception, LociError):
        print_error(
            "A non-Loci note error was passed to handle_loci_error. This should not happen.",
            fatal=True,
        )
        return
    print_error(exception.default_msg, fatal=fatal)


def set_global_working_func():
    global WORKING_FUNC
    WORKING_FUNC = working


# From https://stackoverflow.com/a/56043912
def default_from_context(default_name):
    class OptionDefaultFromContext(click.Option):
        def get_default(self, ctx, call: bool = True):
            if ctx.obj is None:
                return None
            self.default = ctx.obj[default_name]
            return super(OptionDefaultFromContext, self).get_default(ctx, call=call)

    return OptionDefaultFromContext


def check_for_updates():

    # Check for tests being run, and don't do anything if they are.
    env = get_env()
    if env == "TEST":
        return

    # Get the server version
    r = loci_api_req_raw("/", method="GET", authd=False)
    current_server_version = r["version"]

    # Get the CLI version
    current_cli_version = __version__

    if current_server_version == "DEVELOPMENT" and current_cli_version == "DEVELOPMENT":
        # We're running a development server and CLI, so just warn the user and continue on.
        print_info("Development version of Loci server and client detected.")
        return

    # Get the latest releases for both the server and the CLI
    latest_server_version = None
    try:
        timeout = 5000
        url = f"https://gitlab.com/api/v4/projects/{LOCI_SERVER_GITLAB_PROJECT_ID}/releases?sort=desc"
        if WORKING_FUNC:
            # Show the loading animation in console
            with WORKING_FUNC():
                r = requests.request(
                    "GET",
                    url,
                    timeout=timeout,
                )
        else:
            # Dont' show a loading animation, just wait until the call returns.
            r = requests.request(
                "GET",
                url,
                timeout=timeout,
            )

        if r.ok:
            res = r.json()
            latest_server_version = res[0]["tag_name"]
        else:
            # Raise a generic exception if the request failed.
            raise requests.HTTPError()
    except:
        print_warning(
            "Failed to check for updates to the Loci Server. This may be due to a network issue or GitLab being down. Check manually at https://gitlab.com/loci-notes/loci-server/-/releases."
        )

    latest_cli_version = None
    try:
        timeout = 5000
        url = f"https://gitlab.com/api/v4/projects/{LOCI_CLI_GITLAB_PROJECT_ID}/releases?sort=desc"
        if WORKING_FUNC:
            # Show the loading animation in console
            with WORKING_FUNC():
                r = requests.request(
                    "GET",
                    url,
                    timeout=timeout,
                )
        else:
            # Dont' show a loading animation, just wait until the call returns.
            r = requests.request(
                "GET",
                url,
                timeout=timeout,
            )

        if r.ok:
            res = r.json()
            latest_cli_version = res[0]["tag_name"]
        else:
            # Raise a generic exception if the request failed.
            raise requests.HTTPError()
    except:
        print_warning(
            "Failed to check for updates to the Loci CLI. This may be due to a network issue or GitLab being down. Check manually at https://gitlab.com/loci-notes/loci-cli/-/releases."
        )

    if current_server_version == "DEVELOPMENT":
        # Here, the server is reporting as a development version, but not the CLI. This means a prod version of the CLI and an unreleased version of the server are being used. This is fine if the server is being actively developed, but otherwise probably not.
        print_warning(
            "You are running an unreleased version of Loci server. This is not recommended for non-development use."
        )
    elif (
        latest_server_version is not None
        and latest_server_version != current_server_version
    ):
        print_info(
            "A new version of Loci server is available. You are running [bold]v"
            + current_server_version
            + "[/bold], and the latest is [bold]"
            + latest_server_version
            + "[/bold]. Check the release notes for compatability at https://gitlab.com/loci-notes/loci-server/-/releases."
        )

    if (
        current_cli_version != "DEVELOPMENT"
        and current_cli_version != CURRENT_SUPPORTED_SERVER_VERSION
    ):
        print_warning(
            "The Loci server and CLI versions do not match, and this may result in unexpected behavior or errors."
        )
        try:
            correct_cli_version = PAST_CLI_SUPPORT_MAP[current_server_version][0]
            print_info(
                f"Use the correct CLI version with [bold]pip3 install loci-cli=={correct_cli_version}[/bold]."
            )
        except KeyError:
            print_warning(
                f"No supported CLI version was found. You may be using an unsupported version of the server."
            )
