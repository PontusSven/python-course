myfile = open('/Users/pontussvensson/python/education/file-IO/myfile.txt')

# read whole file
print(myfile.read())

# reset the curser
myfile.seek(0)

# put all files into a list
fileList = myfile.readlines()
print(fileList)

# close the file
myfile.close()

# best practise - no need to close the file -

# read
with open('/Users/pontussvensson/python/education/file-IO/myfile.txt', mode="r") as myLocalFile:
    content = myLocalFile.read()
    print(content)

# append
with open('/Users/pontussvensson/python/education/file-IO/myfile.txt', mode='a') as myLocalFile:
    f = myLocalFile.write('\nthis is the fourth line')
    print(f)

# write
with open('/Users/pontussvensson/python/education/file-IO/mysecondfile.txt', mode='a') as f:
    f.write('I CREATED THIS FILE')
    



