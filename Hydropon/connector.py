# Connector - Задача коннекора получение данных из источника (тикеры и котировки)

# получение данных из json
# https://docs.google.com/spreadsheets/d/1FpXjYqodU4JFE8EsbA3AO6qJdXZUctlziJiksB1cEKY/edit#gid=1625604517

# Варианты
# Получение с мосбиржи (15 минут задержка)
# Получение через Тинькофф   https://github.com/Tinkoff/investAPI   https://tinkoff.github.io/investAPI/

# token API v2 (read only gprc)

# https://azzrael.ru/api-v2-tinkoff-invest

from distutils.errors import PreprocessError
import os
os.system('cls||clear')

print ('Connector start...')

from openapi_client import openapi
token = 't.3Vey_qr5UnNJbBr_RKoNWeEbFtkoEKjjjCiPkUCY-aeJx3wIRJ_5MoqjaJZ_mA3JAF7aLABH2oWnRcTjPZVgrw'
client = openapi.api_client(token)
pf = client.portfolio.portfolio_get()  # получаем портфель 

from prettytable import PrettyTable
newtable = PrettyTable(['Номер','Тикер','Название','FIGI','Количество акций','Цена покупки', 'Currency','Итого'])

result_total=0

for i in range(10):
    b = pf.payload.positions[i].balance
    p = pf.payload.positions[i].average_position_price.value
    result = b*p
    newtable.add_row([[i], pf.payload.positions[i].ticker, pf.payload.positions[i].name, pf.payload.positions[i].figi, pf.payload.positions[i].balance, pf.payload.positions[i].average_position_price.value, pf.payload.positions[i].average_position_price.currency,result])
    result_total = result_total + result
print (newtable)
print (result_total)


    #print('Цена покупки:', pf.payload.positions[i].average_position_price.value)
    #print('currency:', pf.payload.positions[i].average_position_price.currency)
    #print('Количество акций:', pf.payload.positions[i].balance)
    #print('Номер бумаги:', pf.payload.positions[i].figi)
    #print('Тикер:', pf.payload.positions[i].ticker)
    #print('Название:', pf.payload.positions[i].name)

#instr = client.market.market_search_by_figi_get('BBG004730RP0') # по figi получить
#print (instr)

#instr2 = client.market.market_search_by_ticker_get('MAGN')   # по тикеру получить
#print(instr2)
