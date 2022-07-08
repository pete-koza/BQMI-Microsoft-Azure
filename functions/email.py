import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def sendRequestApprovalWOL(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, trainingCost, workOrderLead, companySupervisor, workOrderManager):
    try:
        port = 587  # For SSL
        password = "tempPass"
        sender_email = "no-reply-traveltraining@outlook.com"
        
        companySupervisor = companySupervisor.split(', ')[1]

        content = (employeeName + ' is requesting approval for ' + trainingTitle + '.\n'
        + 'Details are as follows:\n\n' 
        +'Employee: ' + employeeName + '\n' 
        + 'Employer: ' + employerName + '\n'
        + 'Work Order Lead: ' + workOrderLead + '\n'
        + 'Company Supervisor: ' + companySupervisor + '\n'
        + 'Work Order Manager: ' + workOrderManager + '\n'
        + 'Project Code: ' + '\n' 
        + 'Purpose: ' + trainingPurpose + '\n'
        + 'Training Title: ' + trainingTitle + '\n'
        + 'Training Dates: ' + trainingStartDate + '--' + trainingEndDate + '\n'
        + 'Certification? (Y / N): ' + certification + '\n'
        + 'Destination: ' + destination + '\n'
        + 'Days of Travel: ' + travelStartDate + '--' + travelEndDate + '\n'
        + 'Total Cost of Training: ' + str(trainingCost) + '\n'
        + 'Total Cost of Trip: ' + str(totalCost))

        message = MIMEMultipart()
        message['Subject'] ="Approval for " + trainingTitle + " Required By Work Order Lead for " + employeeName
        message['From'] = sender_email
        message['To'] = companySupervisor

        message.attach(MIMEText(content))
    
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp-mail.outlook.com", port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, companySupervisor, message.as_string()) # CompanySupervisor Email
            server.quit()

        print('Emails Sent')
        
        
    except Exception as ex:
        print ("Something went wrong….",ex)

def sendRequestApprovalCS(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, totalCost, trainingCost, workOrderLead, companySupervisor, workOrderManager):
    try:
        port = 587  # For SSL
        password = "tempPass"
        sender_email = "no-reply-traveltraining@outlook.com"
        
        companySupervisor = companySupervisor.split(', ')[1]

        content = (employeeName + ' is requesting approval for ' + trainingTitle + '.\n'
        + 'Details are as follows:\n\n' 
        +'Employee: ' + employeeName + '\n' 
        + 'Employer: ' + employerName + '\n'
        + 'Work Order Lead: ' + workOrderLead + '\n'
        + 'Company Supervisor: ' + companySupervisor + '\n'
        + 'Work Order Manager: ' + workOrderManager + '\n'
        + 'Project Code: ' + '\n' 
        + 'Purpose: ' + trainingPurpose + '\n'
        + 'Training Title: ' + trainingTitle + '\n'
        + 'Training Dates: ' + trainingStartDate + '--' + trainingEndDate + '\n'
        + 'Certification? (Y / N): ' + certification + '\n'
        + 'Destination: ' + destination + '\n'
        + 'Days of Travel: ' + travelStartDate + '--' + travelEndDate + '\n'
        + 'Total Cost of Training: ' + str(trainingCost) + '\n'
        + 'Total Cost of Trip: ' + str(totalCost))

        message = MIMEMultipart()
        message['Subject'] ="Approval for " + trainingTitle + " Required By Company Supervisor for " + employeeName
        message['From'] = sender_email
        message['To'] = companySupervisor

        message.attach(MIMEText(content))
    
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp-mail.outlook.com", port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, companySupervisor, message.as_string()) # CompanySupervisor Email
            server.quit()

        print('Emails Sent')
        
        
    except Exception as ex:
        print ("Something went wrong….",ex)

def sendRequestApprovalWOM(employeeName, employeeEmail, employerName, trainingTitle, trainingPurpose, certification, travelStartDate, travelEndDate, destination, trainingStartDate, trainingEndDate, trainingCost, totalCost, workOrderLead, companySupervisor, workOrderManager):
    try:
        port = 587  # For SSL
        password = "tempPass"
        sender_email = "no-reply-traveltraining@outlook.com"
        
        companySupervisor = companySupervisor.split(', ')[1]

        content = (employeeName + ' is requesting approval for ' + trainingTitle + '.\n'
        + 'Details are as follows:\n\n' 
        +'Employee: ' + employeeName + '\n' 
        + 'Employer: ' + employerName + '\n'
        + 'Work Order Lead: ' + workOrderLead + '\n'
        + 'Company Supervisor: ' + companySupervisor + '\n'
        + 'Work Order Manager: ' + workOrderManager + '\n'
        + 'Project Code: ' + '\n' 
        + 'Purpose: ' + trainingPurpose + '\n'
        + 'Training Title: ' + trainingTitle + '\n'
        + 'Training Dates: ' + trainingStartDate + '--' + trainingEndDate + '\n'
        + 'Certification? (Y / N): ' + certification + '\n'
        + 'Destination: ' + destination + '\n'
        + 'Days of Travel: ' + travelStartDate + '--' + travelEndDate + '\n'
        + 'Total Cost of Training: ' + str(trainingCost) + '\n'
        + 'Total Cost of Trip: ' + str(totalCost))

        message = MIMEMultipart()
        message['Subject'] ="Approval for " + trainingTitle + " Required By Work Order Manager for " + employeeName
        message['From'] = sender_email
        message['To'] = companySupervisor

        message.attach(MIMEText(content))
    
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp-mail.outlook.com", port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, companySupervisor, message.as_string()) # CompanySupervisor Email
            server.quit()

        print('Emails Sent')
        
        
    except Exception as ex:
        print ("Something went wrong….",ex)
