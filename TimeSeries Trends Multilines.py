'''
@author: Timothy Stephens
TimeSeries for Various DataSets
6/18/2020
'''
#Importing libraries relevant to intended graphs
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.dates as mdates
from statsmodels.tsa.seasonal import seasonal_decompose

fig, ax = plt.subplots()
ax.grid(True)

year = mdates.YearLocator(month=1)
month = mdates.MonthLocator(interval=3)
year_format = mdates.DateFormatter('%Y')
month_format = mdates.DateFormatter('%m')

ax.xaxis.set_minor_locator(month)

ax.xaxis.grid(True, which = 'minor')
ax.xaxis.set_major_locator(year)
ax.xaxis.set_major_formatter(year_format)

#loading dataframes
dataframeCluster0 = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\v2 MISLE Incident Data (Cluster0).xlsx",sheet_name = "Filter" )
dataframeAll = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data.xlsx",sheet_name = "All" )
dataframeSaR = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (SearchAndRescue).xlsx",sheet_name = "Filter" )
dataframeMarineSafety = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (MarineSafety).xlsx",sheet_name = "Filter" )
dataframeMEP = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (MarineEnvironmentalProtection).xlsx",sheet_name = "Filter" )
dataframeSecurity = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (Security).xlsx",sheet_name = "Filter" )
var = dataframeCluster0['Case Open Date'].value_counts().sort_index()
var2 = dataframeAll['Case Open Date'].value_counts().sort_index()
var3 = dataframeSaR['Case Open Date'].value_counts().sort_index()
var4 = dataframeMarineSafety['Case Open Date'].value_counts().sort_index()
var5 = dataframeMEP['Case Open Date'].value_counts().sort_index()
var6 = dataframeSecurity['Case Open Date'].value_counts().sort_index()
decompC0 = seasonal_decompose(var, model='additive', freq = 365)
decompAll = seasonal_decompose(var2, model='additive', freq = 365)
decompSaR = seasonal_decompose(var3, model='additive', freq = 365)
decompMS = seasonal_decompose(var4, model='additive', freq = 365)
decompMEP = seasonal_decompose(var5, model='additive', freq = 365)
decompSecurity = seasonal_decompose(var6, model='additive', freq = 365)


plt.plot(decompAll.trend.index, decompAll.trend, label = "All")
plt.plot(decompC0.trend.index, decompC0.trend, label = "Cluster0")
plt.plot(decompSaR.trend.index, decompSaR.trend, label = "SearchAndRescue")
plt.plot(decompMS.trend.index, decompMS.trend, label = "MarineSafety")
plt.plot(decompMEP.trend.index, decompMEP.trend, label = "MEP")
plt.plot(decompSecurity.trend.index, decompSecurity.trend, label = "Security")
plt.legend()
ax.patch.set_facecolor('black')
plt.title("USCG Incident Trends from 2013-2020")
plt.show()
