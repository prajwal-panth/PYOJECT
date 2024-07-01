import subprocess
import os
import platform
import sys

fileName = "UNITCONV.bas"

def runQBasic():
    try:
        # Ensure the current working directory is set to the directory of this script
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(scriptDir)

        # Define path variables
        qbasicExecutable = os.path.join(scriptDir, "..", "QBasic", "qb45", "QB.EXE")  # QBasic executable (Pyoject\QBasic\qb45\QB.EXE)
        dosboxPath = os.path.join(scriptDir, "..", "QBasic", "DOSBox-0.74-3", "DOSBox.exe")  # DOSBox (Pyoject\QBasic\DOSBox-0.74-3\DOSBox.exe)
        qbasicRootDir = os.path.join(scriptDir, "..", "QBasic")  # QBasic root (Pyoject\QBasic)

        # Using 8.3 filename convention to avoid spaces or long names
        scriptDir83 = os.path.normpath(scriptDir).replace(" ", "~1")
        qbasicExecutable83 = os.path.normpath(qbasicExecutable).replace(" ", "~1")

        # Prepare DOSBox command for Windows
        dosboxCommand = [
            dosboxPath,
            "-c", f"mount c {qbasicRootDir}",  # Mount QBasic root directory as C: drive
            "-c", f"mount d {scriptDir83}",  # Mount current script directory as D: drive
            "-c", "c:",
            "-c", "cd \\qb45",
            "-c", f"{os.path.basename(qbasicExecutable83)} /RUN d:\\{fileName}",  # Use the 8.3 name for QB.EXE
            "-c", "exit"
        ]

        print(f"Executing command: {' '.join(dosboxCommand)}")

        # Run DOSBox with QBasic
        subprocess.call(dosboxCommand)

    except FileNotFoundError as fnfError:
        print(f"File not found error: {fnfError}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if platform.system() == "Windows":
        print("OS: Windows")
        print(f"Running {fileName}...")
        runQBasic()
        print("Program Exited Successfully.")
    else:
        print("OS not supported. This script only runs on Windows.")
        sys.exit(1)

if __name__ == "__main__":
    main()
