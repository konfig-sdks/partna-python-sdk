# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from partna_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    VOUCHER = "Voucher"
    BALANCE = "Balance"
    PAYMENT = "Payment"
    TRANSACTION = "Transaction"
    WALLET = "Wallet"
    MERCHANTS = "Merchants"
    RATES = "Rates"
    CURRENCY = "Currency"
    WEBHOOK = "Webhook"
    MOCK_PAYMENT = "Mock Payment"
    TRANSACTIONS = "Transactions"
    VOUCHER_FEE = "Voucher fee"
    VOUCHER_MINMAX_AMOUNT = "Voucher min-max amount"
    API_KEY = "ApiKey"
    BANK_ACCOUNT = "BankAccount"
    BANK = "Bank"
