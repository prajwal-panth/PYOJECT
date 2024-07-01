import subprocess
import os
import platform
import sys

def compileNrun():
    compiler = "gcc" 
    dirName = "Projects"
    #file1 and file2 are source files
    file1 = os.path.join(f"{dirName}", "Calculator.c")
    file2 = os.path.join(f"{dirName}", "decoration.c")
    target = "calc"

    # Check if source files exist
    for file in [file1, file2]:
        if not os.path.isfile(file):
            print(f"Error: {file} file not found in the current directory.")
            sys.exit(1)

    # Compile the source files
    compile_command = [compiler, file1, file2, "-o", target]
    subprocess.call(compile_command)

    # Check if compilation was successful and set the correct executable name
    if os.name == 'nt':  # Windows
        executable = target + ".exe"
    elif os.name == 'posix':  # Unix-like systems (Linux, macOS)
        executable = target
    else:
        print(f"Unsupported operating system: {os.name}")
        sys.exit(1)

    if not os.path.isfile(executable):
        print(f"Error: Compilation failed, {executable} not found.")
        sys.exit(1)

    # Run the executable
    if os.name == 'nt':
        subprocess.call(executable)
    else:
        subprocess.call('./' + executable)

    # Delete the executable
    if os.path.isfile(executable):
        os.remove(executable)
        print(f"The executable file '{executable}' has been deleted.\n")


def main():
    os_name = platform.system()
    print(f"Current Operating System: {os_name}")
    compileNrun()

if __name__ == "__main__":
    main()
