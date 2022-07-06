from app import app
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from datetime import date
from dash.exceptions import PreventUpdate
import DB_SQL as db

rf_passedData = []

layout = html.Div(
    id="Full-Form-FS",
    children=[
        html.H2("A Travel and Training form was submitted with the following information:"),
        html.Div(
            id="form-Callback-Info"
        )
    ]
)


def populateForm(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    global rf_passedData
    if(rf_passedData):
        rf_passedData.clear()
        rf_passedData.append(employeeName)
        rf_passedData.append(employeeEmail)
        rf_passedData.append(employerName)
        rf_passedData.append(trainingTitle)
        rf_passedData.append(trainingPurpose)
        rf_passedData.append(certification)
        rf_passedData.append(travelStartDate)
        rf_passedData.append(travelEndDate)
        rf_passedData.append(destination)
        rf_passedData.append(trainingStartDate)
        rf_passedData.append(trainingEndDate)
        rf_passedData.append(totalCost)
        rf_passedData.append(workOrderLead)
        rf_passedData.append(companySupervisor)
        rf_passedData.append(workOrderManager)
    else:
        rf_passedData.append(employeeName)
        rf_passedData.append(employeeEmail)
        rf_passedData.append(employerName)
        rf_passedData.append(trainingTitle)
        rf_passedData.append(trainingPurpose)
        rf_passedData.append(certification)
        rf_passedData.append(travelStartDate)
        rf_passedData.append(travelEndDate)
        rf_passedData.append(destination)
        rf_passedData.append(trainingStartDate)
        rf_passedData.append(trainingEndDate)
        rf_passedData.append(totalCost)
        rf_passedData.append(workOrderLead)
        rf_passedData.append(companySupervisor)
        rf_passedData.append(workOrderManager)


@app.callback(Output('form-Callback-Info', 'children'),
            Input('url', 'pathname')
            )
def formConfirm(pathname):
    if pathname == '/Form-Submitted':
        return html.Div(
            html.Table(
                id='fs_OutputTable',
                children=[
                    html.Thead(
                        html.Tr(
                            [
                                html.Th("Name"),
                                html.Th("Email"),
                                html.Th("Employeer"),
                                html.Th("Training Title"),
                                html.Th("Request Purpose"),
                                html.Th("Certification"),
                                html.Th("Travel Start Date"),
                                html.Th("Travel End Date"),
                                html.Th("Travel Destination"),
                                html.Th("Training Start Date"),
                                html.Th("Training End Date"),
                                html.Th("Total Cost"),
                                html.Th("Work Order Lead"),
                                html.Th("Company Supervisor"),
                                html.Th("Work Order Manager")
                            ]
                        )
                    ),
                    html.Tbody(
                        html.Tr(
                            [ # rf_passedData[i] = passed Data from Request Form | 0-14 Matches Table Headers
                                html.Th(rf_passedData[0]), #Employee Name
                                html.Th(rf_passedData[1]), #Employee Email
                                html.Th(rf_passedData[2]), #Employer
                                html.Th(rf_passedData[3]), #Training Title
                                html.Th(rf_passedData[4]), #Request Purpose
                                html.Th(rf_passedData[5]), #Certification (Y/N)
                                html.Th(rf_passedData[6]), #Travel Start Date
                                html.Th(rf_passedData[7]), #Travel End Date
                                html.Th(rf_passedData[8]), #Travel Destination
                                html.Th(rf_passedData[9]), #Training Start Date
                                html.Th(rf_passedData[10]), #Training End Date
                                html.Th(str(f"${'{0:.2f}'.format(rf_passedData[11])}")), #Total Cost
                                html.Th(rf_passedData[12]), #Work Order Lead
                                html.Th(rf_passedData[13]), #Company Supervisor
                                html.Th(rf_passedData[14]) #Work Order Manager
                            ]
                        )
                    )
                ]
            )
        )
