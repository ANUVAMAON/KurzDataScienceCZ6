import requests
import json

def find_data(data, N_or_D):
    request_name = requests.get(f'http://svatky.adresa.info/json?lang=sk&{N_or_D}={data}')
    if request_name.status_code == 200:
        if len(request_name.text) > 2:
          return 0, request_name.text
        else:
          return 1, "no data"
    elif request_name.status_code != 200:
        return 2, "incorrect query"
    return request_name

while True:
    N_or_D = input("Ak chces hladat podla mena stlac M ak podla datumu stlac D pre ukoncenie sltac Q: ").capitalize()
    data = ""
    if N_or_D == "M":
        data = input("Zadaj meno: ").capitalize()
        N_or_D = "name"
        status0, status1 = find_data(data, N_or_D)
        if status0 == 0:
          data_load = json.loads(status1)
          print(f'Meno {data_load[0]["name"]} ma sviatok {data_load[0]["date"]}')
        elif status0 == 1:
           print (status1)
        elif status0 == 2:
           print (status1)
    elif N_or_D == "D":
        data = int(input("Zadaj datum v tvare DDMM: "))
        N_or_D = "date"
        status0, status1 = find_data(data, N_or_D)
        if status0 == 0:
          data_load = json.loads(status1)
          print(f'Dna {data_load[0]["date"]} ma sviatok {data_load[0]["name"]}')
        elif status0 == 1:
           print (status1)
        elif status0 == 2:
           print (status1)
    elif N_or_D == "Q":
        break