# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:33:29 2020

@author: bishw
"""

import streamlit as st
import pandas as pd
from datetime import timedelta
import os
from smtplib import SMTP
from email.mime.text import MIMEText
from pretty_html_table import build_table
from email.mime.multipart import MIMEMultipart
import dummy_bank_credentials
cred = dummy_bank_credentials.credentials

st.title("SMART NOTIFICATIONS")

st.subheader("Enter Details")

def write_to_db(Primary_Name,Secondary_Name,Bank_Name,Matured_Amount,Maturity_Date):
    if os.path.isfile('Bank_Maturity.xlsx') == False:
        df = pd.DataFrame([[Primary_Name,Secondary_Name,Bank_Name,Matured_Amount,Maturity_Date]],
                          columns=['Primary_Name','Secondary_Name','Bank_Name','Matured_Amount','Maturity_Date'])
        df['Email_Trigger_Date ']= Maturity_Date - timedelta(days=7)
        df.to_excel('Bank_Maturity.xlsx', index=False)
    else:
        df = pd.read_excel('Bank_Maturity.xlsx')
        df = df.append(pd.DataFrame({'Primary_Name':Primary_Name,'Secondary_Name':Secondary_Name,'Bank_Name':Bank_Name,'Matured_Amount':Matured_Amount,'Maturity_Date':Maturity_Date}, index = [0]), ignore_index=False)
        df['Email_Trigger_Date ']= Maturity_Date - timedelta(days=7)
        df.to_excel('Bank_Maturity.xlsx',index=False)
    st.subheader("New Entry")
    st.table(df.iloc[-1:,:])

def send_email(recipients):
    df = pd.read_excel('Bank_Maturity.xlsx')
    body = build_table(df, 'orange_light')
    SENDER = cred.get('SENDER')
    PASSWORD = cred.get('PASSWORD')
    for r in cred.get('RECEPIENT'):
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


def details_input():
    Primary_Name = st.text_input("Enter Primary Account Holder Name")
    Secondary_Name = st.text_input("Enter Sencondary Account Holder Name")
    Bank_Name = st.text_input("Enter Bank Name")
    Matured_Amount = st.text_input("Enter Maturity Amount")
    Maturity_Date = st.date_input("Enter Maturity Date")
    if st.button("Submit"):
        write_to_db(Primary_Name,Secondary_Name,Bank_Name,Matured_Amount,Maturity_Date)
    st.sidebar.title("Details")
    add_selectbox = st.sidebar.selectbox('Would You Like to see all the Data?',('No', 'Yes'))
    if add_selectbox == 'Yes':
        try:
            df = pd.read_excel("Bank_Maturity.xlsx")
            st.write("DETAILS")
            st.table(df)
        except Exception:
            st.write("File Not Found")
    add_selectbox = st.sidebar.selectbox('Would You email this data?',('No', 'Yes'))
    if add_selectbox == 'Yes':
            send_email(["rinabiswas1972@gmail.com","bishwarup1429@gmail.com"])

if __name__=="__main__":
    details_input()


