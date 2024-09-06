import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#----------------------------------------------
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#----------------------------------------------


df = sns.load_dataset('car_crashes')
df.columns
df.info()


[f"NUM_{x.upper()}" if df[x].dtype != "O"  else x.upper() for x in df.columns]


num_cols = df.select_dtypes(include='number').columns.tolist()
big_nums = [f"NUM_{x.upper()}" if x in num_cols else x.upper() for x in df.columns]
#----------------------------------------------

flag_cols = [f"{x}_FLAG" if "NO" not in x else x for x in big_nums]

#----------------------------------------------

og_list = ["abbrev" , "no_previous"]
new_df = [x for x in df.columns if x not in og_list]
new_df = df[new_df]
new_df.head()










