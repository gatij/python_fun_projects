'''
Using Python 3.6 
For installation , use : pip install twilio
After signing up for account , you will get account_sid and auth_token with your registed number.
 
to="valid number" (valid num. means number should have prefix code"
'''
 
from twilio.rest import Client
account_sid = "AC10c93aeb6b4d3cd58630fa0146ef5d88"
auth_token = "1b23a70d94520ab37880d2bdfef015f6"
client = Client(account_sid, auth_token)
message = client.api.account.messages.create(to="+919479604287",from_="+16266244213",body="from twilio using pyscript!")