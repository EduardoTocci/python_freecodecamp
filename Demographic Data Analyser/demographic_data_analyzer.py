import pandas as pd


df = pd.read_csv("adultData.csv")


# d = df["race"].value_counts()
# print(d)

# avg_age_mean = df.loc[df["sex"] == "Male", "age"].mean()
# print(avg_age_mean)

# bacherlors = df.loc[df["education"] == "Bachelors"].shape[0] / df.shape[0] * 100
# print(f"% Bacherlors: {bacherlors :.2f}%")

# qnt_advanced_education = df.loc[(df["salary"] == ">50K") & ((df["education"] == "Bachelors") | (df["education"] == "Masters")  | (df["education"] == "Doctorate")) ].shape[0]
# percent = qnt_advanced_education / df.shape[0] * 100
# print(percent)

# advanced_degrees = ["Bachelors", "Masters", "Doctorate"]
# without_advan_educ = df.loc[(df["salary"] == ">50K") & (~df["education"].isin(advanced_degrees))].shape[0]
# percent = without_advan_educ / df.shape[0] * 100
# print(percent)

# min_hours_week = df["hours-per-week"].min()
# print(min_hours_week)

# min_hours_week_50K = df.loc[(df["salary"] == ">50K") & (df["hours-per-week"] == df["hours-per-week"].min())].shape[0]
# percent = min_hours_week_50K / df.loc[df["hours-per-week"] == df["hours-per-week"].min()].shape[0] * 100
# print(percent)

# country_50k = df.loc[df["salary"] == ">50K","native-country"].value_counts()
# percent = country_50k / country_50k.sum() * 100
# print(f"{percent.idxmax()} : {percent.max() :.2f}%")


# occupation_50k_india = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K"),"occupation"].value_counts()
# print(occupation_50k_india.idxmax())








