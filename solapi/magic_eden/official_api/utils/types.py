from datetime import datetime
from typing import Literal, TypedDict, List, Optional

MagicEdenAPIEnvironment = Literal['DEVNET ', 'MAINNET']


class METokenAttribute(TypedDict):
    trait_type: str
    value: str


class METokenFileProperty(TypedDict):
    uri: str
    type: str


class METokenCreatorProperty(TypedDict):
    address: str
    share: int


class METokenProperties(TypedDict):
    files: List[METokenFileProperty]
    category: str
    creators: List[METokenCreatorProperty]


class METoken(TypedDict):
    mint_address: str
    owner: str
    supply: int
    delegate: str
    symbol: str
    name: str
    update_authority: str
    primary_sale_happened: int
    seller_fee_basis_points: int
    image: str
    animation_url: Optional[str]
    external_url: str
    attributes: List[METokenAttribute]
    properties: METokenProperties


MEActivityType = Literal['BID', 'LIST', 'DELIST', 'BUY_NOW', 'CANCEL_BID']
MEActivitySource = Literal['magiceden', 'magiceden_v2']


class MEActivity(TypedDict):
    signature: str
    type: MEActivityType
    source: MEActivitySource
    token_mint: str
    symbol: str
    slot: int
    block_time: datetime
    buyer: str
    buyer_referral: str
    seller: str
    seller_referral: str
    price: float


class MEOffer(TypedDict):
    pda_address: str
    token_mint: str
    auction_house: str
    buyer: str
    price: float
    token_size: int
    expiry: int


class MEEscrowBalance(TypedDict):
    buyer_escrow: str
    balance: float


class MEListingItem(TypedDict):
    pda_address: str
    auction_house: str
    token_address: str
    token_mint: str
    seller: str
    token_size: int
    price: float


class MECollection(TypedDict):
    symbol: str
    name: str
    description: str
    image: str
    twitter: Optional[str]
    discord: Optional[str]
    website: Optional[str]
    categories: List[str]


class MECollectionStats(TypedDict):
    symbol: str
    floor_price: float
    listed_count: int
    volume_all: float


class MELaunchpadCollection(TypedDict):
    symbol: str
    name: str
    description: str
    featured: Optional[bool]
    edition: str
    image: str
    price: float
    supply: int
    launch_datetime: datetime
