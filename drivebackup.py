<<<<<<< HEAD
import os
import shutil
import distutils
from distuils import dir_util
=======
import os, distutils, shutil
from distutils import dir_util
>>>>>>> 9b8c868dd16442b1690b7594b55adcf345b87fc5

path = "/Users/Neo/Music/Logic"
src = "/Users/Neo/Music/Logic/"
dest = "/Volumes/Googledrive/My Drive/Backup/Audio/LogicProjects/"
list = os.listdir(path)

itemAmount = 0

if len(os.listdir(dest)) == 0: # Checks if the directory is empty. If it is, copies files into it
    print("Destination directory empty, copying files.")

    for i in range(len(list)):
        print("copying: " + list[i])
        if os.path.isdir(src+list[i]):
            distutils.dir_util.copy_tree(src+list[i], dest)
        else:
            shutil.copy(src+list[i], dest)
        itemAmount += 1
        
    print("backup complete. \rcopied " + itemAmount + " items")
else: # When directory is not empty, overwrite and backup. 
    for i in range(len(list)):
        
        statusSource = src+list[i]+"/Resources/ProjectInformation.plist"
        statusSourceVol = dest+list[i]+"/Resources/ProjectInformation.plist"
            
        if not list[i].startswith('.'):
            for j in range(len(list)):
                if str(list[i]) == str(list[j]) and format(os.stat(statusSource).st_mtime) != format(os.stat(statusSourceVol).st_mtime) and not list[i].startswith('.'):
                    itemAmount += 1
                    print("copying: " + list[i])
                    distutils.dir_util.copy_tree(src+list[i], dest)#+list[j]

print("backup complete.")
print("saved " + str(itemAmount) + " out of " + str(len(list)) + " items")
