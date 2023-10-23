

import pandas as pd
import sweetviz as sv

data_url = 'https://raw.githubusercontent.com/sagar-patel-99/DM_Assign_Week-4/main/Part-2/Groceries_dataset.csv'

df = pd.read_csv(data_url)

report = sv.analyze(df)

report.show_html("groceries.html")
