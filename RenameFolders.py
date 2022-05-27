import os
rootdir = 'C:/Users/actua/Desktop/Portraits/'
x = 9


for root, subdir, file in os.walk(rootdir):
    for name in subdir:
        print(os.path.join(root,name))
        x += 1
        os.rename(os.path.join(root,name), os.path.join(root,('00'+str(x))))
