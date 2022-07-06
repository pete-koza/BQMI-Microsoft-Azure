import sqlite3 as sql
import pyodbc as pyo
import os
from os.path import join, dirname, abspath

# conn = pyo.connect('Database/TravelTraining.db')

connString = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:pip-it-sharepoint-prod-eastus.database.windows.net,1433;Database=Travel Training;Uid=pkoza;Pwd=xAgLBmu#7bSeeYt;"
conn = pyo.connect(connString)
cursor = conn.cursor()


cursor.execute("Select [Employee], [Email] From [dbo].[Employees & Emails]")

rows = cursor.fetchall()

employeeList = ["Azure Connected"]
for row in rows:
    employeeList.append('' + str(row[0]) + ', ' + str(row[1]))
    employeeList.sort()
employerList = ["Aerodyne", "BQMI", "COMSAT", "DB Consulting", "Insight Global", "Peerless", "V2 Technologies"]
employerList.sort()


cursor.close()
conn.close()

def submit_New_Request(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    conn = pyo.connect(connString)
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO [dbo].[In Progress Requests] ('Approval Status', 'Employee', 'Employer', 'Training Title', 'Request Purpose', 'Certification', 'Travel Start Date', 'Travel End Date', 'Destination', 'Training Start Date', 'Training End Date', 'Total Cost', 'Work Order Lead', 'Company Supervisor', 'Work Order Manager') VALUES ('In Progress', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(employeeName), str(employerName), str(trainingTitle), str(trainingPurpose), str(certification), str(travelStartDate), str(travelEndDate), str(destination), str(trainingStartDate), str(trainingEndDate), str(totalCost), str(workOrderLead), str(companySupervisor), str(workOrderManager)))

    cursor.execute("INSERT INTO [dbo].[In Progress Requests] ([Approval Status], [Employee],[Employee Email], [Employer], [Training Title], [Training Purpose], [Certification], [Travel Start Date], [Travel End Date], [Destination], [Training Start Date], [Training End Date], [Total Cost], [Work Order Lead], [Company Supervisor], [Work Order Manager]) VALUES ('In Progress', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(employeeName), str(employeeEmail), str(employerName), str(trainingTitle), str(trainingPurpose), str(certification), str(travelStartDate), str(travelEndDate), str(destination), str(trainingStartDate), str(trainingEndDate), str(totalCost), str(workOrderLead), str(companySupervisor), str(workOrderManager)))

    conn.commit()

    cursor.close()
    conn.close()

def loadReqs():
    conn = sql.connect('Database/TravelTraining.db')
    cursor = conn.cursor()
    cursor.execute("SELECT RequestID, Employee FROM 'In Progress Requests'")

    nR = cursor.fetchall()

    totalRequests = []
    for row in nR:
        totalRequests.append('' + str(row[0]) + ', ' + str(row[1]))

    cursor.close()
    conn.close()

    return totalRequests