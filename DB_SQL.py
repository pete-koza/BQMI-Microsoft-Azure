import sqlite3 as sql
import os
from os.path import join, dirname, abspath

conn = sql.connect('Database/TravelTraining.db')
cursor = conn.cursor()


cursor.execute("Select Employee, Email From Employees")

rows = cursor.fetchall()

employeeList = []
for row in rows:
    employeeList.append('' + str(row[0]) + ', ' + str(row[1]))
    employeeList.sort()
employerList = ["Aerodyne", "BQMI", "COMSAT", "DB Consulting", "Insight Global", "Peerless", "V2 Technologies"]
employerList.sort()

cursor.close()
conn.close()

def submit_New_Request(employeeName, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    conn = sql.connect('Database/TravelTraining.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO 'In Progress Requests' ('Approval Status', 'Employee', 'Employer', 'Training Title', 'Request Purpose', 'Certification', 'Travel Start Date', 'Travel End Date', 'Destination', 'Training Start Date', 'Training End Date', 'Total Cost', 'Work Order Lead', 'Company Supervisor', 'Work Order Manager') VALUES ('In Progress', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(employeeName), str(employerName), str(trainingTitle), str(trainingPurpose), str(certification), str(travelStartDate), str(travelEndDate), str(destination), str(trainingStartDate), str(trainingEndDate), str(totalCost), str(workOrderLead), str(companySupervisor), str(workOrderManager)))
    conn.commit()

    
    
    
    print(employeeName, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager)

    cursor.close()
    conn.close()