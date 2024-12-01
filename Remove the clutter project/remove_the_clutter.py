import os

folder="./pythonprojects/Remove the clutter project"
files=os.listdir(folder)
i=1
for file in files:
    if (file.endswith(".png")):
        os.rename(f"./pythonprojects/Remove the clutter project/{file}",f"./pythonprojects/Remove the clutter project/{i}.png")
        i=i+1