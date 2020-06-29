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
dataframeSaR = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (SearchAndRescue).xlsx",sheet_name = "2019" )
dataframeMarineSafety = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (MarineSafety).xlsx",sheet_name = "2019" )
dataframeMEP = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (MarineEnvironmentalProtection).xlsx",sheet_name = "2019" )
dataframeSecurity = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (Security).xlsx",sheet_name = "2019" )
dataframeLawEnforcement = pd.read_excel(r"C:\Users\steph\OneDrive\Desktop\MSC Stuff\MISLE Incident Data (LawEnforcement).xlsx",sheet_name = "2019" )

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
dataSaR = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeSaR["Month"])
        }
varSaR = pd.DataFrame(dataSaR,columns = ['Month','Events'])

dataMarineSafety = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeMarineSafety["Month"])

        }
varMarineSafety = pd.DataFrame(dataMarineSafety,columns = ['Month','Events'])

dataMEP = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeMEP["Month"])

        }
varMEP = pd.DataFrame(dataMEP,columns = ['Month','Events'])

dataSecurity = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeSecurity["Month"])

        }
varSecurity = pd.DataFrame(dataSecurity,columns = ['Month','Events'])

dataLawEnforcement = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December','January'],
        'Events':event_countP(dataframeLawEnforcement["Month"])

        }
varLawEnforcement = pd.DataFrame(dataLawEnforcement,columns = ['Month','Events'])




#polar chart being made
#format is the same for adding figures until satisfied 
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    name = "SaR",
    r = varSaR["Events"],
    theta = varSaR["Month"],
    mode = 'lines',

    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "MarineSafety",
    r = varMarineSafety["Events"],
    theta = varMarineSafety["Month"],
    mode = 'lines',

    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "MEP",
    r = varMEP["Events"],
    theta = varMEP["Month"],
    mode = 'lines',

    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "Security",
    r = varSecurity["Events"],
    theta = varSecurity["Month"],
    mode = 'lines',
   
    connectgaps = True))

fig.add_trace(go.Scatterpolar(
    name = "LawEnforcement",
    r = varLawEnforcement["Events"],
    theta = varLawEnforcement["Month"],
    mode = 'lines',
   
    connectgaps = True))

#layout stuff 
fig.update_layout(
    template="plotly_dark",
    title = '[Combined Types] USCG Incidents per Calendar Month 2019',

    )
#figure being shown
fig.show()

#similar dataframes being made
#note i remove an extra january month and event value since its not a circle

dataSaRB = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeSaR["Month"])
        }
varSaRB = pd.DataFrame(dataSaRB,columns = ['Month','Events'])

dataMarineSafetyB = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeMarineSafety["Month"])

        }
varMarineSafetyB = pd.DataFrame(dataMarineSafetyB,columns = ['Month','Events'])

dataMEPB = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeMEP["Month"])

        }
varMEPB = pd.DataFrame(dataMEPB,columns = ['Month','Events'])

dataSecurityB = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeSecurity["Month"])

        }
varSecurityB = pd.DataFrame(dataSecurityB,columns = ['Month','Events'])

dataLawEnforcementB = {'Month': ['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Events':event_count(dataframeLawEnforcement["Month"])

        }
varLawEnforcementB = pd.DataFrame(dataLawEnforcementB,columns = ['Month','Events'])


#line chart being made
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    name = "SaR",
    x=varSaRB["Month"],
    y=varSaRB["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "MarineSafety",
    x=varMarineSafetyB["Month"],
    y=varMarineSafetyB["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "MEP",
    x=varMEPB["Month"],
    y=varMEPB["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "Security",
    x=varSecurityB["Month"],
    y=varSecurityB["Events"],
    mode= 'lines'))

fig2.add_trace(go.Scatter(
    name = "LawEnforcement",
    x=varLawEnforcementB["Month"],
    y=varLawEnforcementB["Events"],
    mode= 'lines'))



fig2.update_layout(
    template="plotly_dark",
    title='[Combined Types] USCG Incidents per Calendar Month 2019',

    )
#figure being shown
fig2.show()
    

