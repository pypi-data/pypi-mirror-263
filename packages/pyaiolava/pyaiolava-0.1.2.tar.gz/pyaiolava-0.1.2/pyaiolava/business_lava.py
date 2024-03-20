from .factory.invoice_api import AiolavaInvoiceAPI
from .factory.shop_api import AiolavaShopAPI
from .constants import LAVA_BUSINESS_URL


class BusinessAiolava(AiolavaShopAPI, AiolavaInvoiceAPI):
    def __init__(
            self,
            api_key: str,
            shop_id: str,
            api_url: str = LAVA_BUSINESS_URL,
    ):
        """
        Asynchronous library for working with **Business Lava API**. Creating invoices, checking balances and more.

        Args:
            api_key (str): API key.
            shop_id (str): Shop ID.
            api_url (str, optional): API URL. You can use the default URL in constants.
        """
        super().__init__(
            api_key=api_key,
            shop_id=shop_id,
            api_url=api_url
        )