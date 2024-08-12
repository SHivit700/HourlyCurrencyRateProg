import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from forex_python.converter import CurrencyRates
from datetime import datetime
import time
import requests

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'shivit2004@gmail.com'  # Replace with your Gmail address
SENDER_PASSWORD = 'jako jmlh zocf ttye'  # Replace with your App Password or Gmail password
RECIPIENT_EMAIL = 'shivit2004@gmail.com'  # Replace with the recipient's email

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def get_transfer_rate(amount_in_aed):
    api_url = f"https://api.exchangerate-api.com/v4/latest/AED"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Ensure we catch HTTP errors
        data = response.json()
        exchange_rate = data['rates']['GBP']
        amount_in_gbp = amount_in_aed * exchange_rate
        return exchange_rate, amount_in_gbp
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request error: {e}")
        return None, None
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

def send_hourly_transfer_rate():
    amount_in_aed = 190000
    while True:
        exchange_rate, amount_in_gbp = get_transfer_rate(amount_in_aed)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if exchange_rate is not None and amount_in_gbp is not None:
            subject = "Hourly Currency Rate Update"
            body = (f"{current_time}\n {exchange_rate:.4f} AED to GBP.\n"
                    f"{amount_in_aed} AED is equivalent to {amount_in_gbp:.2f} GBP.")
            print(body)
            send_email(subject, body)
        else:
            print(f"As of {current_time}, the exchange rate could not be retrieved.")

if __name__ == "__main__":
    send_hourly_transfer_rate()
