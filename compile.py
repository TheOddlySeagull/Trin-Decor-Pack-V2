import subprocess
import os
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Compile Trin Decor Pack")
parser.add_argument("--skip-1165", action="store_true", help="Skip compiling for 1.16.5")
args = parser.parse_args()

# run py 1-12-2_1-16-5_ID_transformer.py --reverse
subprocess.run(["py", ".\\1-12-2_1-16-5_ID_transformer.py", "--reverse"])
# run gradlew buildForge1122
os.system("gradlew buildForge1122")
# run py 1-12-2_1-16-5_ID_transformer.py
subprocess.run(["py", ".\\1-12-2_1-16-5_ID_transformer.py"])
# run gradlew buildForge1165 if not skipped
if not args.skip_1165:
    os.system("gradlew buildForge1165")
# run py 1-12-2_1-16-5_ID_transformer.py --reverse
subprocess.run(["py", ".\\1-12-2_1-16-5_ID_transformer.py", "--reverse"])
