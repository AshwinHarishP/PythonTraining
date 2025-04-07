# Write Access Mode
# fp = open("F:/Hexaware Training/Python/Pratice/FileHandling/textFile.txt", "w")
# fp.write("Ashwin")
# fp.close()


# Read Access Mode
# fp = open("F:/Hexaware Training/Python/Pratice/FileHandling/textFile.txt", "r")
# print(fp.read())
# fp.close()


#Append Mode
# fp = open("F:/Hexaware Training/Python/Pratice/FileHandling/textFile.txt", "a")
# fp.write(" Harish")
# fp.close()

# Rename a file
# import os
# oldName = "F:/Hexaware Training/Python/Pratice/FileHandling/textFile.txt"
# newName = "F:/Hexaware Training/Python/Pratice/FileHandling/textFileNew.txt"
# os.rename(oldName, newName)

# Remove a File
# import os
# fileName = "F:/Hexaware Training/Python/Pratice/FileHandling/textFileNew.txt"
# os.remove(fileName)


#Working with a binary file

# data = b'/x12'
# fileName = "Pratice/FileHandling/TextFileHandling/binaryFile.txt"
# fp = open(fileName, 'wb')
# fp.write(data)
# fp.close


# #using with open
# fileName = "Pratice/FileHandling/TextFileHandling/binaryFile.txt"
# str = "ashwin harish"
# with open(fileName, 'w') as fp:
#     fp.write(str)


#using with open and writing in binary
# fileName = "Pratice/FileHandling/TextFileHandling/binaryFile.txt"
# str = "b'\x12'ashwin harish"
# with open(fileName, 'wb') as fp:
#     fp.write(str)