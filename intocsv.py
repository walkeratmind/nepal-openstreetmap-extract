import json

from time import time

jsons = open("all_places.info", "r", encoding="utf-8").read().split("\n")

dicts = []

for j in jsons[:-1]:
	dicts.append(json.loads(j))

import csv

# # WRITE
# with open("all_places_csv.info", "w", encoding="utf-8", newline="") as f:
# 	writer = csv.writer(f, delimiter=',',
# 	                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	writer.writerow(['latitude', 'longitude', 'node_id', 'node_info'])
# 	for dic in dicts:
# 		writer.writerow([dic["latitude"], dic["longitude"], dic["node_id"]\
# 		, json.dumps(dic["node_info"],  ensure_ascii=False)])

# READ
with open("all_places_csv.info", encoding="utf-8", newline="") as f:
	reader = csv.reader(f, delimiter=',', quotechar='|')
	
	for row in reader:
		# parse as you like