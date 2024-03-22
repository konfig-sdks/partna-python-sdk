import typing_extensions

from partna_python_sdk.paths import PathValues
from partna_python_sdk.apis.paths.v1_balance import V1Balance
from partna_python_sdk.apis.paths.v1_merchants import V1Merchants
from partna_python_sdk.apis.paths.v1_mock_payment import V1MockPayment
from partna_python_sdk.apis.paths.v1_currency_rates import V1CurrencyRates
from partna_python_sdk.apis.paths.v1_transactions_summary import V1TransactionsSummary
from partna_python_sdk.apis.paths.v1_vouchers import V1Vouchers
from partna_python_sdk.apis.paths.v1_voucher_get_many import V1VoucherGetMany
from partna_python_sdk.apis.paths.v1_voucher import V1Voucher
from partna_python_sdk.apis.paths.v1_voucher_fee import V1VoucherFee
from partna_python_sdk.apis.paths.v1_voucher_min_max import V1VoucherMinMax
from partna_python_sdk.apis.paths.auth_api_key import AuthApiKey
from partna_python_sdk.apis.paths.payment import Payment
from partna_python_sdk.apis.paths.payment_payment_id import PaymentPaymentId
from partna_python_sdk.apis.paths.transaction_transaction_id import TransactionTransactionId
from partna_python_sdk.apis.paths.currency_rate import CurrencyRate
from partna_python_sdk.apis.paths.currency_minimum_allowed import CurrencyMinimumAllowed
from partna_python_sdk.apis.paths.currency_supported import CurrencySupported
from partna_python_sdk.apis.paths.wallet_supported_config import WalletSupportedConfig
from partna_python_sdk.apis.paths.payment_resolve import PaymentResolve
from partna_python_sdk.apis.paths.callbackurl import Callbackurl
from partna_python_sdk.apis.paths.transaction import Transaction
from partna_python_sdk.apis.paths.transaction_summary import TransactionSummary
from partna_python_sdk.apis.paths.wallet import Wallet
from partna_python_sdk.apis.paths.balance_withdraw import BalanceWithdraw
from partna_python_sdk.apis.paths.bank_resolve import BankResolve
from partna_python_sdk.apis.paths.bank_supported import BankSupported
from partna_python_sdk.apis.paths.balance import Balance
from partna_python_sdk.apis.paths.balance_transfer import BalanceTransfer
from partna_python_sdk.apis.paths.wallet_transfer import WalletTransfer

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_BALANCE: V1Balance,
        PathValues.V1_MERCHANTS: V1Merchants,
        PathValues.V1_MOCK_PAYMENT: V1MockPayment,
        PathValues.V1_CURRENCY_RATES: V1CurrencyRates,
        PathValues.V1_TRANSACTIONS_SUMMARY: V1TransactionsSummary,
        PathValues.V1_VOUCHERS: V1Vouchers,
        PathValues.V1_VOUCHER_GETMANY: V1VoucherGetMany,
        PathValues.V1_VOUCHER: V1Voucher,
        PathValues.V1_VOUCHERFEE: V1VoucherFee,
        PathValues.V1_VOUCHERMINMAX: V1VoucherMinMax,
        PathValues.AUTH_APIKEY: AuthApiKey,
        PathValues.PAYMENT: Payment,
        PathValues.PAYMENT_PAYMENT_ID: PaymentPaymentId,
        PathValues.TRANSACTION_TRANSACTION_ID: TransactionTransactionId,
        PathValues.CURRENCY_RATE: CurrencyRate,
        PathValues.CURRENCY_MINIMUMALLOWED: CurrencyMinimumAllowed,
        PathValues.CURRENCY_SUPPORTED: CurrencySupported,
        PathValues.WALLET_SUPPORTED_CONFIG: WalletSupportedConfig,
        PathValues.PAYMENT_RESOLVE: PaymentResolve,
        PathValues.CALLBACKURL: Callbackurl,
        PathValues.TRANSACTION: Transaction,
        PathValues.TRANSACTION_SUMMARY: TransactionSummary,
        PathValues.WALLET: Wallet,
        PathValues.BALANCE_WITHDRAW: BalanceWithdraw,
        PathValues.BANK_RESOLVE: BankResolve,
        PathValues.BANK_SUPPORTED: BankSupported,
        PathValues.BALANCE: Balance,
        PathValues.BALANCE_TRANSFER: BalanceTransfer,
        PathValues.WALLET_TRANSFER: WalletTransfer,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_BALANCE: V1Balance,
        PathValues.V1_MERCHANTS: V1Merchants,
        PathValues.V1_MOCK_PAYMENT: V1MockPayment,
        PathValues.V1_CURRENCY_RATES: V1CurrencyRates,
        PathValues.V1_TRANSACTIONS_SUMMARY: V1TransactionsSummary,
        PathValues.V1_VOUCHERS: V1Vouchers,
        PathValues.V1_VOUCHER_GETMANY: V1VoucherGetMany,
        PathValues.V1_VOUCHER: V1Voucher,
        PathValues.V1_VOUCHERFEE: V1VoucherFee,
        PathValues.V1_VOUCHERMINMAX: V1VoucherMinMax,
        PathValues.AUTH_APIKEY: AuthApiKey,
        PathValues.PAYMENT: Payment,
        PathValues.PAYMENT_PAYMENT_ID: PaymentPaymentId,
        PathValues.TRANSACTION_TRANSACTION_ID: TransactionTransactionId,
        PathValues.CURRENCY_RATE: CurrencyRate,
        PathValues.CURRENCY_MINIMUMALLOWED: CurrencyMinimumAllowed,
        PathValues.CURRENCY_SUPPORTED: CurrencySupported,
        PathValues.WALLET_SUPPORTED_CONFIG: WalletSupportedConfig,
        PathValues.PAYMENT_RESOLVE: PaymentResolve,
        PathValues.CALLBACKURL: Callbackurl,
        PathValues.TRANSACTION: Transaction,
        PathValues.TRANSACTION_SUMMARY: TransactionSummary,
        PathValues.WALLET: Wallet,
        PathValues.BALANCE_WITHDRAW: BalanceWithdraw,
        PathValues.BANK_RESOLVE: BankResolve,
        PathValues.BANK_SUPPORTED: BankSupported,
        PathValues.BALANCE: Balance,
        PathValues.BALANCE_TRANSFER: BalanceTransfer,
        PathValues.WALLET_TRANSFER: WalletTransfer,
    }
)
