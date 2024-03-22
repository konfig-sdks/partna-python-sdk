operation_parameter_map = {
    '/auth/api-key-POST': {
        'parameters': [
            {
                'name': 'otpType'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/v1/balance-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
        ]
    },
    '/balance-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
        ]
    },
    '/balance/transfer-POST': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'receiverUsername'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'otpType'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/balance/withdraw-POST': {
        'parameters': [
            {
                'name': 'accountName'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'bank'
            },
            {
                'name': 'bankCode'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'otpType'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/bank/supported-GET': {
        'parameters': [
            {
                'name': 'country'
            },
        ]
    },
    '/bank/resolve-POST': {
        'parameters': [
            {
                'name': 'accountNumber'
            },
            {
                'name': 'bankCode'
            },
        ]
    },
    '/currency/minimum-allowed-GET': {
        'parameters': [
        ]
    },
    '/currency/supported-GET': {
        'parameters': [
        ]
    },
    '/v1/merchants-GET': {
        'parameters': [
        ]
    },
    '/v1/merchants-PATCH': {
        'parameters': [
            {
                'name': 'callbackUrl'
            },
            {
                'name': 'creditCurrency'
            },
            {
                'name': 'feeBearer'
            },
            {
                'name': 'logo'
            },
        ]
    },
    '/v1/mock/payment-POST': {
        'parameters': [
            {
                'name': 'voucherId'
            },
            {
                'name': 'amount'
            },
        ]
    },
    '/payment-POST': {
        'parameters': [
            {
                'name': 'businessId'
            },
            {
                'name': 'customerEmail'
            },
            {
                'name': 'incomingCurrency'
            },
            {
                'name': 'outgoingCurrency'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'accountName'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'bank'
            },
            {
                'name': 'bankCode'
            },
            {
                'name': 'coinprofileUsername'
            },
            {
                'name': 'country'
            },
            {
                'name': 'incomingAmount'
            },
            {
                'name': 'outgoingAmount'
            },
            {
                'name': 'rateKey'
            },
            {
                'name': 'reference'
            },
        ]
    },
    '/payment/{paymentId}-GET': {
        'parameters': [
            {
                'name': 'paymentId'
            },
        ]
    },
    '/payment/resolve-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'option'
            },
        ]
    },
    '/v1/currency/rates-GET': {
        'parameters': [
        ]
    },
    '/currency/rate-GET': {
        'parameters': [
        ]
    },
    '/transaction/{transactionId}-GET': {
        'parameters': [
            {
                'name': 'transactionId'
            },
        ]
    },
    '/transaction/summary-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'type'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'duration'
            },
        ]
    },
    '/transaction-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'type'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'duration'
            },
        ]
    },
    '/v1/transactions/summary-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
        ]
    },
    '/v1/vouchers-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'email'
            },
            {
                'name': 'fullname'
            },
            {
                'name': 'rateKey'
            },
        ]
    },
    '/v1/voucher/get-many-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'paymentStatus'
            },
        ]
    },
    '/v1/vouchers-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'accountNumber'
            },
        ]
    },
    '/v1/voucher-PATCH': {
        'parameters': [
            {
                'name': 'cryptoAddress'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'email'
            },
            {
                'name': 'network'
            },
            {
                'name': 'voucherCode'
            },
            {
                'name': 'merchantFee'
            },
            {
                'name': 'rateKey'
            },
        ]
    },
    '/v1/vouchers-PATCH': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'voucherCode'
            },
        ]
    },
    '/v1/voucher-fee-GET': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
        ]
    },
    '/v1/voucher-min-max-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
        ]
    },
    '/wallet/transfer-POST': {
        'parameters': [
            {
                'name': 'address'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'network'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'walletType'
            },
        ]
    },
    '/wallet-GET': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'network'
            },
        ]
    },
    '/wallet/supported/config-GET': {
        'parameters': [
        ]
    },
    '/callbackurl-GET': {
        'parameters': [
        ]
    },
    '/callbackurl-PUT': {
        'parameters': [
            {
                'name': 'callbackUrl'
            },
        ]
    },
};