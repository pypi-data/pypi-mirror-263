![alt text](https://telegra.ph/file/ab8d0def9474a9ee31bfb.png)

# :a: Aiolava — a simple and convenient asynchronous library for working with the Business Lava API.

### You will be able to create invoices with all the parameters that are available in the Lava API, as well as receive information about them after creation. Also, you can get information about the balance, and in the future, methods for the Payoff API, the Reccurent API will be implemented

## :arrow_heading_down: Installation (git)
```
git clone git+https://github.com/kesevone/aiolava
```

## :page_facing_up: Simple usage
```python
import asyncio

from pyaiolava import BusinessAiolava
from pyaiolava.models import NewInvoiceModel
from pyaiolava.utils.generators import generate_payment_id


SHOP_ID = 'YOUR_SHOP_ID'
API_KEY = 'YOUR_API_KEY'

lava = BusinessAiolava(
    api_key=API_KEY,
    shop_id=SHOP_ID
)
    
async def main() -> None:
    payment_id = generate_payment_id()
    new_invoice: NewInvoiceModel = await lava.create_invoice(
        payment_id=payment_id,
        amount=150,
        payment_methods=['sbp', 'card'],
        custom_data='Test Custom Data'
    )
    print(new_invoice)

if __name__ == '__main__':
    asyncio.run(main())
```

#### All data returned from the API is converted into a convenient Pydantic-model with clear parameter names.

## :zap: TODO
- [ ] Implement methods for Payoff API
- [ ] Implement methods for Recurrent API

### Thanks to **REPTIS** for providing Lava API tokens.
