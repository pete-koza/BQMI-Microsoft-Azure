from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage

def sendRequestApprovalWOL(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    try:
        port = 587  # For SSL
        password = "tempPass"
        sender_email = "no-reply-traveltraining@outlook.com"
        
        workOrderLead = workOrderLead.split(', ')[1]


        message = MIMEText("This is a test email")
        message['Subject'] = "Travel/Training Request Approval Required By Work Order Lead"
        message['From'] = sender_email
        message['To'] = workOrderLead

        server = smtplib.SMTP("smtp-mail.outlook.com", port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, workOrderLead, message.as_string()) # WorkOrderLead Email

        print('Emails Sent')
        server.quit()
        
    except Exception as ex:
        print ("Something went wrong….",ex)

def sendRequestApprovalCS(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    try:
        port = 587  # For SSL
        password = "tempPass"
        sender_email = "no-reply-traveltraining@outlook.com"
        
        companySupervisor = companySupervisor.split(', ')[1]


        message = MIMEText("This is a test email")
        message['Subject'] = "Travel/Training Request Approval Required By Company Supervisor"
        message['From'] = sender_email
        message['To'] = companySupervisor

        server = smtplib.SMTP("smtp-mail.outlook.com", port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, companySupervisor, message.as_string()) # CompanySupervisor Email

        print('Emails Sent')
        server.quit()
        
    except Exception as ex:
        print ("Something went wrong….",ex)

def sendRequestApprovalWOM(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, workOrderLead, companySupervisor, workOrderManager):
    try:
        port = 587  # For SSL
        password = "tempPass"
        sender_email = "no-reply-traveltraining@outlook.com"
        
        workOrderManager = workOrderManager.split(', ')[1]


        message = MIMEText("This is a test email")
        message['Subject'] = "Travel/Training Request Approval Required By Work Order Manager"
        message['From'] = sender_email
        message['To'] = workOrderManager

        server = smtplib.SMTP("smtp-mail.outlook.com", port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, workOrderManager, message.as_string()) # WorkOrderManager Email

        print('Emails Sent')
        server.quit()
        
    except Exception as ex:
        print ("Something went wrong….",ex)