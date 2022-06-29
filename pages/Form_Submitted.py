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
), 
html.Div(
    id="DummyDiv"
)


def populateForm(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    global rf_passedData
    if(rf_passedData):
        rf_passedData.clear()
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
                                html.Th("Training Purpose"),
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
                            [
                                html.Th(rf_passedData[0]),
                                html.Th(rf_passedData[1]),
                                html.Th(rf_passedData[2]),
                                html.Th(rf_passedData[3]),
                                html.Th(rf_passedData[4]),
                                html.Th(rf_passedData[5]),
                                html.Th(rf_passedData[6]),
                                html.Th(rf_passedData[7]),
                                html.Th(rf_passedData[8]),
                                html.Th(rf_passedData[9]),
                                html.Th(rf_passedData[10]),
                                html.Th("$" + str(rf_passedData[11])),
                                html.Th(rf_passedData[12]),
                                html.Th(rf_passedData[13]),
                                html.Th(rf_passedData[14])
                            ]
                        )
                    )
                ]
            )
        )
