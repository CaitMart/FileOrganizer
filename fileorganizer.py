
# Online Python - IDE, Editor, Compiler, Interpreter
from pathlib import Path
import shutil

def printfiles(files):
    if files:
        print(f"Found {len(files)} file(s):")
        for file in files:
            return files
    else:
        print("No files found in folder")

def movePdfFiles(files):
    source_dest = " "
    destination = " "
    
    for file in files:
        #add source folder and the file from list to source_dest
        source_dest = " "
        shutil.move(source_dest, destination)
    return
    
#Documents file path
folder_path = Path("")
#gathers all pdf files in target directory with .pdf
pdf_files = list(folder_path.glob("*.pdf"))
printfiles(pdf_files)
movePdfFiles(pdf_files)


