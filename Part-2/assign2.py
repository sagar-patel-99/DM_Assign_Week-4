

import pandas as pd
import sweetviz as sv

data_url = 'https://raw.githubusercontent.com/sagar-patel-99/DM-Assignment-Week2/main/Assignment-2(2)/Association/Groceries_dataset.csv'

df = pd.read_csv(data_url)

report = sv.analyze(df)

report.show_html("groceries.html")
