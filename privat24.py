import requests

def get_privat24_exchange_rates():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            for currency in data:
                print(f"{currency['ccy']}/{currency['base_ccy']}: Buy - {currency['buy']}, Sell - {currency['sale']}")
        else:
            print(f"Error {response.status_code}: {data['errorDescription']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_privat24_exchange_rates()
