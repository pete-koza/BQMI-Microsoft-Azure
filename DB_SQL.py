import sqlite3



# serverRQ = "pip-it-sharepoint-prod-eastus.database.windows.net,1433"
# database = "Travel Training"
# username = "pkoza"
# password = "xAgLBmu#7bSeeYt"

# cnxn = pyo.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverRQ+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

# cursor.execute('SELECT TOP (1000) [Employee],[Email]FROM [dbo].[Employees & Emails]')
# rows = cursor.fetchall()
employeeList = ["Test Value"]
# for row in rows:
#     employeeList.append('' + str(row[0]) + ', ' + str(row[1]))
#     employeeList.sort()
employerList = ["Aerodyne", "BQMI", "COMSAT", "DB Consulting", "Insight Global", "Peerless", "V2 Technologies"]
# employerList.sort()




# def submit_New_Request(employeeName, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
#     cnxn = pyo.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+serverRQ+';DATABASE='+database+';UID='+username+';PWD='+ password)
#     cursorNew = cnxn.cursor()
#     cursorNew.execute("INSERT INTO [dbo].[In Progress Requests] ([Approval Status], [Employee], [Employer], [Training Title], [Training Purpose], [Certification], [Travel Start Date], [Travel End Date], [Destination], [Training Start Date], [Training End Date], [Total Cost], [Work Order Lead], [Company Supervisor], [Work Order Manager]) VALUES ('In Progress', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", employeeName, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager)
#     cursorNew.commit()

    
    
    
#     print(employeeName, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager)

#     cursorNew.close()
#     cnxn.close()

# cursor.close()
# cnxn.close()