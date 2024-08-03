import os
from dotenv import load_dotenv
import getpass
import smtplib

HOST = "smtp.gmail.com"
PORT = 587

load_dotenv()
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")

PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: Mail sent using python
Hi this is rev,

this is a test email

Thanks
rev"""

smtp = smtplib.SMTP(HOST, PORT)

status, res = smtp.ehlo()
print(f"[*] Echoing the server: {status} {res}")

status, res = smtp.starttls()
print(f"[*] Starting TLS connection: {status} {res}")

status, res = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status} {res}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()
