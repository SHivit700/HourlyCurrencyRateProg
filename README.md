Python-based software designed to send email updates on exchange rates between AED and GBP. The frequency of these emails is managed on Google Cloud Scheduler.

Create a config.ini file in below format:([email]
sender_email = ******
sender_password = ******
recipient_email = ******
)

Deployed on Google Cloud Services: 

-> Google Cloud Scheduler to run it periodically

-> Google Cloud Functions to store function as a link(https://asia-south2-currency-rate-email-program.cloudfunctions.net/get_currency_exchange_dhs_gbp)
