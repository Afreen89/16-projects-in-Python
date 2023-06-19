from pathlib import Path, PureWindowsPath

folder = Path("C:/Users/arshh/OneDrive/Desktop/PycharmProjects/pythonProject/Day6/test.txt")

windows_path = PureWindowsPath(folder)

print(windows_path)

# print(folder.read_text())
# print(folder.name)
# print(folder.suffix)
# print(folder.stem)

# if not folder.exists():
#     print("This file doesnt exist")
# else:
#     print("Yes, it exists")

