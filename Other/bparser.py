from collections import OrderedDict
from xml.etree import ElementTree as ET
import re
import os
import glob


def show_info(root):
    for child in root.iter():
        print(child.tag[l:], child.attrib, child.text)

def parse(root):
    dif = OrderedDict()
    for child in root.iter():
        for key in child.attrib:
            name = child.tag[l:]+", "+child.attrib[key]
            if name in dif:
                dif[name] += 1
            else:
                dif[name] = 1
    print(dif)
    print()

def convert(root, file):
    actions = ET.Element(root.tag[l:])
    for child in list(root):
        if child.tag[l:] == "action":
            tag = ET.SubElement(actions, child.tag[l:], type="Browser")
            rconvert(child, tag)
        else:
            tag = ET.SubElement(actions, child.tag[l:], attrib=child.attrib)
            tag.text = child.text
            rconvert(child, tag)

    completion = ET.SubElement(actions, "completion")
    window = ET.SubElement(completion, "window", index="0", type="ReadyState", count="1")

    tree = ET.ElementTree(actions)
    tree.write(file[:-3]+".xml")
            
def rconvert(child, tag):
    for sub in list(child):
        subtag = ET.SubElement(tag, sub.tag[l:], attrib=sub.attrib)            
        subtag.text = sub.text
        rconvert(sub, subtag)

l = len("{http://www.keynote.com/namespaces/tstp/script}")
#os.chdir(r"C:\Users\crios\Desktop")
os.chdir(r"C:\Python34\kht Scripts")

for file in glob.glob(r"*.kht"):
    print("Start")
    root = ET.parse(file).getroot()[3]
    #convert(root, file)
    #show_info(root)
    parse(root)
    print("End")



