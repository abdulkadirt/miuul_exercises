import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("persona.csv")
df.head()
# Özellik Tanımları
# PRICE – Müşterinin harcama tutarı
# SOURCE – Müşterinin bağlandığı cihaz türü
# SEX – Müşterinin cinsiyeti
# COUNTRY – Müşterinin ülkesi
# AGE – Müşterinin yaşı

df.info()
df.describe(include='object').T

df[["SOURCE","PRICE"]].nunique()
df["SOURCE"].value_counts()
df["PRICE"].value_counts()
df[["SOURCE","PRICE"]].value_counts()
# price da kategorik olarak ele alınabilir gibi.
df[["SOURCE","PRICE"]].value_counts(normalize=True) # neden yapılır ?

df.groupby("COUNTRY")["PRICE"].agg("sum")

df.groupby("SOURCE")["PRICE"].agg("count")

#§ Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].agg(
    Toplam="sum",
    Ortalama="mean"
)
# § Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].agg( Toplam =  "sum" , Ortalama = "mean")

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY" , "SOURCE"])["PRICE"].agg( Toplam = "sum" , Ortalama = "mean")

# GÖREV2 : COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

agg_df = df.groupby(["COUNTRY" , "SOURCE","SEX" , "AGE"])["PRICE"].agg(Ortalama = "mean")
agg_df.sort_values(by = "Ortalama", ascending = False, inplace = True)
agg_df.head()
agg_df.reset_index(inplace = True)
agg_df.head()

agg_df["AGE_CAT"]  = pd.cut(agg_df["AGE"],[0, 18, 23, 30, 40, 70] , labels=["cocuk", "Genc","HalaGenc","OrtaYaslı","Yaslı"])

agg_df.head()

agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'AGE_CAT']].agg(lambda x: '_'.join(x).upper(), axis=1)
agg_df['customers_level_based'].value_counts()
agg_df = agg_df.groupby("customers_level_based").agg({"Ortalama": "mean"})
agg_df = agg_df.reset_index()
agg_df.head()


# Görev 7:
agg_df["SEGMENT"] = pd.qcut(agg_df["Ortalama"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT")["Ortalama"].agg(Ortalama = "mean" , Max = "max", Min = "min" , Toplam = "sum")

# Görev 8 :
new_user = "TUR_ANDROID_FEMALE_ORTAYASLI"
agg_df[agg_df["customers_level_based"] == new_user]


new_user = "FRA_IOS_FEMALE_ORTAYASLI"
agg_df[agg_df["customers_level_based"] == new_user]






















