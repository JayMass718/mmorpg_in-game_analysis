# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

#------------------------------#

player_count = len(purchase_data["SN"].unique())

totalplayer_table = pd.DataFrame({"Total Players": [player_count]})
totalplayer_table

#------------------------------#

avg_price = purchase_data["Price"].mean()
items_count = len(purchase_data["Item ID"].unique())
n_purchases = purchase_data["Purchase ID"].nunique()
t_revanue = purchase_data[Price].sum()

analysis_table = pd.DataFrame({"Number of Unique Items": [items_count],
                               "Average Price": [avg_price], 
                               "Number of Purchases": [n_purchases],
                               "Total Revanue": [t_revanue]})
analysis_table

#------------------------------#

gender_group = purchase_data.groupby(['Gender'])
s = purchase_data.Gender

gender_total = gender_group["SN"].nunique()
gender_percentage = s.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

gender_analysis = pd.DataFrame({"Total Count": gender_total, 
                                "Percentage of Players": gender_percentage})
gender_analysis

#------------------------------#

gender_group = purchase_data.groupby(['Gender'])
gender_total = gender_group["SN"].nunique()

total_gpurchase = purchase_data["Gender"].value_counts()
average_gprice = gender_group["Price"].mean()
averagetotal_gndrvalue =  gender_group["Price"].sum()
averagetotal_perperson = averagetotal_gndrvalue / gender_total

gender_analysis_two = pd.DataFrame ({"Purchase Count": total_gpurchase, 
                                    "Average Purchase Price": average_gprice, 
                                    "Total Purchase Value": averagetotal_gndrvalue, 
                                    "Average Total Purchase per Person": averagetotal_perperson })
gender_analysis_two

#------------------------------#

bins = [0, 10, 15, 20, 25, 30, 35, 40, 100]
age_bins = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"] 
pd.cut(purchase_data["Age"], bins, labels=age_bins)

purchase_data["Age_Group"] = pd.cut(purchase_data["Age"], bins, labels=age_bins)
a = purchase_data.Age_Group

player_count =  purchase_data["Age_Group"].value_counts()
player_percentage = a.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

age_table = pd.DataFrame ({"Total Count": player_count, 
                           "Percentage of Players": player_percentage})
age_table

#------------------------------#

age_filter = purchase_data.groupby(['Age_Group'])
age_total = age_filter["SN"].nunique()

age_pcount = purchase_data["Age_Group"].value_counts()
age_paverage = age_filter["Price"].mean()
age_ptotal = age_filter["Price"].sum()
age_avgtotalper = age_ptotal / age_total

age_analysis = pd.DataFrame ({"Purchase Count": age_pcount, 
                                    "Average Purchase Price": age_paverage, 
                                    "Total Purchase Value": age_ptotal, 
                                    "Average Total Purchase per Person": age_avgtotalper})
age_analysis

#------------------------------#

SN_filter = purchase_data.groupby(['SN']) 

topSN_pcount = purchase_data['SN'].value_counts()
topSN_avgpprice = SN_filter["Price"].mean()
topSN_ptotal = SN_filter["Price"].sum()

TopSN_analysis = pd.DataFrame ({"Purchase Count": topSN_pcount, 
                                    "Average Purchase Price": topSN_avgpprice, 
                                    "Total Purchase Value": topSN_ptotal})
TopSN_final = TopSN_analysis.sort_values(["Total Purchase Value"], ascending=False)
TopSN_final.head()

#------------------------------#

item_filter = purchase_data.groupby(['Item Name'])

topitemPop_pcount = purchase_data['Item Name'].value_counts()
topitemPop_price = item_filter['Price'].mean()
topitemPop_ptotal = item_filter["Price"].sum()

topitemPop_analysis = pd.DataFrame ({"Purchase Count": topitemPop_pcount, 
                                    "Item Price": topitemPop_price, 
                                    "Total Purchase Value": topitemPop_ptotal})
toppopular_final = topitemPop_analysis.sort_values(["Purchase Count"], ascending=False)
toppopular_final.head()

#------------------------------#

item_filter = purchase_data.groupby(['Item Name'])

topitemProfit_pcount = purchase_data['Item Name'].value_counts()
topitemProfit_price = item_filter["Price"].mean()
topitemProfit_ptotal = item_filter["Price"].sum()

topitemProfit_analysis = pd.DataFrame ({"Purchase Count": topitemProfit_pcount, 
                                    "Item Price": topitemProfit_price, 
                                    "Total Purchase Value": topitemProfit_ptotal})
topprofit_final = topitemProfit_analysis.sort_values(["Total Purchase Value"], ascending=False)
topprofit_final.head()

