import subprocess
import os
import platform
import sys

def compileAndRun():
    dirName = "Projects"
    fileName = "CDTimer"
    javaFile = os.path.join(dirName, fileName + ".java")
    classFiles = [
        os.path.join(dirName, fileName + ".class"),
        os.path.join(dirName, fileName + "$1.class"),
        os.path.join(dirName, fileName + "$ThemeLabel.class"),
        os.path.join(dirName, fileName + "$ThemeListener.class"),
        os.path.join(dirName, fileName + "$TimerListener.class")
    ]

    # Check if source file exists
    if not os.path.isfile(javaFile):
        print(f"Error: {javaFile} file not found.")
        sys.exit(1)

    # Delete existing class files if they exist
    for classFile in classFiles:
        if os.path.isfile(classFile):
            os.remove(classFile)

    # Compile the source file
    compileCommand = ["javac", javaFile]
    subprocess.call(compileCommand)

    # Check if compilation was successful
    if not os.path.isfile(classFiles[0]):
        print(f"Error: Compilation failed, {classFiles[0]} not found.")
        sys.exit(1)

    # Run the compiled Java program with the package name
    runCommand = ["java", "-cp", ".", f"{dirName}.CDTimer"]
    subprocess.call(runCommand)

    # Delete all compiled .class files
    for classFile in classFiles:
        if os.path.isfile(classFile):
            os.remove(classFile)
            print(f"The class file '{classFile}' has been deleted.")
    print()

def main():
    osName = platform.system()
    print(f"Current Operating System: {osName}")
    compileAndRun()

if __name__ == "__main__":
    main()