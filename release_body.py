import os, re

current_folder = os.path.dirname(__file__)
project_folder = os.path.dirname(current_folder)
print('current_folder:', current_folder)
print('project_folder:', project_folder)

body = f"""
# Release info:
**Windows: [.zip file]**
- Portable version for windows 32bit and 64bit, no installation needed, just extract to any folder and run FireDM.exe file
- ffmpeg.exe included, you can download latest version [here](https://ffmpeg.zeranoe.com/builds/)
- The binary version ".exe" prepared by "cx_freeze" on python 3.8, windows8x32bit 
---

**Linux: [.AppImage file]**
- AppImage file, portable, no installation needed, download and make file executable by right clicking the file>Properties>Permissions>Allow executing file as a program, or from terminal by `chmod +x FireDM_xxx.AppImage`
- ffmpeg is not included in this image and must be available on your system, to check for ffmpeg use this command:
```
which ffmpeg
# expected output 
/usr/bin/ffmpeg
``` 
to install ffmpeg you can `sudo apt install ffmpeg` on debian based or ` sudo pacman -S ffmpeg` on Arch based
- The binary version ".AppImage" prepared by "appimage-builder" on linuxmint, and tested on ubuntu 20.04 and Manjaro kde 
---

**changelog:**
"""

# changelog
with open(os.path.join(project_folder, 'ChangeLog.txt'), 'r') as f:
    text = f.read()
    match = re.match(r'(\d+\.\d+\.\d+:.*?)\d+\.\d+\.\d+:', text, re.DOTALL)
    changelog = match.group(1)

body += changelog

print(body)
