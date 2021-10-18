# open file for reading    r       default mode
# write mode for editing   w
# creates file if not exists   x
# adding more content to file   a
# text mode opening file     t        default mode
#  binary mode opening file   b
#  read and write both mode    +


a = open("krishna.txt")
content = a.read()
print(content)
