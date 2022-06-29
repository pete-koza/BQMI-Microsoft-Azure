from app import app
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from datetime import date
from dash.exceptions import PreventUpdate
import DB_SQL as db


# dash.register_page(__name__, path="/Form-Submitted")

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

@app.callback(Output('form-Callback-Info', 'children'),
            Input('url', 'pathname'),
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
                                html.Th(employeeNameForm),
                                html.Th(employeeEmailForm),
                                html.Th(employerNameForm),
                                html.Th(trainingTitleForm),
                                html.Th(trainingPurposeForm),
                                html.Th(certificationForm),
                                html.Th(travelStartDateForm),
                                html.Th(travelEndDateForm),
                                html.Th(destinationForm),
                                html.Th(trainingStartDateForm),
                                html.Th(trainingEndDateForm),
                                html.Th("$" + str(totalCostForm)),
                                html.Th(workOrderLeadForm),
                                html.Th(companySupervisorForm),
                                html.Th(workOrderManagerForm)
                            ]
                        )
                    )
                ]
            )
        )

def get_employeeName(employeeName): #Passes EmployeeName
    global employeeNameForm
    employeeNameForm = employeeName

def get_employeeEmail(employeeEmail): #Passes EmployeeName
    global employeeEmailForm
    employeeEmailForm = employeeEmail

def get_employerName(employerName): #Passes EmployerName
    global employerNameForm
    employerNameForm = employerName

def get_trainingTitle(trainingTitle): #Passes trainingTitle
    global trainingTitleForm
    trainingTitleForm = trainingTitle

def get_trainingPurpose(trainingPurpose): #Passes trainingPurpose
    global trainingPurposeForm
    trainingPurposeForm = trainingPurpose

def get_certification(certification): #Passes certification
    global certificationForm
    certificationForm = certification

def get_travelStartDate(travelStartDate): #Passes travelStartDate
    global travelStartDateForm
    travelStartDateForm = travelStartDate

def get_travelEndDate(travelEndDate): #Passes travelEndDate
    global travelEndDateForm
    travelEndDateForm = travelEndDate

def get_destination(destination): #Passes destination
    global destinationForm
    destinationForm = destination

def get_trainingStartDate(trainingStartDate): #Passes trainingStartDate
    global trainingStartDateForm
    trainingStartDateForm = trainingStartDate

def get_trainingEndDate(trainingEndDate): #Passes trainingEndDate
    global trainingEndDateForm
    trainingEndDateForm = trainingEndDate

def get_totalCost(totalCost): #Passes totalCost
    global totalCostForm
    totalCostForm = totalCost

def get_workOrderLead(workOrderLead): #Passes workOrderLead
    global workOrderLeadForm
    workOrderLeadForm = workOrderLead

def get_companySupervisor(companySupervisor):
    global companySupervisorForm
    companySupervisorForm = companySupervisor

def get_workOrderManager(workOrderManager): #Passes workOrderManager
    global workOrderManagerForm
    workOrderManagerForm = workOrderManager


def populateForm(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    get_employeeEmail(employeeEmail)
    get_employeeName(employeeName)
    get_employerName(employerName)
    get_trainingTitle(trainingTitle)
    get_trainingPurpose(trainingPurpose)
    get_certification(certification)
    get_travelStartDate(travelStartDate)
    get_travelEndDate(travelEndDate)
    get_destination(destination)
    get_trainingStartDate(trainingStartDate)
    get_trainingEndDate(trainingEndDate)
    get_totalCost(totalCost)
    get_workOrderLead(workOrderLead)
    get_companySupervisor(companySupervisor)
    get_workOrderManager(workOrderManager)