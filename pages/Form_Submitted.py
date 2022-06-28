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


# employeeName, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager



def displayFormRequest(employeeName, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    print(employeeName)