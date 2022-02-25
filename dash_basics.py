import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc

#Read the airline data into the pandas dataframe
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                           encoding="ISO-8859-1",
                           dtype={'Div1Airport': str, 
                                  'Div1TailNum': str, 
                                  'Div2Airport': str,
                                  'Div2TailNum': str})

#Randomly sample 500 data points. Setting the random state to be 42 so that we get the same result
data = airline_data.sample(n=500, random_state=42)

#Pie Chart
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance Group Proportion by Flights')

#Create a dash application
app = dash.Dash(__name__)
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard', 
                                        style=({'textAlign':'center', 'color':'#503D36','font-size':40})), 
                                html.P('Proportion of distance group (250 mile distance interval group) by flights', style={'textAlign':'center', 'color':'#F57241'}), 
                                dcc.Graph(figure=fig)])

#Run the application
if __name__ == '__main__':
    app.run_server()