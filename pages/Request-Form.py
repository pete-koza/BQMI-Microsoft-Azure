from operator import index
from click import option
import dash
from dash import dcc, html, callback
import pyodbc as pyo
from dash.dependencies import Input, Output
from datetime import date
from dash.exceptions import PreventUpdate


dash.register_page(__name__, path="/")



serverRQ = "pip-it-sharepoint-prod-eastus.database.windows.net,1433"
database = "Travel Training"
username = "pkoza"
password = "xAgLBmu#7bSeeYt"

cnxn = pyo.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverRQ+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT TOP (1000) [Employee],[Email]FROM [dbo].[Employees & Emails]')
rows = cursor.fetchall()
employeeList = []
for row in rows:
    employeeList.append('' + str(row[0]) + ', ' + str(row[1]))
    employeeList.sort()
employerList = ["Aerodyne", "BQMI", "COMSAT", "DB Consulting", "Insight Global", "Peerless", "V2 Technologies"]
employerList.sort()

cursor.close()

layout = html.Div(
    id="Full-Form",
    children=[
        html.Div(
            id="Form-Left",
            children=[
                html.Div(
                    id="Form-Left-Top",
                    children=[
                        html.H1("Requests"),
                        dcc.Dropdown(
                            id="Employee-Name",
                            options= employeeList,
                            placeholder="Employee Name"
                        ),
                        dcc.Dropdown(
                            id="Employer-Name",
                            options= employerList,
                            placeholder="Employer Name"
                        ),
                        dcc.Dropdown(
                            id="Work-Order-Lead-List",
                            options= employeeList,
                            placeholder="Work Order Lead"
                        ),
                        dcc.Dropdown(
                            id="Company-Supervisor-List",
                            options= employeeList,
                            placeholder="Company Supervisor"
                        ),
                        dcc.Dropdown(
                            id="Work-Order-Manager-List",
                            options= employeeList,
                            placeholder="Work Order Manager"
                        ),
                        dcc.Input(
                            id="Purpose-For-Request",
                            type="text",
                            placeholder="Purpose For Request..."
                        )
                    ]
                ),
                html.Div(
                    id="Form-Left-Bottom",
                    children=[
                        html.Div(
                            children=[
                                html.H1("Training"),
                                dcc.Input(
                                    id="Training-Title",
                                    type="text",
                                    placeholder="Training Title"
                                ),
                                dcc.DatePickerSingle(
                                    id="Training-Start-Date",
                                    placeholder="Start Date"
                                ),
                                dcc.DatePickerSingle(
                                    id="Training-End-Date",
                                    placeholder="End Date"
                                ),
                                html.Div(
                                    dcc.Checklist(
                                        options=["Certification"]
                                    )
                                )
                            ]
                        ),
                        html.Div(
                            children=[
                                html.H1("Travel"),
                                dcc.Input(
                                    id="Travel-City",
                                    type="text",
                                    placeholder="City"
                                ),
                                dcc.Input(
                                    id="Travel-State",
                                    type="text",
                                    placeholder="State"
                                ),
                                dcc.DatePickerSingle(
                                    id="Travel-Start-Date",
                                    placeholder="Start Date"
                                ),
                                dcc.DatePickerSingle(
                                    id="Travel-End-Date",
                                    placeholder="End Date"
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id="Right-Form",
            children=[
                html.H1("Training Cost"),
                dcc.Input(
                    id="Training-Cost",
                    type="number",
                    placeholder="$0.00"
                ),
                html.H2("Itemized Travel Costs"),
                html.Div(
                    id="Sub-Right-Form",
                    children=[
                        html.P("75% M&IE Rate"),
                        html.P("M&IE Rate"),
                        html.P("Lodging Rate"),
                        dcc.Input(
                            id="75-MIE-Rate",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="MIE-Rate",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="Lodging-Rate",
                            type="number",
                            placeholder="$0.00"
                        ),
                        html.P("Estimated \nPer Diem"),
                        html.P("Estimated Lodging \nTaxes and Fees"),
                        html.P("Roundtrip Auto \nMileage Cost"),
                        dcc.Input(
                            id="Est-Per-Diem",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="Est-Lodge-Tax-Fees",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="Round-Mileage-Cost",
                            type="number",
                            placeholder="$0.00"
                        ),
                        html.P("Estimated Ground \nTransportation Fees"),
                        html.P("Estimated Airfare Price"),
                        html.P("Baggage-Fees"),
                        dcc.Input(
                            id="Est-Ground-Trans-Fees",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="Est-Airfare-Price",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="Baggage-Fees",
                            type="number",
                            placeholder="$0.00"
                        ),
                        html.P("Estimated Car \nRental Price"),
                        html.P("Estimated Fuel Cost"),
                        html.P("Other Cost"),
                        dcc.Input(
                            id="Est-Car-Rental-Price",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="Est-Fuel-Cost",
                            type="number",
                            placeholder="$0.00"
                        ),
                        dcc.Input(
                            id="Other-Cost",
                            type="number",
                            placeholder="$0.00"
                        )
                    ]
                ),
                html.Div(
                    [
                        html.H1("Total Travel Cost:"),
                        html.H1(id="Travel-Total-out")
                    ],
                    style={
                            "display": "grid",
                            "grid-template-columns": "75% 20%",
                            "grid-gap": "3%"
                        }
                ),

                html.Div(
                    [
                        html.H1("Grand Total:"),
                        html.H1(id="Total-Cost-out")
                    ],
                    style={
                            "display": "grid",
                            "grid-template-columns": "75% 20%",
                            "grid-gap": "3%"
                        }
                )
            ]
        )
    
    ]
)

@callback(
    Output('Travel-Total-out', 'children'),
    Output('Total-Cost-out', 'children'),
    Input('Training-Cost', 'value'),
    Input('75-MIE-Rate', 'value'),
    Input('MIE-Rate', 'value'),
    Input('Lodging-Rate', 'value'),
    Input('Est-Per-Diem', 'value'),
    Input('Est-Lodge-Tax-Fees', 'value'),
    Input('Round-Mileage-Cost', 'value'),
    Input('Est-Ground-Trans-Fees', 'value'),
    Input('Est-Airfare-Price', 'value'),
    Input('Baggage-Fees', 'value'),
    Input('Est-Car-Rental-Price', 'value'),
    Input('Est-Fuel-Cost', 'value'),
    Input('Other-Cost', 'value'),
    prevent_initial_call=True
)
def update_cost_calc(trainingCost, MIE75, MIE, lodgingRate, estPerDiem, estLodgeTaxFees, roundMileageCost, estGroundTransFees, estAirfarePrice, baggageFees, estCarRentalPrice, estFuelCost, otherCost):
    if(trainingCost == None):
        trainingCost = 0.00
    if(MIE75 == None):
        MIE75 = 0.00
    if(MIE == None):
        MIE = 0.00
    if(lodgingRate == None):
        lodgingRate = 0.00
    if(estPerDiem == None):
        estPerDiem = 0.00
    if(estLodgeTaxFees == None):
        estLodgeTaxFees = 0.00
    if(roundMileageCost == None):
        roundMileageCost = 0.00
    if(estGroundTransFees == None):
        estGroundTransFees = 0.00
    if(estAirfarePrice == None):
        estAirfarePrice = 0.00
    if(baggageFees == None):
        baggageFees = 0.00
    if(estCarRentalPrice == None):
        estCarRentalPrice = 0.00
    if(estFuelCost == None):
        estFuelCost = 0.00
    if(otherCost == None):
        otherCost = 0.00

    travelCosts = float(MIE75 + MIE + lodgingRate + estPerDiem + estLodgeTaxFees + roundMileageCost + estGroundTransFees + estAirfarePrice + baggageFees + estCarRentalPrice + estFuelCost + otherCost)

    trainingCost = trainingCost

    totalCosts = round(travelCosts + trainingCost, 2)
    

    if(travelCosts != None and totalCosts != None):
        return f"${'{0:.2f}'.format(travelCosts)}", f"${'{0:.2f}'.format(totalCosts)}"
    else:
        raise PreventUpdate
