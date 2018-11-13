# elasticsearch-migration
A tool to migration elasticsearch index from one index to another index (can be **different cluster**). You can custom the **docs** that you want to migrate.

# Usage

1. modify **conf.json**

   ```json
   {
     "source": {
       "host": "source_host", # source index's es host
       "index": "source_index", # source index
       "type": "source_type", # source type
       "size_per_handle": 500, # doc count per fetch and bulk index
       "scroll_alive": "1m", # scroll alive time
       "dsl": {} # search dsl
     },
     "target": {
       "host": "target_host", # target index's es host
       "index": "target_index", # target index
       "type": "target_type", # target type
       "index_thread_num": 10 # number of thread to bulk index
     },
     "copy_mapping": true # whether need copy mapping from source index to target index, you can set this value false to set target index mapping manually
   }
   ```

2. custom docs (if necessary)
   * MigTargetEs#handle_id: custom id. Return **None** to ignore this doc.
   * MigTargetEs#handle_source: custom source. Return **None** to ignore this doc.

3. python run.py

```shell
  1%|          | 8000/1381557 [00:15<41:38, 549.85it/s]
```

# Compatibility

It works well under these environment:

* os: macOS Mojave 10.14
* python: 3.6.5
* elasticsearch: 2.2.0, 6.2.3

