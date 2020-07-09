from CreateCertificate import Certificate
import smtplib, ssl, pickle
from sys import argv
import pandas as pd
import CreateEmail

####################################################################################
## All the required files for running the program like certificate template image ##
## and mail list csv file should be present inside a folder called "files". ########
####################################################################################

# Credentials
creds = pickle.load(open('creds.pickle', 'rb'))
sender_email = 'ram.mm2020@gmail.com'
password = creds[sender_email]

# Content for Email
Subject = "Webinar on Machine Learning practices on Forcasting and Planning"
Event = "Machine Learning practices on Forcasting and Planning"
Certificate_Template = 'template.jpg'
CertificateFileName = '_Certificate.pdf'

# Import Mailing list as CSV
# Make sure the column names are exactly the same as below
# 'Email' for email IDs, 'Name' for names
# 'Score' for scores if required

# Also create bathces if required since Gmail only allows to send
# 100 emails per day through API/SMTP
data = pd.read_csv(argv[1])

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)

    for index, row in data.iterrows():
        # Creating Certificate
        certificate = Certificate(f'files/{Certificate_Template}')
        certificate.add_text(
                        825,
                        "Certificate of Completion",
                        'red',
                        150,
                        'certificatebold.ttf')
        certificate.add_text(
                        1050,
                        "This certificate is proudly presented to", 'black',
                        70,
                        'CooperHewitt-Book.otf')
        certificate.add_text(
                        1145,
                        row.Name,
                        'black',
                        130,
                        'name.ttf')
        certificate.add_para(
                        1400,
                        f'For completing the webinar on "{Event}" conducted on June 22, 2020 Organized by "Christ College of Engineering and Technology". We appreciate your effort in protecting yourself and others in this pandemic.',
                        'black',
                        70,
                        'CooperHewitt-Book.otf')
        certificate.save(row.Name, CertificateFileName)

        # Creating the main message
        message = CreateEmail.Email(sender_email,
                        row.Name,
                        Subject,
                        CreateEmail.WebinarText(row.Name, Event),
                        f'files/{row.Name}{CertificateFileName}')

        server.sendmail(sender_email, row.Email, message)
        print (f'Mail Sent to {row.Name}')
    server.quit()