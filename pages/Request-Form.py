from operator import index
from click import option
import dash
from dash import dcc, html, callback
import pyodbc as pyo
from dash.dependencies import Input, Output
from datetime import date
from dash.exceptions import PreventUpdate
import DB_SQL as db


dash.register_page(__name__, path="/")


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
                            options= db.employeeList,
                            placeholder="Employee Name"
                        ),
                        dcc.Dropdown(
                            id="Employer-Name",
                            options= db.employerList,
                            placeholder="Employer Name"
                        ),
                        dcc.Dropdown(
                            id="Work-Order-Lead-List",
                            options= db.employeeList,
                            placeholder="Work Order Lead"
                        ),
                        dcc.Dropdown(
                            id="Company-Supervisor-List",
                            options= db.employeeList,
                            placeholder="Company Supervisor"
                        ),
                        dcc.Dropdown(
                            id="Work-Order-Manager-List",
                            options= db.employeeList,
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
                                        id="Certification",
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
                            id="SevenFive-MIE-Rate",
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
                        html.P("Baggage Fees"),
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
                ),
                html.Div(
                    id="buttonSection",
                    children=[
                        html.Div([
                            html.H4("Reset"),
                            html.Button('✘', id='reset-btn')
                        ],
                        style={
                            "padding-left": "2%",
                        }),
                        html.Div([
                            html.H4("Submit"),
                            html.Span(
                                html.Button('✓', id='submit-btn', type='Submit'),
                            )
                        ],
                        style={
                            "padding-left": "2%",
                        })
                    ],
                    style={
                        "padding": "2%",
                        "display": "grid",
                        "grid-template-columns": "75% 25%"
                    }
                )
            ]
        )
    
    ]
)


@callback( # Used for Enabling / Disabling the Submit Button
    Output('submit-btn', 'disabled'),
    Input('Employee-Name', 'value'),
    Input('Employer-Name', 'value'),
    Input('Work-Order-Lead-List', 'value'),
    Input('Company-Supervisor-List', 'value'),
    Input('Work-Order-Manager-List', 'value'),
    Input('Purpose-For-Request', 'value')
)
def unlock_Submit_Button(employeeName, employerName, workOrderLeadList, companySupervisorList, workOrderManagerList, purposeForRequest):
    if (employeeName == None):
        return True
    elif (employerName == None):
        return True
    elif (workOrderLeadList == None):
        return True
    elif (companySupervisorList == None):
        return True
    elif (workOrderManagerList == None):
        return True
    elif (purposeForRequest == None):
        return True
    else:
        return False

@callback( # Used for Calculating and Outputting costs
    Output('Travel-Total-out', 'children'),
    Output('Total-Cost-out', 'children'),
    Input('Training-Cost', 'value'),
    Input('SevenFive-MIE-Rate', 'value'),
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
    Input('Other-Cost', 'value')
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

    totalCosts = round(travelCosts + trainingCost, 2)
    

    if(travelCosts != None and totalCosts != None):
        return f"${'{0:.2f}'.format(travelCosts)}", f"${'{0:.2f}'.format(totalCosts)}"
    else:
        raise PreventUpdate

@callback(
    Output('Full-Form', 'value'),
    Input('submit-btn', 'n_clicks'),
    Input('Employee-Name', 'value'),
    Input('Employer-Name', 'value'),
    Input('Work-Order-Lead-List', 'value'),
    Input('Company-Supervisor-List', 'value'),
    Input('Work-Order-Manager-List', 'value'),
    Input('Purpose-For-Request', 'value'),
    Input('Training-Title', 'value'),
    Input('Training-Start-Date', 'value'),
    Input('Training-End-Date', 'value'),
    Input('Certification', 'value'),
    Input('Travel-City', 'value'),
    Input('Travel-State', 'value'),
    Input('Travel-Start-Date', 'value'),
    Input('Travel-End-Date', 'value'),
    Input('Training-Cost', 'value'),
    Input('SevenFive-MIE-Rate', 'value'),
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
    prevent_initial_call = True
)
def submit_Request_onClick(button_click, employeeName, employerName, workOrderLead, companySupervisor, workOrderManager, purposeForRequest, trainingTitle, trainingStartDate, trainingEndDate, certification, travelCity, travelState, travelStartDate, travelEndDate, trainingCost, MIE75, MIE, lodgingRate, estPerDiem, estLodgeTaxFees, roundMileageCost, estGroundTransFees, estAirfarePrice, baggageFees, estCarRentalPrice, estFuelCost, otherCost):


    if button_click:
        # Spacer
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
        if(travelCity == None):
            travelCity = 'N/A'
        if(travelState == None):
            travelState = 'N/A'




        # Spacer
        travelCosts = float(MIE75 + MIE + lodgingRate + estPerDiem + estLodgeTaxFees + roundMileageCost + estGroundTransFees + estAirfarePrice + baggageFees + estCarRentalPrice + estFuelCost + otherCost)
        # Spacer
        totalCosts = round(travelCosts + trainingCost, 2)
        travelLocation = '' + travelCity + ', ' + travelState
        # Spacer
        db.submit_New_Request(employeeName=employeeName, employerName=employerName, trainingTitle=trainingTitle, trainingPurpose=purposeForRequest, certification=certification, travelStartDate=travelStartDate, travelEndDate=travelEndDate, destination=travelLocation, trainingStartDate=trainingStartDate, trainingEndDate=trainingEndDate, totalCost=totalCosts, workOrderLead=workOrderLead, companySupervisor=companySupervisor, workOrderManager=workOrderManager)
        # Spacer
    raise PreventUpdate