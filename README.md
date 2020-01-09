# Nepal OSM Extract 

The file `all_places.info` (16 MB) contains the information about all labeled nodes as available in the January 2020 OSM extract of the region covered by Nepal. The OSM-XML file which was used to extract it is available at the [Geofabrik page for Nepal](https://download.geofabrik.de/asia/nepal.html). `extract.py` was used to extract all the information. 

### Format
First, node dictionaries are made from node information. Attributes like `latitude`, `longitude`, `node_id` (useful to identify places on OSM maps), `node_info` are available.

`node_info` inside each node dictionary gives another dictionary that provides more details about the node (place). Some attributes under `node_info` are `name`, `amenity`, etc. An example of a node dictionary:

```
{
	"latitude": "28.1614946", 
	"node_info": {
		"source:alt_name_1": "GNS", 
		"alt_name_1": "Syābru Bensi", 
		"place": "town", 
		"name": "Syabru Bensi", 
		"alt_name": "Shyaphru Besi;Syrapru Besi"
	}, 
	"node_id": "267564991", 
	"longitude": "85.3367869"
}
```

These dictionaries are then json-dumped, one per line, in the present state as seen in the file.

**USAGE**: The file can be loaded and split at newlines and each line can be json-loaded using `json.loads()` to get back the dictionaries.

**CSV FORMAT**: For more flexible usage, there is also the CSV format `all_places_csv.info`. `intocsv.py` has code to read and write to CSV using Python's inbuilt `csv`. Usage in `pandas` should not very different.

### Acknowledgements
The original OSM-XML file was about 6 GB in size. The extraction was possible thanks to computational resources provided by the Kathmandu University Supercomputer Centre, which was established with equipment donated by CERN.

All OSM content belongs to OpenStreetMap Contributors. For usage, please refer to their terms of use.