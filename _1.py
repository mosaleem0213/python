# write a program to read  the txt from a given file 'poem.txt' and find out wheather it contains the word 'jumps'
f=open('file handling/poems.txt')
txt=f.read()
if 'jumps' in txt:
    print("jumps is present in txt file")
else:
    print("jumps is not present in text file")
f.close()


# Note we use with open than  we have no need to f.close()
# LIKE with open()