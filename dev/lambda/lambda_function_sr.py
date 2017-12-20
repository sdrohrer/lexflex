########################################
#this is the sample python 3.6 lambda function blueprint code
#I called mine steveohello
#to execute this in the Lambda Management Console you must save the code and then configure the basic test event and then TEST
#This tutorial https://www.youtube.com/watch?v=hzlxWBs1Qt4 covers it (just first 8 minutes)
########################################
import json
# you import the json package to use this

print('Loading function')

#lambda takes a few inputs, so far I only understand event as the trigger
#not sure about context or callback which is not mentioned yet
def lambda_handler(event, context):
    
    #ignore this print command for now
    ##print("Received event: " + json.dumps(event, indent=2))
    
    #these print commands only show up in the log
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    
    #this return command is ultimately the only thing rendered. meaning only the key1 passed to the class is output
    return event['key1']  # Echo back the first key value
    
    #ignore this raise command for now
    ##raise Exception('Something went wrong')
