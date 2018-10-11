# elasticsearch-migration
A tool to migration elasticsearch index from one cluster to another cluster

# Usage

1. modify **conf.json**
2. python run.py

```shell
  1%|          | 8000/1381557 [00:15<41:38, 549.85it/s]
```

# Conf

```json
{
  "source": {
    "host": "source_host", # source index's es host
    "index": "source_index", # source index
    "type": "source_type", # source type
    "size_per_search": 500, # doc count per request
    "scroll_alive": "1m" # scroll alive time
  },
  "target": {
    "host": "target_host", # target index's es host
    "index": "target_index", # target index
    "type": "target_type" # target type
  },
  "copy_mapping": true # whether need copy mapping from source index to target index, you can set this value false to set target index mapping manually
}
```

# Compatibility

It works well under these environment:

* os: macOS Mojave 10.14
* python: 3.6.5
* elasticsearch: 6.2.3

