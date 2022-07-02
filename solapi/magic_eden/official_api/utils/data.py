from solapi.magic_eden.official_api.utils.consts import METokenResponse, MEActivityResponse, MEOfferResponse, \
    MEEscrowBalanceResponse, MEListingResponse, MECollectionStatsResponse, MELaunchpadCollectionResponse
from solapi.magic_eden.official_api.utils.types import METoken, MEActivity, MEOffer, MEEscrowBalance, MEListingItem, \
    MECollectionStats
from solapi.utils.converters import convert_sol_absolute
from solapi.utils.datetime import parse_timestamp, parse_date


def token_response_mapper(data: dict) -> METoken:
    return {
        'mint_address': data.get(METokenResponse.mint_address, ''),
        'owner': data.get(METokenResponse.owner, ''),
        'supply': data.get(METokenResponse.supply, 0),
        'delegate': data.get(METokenResponse.delegate, ''),
        'symbol': data.get(METokenResponse.symbol, ''),
        'name': data.get(METokenResponse.name, ''),
        'update_authority': data.get(METokenResponse.update_authority, ''),
        'primary_sale_happened': data.get(METokenResponse.primary_sale_happened, 0),
        'seller_fee_basis_points': data.get(METokenResponse.seller_fee_bases_point, 0),
        'image': data.get(METokenResponse.image, ''),
        'animation_url': data.get(METokenResponse.animation_url, None),
        'external_url': data.get(METokenResponse.external_url, ''),
        'attributes': data.get(METokenResponse.attributes, []),
        'properties': data.get(METokenResponse.properties, {})
    }


_ACTIVITY_TYPE_MAPPING = {
    'bid': 'BID',
    'list': 'LIST',
    'buyNow': 'BUY_NOW',
    'cancelBid': 'CANCEL_BID',
    'delist': 'DELIST',
}


def activity_response_mapper(data: dict) -> MEActivity:
    _type = data.get(MEActivityResponse.type, None)
    if _type:
        _type = _ACTIVITY_TYPE_MAPPING.get(_type, None)
    return {
        'signature': data.get(MEActivityResponse.signature, ''),
        'type': _type,
        'source': data.get(MEActivityResponse.source, ''),
        'token_mint': data.get(MEActivityResponse.token_mint, ''),
        'symbol': data.get(MEActivityResponse.symbol, ''),
        'slot': data.get(MEActivityResponse.slot, ''),
        'block_time': parse_timestamp(data.get(MEActivityResponse.block_time, 0)),
        'buyer': data.get(MEActivityResponse.buyer, ''),
        'buyer_referral': data.get(MEActivityResponse.buyer_referral, ''),
        'seller': data.get(MEActivityResponse.seller, ''),
        'seller_referal': data.get(MEActivityResponse.seller_referral, ''),
        'price': data.get(MEActivityResponse.price, 0),
    }


def offer_response_mapper(data: dict) -> MEOffer:
    return {
        'pda_address': data.get(MEOfferResponse.pda_address, ''),
        'token_mint': data.get(MEOfferResponse.token_mint, ''),
        'auction_house': data.get(MEOfferResponse.auction_house, ''),
        'buyer': data.get(MEOfferResponse.buyer, ''),
        'price': data.get(MEOfferResponse.price, 0),
        'token_size': data.get(MEOfferResponse.token_size, 0),
        'expiry': data.get(MEOfferResponse.expiry, 0)
    }


def escrow_balance_response_mapper(data: dict) -> MEEscrowBalance:
    return {
        'buyer_escrow': data.get(MEEscrowBalanceResponse.buyer_escrow, ''),
        'balance': data.get(MEEscrowBalanceResponse.balance, 0)
    }


def listing_response_mapper(data: dict) -> MEListingItem:
    return {
        'pda_address': data.get(MEListingResponse.pda_address, ''),
        'auction_house': data.get(MEListingResponse.auction_house, ''),
        'token_address': data.get(MEListingResponse.token_address, ''),
        'token_mint': data.get(MEListingResponse.token_mint, ''),
        'seller': data.get(MEListingResponse.seller, ''),
        'token_size': data.get(MEListingResponse.token_size, 0),
        'price': data.get(MEListingResponse.price, 0)
    }


def collection_stats_mapper(data: dict) -> MECollectionStats:
    return {
        'symbol': data.get(MECollectionStatsResponse.symbol, ''),
        'floor_price': convert_sol_absolute(data.get(MECollectionStatsResponse.floor_price, 0)),
        'listed_count': data.get(MECollectionStatsResponse.listed_count, 0),
        'volume_all': convert_sol_absolute(data.get(MECollectionStatsResponse.volume_all, 0))
    }


def launchpad_collection_mapper(data: dict):
    return {
        'symbol': data.get(MELaunchpadCollectionResponse.symbol, ''),
        'name': data.get(MELaunchpadCollectionResponse.name, ''),
        'description': data.get(MELaunchpadCollectionResponse.description, ''),
        'featured': data.get(MELaunchpadCollectionResponse.featured, None),
        'edition': data.get(MELaunchpadCollectionResponse.edition, ''),
        'image': data.get(MELaunchpadCollectionResponse.image, ''),
        'price': data.get(MELaunchpadCollectionResponse.price, 0),
        'supply': data.get(MELaunchpadCollectionResponse.supply, 0),
        'launch_datetime': parse_date(data.get(MELaunchpadCollectionResponse.launch_datetime))
    }
