import pandas as pd
from twilio.rest import Client
with open("Information_of_Orders.csv","r") as f:
    reader=csv.reader(f,delimiter=",")
    data=list(reader)
    row_count=len(data)
max=row_count+5
i=0
account_sid = "AC1a5567d64e9871034870d761ae88feb3"
auth_token = "4694e6fa59a2faf68918d2f108984fec"
client = Client(account_sid, auth_token)
df=pd.read_csv("Information_of_Orders.csv")
column=df['Phone No.']
message=client.api.account.messages.create(to=column[i++],from_="+1760-615-3758 ",body="The Discount time has started, please do list your products asap,first five will get discounts")
if(row_count<=max):
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
        response.say("Please tell your full address.",voice='alice')
        response.record()
        seller_address=str(response)
        response.say("What is your product category.",voice='alice')
        response.record()
        product_category=str(response)
        response.say("What is your product name.",voice='alice')
        response.record()
        product_name=str(response)
        response.say("What is the total weight of your goods.",voice='alice')
        response.record()
        product_weight=float(str(response))
        response.say("What is the price at which do you want to sell.",voice='alice')
        response.record()
        product_sp=flaot(str(response))
        response.say("What is cost of the product.",voice='alice')
        response.record()
        product_cp=float(str(response))
        response.say("Where do you want to sell.",voice='alice')
        response.say("1 Local",voice='alice')
        response.say("2 Regional",voice='alice')
        response.say("3 National",voice='alice')
        response.say("Say 1 or 2 or 3",voice='alice')
        response.record()
        selling_bounds=int(str(response))
        if((product_sp>=0)&(product_sp<=500)):
            fixed_closing_price=10
        if((product_sp>=500)&(product_sp<=1000)):
            fixed_closing_price=20
        if(product_sp>1000):
            fixed_closing_price=40
        #referral charges
        #shipping charges
        amazon_charges=fixed_closing_charges+referral_charges+shipping_charges
        gst_charges=0.18(amazon_charges)
        profit=product_sp-(product_cp+amazon_charges+gst_charges)    
        response.say("The profit you will make"+profit,voice='alice')
        response.hangup()
        list=[]
        list.extend([seller_phone_number,seller_address,product_category,product_name,product_weight,product_sp,selling_bounds,
                 fixed_closing_price,referral_charges,shipping_prices,amazon_charges,gst_charges,"Pending",0])
        f=open("information_of_Orders.csv",'a')
        with f:
            writer=csv.writer(f)
            writer.writerows(list)
    if __name__=="__main__":
        app.run(debug=True)
    row_count=row_count+1
i=0
account_sid = "AC1a5567d64e9871034870d761ae88feb3"
auth_token = "4694e6fa59a2faf68918d2f108984fec"
client = Client(account_sid, auth_token)
df=pd.read_csv("Information_of_Orders.csv")
column=df['Phone No.']
message=client.api.account.messages.create(to=column[i++],from_="+1760-615-3758 ",body="The discount time is over.Please try next time")


    
