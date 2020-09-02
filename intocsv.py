import tqdm
import csv
import json

from time import time

jsons = open("all_places.info", "r", encoding="utf-8").read().split("\n")

dicts = []

for j in jsons[:-1]:
    dicts.append(json.loads(j))


# # WRITE
# with open("all_places_csv.info", "w", encoding="utf-8", newline="") as f:
# 	writer = csv.writer(f, delimiter=',',
# 	                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	writer.writerow(['latitude', 'longitude', 'node_id', 'node_info'])
# 	for dic in dicts:
# 		writer.writerow([dic["latitude"], dic["longitude"], dic["node_id"]\
# 		, json.dumps(dic["node_info"],  ensure_ascii=False)])

# READ

data = []
with open("all_places_csv.info", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')

    for row in (reader):
        # parse as you like

        data.append(row)

        # for data in row:


print(len(data))
print(data[0])

with open('places.csv', 'w', newline='') as csvfile:
    fieldnames = ['location', 'latitude', 'longitude', 'node_id', 'node_info']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row_data in tqdm.tqdm(data[1:]):  # skip first element in list
        node_info = json.loads(row_data[3])
        # print(type(node_info))

        location = ''
        # if node_info.has_key('name'):
        if 'name' in node_info:
            location = node_info['name']
        writer.writerow(
            {'location': location, 'latitude': row_data[0], 'longitude': row_data[1], 'node_id': row_data[2], 'node_info': node_info})
