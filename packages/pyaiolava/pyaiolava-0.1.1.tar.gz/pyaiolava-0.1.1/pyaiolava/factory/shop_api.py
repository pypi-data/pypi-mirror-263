from .invoice_api import AiolavaInvoiceAPI
from ..enums import ShopEndpoint
from ..models import BalanceModel
from ..utils.generators import generate_signature


class AiolavaShopAPI(AiolavaInvoiceAPI):
    """ShopAPI client."""

    async def get_balance(self) -> BalanceModel:
        """
        Gets the shop balance.

        Raises:
            RequestError: An unhandled error occurred while sending the request.

        Returns:
            BalanceModel
        """
        data = {
            'shopId': self._shop_id,
        }

        headers, data = generate_signature(data, self._api_key)
        response_data = await self._post(
            api_url=self._api_url,
            endpoint=ShopEndpoint.GET_BALANCE,
            headers=headers,
            data=data
        )

        return BalanceModel(
            current_amount=response_data['balance'],
            frozen_amount=response_data['freeze_balance'],
        )