# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from partna_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_BALANCE = "/v1/balance"
    V1_MERCHANTS = "/v1/merchants"
    V1_MOCK_PAYMENT = "/v1/mock/payment"
    V1_CURRENCY_RATES = "/v1/currency/rates"
    V1_TRANSACTIONS_SUMMARY = "/v1/transactions/summary"
    V1_VOUCHERS = "/v1/vouchers"
    V1_VOUCHER_GETMANY = "/v1/voucher/get-many"
    V1_VOUCHER = "/v1/voucher"
    V1_VOUCHERFEE = "/v1/voucher-fee"
    V1_VOUCHERMINMAX = "/v1/voucher-min-max"
    AUTH_APIKEY = "/auth/api-key"
    PAYMENT = "/payment"
    PAYMENT_PAYMENT_ID = "/payment/{paymentId}"
    TRANSACTION_TRANSACTION_ID = "/transaction/{transactionId}"
    CURRENCY_RATE = "/currency/rate"
    CURRENCY_MINIMUMALLOWED = "/currency/minimum-allowed"
    CURRENCY_SUPPORTED = "/currency/supported"
    WALLET_SUPPORTED_CONFIG = "/wallet/supported/config"
    PAYMENT_RESOLVE = "/payment/resolve"
    CALLBACKURL = "/callbackurl"
    TRANSACTION = "/transaction"
    TRANSACTION_SUMMARY = "/transaction/summary"
    WALLET = "/wallet"
    BALANCE_WITHDRAW = "/balance/withdraw"
    BANK_RESOLVE = "/bank/resolve"
    BANK_SUPPORTED = "/bank/supported"
    BALANCE = "/balance"
    BALANCE_TRANSFER = "/balance/transfer"
    WALLET_TRANSFER = "/wallet/transfer"
