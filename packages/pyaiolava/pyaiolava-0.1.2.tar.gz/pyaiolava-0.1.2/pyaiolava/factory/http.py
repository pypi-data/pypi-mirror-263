from typing import Optional

import aiohttp

from ..enums import InvoiceError
from ..exceptions import AuthError, RequestError, PaymentIdNonUniqueError, NoPaymentMethodsError


class AiolavaHTTP(object):

    @staticmethod
    async def _check_api(api_url: str, endpoint: str, api_key: Optional[str]):    # TODO: API key and API url checker
        raise NotImplementedError()

    @staticmethod
    async def _post(
            api_url: str,
            endpoint: str,
            headers: Optional[dict],
            data: Optional[dict]
    ) -> dict:

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    api_url + endpoint,
                    headers=headers,
                    json=data
            ) as response:
                response_data: dict = await response.json()

                if response.status == 401:
                    raise AuthError('Invalid API key.')
                elif response.status == 422:
                    error: dict = response_data.get('error')
                    if error:
                        error_type = [key for key in error.keys()][0]

                        if error_type == InvoiceError.ORDERID_NOT_UNIQUE:
                            raise PaymentIdNonUniqueError('Payment ID is not unique.')
                        elif error_type == InvoiceError.NO_PAYMENT_METHODS:
                            raise NoPaymentMethodsError('Payment methods are specified incorrectly or not specified at all.')

                        error_info = [value[0] for value in error.values()][0]
                        raise RequestError(error_info)
                    raise RequestError(response_data)
                elif response.status == 404:
                    error: str = response_data.get('error')
                    if not error:
                        raise RequestError(response_data)
                    raise RequestError(error)

                return response_data.get('data')