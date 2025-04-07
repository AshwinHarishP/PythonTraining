import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("EmployeeRecords")

# Sample data
students = [
    {"id": "101", "name": "Aravind", "department": "CSE"},
    {"id": "102", "name": "Ashwin", "department": "ECE"},
    {"id": "103", "name": "Ravi", "department": "MECH"}
]

# Add student data to XML
for student in students:
    student_element = ET.SubElement(root, "Student")
    ET.SubElement(student_element, "ID").text = student["id"]
    ET.SubElement(student_element, "Name").text = student["name"]
    ET.SubElement(student_element, "Department").text = student["department"]

# Create an ElementTree object and write to a file
tree = ET.ElementTree(root)
with open("Pratice/FileHandling/XML_Handling/EmployeeRecords.xml", "wb") as xmlfile:
    tree.write(xmlfile, encoding="utf-8", xml_declaration=True)

print("XML file written successfully!")
