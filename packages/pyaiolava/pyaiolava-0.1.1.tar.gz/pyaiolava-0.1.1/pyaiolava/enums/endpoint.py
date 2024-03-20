from enum import StrEnum


class InvoiceEndpoint(StrEnum):
    CREATE_INVOICE = '/invoice/create'
    GET_INVOICE = '/invoice/status'

class ShopEndpoint(StrEnum):
    GET_BALANCE = '/shop/get-balance'

class PayoffEndpoint(StrEnum):
    CREATE_PAYOFF = '/payoff/create'
    GET_PAYOFF = '/payoff/info'
    GET_TARIFFS = '/payoff/get-tariffs'
    CHECK_WALLET_VALIDITY = '/payoff/check-wallet'