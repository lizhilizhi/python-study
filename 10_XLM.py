import xml.etree.ElementTree as  ET
tree = ET.parse('./../AutoApi.iml')
root = tree.getroot()
print(root.tag)
print(root.attrib)



