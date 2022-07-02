from solapi.magic_eden.official_api.utils.types import MagicEdenAPIEnvironment


class MEUrlBuilder:
    _endpoint: str

    def __init__(self, environment: MagicEdenAPIEnvironment = 'MAINNET'):
        if environment == 'DEVNET':
            self._endpoint = 'https://api-devnet.magiceden.dev/v2'
        elif environment == 'MAINNET':
            self._endpoint = 'https://api-mainnet.magiceden.dev/v2'
        else:
            raise ValueError(f'Invalid environment expected {MagicEdenAPIEnvironment} but get {environment}')


class MEAPITokensUrlBuilder(MEUrlBuilder):
    def get_token(self, token: str):
        return f'{self._endpoint}/tokens/{token}'

    def listings(self, token):
        return f'{self._endpoint}/tokens/{token}/listings'

    def offer_received(self, token, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/tokens/{token}/offer_received?offset={offset}&limit={limit}'

    def activities(self, token, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/tokens/{token}/activities?offset={offset}&limit={limit}'


class MEAPIWalletUrlsBuilder(MEUrlBuilder):
    def tokens(self, wallet_address: str, offset: int = 0, limit: int = 100, listed_only: bool = None):
        res = f'{self._endpoint}/wallets/{wallet_address}/tokens' \
              f'?offset={offset}&limit={limit}'
        if listed_only is not None:
            res = f'{res}&listedOnly={str(listed_only).lower()}'
        return res

    def activities(self, wallet_address: str, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/wallets/{wallet_address}/activities?offset={offset}&limit={limit}'

    def offers_made(self, wallet_address: str, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/wallets/{wallet_address}/activities?offset={offset}&limit={limit}'

    def offers_received(self, wallet_address: str, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/wallets/{wallet_address}/offers_received?offset={offset}&limit={limit}'

    def escrow_balance(self, wallet_address: str):
        return f'{self._endpoint}/wallets/{wallet_address}/escrow_balance'


class MEAPICollectionsUrlsBuilder(MEUrlBuilder):
    def collections(self, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/collections?offset={offset}&limit={limit}'

    def listings(self, symbol: str, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/collections/{symbol}/listings?offset={offset}&limit={limit}'

    def activities(self, symbol: str, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/collections/{symbol}/activities?offset={offset}&limit={limit}'

    def stats(self, symbol: str, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/collections/{symbol}/stats?offset={offset}&limit={limit}'


class MEAPILaunchpadUrlsBuilder(MEUrlBuilder):
    def collections(self, offset: int = 0, limit: int = 100):
        return f'{self._endpoint}/launchpad/collections?offset={offset}&limit={limit}'


class METokenResponse:
    mint_address = 'mintAddress'
    owner = 'owner'
    supply = 'supply'
    delegate = 'delegate'
    symbol = 'collection'
    name = 'name'
    update_authority = 'updateAuthority'
    primary_sale_happened = 'primarySaleHappened'
    seller_fee_bases_point = 'sellerFeeBasesPoint'
    image = 'image'
    animation_url = 'animationUrl'
    external_url = 'externalUrl'
    attributes = 'attributes'
    properties = 'properties'


class MEActivityResponse:
    signature = 'signature'
    type = 'type'
    source = 'source'
    token_mint = 'tokenMint'
    symbol = 'collection'
    slot = 'slot'
    block_time = 'blockTime'
    buyer = 'buyer'
    buyer_referral = 'buyerReferral'
    seller = 'seller'
    seller_referral = 'sellerReferral'
    price = 'price'


class MEOfferResponse:
    pda_address = 'pdaAddress'
    token_mint = 'tokenMint'
    auction_house = 'auctionHouse'
    buyer = 'buyer'
    price = 'price'
    token_size = 'tokenSize'
    expiry = 'expiry'


class MEEscrowBalanceResponse:
    buyer_escrow = 'buyerEscrow'
    balance = 'balance'


class MEListingResponse:
    pda_address = 'pdaAddress'
    auction_house = 'auctionHouse'
    token_address = 'tokenAddress'
    token_mint = 'tokenMint'
    seller = 'seller'
    token_size = 'tokenSize'
    price = 'price'


class MECollectionStatsResponse:
    symbol = 'symbol'
    floor_price = 'floorPrice'
    listed_count = 'listedCount'
    volume_all = 'volumeAll'


class MELaunchpadCollectionResponse:
    symbol = 'symbol'
    name = 'name'
    description = 'description'
    featured = 'featured'
    edition = 'edition'
    image = 'image'
    price = 'price'
    supply = 'size'
    launch_datetime = 'launchDatetime'
