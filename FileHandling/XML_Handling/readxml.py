from bs4 import BeautifulSoup

with open("F:/Hexaware Training/Python/Pratice/FileHandling/XML_Handling/Employee.xml", "r") as readFile:
    data = readFile.read()

print(data)

#Reading in xml file format
bs_data = BeautifulSoup(data, "xml")
print(bs_data)