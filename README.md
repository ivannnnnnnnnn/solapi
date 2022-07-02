# Python wrap for solana NFT marketplaces api such as MagicEden and Solanart

```pip install git+https://github.com/ivannnnnnnnnn/solapi.git```

## How to use?

1. Import api class
2. Create class instance
3. Use methods of class

### Important

##### Method ended with ```_dirty``` its clear answer from marketplace

##### Other methods, contain processed data and correspond to type annotations


## Example

```
from solapi.magic_eden.site_api.collection import MagicEdenCollectionApi

magic_eden_api = MagicEdenCollectionApi()

collections = magic_eden_api.get_collection_list()    

```

### You can also import types for annotation

```
from solapi.magic_eden.site_api.utils.types import MECollectionInfo
from typings import List

collections: List[MECollectionInfo] = []
```

### Available api classes and methods for use site api
```

MagicEdeneCollectionApi: solapi.magic_eden.site_api.collection.MagicEdeneCollectionApi
TypeAnnotations: solapi.magic_eden.site_api.utils.types

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

### Official MagicEden api python wrapper

```
from solapi.magic_eden.official_api import (
  MagicEdenTokensApi, 
  MagicEdenWalletsApi, 
  MagicEdenCollectionsApi, 
  MagicEdenLaunchpadApi
)  
```

#### Api classes have methods corresponded to endpoints from official [docs](https://api.magiceden.dev/)

#### Type annotations:
```
from solapi.magic_eden.official_api.utils.types import *
```

#### Constructor of official api classes take one parameter (environment,)
```
wallet_api = MagicEdenWalletsApi(environment = 'DEVNENT') #  by default value = 'MAINNET'
```
