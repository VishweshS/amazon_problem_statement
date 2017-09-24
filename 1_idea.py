import pandas
from flask import Flask,request,redirect
import twilio.twiml
import csv
from twilio.rest import TwilioRestClient
account_sid="AC1a5567d64e9871034870d761ae88feb3"
auth_token="4694e6fa59a2faf68918d2f108984fec"
client=TwilioRestClient(account_sid, auth_token)
app=Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def sender():
    from_number=request.values.get('From', None)
    sms_body=request.values.get('Body', None)
    i=0
    df=pd.read_csv("Information_of_Orders.csv")
    column=df['Phone No.']
    message = client.sms.messages.create(to=column[i++], from_="+1760-615-3758",body=sms_body+"Please reply LIKE if you find it useful")
if __name__ == "__main__":
    app.run(debug=True)
client=TwilioRestClient(account_sid, auth_token)
app=Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def sender():
    from_number1=request.values.get('From', None)
    sms_body1=request.values.get('Body', None)
    if(sms_body1=="LIKE"):
        with open("Information_of_Orders.csv",'rt') as f:
            reader=csv.reader(f,delimiter=',')
            for row in reader:
                if from_number==row[0]:
                    row[13]=row[13]+1

if __name__ == "__main__":
    app.run(debug=True)    
