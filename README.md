<div align="center">

[![Visit Partna](./header.png)](https://getpartna.com&#x2F;)

# Partna<a id="partna"></a>

Coinprofile business API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`partna.api_key.generate_new_api_key`](#partnaapi_keygenerate_new_api_key)
  * [`partna.balance.get_account_balance`](#partnabalanceget_account_balance)
  * [`partna.balance.get_account_balance_0`](#partnabalanceget_account_balance_0)
  * [`partna.balance.transfer_funds`](#partnabalancetransfer_funds)
  * [`partna.balance.withdraw_funds`](#partnabalancewithdraw_funds)
  * [`partna.bank.get_supported_banks`](#partnabankget_supported_banks)
  * [`partna.bank_account.verify_and_return_details`](#partnabank_accountverify_and_return_details)
  * [`partna.currency.get_minimum_allowed`](#partnacurrencyget_minimum_allowed)
  * [`partna.currency.list_supported_currencies`](#partnacurrencylist_supported_currencies)
  * [`partna.merchants.get_record`](#partnamerchantsget_record)
  * [`partna.merchants.update_record`](#partnamerchantsupdate_record)
  * [`partna.mock_payment.request_submission`](#partnamock_paymentrequest_submission)
  * [`partna.payment.create_new_payment`](#partnapaymentcreate_new_payment)
  * [`partna.payment.get_single`](#partnapaymentget_single)
  * [`partna.payment.resolve_overpaid_transaction`](#partnapaymentresolve_overpaid_transaction)
  * [`partna.rates.get_conversion_rates`](#partnaratesget_conversion_rates)
  * [`partna.rates.get_current_rates`](#partnaratesget_current_rates)
  * [`partna.transaction.get_details`](#partnatransactionget_details)
  * [`partna.transaction.get_user_transaction_summary`](#partnatransactionget_user_transaction_summary)
  * [`partna.transaction.get_user_transactions`](#partnatransactionget_user_transactions)
  * [`partna.transactions.get_merchant_transaction_summary`](#partnatransactionsget_merchant_transaction_summary)
  * [`partna.voucher.create_payment`](#partnavouchercreate_payment)
  * [`partna.voucher.get_multiple_records`](#partnavoucherget_multiple_records)
  * [`partna.voucher.get_record`](#partnavoucherget_record)
  * [`partna.voucher.redeem_and_withdraw`](#partnavoucherredeem_and_withdraw)
  * [`partna.voucher.redeem_existing_unused`](#partnavoucherredeem_existing_unused)
  * [`partna.voucher_fee.get_fee`](#partnavoucher_feeget_fee)
  * [`partna.voucher_min_max_amount.get_min_max_amount`](#partnavoucher_min_max_amountget_min_max_amount)
  * [`partna.wallet.execute_transfer`](#partnawalletexecute_transfer)
  * [`partna.wallet.get_addresses`](#partnawalletget_addresses)
  * [`partna.wallet.get_supported_config`](#partnawalletget_supported_config)
  * [`partna.webhook.get_callback_url`](#partnawebhookget_callback_url)
  * [`partna.webhook.subscribe_webhook_callback`](#partnawebhooksubscribe_webhook_callback)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Partna&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from partna_python_sdk import Partna, ApiException

partna = Partna(
    api_key="YOUR_API_KEY",
    api_user="YOUR_API_KEY",
    user_version="YOUR_API_KEY",
)

try:
    # Create api key
    generate_new_api_key_response = partna.api_key.generate_new_api_key(
        otp_type="string_example",
        token="string_example",
    )
    print(generate_new_api_key_response)
except ApiException as e:
    print("Exception when calling ApiKeyApi.generate_new_api_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from partna_python_sdk import Partna, ApiException

partna = Partna(
    api_key="YOUR_API_KEY",
    api_user="YOUR_API_KEY",
    user_version="YOUR_API_KEY",
)


async def main():
    try:
        # Create api key
        generate_new_api_key_response = await partna.api_key.agenerate_new_api_key(
            otp_type="string_example",
            token="string_example",
        )
        print(generate_new_api_key_response)
    except ApiException as e:
        print("Exception when calling ApiKeyApi.generate_new_api_key: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from partna_python_sdk import Partna, ApiException

partna = Partna(
    api_key="YOUR_API_KEY",
    api_user="YOUR_API_KEY",
    user_version="YOUR_API_KEY",
)

try:
    # Create api key
    generate_new_api_key_response = partna.api_key.raw.generate_new_api_key(
        otp_type="string_example",
        token="string_example",
    )
    pprint(generate_new_api_key_response.body)
    pprint(generate_new_api_key_response.body["data"])
    pprint(generate_new_api_key_response.headers)
    pprint(generate_new_api_key_response.status)
    pprint(generate_new_api_key_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ApiKeyApi.generate_new_api_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `partna.api_key.generate_new_api_key`<a id="partnaapi_keygenerate_new_api_key"></a>

Create a new api key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_new_api_key_response = partna.api_key.generate_new_api_key(
    otp_type="string_example",
    token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### otp_type: `str`<a id="otp_type-str"></a>

##### token: `str`<a id="token-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApiKeyGenerateNewApiKeyRequest`](./partna_python_sdk/type/api_key_generate_new_api_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApiKeyGenerateNewApiKeyResponse`](./partna_python_sdk/pydantic/api_key_generate_new_api_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/api-key` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.balance.get_account_balance`<a id="partnabalanceget_account_balance"></a>

Retrieves account balance for the selected currency

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_balance_response = partna.balance.get_account_balance(
    currency="NGN",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

One of supported currencies

#### 🔄 Return<a id="🔄-return"></a>

[`BalanceGetAccountBalanceResponse`](./partna_python_sdk/pydantic/balance_get_account_balance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/balance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.balance.get_account_balance_0`<a id="partnabalanceget_account_balance_0"></a>

Retrieves account balance for each currency

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_balance_0_response = partna.balance.get_account_balance_0(
    currency="NGN",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

Currency for which balance is to be retrieved. When this is not supplied, balance will be retrieved for all available currencies.

#### 🔄 Return<a id="🔄-return"></a>

[`BalanceGetAccountBalance200Response`](./partna_python_sdk/pydantic/balance_get_account_balance200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/balance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.balance.transfer_funds`<a id="partnabalancetransfer_funds"></a>

Transfer funds from user's balance to another user (fiat-to-fiat)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
transfer_funds_response = partna.balance.transfer_funds(
    currency="NGN",
    receiver_username="string_example",
    amount="string_example",
    memo="string_example",
    otp_type="otp",
    token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

Currency being sent.

##### receiver_username: `str`<a id="receiver_username-str"></a>

Receiver's coinprofile username.

##### amount: `str`<a id="amount-str"></a>

Amount to transfer.

##### memo: `str`<a id="memo-str"></a>

Transaction memo.

##### otp_type: `str`<a id="otp_type-str"></a>

The type of OTP to be used.

##### token: `str`<a id="token-str"></a>

The token to be used for OTP.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BalanceTransferFundsRequest`](./partna_python_sdk/type/balance_transfer_funds_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BalanceTransferFundsResponse`](./partna_python_sdk/pydantic/balance_transfer_funds_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/balance/transfer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.balance.withdraw_funds`<a id="partnabalancewithdraw_funds"></a>

Withdraw funds from the user's balance

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
withdraw_funds_response = partna.balance.withdraw_funds(
    account_name="string_example",
    account_number="string_example",
    amount="string_example",
    bank="string_example",
    bank_code="string_example",
    currency="string_example",
    otp_type="otp",
    token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_name: `str`<a id="account_name-str"></a>

The account name. This is the name of the account holder.

##### account_number: `str`<a id="account_number-str"></a>

The account number of the user's bank account.

##### amount: `str`<a id="amount-str"></a>

The amount to be withdrawn.

##### bank: `str`<a id="bank-str"></a>

The bank name. e.g. \\\"Access Bank\\\".

##### bank_code: `str`<a id="bank_code-str"></a>

The bank code. e.g. \\\"044\\\".

##### currency: `str`<a id="currency-str"></a>

The currency of the withdrawal.

##### otp_type: `str`<a id="otp_type-str"></a>

The type of OTP to be used.

##### token: `str`<a id="token-str"></a>

The token to be used for OTP.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BalanceWithdrawFundsRequest`](./partna_python_sdk/type/balance_withdraw_funds_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BalanceWithdrawFundsResponse`](./partna_python_sdk/pydantic/balance_withdraw_funds_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/balance/withdraw` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.bank.get_supported_banks`<a id="partnabankget_supported_banks"></a>

Retrieve a list of supported banks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_supported_banks_response = partna.bank.get_supported_banks(
    country="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

The country from which to retrieve supported banks

#### 🔄 Return<a id="🔄-return"></a>

[`BankGetSupportedBanksResponse`](./partna_python_sdk/pydantic/bank_get_supported_banks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank/supported` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.bank_account.verify_and_return_details`<a id="partnabank_accountverify_and_return_details"></a>

Verifies the bank account and returns the bank account details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_and_return_details_response = partna.bank_account.verify_and_return_details(
    account_number="string_example",
    bank_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_number: `str`<a id="account_number-str"></a>

The account number.

##### bank_code: `str`<a id="bank_code-str"></a>

The bank code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountVerifyAndReturnDetailsRequest`](./partna_python_sdk/type/bank_account_verify_and_return_details_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountVerifyAndReturnDetailsResponse`](./partna_python_sdk/pydantic/bank_account_verify_and_return_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank/resolve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.currency.get_minimum_allowed`<a id="partnacurrencyget_minimum_allowed"></a>

Get minimum amount allowed

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_minimum_allowed_response = partna.currency.get_minimum_allowed()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CurrencyGetMinimumAllowedResponse`](./partna_python_sdk/pydantic/currency_get_minimum_allowed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/currency/minimum-allowed` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.currency.list_supported_currencies`<a id="partnacurrencylist_supported_currencies"></a>

Get supported currencies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_supported_currencies_response = partna.currency.list_supported_currencies()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CurrencyListSupportedCurrenciesResponse`](./partna_python_sdk/pydantic/currency_list_supported_currencies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/currency/supported` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.merchants.get_record`<a id="partnamerchantsget_record"></a>

Retrieves merchant record - username, email, callback URL, merchant logo, creditCurrency, API key expiry date-time

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = partna.merchants.get_record()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MerchantsGetRecordResponse`](./partna_python_sdk/pydantic/merchants_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/merchants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.merchants.update_record`<a id="partnamerchantsupdate_record"></a>

Updates merchant record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_record_response = partna.merchants.update_record(
    callback_url="https://www.example.com/webhook/ventogram",
    credit_currency="NGN",
    fee_bearer="client",
    logo="https://www.example.com/favicon",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

Merchant callback URL. Webhook will be sent to this URL.

##### credit_currency: `str`<a id="credit_currency-str"></a>

Merchants can set this property to their desired currency. Their balance on Ventogram will be credited with this currency when their users redeem voucher created on Ventogram. Conversion between different currencies will be performed at the rate which is obtainable at the time of redeeming the voucher. If this is not set by the merchant,  their balance will be credited with the currency used in creating the voucher.

##### fee_bearer: `str`<a id="fee_bearer-str"></a>

Bearer of the voucher fee

##### logo: `str`<a id="logo-str"></a>

Merchant logo URL

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MerchantsUpdateRecordRequest`](./partna_python_sdk/type/merchants_update_record_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MerchantsUpdateRecordResponse`](./partna_python_sdk/pydantic/merchants_update_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/merchants` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.mock_payment.request_submission`<a id="partnamock_paymentrequest_submission"></a>

Sends a mock payment request (only in staging environment)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_submission_response = partna.mock_payment.request_submission(
    voucher_id="string_example",
    amount=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### voucher_id: `str`<a id="voucher_id-str"></a>

ID of the voucher to be paid

##### amount: `int`<a id="amount-int"></a>

Amount to pay. This can be used to simulate overpayment and underpayment in staging environment. If this field is not provided, the expected amount will be paid.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MockPaymentRequestSubmissionRequest`](./partna_python_sdk/type/mock_payment_request_submission_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MockPaymentRequestSubmissionResponse`](./partna_python_sdk/pydantic/mock_payment_request_submission_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/mock/payment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.payment.create_new_payment`<a id="partnapaymentcreate_new_payment"></a>

Create a new payment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_payment_response = partna.payment.create_new_payment(
    business_id="string_example",
    customer_email="string_example",
    incoming_currency="string_example",
    outgoing_currency="string_example",
    payment_type="string_example",
    account_name="string_example",
    account_number="string_example",
    bank="string_example",
    bank_code="string_example",
    coinprofile_username="string_example",
    country="string_example",
    incoming_amount=3.14,
    outgoing_amount=3.14,
    rate_key="string_example",
    reference="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### business_id: `str`<a id="business_id-str"></a>

The business id

##### customer_email: `str`<a id="customer_email-str"></a>

The rate key

##### incoming_currency: `str`<a id="incoming_currency-str"></a>

The incoming currency

##### outgoing_currency: `str`<a id="outgoing_currency-str"></a>

The outgoing currency

##### payment_type: `str`<a id="payment_type-str"></a>

The payment type

##### account_name: `str`<a id="account_name-str"></a>

The account name. Required when paymentType is bank

##### account_number: `str`<a id="account_number-str"></a>

The account number. Required when paymentType is bank

##### bank: `str`<a id="bank-str"></a>

The bank name. Required when paymentType is bank

##### bank_code: `str`<a id="bank_code-str"></a>

The bank code. Required when paymentType is bank

##### coinprofile_username: `str`<a id="coinprofile_username-str"></a>

The coinprofile username. Required when paymentType is profile

##### country: `str`<a id="country-str"></a>

The country. Required when paymentType is bank

##### incoming_amount: `Union[int, float]`<a id="incoming_amount-unionint-float"></a>

The incoming amount

##### outgoing_amount: `Union[int, float]`<a id="outgoing_amount-unionint-float"></a>

The outgoing amount

##### rate_key: `str`<a id="rate_key-str"></a>

The rate key

##### reference: `str`<a id="reference-str"></a>

The reference

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentCreateNewPaymentRequest`](./partna_python_sdk/type/payment_create_new_payment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentCreateNewPaymentResponse`](./partna_python_sdk/pydantic/payment_create_new_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.payment.get_single`<a id="partnapaymentget_single"></a>

Get a single payment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_response = partna.payment.get_single(
    payment_id="paymentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

The ID of the created payment

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentGetSingleResponse`](./partna_python_sdk/pydantic/payment_get_single_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/{paymentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.payment.resolve_overpaid_transaction`<a id="partnapaymentresolve_overpaid_transaction"></a>

Resolve overpaid Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
resolve_overpaid_transaction_response = partna.payment.resolve_overpaid_transaction(
    id="id_example",
    option="refundexcess",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the unresolved transaction

##### option: `str`<a id="option-str"></a>

This is the way you want the transaction to be completed. Either refundExcess or PayAll option

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentResolveOverpaidTransactionResponse`](./partna_python_sdk/pydantic/payment_resolve_overpaid_transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/resolve` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.rates.get_conversion_rates`<a id="partnaratesget_conversion_rates"></a>

Retrieves conversion rates for all supported currencies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_conversion_rates_response = partna.rates.get_conversion_rates()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RatesGetConversionRatesResponse`](./partna_python_sdk/pydantic/rates_get_conversion_rates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/currency/rates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.rates.get_current_rates`<a id="partnaratesget_current_rates"></a>

Get the current rates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_current_rates_response = partna.rates.get_current_rates()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RatesGetCurrentRatesResponse`](./partna_python_sdk/pydantic/rates_get_current_rates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/currency/rate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.transaction.get_details`<a id="partnatransactionget_details"></a>

Get a transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = partna.transaction.get_details(
    transaction_id="transactionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionGetDetailsResponse`](./partna_python_sdk/pydantic/transaction_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transaction/{transactionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.transaction.get_user_transaction_summary`<a id="partnatransactionget_user_transaction_summary"></a>

Retrieves all user transactions summary

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_transaction_summary_response = partna.transaction.get_user_transaction_summary(
    currency="NGN",
    type="deposit",
    page=3.14,
    limit=3.14,
    duration="one day",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

Currency for which transactions are to be retrieved. When this is not supplied, transactions will be retrieved for all available currencies.

##### type: `str`<a id="type-str"></a>

Type of transactions to be retrieved. When this is not supplied, transactions will be retrieved for all available types.

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Number of pages to be retrieved.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Number of transaction records to be retrieved per page page.

##### duration: `str`<a id="duration-str"></a>

Duration of the transaction to be retrieved per page page.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionGetUserTransactionSummaryResponse`](./partna_python_sdk/pydantic/transaction_get_user_transaction_summary_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transaction/summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.transaction.get_user_transactions`<a id="partnatransactionget_user_transactions"></a>

Retrieves all user transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_transactions_response = partna.transaction.get_user_transactions(
    currency="NGN",
    type="deposit",
    page=3.14,
    limit=3.14,
    duration="one day",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

Currency for which transactions are to be retrieved. When this is not supplied, transactions will be retrieved for all available currencies.

##### type: `str`<a id="type-str"></a>

Type of transactions to be retrieved. When this is not supplied, transactions will be retrieved for all available types.

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Number of pages to be retrieved.

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Number of transaction records to be retrieved per page page.

##### duration: `str`<a id="duration-str"></a>

Duration of the transaction to be retrieved per page page.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionGetUserTransactionsResponse`](./partna_python_sdk/pydantic/transaction_get_user_transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transaction` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.transactions.get_merchant_transaction_summary`<a id="partnatransactionsget_merchant_transaction_summary"></a>

Retrieves transaction summary for the selected currency for a merchant

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_merchant_transaction_summary_response = (
    partna.transactions.get_merchant_transaction_summary(
        currency="NGN",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

One of supported currencies

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsGetMerchantTransactionSummaryResponse`](./partna_python_sdk/pydantic/transactions_get_merchant_transaction_summary_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/transactions/summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.voucher.create_payment`<a id="partnavouchercreate_payment"></a>

Creates a new voucher payment for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payment_response = partna.voucher.create_payment(
    amount=1,
    currency="NGN",
    email="string_example",
    fullname="string_example",
    rate_key="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Required voucher amount

##### currency: `str`<a id="currency-str"></a>

Required voucher currency

##### email: `str`<a id="email-str"></a>

User email

##### fullname: `str`<a id="fullname-str"></a>

Fullname of the user creating voucher

##### rate_key: `str`<a id="rate_key-str"></a>

This is a Ventogram-signed rate key. If provided when a voucher is created, the conversion will use the rate signed with this key if it is valid at the time of redeeming a voucher. Conversion will use the current rate if key has expired.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VoucherCreatePaymentRequest`](./partna_python_sdk/type/voucher_create_payment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VoucherCreatePaymentResponse`](./partna_python_sdk/pydantic/voucher_create_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/vouchers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.voucher.get_multiple_records`<a id="partnavoucherget_multiple_records"></a>

Retrieves a collection of voucher records, sorted in descending order by their creation date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_multiple_records_response = partna.voucher.get_multiple_records(
    page=3.14,
    page_size=3.14,
    payment_status="paid",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Defaults to 1. This is the current page being requested relative to size of a page

##### page_size: `Union[int, float]`<a id="page_size-unionint-float"></a>

The number of items to be retured per page

##### payment_status: `str`<a id="payment_status-str"></a>

Voucher payment status

#### 🔄 Return<a id="🔄-return"></a>

[`VoucherGetMultipleRecordsResponse`](./partna_python_sdk/pydantic/voucher_get_multiple_records_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/voucher/get-many` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.voucher.get_record`<a id="partnavoucherget_record"></a>

Retrieves an existing voucher record(s). When no query param is provided, all the voucher record for the merchant will be returned. If accountNumber field is provided in the query, all the voucher records associated with the given accountNumber for the merchant will be returned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = partna.voucher.get_record(
    id="string_example",
    memo="string_example",
    account_number="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Voucher id

##### memo: `str`<a id="memo-str"></a>

Voucher memo or reference number

##### account_number: `str`<a id="account_number-str"></a>

The account number used to pay for voucher

#### 🔄 Return<a id="🔄-return"></a>

[`VoucherGetRecordResponse`](./partna_python_sdk/pydantic/voucher_get_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/vouchers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.voucher.redeem_and_withdraw`<a id="partnavoucherredeem_and_withdraw"></a>

Redeems an existing unused voucher and transfers crypto to the provided wallet address

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
redeem_and_withdraw_response = partna.voucher.redeem_and_withdraw(
    crypto_address="string_example",
    currency="USDC",
    email="string_example",
    network="string_example",
    voucher_code="string_example",
    merchant_fee="string_example",
    rate_key="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### crypto_address: `str`<a id="crypto_address-str"></a>

Must be provided along with newtwork. The crypto wallet address on the provided network, to which crypto equivalent will be sent

##### currency: `str`<a id="currency-str"></a>

Cryptocurrency to send to the provided wallet details

##### email: `str`<a id="email-str"></a>

Email that was used to create the voucher

##### network: `str`<a id="network-str"></a>

Supported crypto network

##### voucher_code: `str`<a id="voucher_code-str"></a>

Voucher code to be redeemed

##### merchant_fee: `str`<a id="merchant_fee-str"></a>

In USD (optional) with a precision of 2 decimal places (max). Can be supplied if the merchant want to withdraw a portion of the voucher amount into their Ventogram balance. This must be a fraction or all of voucher value (ie received amount - voucher fee)

##### rate_key: `str`<a id="rate_key-str"></a>

This is a Ventogram-signed rate key. This will be returned in response if the signed rate was used for conversion.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VoucherRedeemAndWithdrawRequest`](./partna_python_sdk/type/voucher_redeem_and_withdraw_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VoucherRedeemAndWithdrawResponse`](./partna_python_sdk/pydantic/voucher_redeem_and_withdraw_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/voucher` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.voucher.redeem_existing_unused`<a id="partnavoucherredeem_existing_unused"></a>

Redeems an existing unused voucher

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
redeem_existing_unused_response = partna.voucher.redeem_existing_unused(
    email="string_example",
    voucher_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Email that was used to create the voucher

##### voucher_code: `str`<a id="voucher_code-str"></a>

Voucher code to be redeemed

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VoucherRedeemExistingUnusedRequest`](./partna_python_sdk/type/voucher_redeem_existing_unused_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`VoucherRedeemExistingUnusedResponse`](./partna_python_sdk/pydantic/voucher_redeem_existing_unused_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/vouchers` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.voucher_fee.get_fee`<a id="partnavoucher_feeget_fee"></a>

Retrieves fee for a given voucher amount and currency.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fee_response = partna.voucher_fee.get_fee(
    amount=1,
    currency="NGN",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Voucher amount

##### currency: `str`<a id="currency-str"></a>

Voucher currency

#### 🔄 Return<a id="🔄-return"></a>

[`VoucherFeeGetFeeResponse`](./partna_python_sdk/pydantic/voucher_fee_get_fee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/voucher-fee` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.voucher_min_max_amount.get_min_max_amount`<a id="partnavoucher_min_max_amountget_min_max_amount"></a>

Retrieves minimum and maximum voucher amounts for each currency.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_min_max_amount_response = partna.voucher_min_max_amount.get_min_max_amount(
    currency="NGN",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

Voucher currency

#### 🔄 Return<a id="🔄-return"></a>

[`VoucherMinmaxAmountGetMinMaxAmountResponse`](./partna_python_sdk/pydantic/voucher_minmax_amount_get_min_max_amount_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/voucher-min-max` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.wallet.execute_transfer`<a id="partnawalletexecute_transfer"></a>

Transfer crypto from one wallet address to another

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_transfer_response = partna.wallet.execute_transfer(
    address="string_example",
    amount=3.14,
    currency="string_example",
    network="string_example",
    memo="string_example",
    wallet_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### address: `str`<a id="address-str"></a>

Wallet address to transfer crypto

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of crypto to be transferred

##### currency: `str`<a id="currency-str"></a>

Currency of the crypto to be transferred

##### network: `str`<a id="network-str"></a>

Network on which crypto is to be transferred

##### memo: `str`<a id="memo-str"></a>

Optional transaction memo

##### wallet_type: `str`<a id="wallet_type-str"></a>

Wallet type

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WalletExecuteTransferRequest`](./partna_python_sdk/type/wallet_execute_transfer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WalletExecuteTransferResponse`](./partna_python_sdk/pydantic/wallet_execute_transfer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/wallet/transfer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.wallet.get_addresses`<a id="partnawalletget_addresses"></a>

get wallet

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_addresses_response = partna.wallet.get_addresses(
    currency="string_example",
    network="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The cryptocurrency for which address will be retrieved

##### network: `str`<a id="network-str"></a>

The crypto network of the retrieved wallet address

#### 🔄 Return<a id="🔄-return"></a>

[`WalletGetAddressesResponse`](./partna_python_sdk/pydantic/wallet_get_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/wallet` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.wallet.get_supported_config`<a id="partnawalletget_supported_config"></a>

Get supported cryptocurrencies and networks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_supported_config_response = partna.wallet.get_supported_config()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WalletGetSupportedConfigResponse`](./partna_python_sdk/pydantic/wallet_get_supported_config_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/wallet/supported/config` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.webhook.get_callback_url`<a id="partnawebhookget_callback_url"></a>

Retrieve the callback url used as webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_callback_url_response = partna.webhook.get_callback_url()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookGetCallbackUrlResponse`](./partna_python_sdk/pydantic/webhook_get_callback_url_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/callbackurl` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `partna.webhook.subscribe_webhook_callback`<a id="partnawebhooksubscribe_webhook_callback"></a>

Set the callback url that will be used as webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
subscribe_webhook_callback_response = partna.webhook.subscribe_webhook_callback(
    callback_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

The callback url. e.g. https://www.example.com/callback

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookSubscribeWebhookCallbackRequest`](./partna_python_sdk/type/webhook_subscribe_webhook_callback_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscribeWebhookCallbackResponse`](./partna_python_sdk/pydantic/webhook_subscribe_webhook_callback_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/callbackurl` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
