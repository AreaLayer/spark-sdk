import logging
from breez_sdk_spark import BreezSdk, ReceivePaymentMethod, ReceivePaymentRequest


async def receive_lightning(sdk: BreezSdk):
    # ANCHOR: receive-payment-lightning-bolt11
    try:
        description = "<invoice description>"
        # Optionally set the invoice amount you wish the payer to send
        optional_amount_sats = 5_000
        payment_method = ReceivePaymentMethod.BOLT11_INVOICE(
            description=description, amount_sats=optional_amount_sats
        )
        request = ReceivePaymentRequest(payment_method=payment_method)
        response = await sdk.receive_payment(request=request)

        payment_request = response.payment_request
        logging.debug(f"Payment Request: {payment_request}")
        receive_fee_sats = response.fee_sats
        logging.debug(f"Fees: {receive_fee_sats} sats")
        return response
    except Exception as error:
        logging.error(error)
        raise
    # ANCHOR_END: receive-payment-lightning-bolt11


async def receive_onchain(sdk: BreezSdk):
    # ANCHOR: receive-payment-onchain
    try:
        request = ReceivePaymentRequest(
            payment_method=ReceivePaymentMethod.BITCOIN_ADDRESS
        )
        response = await sdk.receive_payment(request=request)

        payment_request = response.payment_request
        logging.debug(f"Payment Request: {payment_request}")
        receive_fee_sats = response.fee_sats
        logging.debug(f"Fees: {receive_fee_sats} sats")
        return response
    except Exception as error:
        logging.error(error)
        raise
    # ANCHOR_END: receive-payment-onchain


async def receive_spark(sdk: BreezSdk):
    # ANCHOR: receive-payment-spark
    try:
        request = ReceivePaymentRequest(
            payment_method=ReceivePaymentMethod.SPARK_ADDRESS
        )
        response = await sdk.receive_payment(request=request)

        payment_request = response.payment_request
        logging.debug(f"Payment Request: {payment_request}")
        receive_fee_sats = response.fee_sats
        logging.debug(f"Fees: {receive_fee_sats} sats")
        return response
    except Exception as error:
        logging.error(error)
        raise
    # ANCHOR_END: receive-payment-spark
