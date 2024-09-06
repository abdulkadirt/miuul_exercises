import pandas as pd
import numpy as np
import seaborn as sns
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width',200)
#
titanic = sns.load_dataset('titanic')
df = titanic.copy()
df.head()
df.info()

#
df["sex"].value_counts()
#

df.nunique()
# bu sonuca bakarak kesikli ve sürekli değişken ayrımı yapılabilir aslında.

#
df["pclass"].nunique()
#

#
df[["pclass","parch"]].nunique()
#

df["embarked"].dtype # object
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype # category
#
df.loc[df["embarked"] == "C" , :].count()
#
df.loc[df["embarked"] != "S" , :].count()
#
df.query("age < 30 and sex == 'female' ")
#
df[(df["fare"] > 500 ) & (df["age"] > 70 )]
#
df.query("fare > 500 or age > 70  ")
#
df.isnull().sum()
#
#
df.drop("who", axis=1, inplace=True)
#
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
#
df["age"].fillna(df["age"].median(), inplace=True)
#
df.groupby(["pclass","sex"])["survived"].agg(["sum", "count", "mean"])
# Görev 16:
df["age_flag"] = df["age"].apply(lambda x: 1 if x >= 30 else 0)
#
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset("tips")
df.head()
#
# Görev 18:
df.groupby("time")["total_bill"].agg(["min","max", "mean"])
#
df.groupby(["day","time"])["total_bill"].agg(["sum","min","max", "mean"])
#
# Görev 20:
# 1.çözüm :
df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill":["min","max","sum","mean"],"tip" : ["min","max","sum","mean"]})
# 2.çözüm
filtered_df = df[(df["time"] == "Lunch") & (df["sex"] == "Female")]

pivot_table_result = filtered_df.pivot_table(
    values=["total_bill", "tip"],
    index="day",
    aggfunc=["min", "max", "sum", "mean"],
    fill_value=0
)

#
df.loc[(df["size"]< 3) & (df["total_bill"] > 10), "total_bill"].mean()

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
#
new_df = df.sort_values("total_bill_tip_sum" , ascending=False , ignore_index=True).head(30)


