from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import csv
app=Flask(__name__)
@app.route("/record",methods=['GET','POST'])
def conservation():
    response=VoiceResponse()
    response.say("Welcome to Amazon Seller Centre.",voice='alice')
    response.say("Please tell your Phone number.",voice='alice')
    response.record()
    seller_phone_number=str(response)
    response.say("Do you have any referral code If yes press 1 or press 0",voice='alice')
    response.record()
    choice=int(str(response))
    if(choice==1):
        say.response("Please tell your reference's phone number",voice='alice')
        response.record()
        reference_phone_number=str(response)
        with open("Information_of_Orders.csv",'rt') as f:
            reader=csv.reader(f,delimiter=',')
            for row in reader:
                if reference_phone_number==row[0]:
                    row[13]=row[13]+1
    response.hangup()
if __name__=="__main__":
    app.run(debug=True)
   
            
     
