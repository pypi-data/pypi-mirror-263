import logging
import json
import shlex
from subprocess import (
    Popen,
    PIPE,
    CalledProcessError,
    check_call,
    DEVNULL
)
from typing import Iterable, Dict, Any, List, Optional

logger = logging.getLogger(__name__)


def run_process_quiet(command: str, env: Optional[Dict[str, str]] = None):
    check_call(shlex.split(command), stdout=DEVNULL, stderr=DEVNULL, env=env)


def run_process_stream_result(command: str, env: Optional[Dict[str, str]] = None) -> Iterable[str]:
    """
    Run subprocess that streams stdout and stderr to handler functions
    :param command: the command line string to be executed
    :return: a generator of each returned line from STDOUT
    """
    err = None
    with Popen(shlex.split(command), stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True, env=env, encoding='utf-8') as p:
        if p.stdout:
            for line in p.stdout:
                if line:
                    yield line
        if p.stderr:
            err = p.stderr.read()
    if p.returncode != 0 and err:
        for line in err.split('\n'):
            logger.error(line)
        raise CalledProcessError(p.returncode, p.args, stderr=err)


def process_output_as_json(process_output: Iterable[str]) -> List[Dict[str, Any]]:
    """
    Convert the results of a subprocess to a json generator
    :param process_output: output from running `run_process(...)`
    :return:
    """
    return [json.loads(output) for output in process_output]


def run_process(command: str, env: Optional[Dict[str, str]] = None) -> List[str]:
    return list(run_process_stream_result(command, env))


def run_process_single_result(command: str, env: Optional[Dict[str, str]] = None) -> str:
    return run_process(command, env)[0]

