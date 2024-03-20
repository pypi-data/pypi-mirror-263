import asyncio

from pyaiolava import BusinessAiolava, NewInvoiceModel, OldInvoiceModel
from pyaiolava.utils.generators import generate_payment_id

SHOP_ID = ''
API_KEY = ''
lava = BusinessAiolava(
    api_key=API_KEY,
    shop_id=SHOP_ID
)

async def main() -> None:
    payment_id = generate_payment_id()  # USED FOR TESTING ONLY
    new_invoice: NewInvoiceModel = await lava.create_invoice(
        payment_id=payment_id,
        amount=150,
        payment_methods=['card'],
        comment='Test Comment'
    )
    print(new_invoice)

    # You can use Payment ID
    # old_invoice: OldInvoiceModel = await lava.get_invoice(shop_id=new_invoice.shop_id, payment_id=payment_id)

    old_invoice: OldInvoiceModel = await lava.get_invoice(shop_id=new_invoice.shop_id, invoice_id=new_invoice.id)
    print(old_invoice)

if __name__ == '__main__':
    asyncio.run(main())