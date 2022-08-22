from datetime import date
import pandas as pd

today = date.today()
print("Today's date:", today)
print("Heyyy from Jenkins")

dataframe1 = pd.read_excel('Input/excel_input.xlsx')
print(dataframe1)
