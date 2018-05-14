import os
import sys
import shutil
import distutils
from distutils import dir_util

path = "/Users/Neo/Music/Logic"
src = "/Users/Neo/Music/Logic/"
dest = "/Volumes/Googledrive/My Drive/Backup/Audio/LogicProjects/"
list = os.listdir(path)

itemAmount = 0

CGreen = "\033[38:5:10m"
CRed = "\033[38:5:9m"
CEnd = "\033[0m"

if len(os.listdir(dest)) == 0: # Checks if the directory is empty. If it is, copies files into it
    print("Destination directory empty, copying files.")

    for i in range(len(list)):
        print("copying: " + list[i])
        if os.path.isdir(src+list[i]):
            distutils.dir_util.copy_tree(src+list[i], dest)
        else:
            shutil.copy(src+list[i], dest)
        itemAmount += 1
        
    print("backup complete. \rcopied " + str(itemAmount) + " items")
else: # When directory is not empty, overwrite and backup. 
    try:
        for i in range(len(list)):
            
            statusSource = src+list[i]+"/Resources/ProjectInformation.plist"
            statusSourceVol = dest+list[i]+"/Resources/ProjectInformation.plist"
                
            if not list[i].startswith('.'):
                for j in range(len(list)):
                    try:
                        if str(list[i]) == str(list[j]) and format(os.stat(statusSource).st_mtime) != format(os.stat(statusSourceVol).st_mtime) and not list[i].startswith('.'):
                            itemAmount += 1
                            print("copying: " + list[i])
                            try:
                                distutils.dir_util.copy_tree(src+list[i], dest)#+list[j]
                            except FileNotFoundError:
                                print(CRed + src+list[i] + " not found, skipping"+ CEnd)
                                pass
                    except FileNotFoundError:
                        itemAmount += 1
                        print("copying: " + list[i])
                        distutils.dir_util.copy_tree(src+list[i], dest)

    except KeyboardInterrupt:
            print(CRed + " Failed" + CEnd)
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
                    

print(CGreen + "backup complete." + CEnd)
print("saved " + str(itemAmount) + " out of " + str(len(list)) + " items")
