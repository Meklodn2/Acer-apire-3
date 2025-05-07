import requests

response = requests.get("https://nbu.uz/uz/exchange-rates/json/")
# print(response.status_code)
# print(response.json())

# url = "https://nbu.uz/uz/exchange-rates/json/"
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     for currency in data:
#         print(f"{currency['code']}  {currency['cb_price']} UZS,")
# else:
#     print("Currency is not difinded")

data = response.json()
# print(data)


# for currency in data:
#     if currency['code'] == 'EUR':
#         print(f'1 EUR = {currency['cb_price']} UZS')

# currencies = ["USD","RUB","EUR"]
# for currency in data:
#     if currency['code'] in currencies:
#         print(f"1 {currency['code']} = {currency['cb_price']} UZS")
for currency in data:
    if currency['code'] == 'USD':
        cb_price = float(currency['cb_price'])  # `cb_price`ni raqamga aylantirish
        print(f"100 USD = {cb_price * 100:.2f} UZS")