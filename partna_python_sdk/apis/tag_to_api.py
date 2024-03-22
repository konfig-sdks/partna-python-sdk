import typing_extensions

from partna_python_sdk.apis.tags import TagValues
from partna_python_sdk.apis.tags.voucher_api import VoucherApi
from partna_python_sdk.apis.tags.balance_api import BalanceApi
from partna_python_sdk.apis.tags.payment_api import PaymentApi
from partna_python_sdk.apis.tags.transaction_api import TransactionApi
from partna_python_sdk.apis.tags.wallet_api import WalletApi
from partna_python_sdk.apis.tags.merchants_api import MerchantsApi
from partna_python_sdk.apis.tags.rates_api import RatesApi
from partna_python_sdk.apis.tags.currency_api import CurrencyApi
from partna_python_sdk.apis.tags.webhook_api import WebhookApi
from partna_python_sdk.apis.tags.mock_payment_api import MockPaymentApi
from partna_python_sdk.apis.tags.transactions_api import TransactionsApi
from partna_python_sdk.apis.tags.voucher_fee_api import VoucherFeeApi
from partna_python_sdk.apis.tags.voucher_min_max_amount_api import VoucherMinMaxAmountApi
from partna_python_sdk.apis.tags.api_key_api import ApiKeyApi
from partna_python_sdk.apis.tags.bank_account_api import BankAccountApi
from partna_python_sdk.apis.tags.bank_api import BankApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.VOUCHER: VoucherApi,
        TagValues.BALANCE: BalanceApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.WALLET: WalletApi,
        TagValues.MERCHANTS: MerchantsApi,
        TagValues.RATES: RatesApi,
        TagValues.CURRENCY: CurrencyApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.MOCK_PAYMENT: MockPaymentApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.VOUCHER_FEE: VoucherFeeApi,
        TagValues.VOUCHER_MINMAX_AMOUNT: VoucherMinMaxAmountApi,
        TagValues.API_KEY: ApiKeyApi,
        TagValues.BANK_ACCOUNT: BankAccountApi,
        TagValues.BANK: BankApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.VOUCHER: VoucherApi,
        TagValues.BALANCE: BalanceApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.WALLET: WalletApi,
        TagValues.MERCHANTS: MerchantsApi,
        TagValues.RATES: RatesApi,
        TagValues.CURRENCY: CurrencyApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.MOCK_PAYMENT: MockPaymentApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.VOUCHER_FEE: VoucherFeeApi,
        TagValues.VOUCHER_MINMAX_AMOUNT: VoucherMinMaxAmountApi,
        TagValues.API_KEY: ApiKeyApi,
        TagValues.BANK_ACCOUNT: BankAccountApi,
        TagValues.BANK: BankApi,
    }
)
