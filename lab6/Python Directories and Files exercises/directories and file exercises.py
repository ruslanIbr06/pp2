import os

#1 Write a Python program to list only directories, files and all directories, files in a specified path.
def listContents(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All contents:", os.listdir(path))

listContents(".")
'''
Directories: ['.venv', '.idea']
Files: ['main.py', 'example.txt', 'directories and file exercises.py', 'output.txt', 'A.txt', 'B.txt', 'C.txt', 'D.txt', 'E.txt', 'F.txt', 'G.txt', 'H.txt', 'I.txt', 'J.txt', 'K.txt', 'L.txt', 'M.txt', 'N.txt', 'O.txt', 'P.txt', 'Q.txt', 'R.txt', 'S.txt', 'T.txt', 'U.txt', 'V.txt', 'W.txt', 'X.txt', 'Y.txt', 'Z.txt', 'source.txt', 'copy.txt']
All contents: ['.venv', 'main.py', '.idea', 'example.txt', 'directories and file exercises.py', 'output.txt', 'A.txt', 'B.txt', 'C.txt', 'D.txt', 'E.txt', 'F.txt', 'G.txt', 'H.txt', 'I.txt', 'J.txt', 'K.txt', 'L.txt', 'M.txt', 'N.txt', 'O.txt', 'P.txt', 'Q.txt', 'R.txt', 'S.txt', 'T.txt', 'U.txt', 'V.txt', 'W.txt', 'X.txt', 'Y.txt', 'Z.txt', 'source.txt', 'copy.txt']
'''

#2 Write a Python program to check for access to a specified path.
def checkAccess(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

checkAccess(".")
'''
Exists: True
Readable: True
Writable: True
Executable: True
'''


#3 Write a Python program to test whether a given path exists or not.
def pathInfo(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")

pathInfo("./example.txt")
'''
Filename: example.txt
Directory: .Filename: example.txt
Directory: .
'''

#4 Write a Python program to count the number of lines in a text file.
def countLines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

print(countLines("example.txt"))
# 7

#5 Write a Python program to write a list to a file.
def writeListToFile(filename, lst):
    with open(filename, 'w') as f:
        f.writelines("\n".join(lst))

writeListToFile("output.txt", ["Hello", "World"])


#6 Write a Python program to generate 26 text files named A.txt, B.txt, ..., Z.txt
def generateFiles():
    for char in range(65, 91):
        with open(f"{chr(char)}.txt", 'w') as f:
            f.write(f"{chr(char)}.txt")

generateFiles()


#7 Write a Python program to copy the contents of a file to another file without using shutil.
def copyFile(source, copy):
    with open(source, 'r') as f_source, open(copy, 'w') as f_copy:
        f_copy.write(f_source.read())

copyFile("source.txt", "copy.txt")


#8 Write a Python program to delete file by specified path.
def deleteFile(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("File can not be deleted")

deleteFile("deleteme.txt")
# File deleted