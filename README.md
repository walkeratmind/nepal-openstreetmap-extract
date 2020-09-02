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
