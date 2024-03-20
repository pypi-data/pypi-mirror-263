from typing import Union, List

from .http import AiolavaHTTP
from ..constants import (
    AMOUNT_INVALID_TEXT,
    MIN_PAYMENT_AMOUNT,
    MAX_PAYMENT_AMOUNT,
    MAX_PAYMENT_TIME,
    MIN_PAYMENT_TIME,
    TIME_INVALID_TEXT
)
from ..enums import InvoiceStatus, InvoiceEndpoint
from ..exceptions import AmountInvalidError, MutuallyExclusiveError, PaymentTimeInvalidError
from ..models import NewInvoiceModel, OldInvoiceModel
from ..utils.converters import str2datetime
from ..utils.generators import generate_signature
from ..utils.validators import is_valid_amount, is_valid_payment_time


class AiolavaInvoiceAPI(AiolavaHTTP):

    def __init__(
            self,
            api_key: str = None,
            shop_id: str = None,
            api_url: str = None
    ) -> None:
        """
        InvoiceAPI client.

        Args:
            api_key (str): API key.
            shop_id (str): Shop ID.
            api_url (str): API URL. You can use the default URL in constants.
        """

        if not api_key:
            raise ValueError('API key is required.')
        if not shop_id:
            raise ValueError('Shop ID is required.')
        if not api_url:
            raise ValueError('API URL is required.')

        self._api_key = api_key
        self._shop_id = shop_id
        self._api_url = api_url

    async def create_invoice(
            self,
            payment_id: Union[str, int],
            amount: float,
            payment_methods: List[str],
            webhook_url: str = None,
            fail_url: str = None,
            success_url: str = None,
            custom_data: str = None,
            comment: str = None,
            expired_at: int = 15
    ) -> NewInvoiceModel:
        """
        Creates a new invoice.

        Args:
            payment_id (Union[str, int]): Unique payment ID in your system.
            amount (float): Amount of payment (1-2000000).
            payment_methods (List[str]): A list of payment methods that should be available to the client to choose from (e.x ['sbp', 'card']).
            webhook_url (str): The webhook URL.
            fail_url (str, optional): URL to redirect the client, if payment is failed.
            success_url (str, optional): URL to redirect the client, if payment is success.
            custom_data (str, optional): Custom information that can be obtained in the **get_invoice()** function.
            comment (str, optional): Comment for the invoice.
            expired_at (int, optional): Number of minutes after which the invoice expires (1-43200). Default is 15.

        Raises:
            AmountInvalidError: The payment amount is too small or exceeds Lava API limits.
            PaymentTimeInvalidError: Payment expiration date is too short or exceeds Lava API limits
            PaymentIdNonUniqueError: The payment ID passed is non-unique and already exists in Lava.
            NoPaymentMethodsError: No payment methods were passed or no such methods exist.
            RequestError: An unhandled error occurred while sending the request.

        Returns:
            NewInvoiceModel
        """

        if not is_valid_amount(amount):
            raise AmountInvalidError(
                AMOUNT_INVALID_TEXT.format(
                    min_payment_amount=MIN_PAYMENT_AMOUNT,
                    max_payment_amount=MAX_PAYMENT_AMOUNT
                )
            )

        if not is_valid_payment_time(expired_at):
            raise PaymentTimeInvalidError(
                TIME_INVALID_TEXT.format(
                    min_payment_time=MIN_PAYMENT_TIME,
                    max_payment_time=MAX_PAYMENT_TIME
                )
            )

        data = {
            'sum': amount,
            'orderId': payment_id,
            'shopId': self._shop_id,
            'hookUrl': webhook_url,
            'failUrl': fail_url,
            'successUrl': success_url,
            'customFields': custom_data,
            'comment': comment,
            'includeService': payment_methods,
            'expire': expired_at
        }

        headers, data = generate_signature(data, self._api_key)
        response_data = await self._post(
            api_url=self._api_url,
            endpoint=InvoiceEndpoint.CREATE_INVOICE,
            headers=headers,
            data=data
        )

        return NewInvoiceModel(
            id=response_data['id'],
            shop_id=response_data['shop_id'],
            shop_name=response_data['merchantName'],
            amount=response_data['amount'],
            payment_url=response_data['url'],
            payment_methods=response_data['include_service'],
            status=response_data['status'],
            comment=response_data['comment'],
            expired_at=str2datetime(response_data['expired']),
        )

    async def get_invoice(
            self,
            shop_id: str,
            invoice_id: str = None,
            payment_id: str = None
    ) -> OldInvoiceModel:
        """
        Receives an invoice by payment or invoice ID. Both IDs are mutually exclusive; you must pass one or the other.

        Args:
            shop_id (str): Shop ID.
            invoice_id (str, optional): Invoice ID.
            payment_id (str, optional): Payment ID.

        Raises:
            MutuallyExclusiveError: Invoice and payment IDs are mutually exclusive.
            RequestError: An unhandled error occurred while sending the request.

        Returns:
            OldInvoiceModel
        """

        if invoice_id and payment_id:
            raise MutuallyExclusiveError('The invoice ID (invoice_id) and payment ID (payment_id) are mutually exclusive, please specify one.')

        if invoice_id:
            data = {'shopId': shop_id, 'invoiceId': invoice_id}
        else:
            data = {'shopId': shop_id, 'orderId': payment_id}

        headers, data = generate_signature(data, self._api_key)
        response_data = await self._post(
            api_url=self._api_url,
            endpoint=InvoiceEndpoint.GET_INVOICE,
            headers=headers,
            data=data
        )

        return OldInvoiceModel(
            id=response_data['id'],
            payment_id=response_data['order_id'],
            shop_id=response_data['shop_id'],
            amount=response_data['amount'],
            payment_methods=response_data['include_service'],
            fail_url=response_data['fail_url'],
            success_url=response_data['success_url'],
            webhook_url=response_data['hook_url'],
            status=InvoiceStatus(response_data['status']),
            custom_data=response_data['custom_fields'],
            error_message=response_data['error_message'],
            expired_at=str2datetime(response_data['expire']),
        )