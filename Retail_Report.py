import pandas as pd
from ydata_profiling import ProfileReport

df= pd.read_excel("Retail.xlsx")
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Retail.html")
