'''
Script to extract all labeled nodes from any XML map file generated from
the OpenStreetMap (https://www.openstreetmap.org/).

Extract the map information for any portion of the map using different available
services. (For example, Geofabrik.de provides country-wise map information
in various filetypes. BBBike Extract Service (https://extract.bbbike.org/)
allows extraction based on regions. OSM's own website provides extraction
for smaller regions.)

Such XML map file can be loaded here and all labeled nodes will be extracted
by this script.

All OSM content belong to OpenStreetMap Contributors.

This script was written with minimal external libraries usage and in Python 2
for a specific reason. Conversion to Python 3 is straight-forward and external
libraries (like lxml) might help with efficieny.

'''

import xml.etree.ElementTree as ET
import json
import codecs  # Only for Python 2 to support utf-8 encoding
from time import time

file_to_process = "nepal-latest.osm"  # XML file
save_file = "places_all.info"  # save info to file


def getvalue(element, getby):
    return element.attrib[getby]


start = time()

places = []

for event, el in ET.iterparse(file_to_process, events=("end",)):
    tags = el.findall(".//tag")

    try:
        if tags:
            place = {}
            place["node_id"] = getvalue(el, "id")
            place["latitude"] = getvalue(el, "lat")
            place["longitude"] = getvalue(el, "lon")

            node_info = {}
            for tag in tags:
                node_info[getvalue(tag, "k")] = getvalue(tag, "v")

            place["node_info"] = node_info

            places.append(json.dumps(place, ensure_ascii=False))

            el.clear()
        else:
            el.clear()
    except:
        el.clear()

with codecs.open(save_file, 'w', "utf-8") as f:
    errors, samples = 0, 0
    for place in places:
        samples += 1
        try:
            f.write(u"" + place + "\n")
        except:
            errors += 1
    print("{} errors".format(errors/samples * 100))
print("time taken: {}".format(time()-start))


'''

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
