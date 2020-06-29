'''
@author: Timothy Stephens
MSC Charts for Security
6/22/2020
'''
#Importing libraries relevant to intended graphs
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#importing dataframes from excel file
dataframeCluster0 = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\v2 MISLE Incident Data (Cluster0).xlsx",sheet_name = "2019" )
dataframeCluster6 = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\v2 MISLE Incident Data (Cluster6).xlsx",sheet_name = "2019" )
dataframeCluster7 = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\v2 MISLE Incident Data (Cluster7).xlsx",sheet_name = "2019" )



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
dataCluster0 = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeCluster0["Month"])
        }
varCluster0 = pd.DataFrame(dataCluster0,columns = ['Month','Events'])

dataCluster6 = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeCluster6["Month"])

        }
varCluster6 = pd.DataFrame(dataCluster6,columns = ['Month','Events'])

dataCluster7 = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeCluster7["Month"])

        }
varCluster7 = pd.DataFrame(dataCluster7,columns = ['Month','Events'])



#polar chart being made
#format is the same for adding figures until satisfied 
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    name = "Cluster0",
    r = varCluster0["Events"],
    theta = varCluster0["Month"],
    mode = 'lines',

    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "Cluster6",
    r = varCluster6["Events"],
    theta = varCluster6["Month"],
    mode = 'lines',

    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "Cluster7",
    r = varCluster7["Events"],
    theta = varCluster7["Month"],
    mode = 'lines',

    connectgaps = True))


#layout stuff 
fig.update_layout(
    template="plotly_dark",
    title = '[Combined Clusters] USCG Incidents per Calendar Month 2019',

    )
#figure being shown
fig.show()

#similar dataframes being made
#note i remove an extra january month and event value since its not a circle

dataCluster0B = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeCluster0["Month"])
        }
varCluster0B = pd.DataFrame(dataCluster0B,columns = ['Month','Events'])

dataCluster6B = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeCluster6["Month"])

        }
varCluster6B = pd.DataFrame(dataCluster6B,columns = ['Month','Events'])

dataCluster7B = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeCluster7["Month"])

        }
varCluster7B = pd.DataFrame(dataCluster7B,columns = ['Month','Events'])


#line chart being made
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    name = "Cluster0",
    x=varCluster0B["Month"],
    y=varCluster0B["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "Cluster6",
    x=varCluster6B["Month"],
    y=varCluster6B["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "Cluster7",
    x=varCluster7B["Month"],
    y=varCluster7B["Events"],
    mode= 'lines'))



fig2.update_layout(
    template="plotly_dark",
    title='[Combined Clusters] USCG Incidents per Calendar Month 2019',

    )
#figure being shown
fig2.show()
    

