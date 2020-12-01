# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:43:09 2020

@author: bishw
"""
from smtplib import SMTP
from email.mime.text import MIMEText
from pretty_html_table import build_table
from email.mime.multipart import MIMEMultipart
import pandas as pd

def send_email(recipients):
    df = pd.read_excel('Bank_Manurity.xlsx')
    body = build_table(df, 'orange_light')
    SENDER = "notification.maturity.bank@gmail.com"
    PASSWORD = "notification.maturity.bank1429"
    for r in recipients:
        message = MIMEMultipart()
        message['Subject'] = 'SMART NOTIFICATION - Maturity Amount Alert!!'
        message['From'] = SENDER
        message['To'] = r
        body_content = body
        message.attach(MIMEText(body_content, "html"))
        msg_body = message.as_string()
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER, PASSWORD)
        server.sendmail(message['From'], message['To'], msg_body)
        server.quit()
        print("Email sent!")
if __name__ == '__main__':
    send_email(["rinabiswas1972@gmail.com","bishwarup1429@gmail.com"])