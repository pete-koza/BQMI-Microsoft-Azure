from operator import index
from click import option
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
from datetime import date
from dash.exceptions import PreventUpdate
import DB_SQL as db
from app import app
from pages import Form_Submitted as fs


# dash.register_page(__name__, path="/")

content = html.Div(
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
                        dcc.Textarea(
                            id="Purpose-For-Request",
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
                    id="Right-Form-Block",
                    children=[
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
                        html.Br(),
                        html.Div(
                            id="Cost-Block",
                            children=[
                                html.H2("Total Travel Cost:"),
                                html.H2(id="Travel-Total-out"),
                                html.H2("Grand Total:"),
                                html.H2(id="Total-Cost-out")
                            ],
                            style={
                                    "display": "grid",
                                    "grid-template-columns": "75% 20%",
                                    "grid-gap": "3%"
                                }
                            ),
                    ]
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
                                dcc.Link(
                                    html.Button('✓', id='submit-btn', type='Submit'), href='/Form-Submitted', refresh=True
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


@app.callback( # Used for Enabling / Disabling the Submit Button
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

@app.callback( # Used for Calculating and Outputting costs
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

@app.callback(
    Output('Full-Form', 'value'), # Output does nothing, reverts to html.button() HREF tag
    Input('submit-btn', 'n_clicks'),
    Input('Employee-Name', 'value'),
    Input('Employer-Name', 'value'),
    Input('Work-Order-Lead-List', 'value'),
    Input('Company-Supervisor-List', 'value'),
    Input('Work-Order-Manager-List', 'value'),
    Input('Purpose-For-Request', 'value'),
    Input('Training-Title', 'value'),
    Input('Training-Start-Date', 'date'),
    Input('Training-End-Date', 'date'),
    Input('Certification', 'value'),
    Input('Travel-City', 'value'),
    Input('Travel-State', 'value'),
    Input('Travel-Start-Date', 'date'),
    Input('Travel-End-Date', 'date'),
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


        print(travelStartDate)

        # Spacer
        travelCosts = float(MIE75 + MIE + lodgingRate + estPerDiem + estLodgeTaxFees + roundMileageCost + estGroundTransFees + estAirfarePrice + baggageFees + estCarRentalPrice + estFuelCost + otherCost)
        # Spacer
        totalCosts = round(travelCosts + trainingCost, 2)
        travelLocation = '' + travelCity + ', ' + travelState
        if (", " in employeeName):
            employeeEmail = employeeName.split(", ")[1]
            employeeName = employeeName.split(", ")[0]
        else:
            employeeEmail = "N/A"
            employeeName = employeeName




        if(travelStartDate != None):
            date_object = date.fromisoformat(travelStartDate)
            travelStartDate = date_object.strftime('%B %d, %Y')
        else:
            travelStartDate = "N/A"

        if(travelEndDate != None):
            date_object = date.fromisoformat(travelEndDate)
            travelEndDate = date_object.strftime('%B %d, %Y')
        else:
            travelEndDate = "N/A"

        if(trainingStartDate != None):
            date_object = date.fromisoformat(trainingStartDate)
            trainingStartDate = date_object.strftime('%B %d, %Y')
        else:
            trainingStartDate = "N/A"

        if(trainingEndDate != None):
            date_object = date.fromisoformat(trainingEndDate)
            trainingEndDate = date_object.strftime('%B %d, %Y')
        else:
            trainingEndDate = "N/A"



        # Spacer
        # db.submit_New_Request(employeeName=employeeName, employerName=employerName, trainingTitle=trainingTitle, trainingPurpose=purposeForRequest, certification=certification, travelStartDate=travelStartDate, travelEndDate=travelEndDate, destination=travelLocation, trainingStartDate=trainingStartDate, trainingEndDate=trainingEndDate, totalCost=totalCosts, workOrderLead=workOrderLead, companySupervisor=companySupervisor, workOrderManager=workOrderManager)
        fs.populateForm(employeeName=employeeName, employeeEmail=employeeEmail, employerName=employerName, trainingTitle=trainingTitle, trainingPurpose=purposeForRequest, certification=certification, travelStartDate=travelStartDate, travelEndDate=travelEndDate, destination=travelLocation, trainingStartDate=trainingStartDate, trainingEndDate=trainingEndDate, totalCost=totalCosts, workOrderLead=workOrderLead, companySupervisor=companySupervisor, workOrderManager=workOrderManager)
        # Spacer
    else:
        raise PreventUpdate


@app.callback(
    Output('url', 'href'),
    Input('reset-btn', 'n_clicks')
)
def reset_page(reset_button_click):
    if reset_button_click:
        print("Reset Button Clicked")
        return "/"
    raise PreventUpdate