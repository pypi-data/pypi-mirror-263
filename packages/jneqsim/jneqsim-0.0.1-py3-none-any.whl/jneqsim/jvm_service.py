import logging
from pathlib import Path

import jpype

if not jpype.isJVMStarted():
    neqsim_jar_path = str(Path(__file__).parent / "neqsim.jar")
    jpype.startJVM(classpath=[neqsim_jar_path], convertStrings=True)
    logging.info("JVM started")

    jvm_version = jpype.getJVMVersion()[0]
    if jvm_version < 11:
        raise OSError("Outdated Java version, Java 11 or higher is required")

import jpype.imports

# This is the java package, added to the python scope by "jpype.imports"
import neqsim  # noqa (ruff wants to remove this line, since it's not used)


logging.debug("NeqSim successfully imported")
