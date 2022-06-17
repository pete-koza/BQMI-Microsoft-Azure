
from flask import Flask, render_template, request
from dash import dash, dcc, html, Input, Output, callback
from datetime import datetime
import pandas as pd
import pyodbc as pyo


server = Flask(__name__)
app = dash.Dash(__name__)

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



# @app.callback(
#     Output('Travel-Total', 'children'),
#     Output('Total-Cost', 'children'),
#     Input('Training-Cost', 'value'),
#     Input('75-MIE-Rate', 'value'),
#     Input('MIE-Rate', 'value'),
#     Input('Lodging-Rate', 'value'),
#     Input('Est-Per-Diem', 'value'),
#     Input('Est-Lodge-Tax-Fees', 'value'),
#     Input('Round-Milage-Cost', 'value'),
#     Input('Est-Ground-Trans-Fees', 'value'),
#     Input('Est-Airfare-Price', 'value'),
#     Input('Baggage-Fees', 'value'),
#     Input('Est-Car-Rental-Price', 'value'),
#     Input('Est-Fuel-Cost', 'value'),
#     Input('Other-Cost', 'value'),
# )
@server.route("/")
def main():
    # Training_Cost, MIE_Rate_75, MIE_Rate, Lodging_rate, Est_Per_Diem, Est_Lodge_Tax_Fees, Round_Mileage_Cost, Est_Ground_Trans_Fees, Est_Airfair_Price, Baggage_Fees, Est_Car_Rental_Price, Est_Fuel_Price, Other_Cost
    return render_template("index.html", employeeList=employeeList, employeeListLength=len(employeeList), employerList=employerList, employerListLength=len(employerList))

@server.route("/form", methods=["POST"])
def form():
    Employee_Name = request.form.get("Employee-Name")
    Employer_Name = request.form.get("Employer-Name")
    Work_Order_Lead = request.form.get("Work-Order-Lead")
    Company_Supervisor = request.form.get("Company-Supervisor")
    Work_Order_Manager = request.form.get("Work-Order-Manager")
    Purpose_For_Request = request.form.get("Purpose-For-Request")
    Training_Title = request.form.get("Training-Title")
    Training_Start_Date = request.form.get("Training-Start-Date")
    Training_End_Date = request.form.get("Training-End-Date")
    Certification = request.form.get("Certification")
    Travel_City = request.form.get("Travel-City")
    Travel_State = request.form.get("Travel-State")
    Travel_Start_Date = request.form.get("Travel-Start-Date")
    Travel_End_Date = request.form.get("Travel-End-Date")
    Training_Cost = request.form.get("Training-Cost")
    MIE_Rate_75 = request.form.get("75-MIE-Rate")
    MIE_Rate = request.form.get("MIE-Rate")
    Lodging_Rate = request.form.get("Lodging-Rate")
    Est_Per_Diem = request.form.get("Est-Per-Diem")
    Est_Lodge_Tax_Fees = request.form.get("Est-Lodge-Tax-Fees")
    Round_Mileage_Cost = request.form.get("Round-Mileage-Cost")
    Est_Ground_Trans_Fees = request.form.get("Est-Ground-Trans-Fees")
    Est_Airfare_Price = request.form.get("Est-Airfare-Price")
    Baggage_Fees = request.form.get("Baggage_Fees")
    Est_Car_Rental_Price = request.form.get("Est-Car-Rental-Price")
    Est_Fuel_Cost = request.form.get("Est-Fuel-Cost")
    Other_Cost = request.form.get("Other-Cost")
    return render_template("form.html", Employee_Name=Employee_Name, Employer_Name=Employer_Name, Work_Order_Lead=Work_Order_Lead, Company_Supervisor=Company_Supervisor, Work_Order_Manager=Work_Order_Manager, Purpose_For_Request=Purpose_For_Request, Training_Title=Training_Title, Training_Start_Date=Training_Start_Date, Training_End_Date= Training_End_Date, Certification=Certification, Travel_City=Travel_City, Travel_State=Travel_State, Travel_Start_Date=Travel_Start_Date, Travel_End_Date=Travel_End_Date, Training_Cost=Training_Cost, MIE_Rate_75=MIE_Rate_75, MIE_Rate=MIE_Rate, Lodging_Rate=Lodging_Rate, Est_Per_Diem=Est_Per_Diem, Est_Lodge_Tax_Fees=Est_Lodge_Tax_Fees, Round_Mileage_Cost=Round_Mileage_Cost, Est_Ground_Trans_Fees=Est_Ground_Trans_Fees, Est_Airfare_Price=Est_Airfare_Price, Baggage_Fees=Baggage_Fees, Est_Car_Rental_Price=Est_Car_Rental_Price, Est_Fuel_Cost=Est_Fuel_Cost, Other_Cost=Other_Cost)

cursor.close()