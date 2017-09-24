from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
import csv
app=Flask(__name__)
@app.route("/record",methods=['GET','POST'])
def conservation():
    response=VoiceResponse()
    response.say("Welcome to loan section.",voice='alice')
    response.say("Please tell your Phone number.",voice='alice')
    response.record()
    loanee_phone_number=str(response)
    response.say("What product category are you planing to produce.",voice='alice')
    response.record()
    product_category=str(response)
    response.say("How much amount do you want to lend.",voice='alice')
    response.record()
    principle_amt=float(str(response))
    response.say("For how many years.",voice='alice')
    response.record()
    time=float(str(response))
    # Interest Rates
    interest=(principle_amt*time*interest_rate)/100
    response.say("The interest for one year is"+interest,voice='alice')
    response.say("Do you want to avail the loan",voice='alice')
    response.say("1 for yes and 2 for no",voice='alice')
    reponse.record()
    choice=int(str(response))
    if(choice==1):
        list=[]
        list.extend([loanee_phone_number,product_category,principle_amt,time,interest_rate,interest,"Pending"])
        f=open("Loan Details.csv",'a')
        with f:
            writer=csv.writer(f)
            writer.writerows(list)
        response.say("You will be soon contacted for further process",voice='alice')     
    if(choice==0):
        response.say("Thanks for using Amazon Loan Services",voice='alice')
    reponse.hangup()
if __name__=="__main__":
    app.run(debug=True)    
        
