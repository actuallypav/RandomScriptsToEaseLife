import os
rootdir = {INSERT FILE PATH HERE}
#what value you want to rename it to (this case it was a digit)
x = 9

#loop through the folders, get the root directory, the subdirectories, and the files within
for root, subdir, file in os.walk(rootdir):
    #only care for the folders
    for name in subdir:
        #print the folders just in case
        print(os.path.join(root,name))
        #increase the value so not all folders are the same
        x += 1
        #rename folders
        os.rename(os.path.join(root,name), os.path.join(root,('00'+str(x))))
