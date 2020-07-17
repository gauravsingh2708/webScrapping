import pandas as pd

read_file = pd.read_csv (r'zerodha_data.csv')
read_file.to_excel (r'zerpdha_excel_file.xlsx', index = None, header=True)