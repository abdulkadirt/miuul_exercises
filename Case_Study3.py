import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel("miuul_gezinomi.xlsx")
print(df.head())
df.info()
cat_sum = df.describe(include=["object"]).T

df["SaleCityName"].value_counts()
df["ConceptName"].value_counts()

df.groupby("SaleCityName").agg({"Price": "sum"}).sort_values(by="Price")
df.groupby("ConceptName").agg({"Price": "sum"}).sort_values(by="Price")

df.groupby("SaleCityName").agg({"Price": "mean"}).sort_values(by="Price")

# iki değer birden
df.groupby("SaleCityName").agg({"Price": ["mean", "sum"]}).sort_values(by=("Price", "mean"))

df.groupby("ConceptName").agg({"Price": "mean"}).sort_values(by="Price")
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"}).sort_values(by="Price")

df["SaleCheckInDayDiff"] = pd.cut(df["SaleCheckInDayDiff"] , bins = [0,7,30,90,df["SaleCheckInDayDiff"].max()] , labels=["Last Minuters", "Potential Planners", "Planners", "Early Bookers"])
df["SaleCheckInDayDiff"]


# Şehir-Concept-EB Score,
#  Şehir-Concept- Sezon,
#   Şehir-Concept-CInDay
df.columns
df.groupby(["SaleCityName", "ConceptName" , "CInDay"]).agg({"Price": ["count" , "mean"]})

# City-Concept-Season
agg_df = df.groupby(["SaleCityName", "ConceptName" , "Seasons"]).agg({"Price" : "mean"}).sort_values(by = "Price", ascending = False)
agg_df.head()

agg_df = agg_df.reset_index()

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName" , "Seasons"]].agg(lambda x : "_".join(x).upper() , axis=1)

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], q=4, labels=["D","C","B","A"])

agg_df.groupby("SEGMENT").agg({"Price" : ["mean" ,"max" , "sum"]})

new_customer = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_customer]

new_customer2 = "GIRNE_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_customer2]