'''
@author: Timothy Stephens
MSC Charts for SearchAndRescue
6/25/2020
'''
#Importing libraries relevant to intended graphs
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#importing dataframes from excel file
dataframe2017 = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (SearchAndRescue).xlsx",sheet_name = "2017" )
dataframe2018 = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (SearchAndRescue).xlsx",sheet_name = "2018" )
dataframe2019 = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (SearchAndRescue).xlsx",sheet_name = "2019" )


#creating a function to count events per month for a year, so 12 numbers total listed
def event_count(dataframe):
    eventlist = []
    month = 1
    counter = 0
    while month < 13:
        for x in dataframe:
            if x == month:
                counter += 1
        eventlist.append(counter)
        month += 1
        counter = 0
    return eventlist

#separate function for polar charts since i have to recount January to close circle
def event_countP(dataframe):
    eventlist = []
    month = 1
    counter = 0
    while month < 13:
        for x in dataframe:
            if x == month:
                counter += 1
        eventlist.append(counter)
        month += 1
        counter = 0
    eventlist.append(eventlist[0])
    return eventlist



                
#dataframes being made
#note i add an extra january month and event value to complete the circle
data2017 = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframe2017["Month"])

        }
var2017 = pd.DataFrame(data2017,columns = ['Month','Events'])

data2018 = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframe2018["Month"])

        }
var2018 = pd.DataFrame(data2018,columns = ['Month','Events'])

data2019 = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframe2019["Month"])

        }
var2019 = pd.DataFrame(data2019,columns = ['Month','Events'])


#polar chart being made
#format is the same for adding figures until satisfied 
fig = go.Figure()


fig.add_trace(go.Scatterpolar(
    name = "2017",
    r = var2017["Events"],
    theta = var2017["Month"],
    mode = 'lines',

    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "2018",
    r = var2018["Events"],
    theta = var2018["Month"],
    mode = 'lines',
   
    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "2019",
    r = var2019["Events"],
    theta = var2019["Month"],
    mode = 'lines',

    connectgaps = True))

#layout stuff 
fig.update_layout(
    template="plotly_dark",
    title = '[SearchAndRescue] USCG Incidents per Calendar Month 2017 to 2019',

    )
#figure being shown
fig.show()

#similar dataframes being made
#note i remove an extra january month and event value since its not a circle

data2017B = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events': event_count(dataframe2017["Month"])
        }
var2017B = pd.DataFrame(data2017B,columns = ['Month','Events'])

data2018B = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events': event_count(dataframe2018["Month"])
        }
var2018B = pd.DataFrame(data2018B,columns = ['Month','Events'])

data2019B = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events': event_count(dataframe2019["Month"])
        }
var2019B = pd.DataFrame(data2019B,columns = ['Month','Events'])



#line chart being made
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    name = "2017",
    x=var2017B["Month"],
    y=var2017B["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "2018",
    x=var2018B["Month"],
    y=var2018B["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "2019",
    x=var2019B["Month"],
    y=var2019B["Events"],
    mode= 'lines'))




fig2.update_layout(
    template="plotly_dark",
    title = '[SearchAndRescue] USCG Incidents per Calendar Month 2017 to 2019',

    )
#figure being shown
fig2.show()
    

