
import xml.etree.ElementTree as ET

data = ET.Element('play')
 
# add subtags with attributes
actors = ET.SubElement(data, 'actors')
 
ham = ET.SubElement(actors, 'actor')
ham.set('name', 'Hamlet')
ham.text = "Hamlet, the Prince of Denmark"

oph = ET.SubElement(actors, 'actress')
oph.set('name', 'Ophelia')
oph.text = "Ophelia"
 
# write as a binary string
with open("actors.xml", "wb") as f:
    f.write(ET.tostring(data))
