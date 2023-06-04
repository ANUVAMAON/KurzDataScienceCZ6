import pandas as pd

data = pd.read_csv('real-estate-price-total.csv', header=1, sep=';')

df = pd.DataFrame(data)

df.plot
