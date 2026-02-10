from pathlib import Path
import subprocess
import sys
import os
from typing import IO, Any, Optional

current_directory = Path(__file__).parent.resolve()
paxtools_jar = current_directory / 'paxtools' / 'paxtools-console' / 'target' / 'paxtools.jar'

def run(
        args: Optional[list[str]] = None,
        stdout: Optional[int | IO[Any]] = None,
        stderr: Optional[int | IO[Any]] = None
    ) -> subprocess.CompletedProcess[bytes]:
    if not args: args = sys.argv[1:]

    default_java = "java"
    java_path = (Path(os.environ['JAVA_HOME'].strip(), 'bin', 'java') if 'JAVA_HOME' in os.environ else default_java) or default_java

    output = subprocess.run(
        [java_path, '-jar', str(paxtools_jar)] + args,
        stdout=stdout,
        stderr=stderr
    )
    return output


def main(args: Optional[list[str]] = None) -> int:
    return run(args).returncode
