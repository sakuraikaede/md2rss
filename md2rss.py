import mistune
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree
from email.utils import formatdate
from xml.dom import minidom
import os

markdown = mistune.create_markdown(plugins=['task_lists','url','def_list'])

rss = Element('rss')
rss.set('version','2.0')

channel = SubElement(rss,'channel')
# Start RSS Channel

# Information for RSS Channel

description = SubElement(channel,'description')
link = SubElement(channel,'link')
generator = SubElement(channel,'md2rss')
lastBuildDate = (channel,formatdate())
author = (channel,'author')
number = 0
for root,dirname,filenames in os.walk(os.getcwd()):  
       for filename in filenames:  
            if os.path.splitext(filename)[1]=='.md':
                number += 1
                print("Found file: "+ filename)
                if (os.path.exists('.cache') == False):
                    os.makedirs('.cache')
                with open(filename) as f:
                    line = f.readline()
                    while line:
                        origin = markdown(line)
                        d = open(".cache" + "/" + os.path.splitext(filename)[0] + ".html", "a")
                        d.write(origin)
                        d.close()
                        line = f.readline()
print("Total: "+ str(number))