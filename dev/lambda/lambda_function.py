########################################
#this is the sample python 3.6 lambda function blueprint code
#I called mine steveohello
#to execute this in the Lambda Management Console you must save the code and then configure the basic test event and then TEST
#This tutorial https://www.youtube.com/watch?v=hzlxWBs1Qt4 covers it (just first 8 minutes)
########################################
import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    

    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
