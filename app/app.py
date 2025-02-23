import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data for the graphs (replace with actual data)
data = pd.read_csv('C:/Users/oscar/OneDrive/Escritorio/Python_Projects/automobile_sales_visualizations/data/historical_automobile_sales.csv')
# Create a sample recession data graph
recession_sales_data = data[data['Recession'] == 1]  # Filter for recession data
fig = px.bar(recession_sales_data, x='Vehicle_Type', y='Automobile_Sales', title='Sales During Recession Period')

# Create a sample yearly data graph
yearly_sales_data = data.groupby(['Year'])['Automobile_Sales'].sum().reset_index()
fig_yearly = px.line(yearly_sales_data, x='Year', y='Automobile_Sales', title='Yearly Sales Report')

# Define the layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Dashboard", style={"text-align": "center"}),

    # Dropdown for selecting Vehicle Type
    html.Div([
        html.Label("Select Vehicle Type:"),
        dcc.Dropdown(
            id='vehicle-dropdown',
            options=[
                {'label': 'Medium Family Car', 'value': 'Mediumfamilycar'},
                {'label': 'Small Family Car', 'value': 'Smallfamiliycar'},
                {'label': 'Super Mini Car', 'value': 'Supperminicar'},
            ],
            value='Mediumfamilycar'  # Default value
        ),
    ], className="dropdown-container"),

    # Recession Report Graph
    dcc.Graph(
        id='recession-graph',
        figure=fig
    ),

    # Yearly Report Graph
    dcc.Graph(
        id='yearly-graph',
        figure=fig_yearly
    ),

    # Output display area
    html.Div(id="output-container", className="output-container")
])

# Callback function to update output based on dropdown selection
@app.callback(
    Output('output-container', 'children'),
    Input('vehicle-dropdown', 'value')
)
def update_output(selected_vehicle):
    return f"You have selected: {selected_vehicle}"

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
