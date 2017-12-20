# Business Understanding for Building AI Chatbots in the Cloud (AWS Lex)
AWS Lex is the service used to build conversational interfaces, or chat bots. It is the critical entity between the customer and their device, and the backend architecture. More on AWS Lex [can be found here](https://aws.amazon.com/lex). The details below were extrapolated from the [following video by AWS](https://youtu.be/qe9nRU6ZHAI).

[1. 8 Components to AWS Lex: What you need to know](#8-components-to-aws-lex)</br>
[2. Event mapping within a chatbot on AWS Lex:  Understanding the process](#event-mapping-within-a-chatbot-on-aws-lex)</br>
[3. Chatbot example use cases using AWS Lex:  Food for thought](#chatbot-example-use-cases-using-aws-lex)<br/>
[4. Capturing Conversation Context:  A ton of data is collected](#capturing-conversation-context)


## 8 Components to AWS Lex
Conversational bots are end to end voice and text automated communication, and engage the customer on everyday activities. For AWS Lex there are 8 different components that make up the entire solution as seen below:</br>
1. **Speech to Intent** - This is the speech recognition engine and the natural language understanding engine which take care of consuming the voice captured and translating that into the "Intent" for which you design the bot to handle
2. **Dialog Management** - part of the solution that maintains context (more later) and allows for variations of the dialogue to occur but still handle the "Intent"
3. **Deployment** - deployment is referencing the simplicity of a one-click option and delivery of each bot, meaning that you can easily iterate and adjust as you go along. There is a simple UI that goes with AWS Lex
4. **Scale** - scalability comes with AWS, but specifically Lex was designed to be auto-managed so whether you are processing 5 conversations or 10,000 the environment scales to handle the workload
5. **Business Logic** - More to come on this. This part uses AWS Lambda which techncially is a serverless triggering service.
6. **Security** - Security will be very important for us. According to docs the data passed back and forth is encrypted
7. **Analytics** - This comes in the way of mostly monitoring and reporting to be able to see how the bot is working and being used. The way text and voice are captured, processed, and distributed by AWS services like Lex, allow us to get down to when and what was passed and if it was accepted
8. **Text to Speech** - While AWS Lex handles the speech recognition and the natural language understanding, it uses AWS Polly to then send back the output from the bot as a computer generated voice. AWS Polly is provided as its own service with many capabilities

![lex_1](/docs/images/aws_lex_arch_1.PNG)
</br>*Complete AWS Lex Solution and its 8 Core Components*

## Event Mapping within a Chatbot on AWS Lex 
When a customer interacts with a chatbot they provide an "Intent" for which the chatbot was designed to accomodate. This is the action for which they are trying to complete whether it be checking the weather, finding out the bank balance, or setting up a scheduled appointment on their spouse's calendar. The **Intent** or action is what a chatbot was built to handle. With the chatbot engaged the customer then provides "Utterances" to initiate the task they would like to complete with it via text or voice. These **Utterances** or commands tell the chatbot what steps it needs to take next. Typically in the interaction additional detail is necessary and so the chatbot asks for the customer to fill "Slots" to better understand what its next step is. A chatbot's **Slots** or input data are details required to fulfill the action. Lastly the chatbot performs "Fulfillment" and the "Intent" is completed or awaiting the next "Utterance." Here the **Fullfillment** is just the intended and desired action that the chatbot finally completes.

* A **Chatbot** can have many **Intents**
* An **Intent** can have many **Utterances**
  - An **Utterance** initiates an **Intent**
  - An **Utterance** can switch the **Intent**
* An **Utterance** can have many **Utterances** 
* An **Utterance** can require a  **Slot**
* A **Slot** can have an **Utterance** or a **Fulfillment**
* A **Fulfillment** returns to the **Chatbot**

![lex_2](/docs/images/aws_lex_arch_2.PNG)
</br>*Heirarchy of AWS Lex Chatbot Events*

## Chatbot example use cases using AWS Lex
The following use cases are good examples to get a better understanding of how the chatbot events work together to provide an entire experience outside of just getting the local weather.

### Employee Assistant Bot
1. **Welcome Intent** initializes the bot
2. 3 sets of utterances are required to initiate 1 of the 3 next Intents
   1. *File time off*
   2. *Book a conference room*
   3. *Create expense report*
3. 1 of the 3 Intents are then initialized by the utterances
   1. **Time off Intent**
   2. **Conference Room Intent**
   3. **Expense Report Intent**
4. The appropriate utterances are provided based on the choice of the customer
5. If details are required the the chatbot requests *Slots* to be filled
   1. *Start Date*, *End Date*
   2. *Conference Room*, *Time*, *Duration*
6. The Intent is fulfilled and has returned to the start
   1. The **Expense Report Intent** initializes another level of utterances and intents needed to complete something as complex as a expense report
  
![lex_3](/docs/images/aws_lex_arch_3.PNG)
</br>*Example Use Case:  Employee Assistant Bot*

### Customer Service Bot
In this next bot use case, you'll see it mirrors closely to the structure and implementation as the Employee Assistant Bot. Notice though, in the utterances that follow the **Upgrade Plan Intent** and **Schedule Appt. Intent**, there are a variety of them that can be used to engage the chatbot to request the same *Slots* like *Plan* and *Start Date*.

![lex_4](/docs/images/aws_lex_arch_4.PNG)
</br>*Example Use Case:  Customer Service Bot*

### DevOps Bot
Here the bot structure is still very simple and similar to the other use cases; straightforward and to the point with multiple utterances and intents that require slots to be fulfilled. However, when contrasting against the prior use cases you will see how the chatbots can be used to complete many everyday tasks within any business domain.

![lex_5](/docs/images/aws_lex_arch_5.PNG)
</br>*Example Use Case:  DevOps Bot*

## Capturing Conversation Context
Each conversation between customer and chatbot contains many data elements that are captured. These data elements sit at the event level such as intents and slots, but also provide additional metadata about them as well. In the graph below you can see how different slots, prompts, and attributes are caught and stored to be used by the chatbot and to aide future development. Even missed utterances are captured and can be used to expand your utterance library!

![lex_6](/docs/images/aws_lex_arch_6.PNG)
</br>*Context Captured Elements from Chatbot Conversations*

In the below Dynamic Conversation Flow you can see how at the top, the Intent can be switched - similar to our prior examples where there was always a 3rd sub-Intent not discussed. These Intents continue on with their own utterances, slots, fulfillment, and yes, more Intents.

On the bottom of the graph you can see how Intents are chained together sequentially, just how we have described before as resetting or restarting the chatbot.
![lex_7](/docs/images/aws_lex_arch_7.PNG)
</br>*Context Captured Elements from Chatbot Conversations*
