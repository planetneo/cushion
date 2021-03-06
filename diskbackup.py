import os, distutils, shutil

path = "/Users/Neo/Music/Logic"
src = "/Users/Neo/Music/Logic/"
dest = "/Volumes/PeteBackup/Audio/Music/Logic/"
list = os.listdir(path)

itemAmount = 0

for i in range(len(list)): #range(len(list)) finds the length of the dictionary that is returned by listidr

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
    

