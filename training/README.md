# Building AI Chatbots
## Conversational Interfaces (AWS Lex)
AWS Lex is the service used to build conversational interfaces, or chat bots. It is the critical entity between the customer and their device, and the backend architecture. More on AWS Lex [can be found here](https://aws.amazon.com/lex).

[1. Business Understanding and Business Case](#1-business-understanding-and-business-case)

### 1. Business Understanding and Business Case
Conversational bots are end to end voice and text automated communication, and engage the customer on everyday activities. For AWS Lex there are 8 different components that make up the entire solution as seen below:</br>
* **Speech to Intent** - This is the speech recognition engine and the natural language understanding engine which take care of consuming the voice captured and translating that into the "Intent" for which you design the bot to handle
* **Dialog Management** - part of the solution that maintains context (more later) and allows for variations of the dialogue to occur but still handle the "Intent"
* **Deployment** - deployment is referencing the simplicity of a one-click option and delivery of each bot, meaning that you can easily iterate and adjust as you go along. There is a simple UI that goes with AWS Lex
* **Scale** - scalability comes with AWS, but specifically Lex was designed to be auto-managed so whether you are processing 5 conversations or 10,000 the environment scales to handle the workload
* **Business Logic** - More to come on this. This part uses AWS Lambda which techncially is a serverless triggering service.
* **Security** - Security will be very important for us. According to docs the data passed back and forth is encrypted
* **Analytics** - This comes in the way of mostly monitoring and reporting to be able to see how the bot is working and being used. The way text and voice are captured, processed, and distributed by AWS services like Lex, allow us to get down to when and what was passed and if it was accepted
* **Text to Speech** - While AWS Lex handles the speech recognition and the natural language understanding, it uses AWS Polly to then send back the output from the bot as a computer generated voice. AWS Polly is provided as its own service with many capabilities

![lex_1](/training/aws_lex_arch_1.PNG)
</br>*Complete AWS Lex Solution and its 8 Core Components*

When a customer interacts with a chat bot they provide an "Intent" for which the chatbot was designed to accomodate. This is the action for which they are trying to complete whether it be checking the weather, finding out the bank balance, or setting up a scheduled appointment on their spouse's calendar. The **Intent** or action is what a chatbot was built to handle. With the chatbot engaged the customer then provides "Utterances" to initiate the task they would like to complete with it via text or voice. These **Utterances** or commands tell the chatbot what steps it needs to take next. Typically in the interaction additional detail is necessary and so the chatbot asks for the customer to fill "Slots" to better understand what its next step is. A chatbot's **Slots** or input data or details required to fulfill the action.

![lex_2](/training/aws_lex_arch_2.PNG)
</br>*Heirarchy of AWS Lex Chatbot Events*

![lex_3](/training/aws_lex_arch_3.PNG)

![lex_4](/training/aws_lex_arch_4.PNG)

![lex_5](/training/aws_lex_arch_5.PNG)

![lex_6](/training/aws_lex_arch_6.PNG)

![lex_7](/training/aws_lex_arch_7.PNG)
