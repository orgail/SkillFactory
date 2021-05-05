import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        # values = message.text.split(' ')

        # quote, base, amount = values

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}. Будет такая же сумма.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(
                f'Не удалось обработать валюту {quote}. Бот пока не умеет работать с такой валютой.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(
                f'Не удалось обработать валюту {base}. Бот пока не умеет работать с такой валютой.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}. Должно быть число.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        # print(total_base)

        return total_base