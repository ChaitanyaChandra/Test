from datetime import date
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import zipfile
import sys
import pandas as pd


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "chandrachaitanya01@gmail.com"
SMTP_PASSWORD = "oquu qruh zqlv dhmg"

EMAIL_TO = ['majorchowdary@gmail.com', 'ChandraChaitanya@icloud.com']
EMAIL_FROM = "Chaitanya<chandrachaitanya01@gmail.com>"
EMAIL_SUBJECT = "Demo Email : "

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

DATA='This is the content of the email.'


# Function to zip all .txt files in a folder
def zip_txt_files(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.txt'):
                    zipf.write(os.path.join(root, file), file)


def send_email(attachment_path, body):
    msg = MIMEMultipart()
    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    msg.attach(MIMEText(body, 'html'))
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
        msg.attach(part)
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()




# df =  pd.DataFrame()
# cols = {
#     "f_name": "first name",
#     "l_name": "last name"
# }
#
# pd1 = pd.DataFrame({"Items": list(cols.keys())})
#
# print(pd1)
#
# data = {
#     "f_name": "chaitanya",
#     "l_name": "chandra"
# }
# pd1['one'] = pd1['Items'].map(data)
#
#
# body_data = f"<p>Please find the summary of drifted configuration information.</p>"
# k8s_table = pd1.to_html(index=False)
# body = f"""
# <html>
# <body>
#     <p>Team,</p>
#     {body_data}
#     <h3 style="color:gray;"><b>2) System Components Report:</b></h3>
#     {k8s_table}
#     <br>
#     <p>Regards,<br>HCC Kubernetes Team.</p>
# </body>
# </html>
# """
#
#
# pwd = os.getcwd()
# folder_path = f"{pwd}/files/consolidated/"
# zip_name = 'attachments.zip'
# zip_txt_files(folder_path, zip_name)
# send_email(zip_name, body)
