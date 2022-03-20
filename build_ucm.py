
# Major spaghetti code down here,
# Viewer discretion is advised.

import os

# Get starting path
startingPath = os.getcwd()

# Clone board overlays
os.system("git clone https://chromium.googlesource.com/chromiumos/overlays/board-overlays --depth 1")

# Change directory to board overlays
os.chdir("board-overlays")

# Loop through overlays
overlayList = []
files = os.listdir()
for filename in files:
    if "overlay" in filename:
        overlayList.append(filename.replace("overlay-", ""))
for overlay in overlayList:

    legacy = False

    try:
        os.chdir(f"overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/")
    except FileNotFoundError:
        print("Directory could not be found:")
        print(f"{os.getcwd()}/overlay-{overlay}/chromeos-base/chromeos-bsp-{overlay}/files/")
        print(f"Skipping {overlay}\n")
        continue
    boards = os.listdir()
    for board in boards:
        startingBoardPath = os.getcwd()

        try:
            if "audio-config" in boards:
                legacy = True
                os.chdir(f"audio-config/ucm-config")
            elif not os.path.isdir(f"{board}/audio/ucm-config"):
                os.chdir(f"{board}/audio-5_4/ucm-config")
            else:
                os.chdir(f"{board}/audio/ucm-config")
        except:
            print(f"Folder not found: {os.getcwd()}/{board}/audio/ucm-config or audio-5_4")
            continue
        
        if not legacy:
            os.makedirs(f"{startingPath}/{overlay}/{board}/", exist_ok=True)
            os.system(f"cp -R * {startingPath}/{overlay}/{board}/")
            os.chdir(startingBoardPath)

    if legacy:
        os.makedirs(f"{startingPath}/{overlay}/", exist_ok=True)
        os.system(f"cp -R * {startingPath}/{overlay}/")
        os.chdir(startingBoardPath)

    os.chdir(f"{startingPath}/board-overlays")
    print("\n")