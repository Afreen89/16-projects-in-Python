import os
import shutil
import send2trash

# print(os.getcwd())
#
# file = open("course.txt", "w")
# file.write("test text")
# file.close()
#
# print(os.listdir())

# shutil.move("course.txt", "C:\\Users\\arshh\\OneDrive\\Desktop\\PycharmProjects\\pythonProject")
# send2trash.send2trash("course.txt")

path = "C:\\Users\\arshh\\OneDrive\\Desktop\\PycharmProjects\\pythonProject"

for folder, subfolder, file in os.walk(path):
    print(f"In folder: {folder}")
    print(f"subfolders are: ")
    for sub in subfolder:
        print(f"\t{sub}")
    print("Files are: ")
    for fi in file:
        if fi.startswith("Python"):
            print(f"\t{fi}")
    print("\t")