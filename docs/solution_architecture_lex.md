# Chatbot Solution Architecture (AWS Lex)
AWS Lex is a single service that packages and consolidates many of the steps for building chatbots. However, typically for a complete end-to-end deployment of a chatbot you are required to leverage other AWS services and systems to properly serve your customers. More on AWS Lex [can be found here](https://aws.amazon.com/lex). 

[1. Sample Use Case Architecture with AWS Lex: What you need to know](#sample-use-case-architecture-with-aws-lex)</br>

## Sample Use Case Architecture with AWS Lex
Here you can see how AWS Lex is positioned with other services to deliver a chatbot that accepts voice input, leverages security authentication, responds in voice to both acquire data input for slots and fulfill the intent request back.
1. **AWS Cognito** - customer and user authentication system for security
2. **AWS Polly** - Text to Speech service; Lex handles Speech to Text
3. **AWS Lex** - The speech recognition engine, natural language understanding engine, and dialogue management
3. **AWS Lambda** - This is a serverless compute triggering service; think really fast business rules engine
4. **AWS Dynamo DB** - This is a scalable, high performance NoSQL database built to support web based applications
5. **AWS Cloudwatch** - This is a monitoring tool to check the ongoing performance and health of the chatbot and other service operations
6. **SNS and SES** - This allows for messaging across different channels to relay information
7. **Other AWS Services** - These can be any number of services, and depends on your infrastructure and business
8. **Actual chatbot application** - This is how your customers interacts with the chatbot

![sol_lex_1](/docs/images/aws_lex_sol_arch_1.PNG)
</br>*Sample Solution Architecture - Banking Chatbot*
