from pathlib import Path
import subprocess
import sys
import os

current_directory = Path(__file__).parent.resolve()
paxtools_jar = current_directory / 'paxtools' / 'paxtools-console' / 'target' / 'paxtools.jar'

def main() -> int:
    default_java = "java"
    java_path = (os.environ['JAVA_HOME'].strip() if 'JAVA_HOME' in os.environ else default_java) or default_java

    output = subprocess.run([java_path, '-jar', str(paxtools_jar)] + sys.argv[1:])
    return output.returncode
