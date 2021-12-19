# Python wrap for solana NFT marketplaces api such as MagicEden and Solanart

```pip install git+https://github.com/ivannnnnnnnnn/solapi.git```

## How to use?

1. Import api class
2. Create class instance
3. Use methods of class
 
 ## Example
```
from solapi.magic_eden.api.collection import MagicEdenCollectionApi

magic_eden_api = MagicEdenCollectionApi()

collections = magic_eden_api.get_collection_list()    

```

### You can also import types for annotation
```
from solapi.magic_eden.utils.types import MECollectionInfo
from typings import List

collections: List[MECollectionInfo] = []
``` 


### Available api classes and methods
##### Method ended with ```_dirty``` its clear answer from marketplace
##### Other methods, contain processed data and correspond to type annotations
 

```
MagicEdeneCollectionApi: solapi.magic_eden.api.collection.MagicEdeneCollectionApi
TypeAnnotations: solapi.magic_eden.utils.types

MagicEdenCollectionApi:
    get_collection_list_dirty(): List[Dict]
    get_collection_list(): List[MECollectionInfo]
    get_collection_list_stats_dirty(): List[Dict]
    get_collection_list_stats(): List[MECollectionMetrics]
    get_collection_info_dirty(symbol:str): Dict
    get_collection_info(symbol:str): MECollectionInfo
    get_collection_stats_dirty(symbol:str): Dict
    get_collection_stats(symbol:str): MECollectionStats



SolanartCollectionApi: solapi.solanart.api.collection.SolanartCollectionApi
TypeAnnotations: solapi.solanart.utils.types

SolanartCollectionApi:
    get_collection_list_dirty(): List[Dict]
    get_collection_list(): List[SACollectionInfo]
    get_collection_list_stats_dirty(): List[Dict]
    get_collection_list_stats(): List[SACollectionStats]
   
```
