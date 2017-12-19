# Conversational Bot Training 
## AWS Lex
[1. Business Understanding and Business Case](#1-business-understanding-and-business-case)


### 1. Business Understanding and Business Case
Conversational bots are end to end, and engage the customer. There are 8 different components that make up the entire solution as seen below:</br>
* **Speech to Intent** - This is the speech recognition engine and the natural language understanding engine which take care of consuming the voice captured and translating that into the "Intent" for which you design the bot to handle
* **Dialog Management** - part of the solution that maintains context (more later) and allows for variations of the dialogue to occur but still handle the "Intent"
* **Deployment** - deployment is referencing the simplicity of a one-click option and delivery of each bot, meaning that you can easily iterate and adjust as you go along. There is a simple UI that goes with AWS Lex
* **Scale** - scalability comes with AWS, but specifically Lex was designed to be auto-managed so whether you are processing 5 conversations or 10,000 the environment scales to handle the workload
* **Business Logic** - More to come on this. This part uses AWS Lambda which techncially is a serverless triggering service.
* **Security** - Security will be very important for us. According to docs the data passed back and forth is encrypted
* **Analytics** - This comes in the way of mostly monitoring and reporting to be able to see how the bot is working and being used. The way text and voice are captured, processed, and distributed by AWS services like Lex, allow us to get down to when and what was passed and if it was accepted
* **Text to Speech** - While AWS Lex handles the speech recognition and the natural language understanding, it uses AWS Polly to then send back the output from the bot as a computer generated voice. AWS Polly is provided as its own service with many capabilities

![](https://github.com/sdrohrer/lexflex/blob/master/training/aws_lex_arch_1.PNG)
</br>*Complete Solution Diagram*

![](https://github.com/sdrohrer/lexflex/blob/master/training/aws_lex_arch_2.PNG "Complete Solution Diagram 1")

![](https://github.com/sdrohrer/lexflex/blob/master/training/aws_lex_arch_3.PNG "Complete Solution Diagram 1")

![](https://github.com/sdrohrer/lexflex/blob/master/training/aws_lex_arch_4.PNG "Complete Solution Diagram 1")

![](https://github.com/sdrohrer/lexflex/blob/master/training/aws_lex_arch_5.PNG "Complete Solution Diagram 1")

![](https://github.com/sdrohrer/lexflex/blob/master/training/aws_lex_arch_6.PNG "Complete Solution Diagram 1")


![](https://github.com/sdrohrer/lexflex/blob/master/training/aws_lex_arch_7.PNG "Complete Solution Diagram 1")
