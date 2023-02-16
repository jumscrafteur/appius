import os
import shutil

currentDir = os.path.dirname(__file__)

try:
    assetPath = os.path.join(currentDir, "C3_sprites", "C3")
    fileList = os.listdir(assetPath)
except FileNotFoundError as err:
    print("Fichiers du jeu non trouvé dans le répertoire :")
    print(err.filename)
    exit(1)


for fileName in fileList:
    if ".png" not in fileName:
        continue

    (*folders, name) = fileName.split("_")

    for i, folder in enumerate(folders):
        currentAssetFolder = os.listdir(os.path.join(currentDir, *folders[:i]))
        if folder not in currentAssetFolder:
            os.mkdir(os.path.join(currentDir, *folders[: i + 1]))

    shutil.copy(
        os.path.join(assetPath, fileName), os.path.join(currentDir, *folders, name)
    )
