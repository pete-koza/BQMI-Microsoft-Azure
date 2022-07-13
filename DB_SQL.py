import pyodbc as pyo

searchResults = []

try:
    connString = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:pip-it-sharepoint-prod-eastus.database.windows.net,1433;Database=Travel Training;Uid=pkoza;Pwd=xAgLBmu#7bSeeYt;"
    conn = pyo.connect(connString)
    cursor = conn.cursor()


    cursor.execute("Select [Employee Name], [Email] From [dbo].[Employees & Emails]")

    rows = cursor.fetchall()

    employeeList = []
    for row in rows:
        employeeList.append('' + str(row[0]) + ', ' + str(row[1]))
        employeeList.sort()
    employerList = ["Aerodyne", "BQMI", "COMSAT", "DB Consulting", "Insight Global", "Peerless", "V2 Technologies"]
    employerList.sort()

    projectCodes = []
    cursor.execute("SELECT [Number], [Title] FROM [dbo].[PACE Project Codes] Order BY [Number]")
    rows = cursor.fetchall()
    for row in rows:
        projectCodes.append('' + str(row[0]) + ' - ' + str(row[1]))

    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)
    employeeList = ["**Working in offline mode. Database not loaded**", "**Test Email**, pkoza@bqmi.com", "Jake Parrish, jparrish@bqmi.com", "Joe Homan, jhoman@bqmi.com", "Ty Kujawa, tkujawa@bqmi.com", "Joe Banks,, jbanks@bqmi.com"]
    employerList = ["Aerodyne", "BQMI", "COMSAT", "DB Consulting", "Insight Global", "Peerless", "V2 Technologies"]
    employerList.sort()
    projectCodes = ["01.01.01 - Test Code", "01.02.03 - Test Code 2"]

def submit_New_Request(employeeName, employeeEmail, employerName, projectCode, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager, trainingCost, tripMIE, tripLodging, lodgingTF, autoMileage, carRental, groundTrans, estFuel, estAirfair, baggage, other):
    try:
        conn = pyo.connect(connString)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO [dbo].[In Progress Requests] ([Approval Status], [Employee],[Employee Email], [Employer], [Training Title], [Training Purpose], [Certification], [Travel Start Date], [Travel End Date], [Destination], [Training Start Date], [Training End Date], [Total Cost], [Work Order Lead], [Company Supervisor], [Work Order Manager], [Training Cost], [Trip M&IE], [Trip Lodging], [Trip Lodging T&F], [Round-trip Auto Mileage], [Car Rental Price], [Ground Transportation], [Est. Fuel], [Est. Airfare], [Baggage], [Other]) VALUES ('In Progress', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(employeeName), str(employeeEmail), str(employerName), str(trainingTitle), str(trainingPurpose), str(certification), str(travelStartDate), str(travelEndDate), str(destination), str(trainingStartDate), str(trainingEndDate), str(totalCost), str(workOrderLead), str(companySupervisor), str(workOrderManager), str(trainingCost), str(tripMIE), str(tripLodging), str(lodgingTF), str(autoMileage), str(carRental), str(groundTrans), str(estFuel), str(estAirfair), str(baggage), str(other)))

        conn.commit()

        cursor.close()
        conn.close()
    except:
        print("**Working in offline mode. Database access prevented")

def genSearchReq(employee, employer, projectCode):
    try:
        global searchResults
        conn = pyo.connect(connString)
        cursor = conn.cursor()
        if(employee == None and employer == None and projectCode == None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests]")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)
        elif(employee is not None and employer == None and projectCode == None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests] WHERE [Employee] = '" + employee + "'")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)
        elif(employee == None and employer is not None and projectCode == None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests] WHERE [Employer] = '" + employer + "'")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)
        elif(employee == None and employer == None and projectCode is not None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests] WHERE [Project Code] = '" + projectCode + "'")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)
        elif(employee is not None and employer is not None and projectCode == None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests] WHERE [Employee] = '" + employee + "' AND [Employer] = '" + employer + "'")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)
        elif(employee is not None and employer == None and projectCode is not None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests] WHERE [Employee] = '" + employee + "' AND [Project Code] = '" + projectCode + "'")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)
        elif(employee == None and employer is not None and projectCode is not None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests] WHERE [Employer] = '" + employer + "' AND [Project Code] = '" + projectCode + "'")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)
        elif(employee is not None and employer is not None and projectCode is not None):
            cursor.execute("SELECT * FROM [dbo].[In Progress Requests] WHERE [Employee] = '" + employee + "' AND [Employer] = '" + employer + "' AND [Project Code] = '" + projectCode + "'")
            rows = cursor.fetchall()
            for row in rows:
                searchResults.append(row)


        cursor.close()
        conn.close()
        return searchResults
    except:
        print("**Working in offline mode. Database access prevented")
