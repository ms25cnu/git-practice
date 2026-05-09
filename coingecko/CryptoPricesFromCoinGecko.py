import requests
import sys

def get_crypto_prices():
    crypto_ids = ['bitcoin', 'ethereum', 'dogecoin']
    vs_currency = 'usd'

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies={vs_currency}"

    print("-" * 30)
    print(" КУРС КРИПТОВАЛЮТ (CoinGecko API) ")
    print("-" * 30)

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\nПоточні ціни:")
            for crypto_id in crypto_ids:
                crypto_name = crypto_id.capitalize()
                price = data[crypto_id][vs_currency]
                
                print(f"{crypto_name}: ${price:,} {vs_currency.upper()}")
        
        else:
            print(f"\nПомилка: Не вдалося отримати дані від API.")
            print(f"Статус-код сервера: {response.status_code}")
            
            if response.status_code == 404:
                print("Можливо, неправильний URL або ресурс не знайдено.")
            elif response.status_code == 401:
                print("Проблема з авторизацією (хоча CoinGecko без ключа).")
            elif response.status_code == 429:
                print("Занадто багато запитів. Спробуйте пізніше.")

    except requests.exceptions.RequestException as e:
        print(f"\nСталася мережева помилка: {e}")
    except KeyError:
        print("\nПомилка: Неочікуваний формат відповіді від API.")

if __name__ == "__main__":
    try:
        get_crypto_prices()
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")
        sys.exit(0)
