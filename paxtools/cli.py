from pathlib import Path
import subprocess
import sys
import os
from typing import IO, Any, Optional

from paxtools.util import optional

current_directory = Path(__file__).parent.resolve()
paxtools_jar = current_directory / 'paxtools' / 'paxtools-console' / 'target' / 'paxtools.jar'

def run(
        args: Optional[list[str]] = None,
        stdout: Optional[int | IO[Any]] = None,
        stderr: Optional[int | IO[Any]] = None,

        denylist: Optional[os.PathLike | str] = None
    ) -> subprocess.CompletedProcess[bytes]:
    """
    Runs the Paxtools main jar file using `java` (or the java bin under JAVA_HOME if applicable).

    @param args: the extra arguments to run
    @param stdout: the standard output stream to use
    @param stderr: the standard error stream to use
    @param denylist: the list of [usually small molecules] to filter out, passed in as the JVM configuration option `Dpaxtools.pattern.blacklist`.
    """
    if not args: args = sys.argv[1:]

    default_java = "java"
    java_path = (Path(os.environ['JAVA_HOME'].strip(), 'bin', 'java') if 'JAVA_HOME' in os.environ else default_java) or default_java

    output = subprocess.run(
        [
            java_path,
            *optional(f'-Dpaxtools.pattern.blacklist={denylist}', denylist is not None),
            '-jar', str(paxtools_jar)
        ] + args,
        stdout=stdout,
        stderr=stderr
    )
    return output


def main(args: Optional[list[str]] = None) -> int:
    return run(args).returncode
