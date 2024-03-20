import asyncio

from pyaiolava import BusinessAiolava

SHOP_ID = ''
API_KEY = ''
lava = BusinessAiolava(
    api_key=API_KEY,
    shop_id=SHOP_ID
)

async def main() -> None:
    # Getting balance information
    balance = await lava.get_balance()
    print(balance.current_amount)
    print(balance.frozen_amount)

if __name__ == '__main__':
    asyncio.run(main())