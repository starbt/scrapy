import os
import os.path
path = r'/home/xcv/learning_python/scrapy/picture'
for parent, dirnames, filenames in os.walk(path):
    cnt = 0
    for filename in filenames:
        cnt = cnt + 1
        endName =  os.path.splitext(filename)[1]
        firstName = os.path.splitext(filename)[0]
        if endName == '.jpg' or endName == '.png':
            newName = str(cnt) + endName
            os.rename(os.path.join(parent, filename), os.path.join(parent, newName))
        else:
            newName = firstName + '.jpg'
            os.rename(os.path.join(parent, filename), os.path.join(parent, newName))



