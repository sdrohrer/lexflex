# Benefits
## Lex
1. Uses Automatic Speech Recognition (ASR) and Natural Language Understanding (NLU) 
    * Converting speech to text and recognizing the intent of that text
    * Improves over time using pre-built deep learning framework
2. Has SDKs for runtime services in Python (can also build Bots using it)
3. Monitoring dashboard tracks usage and QA stats we can utilize for product improvement
4. Can deploy one version into production while developing changes in another (no product downtime/service delays)
5. Billing per request means we can test usage on trial clients while we figure out a billing structure
    * Free Tier (Current) : 10000 text requests, 5000 speech requests / month for the first year
    * Paid Tier : $0.004 per Voice request, $0.00075 per Text request
    
## Polly
1. Converts text inputs to speech
    * Plays the other end of the spectrum, so our product can interact back with the user
2. Unlimited free replays once you pay for initial generation
    * Voice file is stored in cloud once generated so it can be called quickly and without perceived delays
        * Seemless conversation flow
3. Speech Marks
    * alongside the synthesized speech, these marks can provide enhanced user visual experience such as 
    speech-synchronized animation or karaoke-style highlighting.
    * can be marked by Sentence, Word, Viseme (describes the shape of the lips that corresponds to the 
    sound that is spoken), or SSML (Speech Synthesis Markup Language used in the text)
4. Billed per character
    * Free Tier (Current) : 5 million characters per month for speech or Speech Marks requests for the 
    first 12 months starting from the first request for speech
    * Paid Tier : $4.00 per 1 million characters
    
## Transcribe
1. Analyzes audio files (ASR) stored in S3 and returns a text file of the transcribed speech.
2. Works with all common audio formats (WAV, MP3, etc.)
3. It's accuracy can be leveraged to generate subtitles on audio and video content
    * Interested in testing for Call Notes use case
4. Billing per second, charged monthly
    * Free Tier (Current) : 60 minutes per month for 12 months
    * Paid Tier : $0.0004 per second with a minimum per request charge of 15 seconds
    
## SageMaker
1. Build, train, and deploy ML models at any scale
2. Pre-configured for TensorFlow and Apache MXNet
3. Access to hosted Jupyter Notebooks for exploration/visualization of training data stored in S3
    * Can use AWS Glue to move data from Amazon RDS, Amazon DynamoDB, and Amazon Redshift into S3 
    for analysis in the notebook.
5. Includes ["10 most common ML"](https://aws.amazon.com/sagemaker/features/) algo's pre-installed and optimized
6. Easy deployment of trained models into existing applications by providing an HTTPS endpoint
7. [Billed by hour](https://aws.amazon.com/sagemaker/pricing/#)
    * Some use cases point to simply using this service for some compute muscle
    
## Comprehend
1. Natural Language Processing (NLP) to find insights/relationships in text
    * language identification
    * extraction of key phrases, places, people, brands, or events
    * sentiment analysis
    
![AWS-Comprenhend-Example](/docs/images/Comprehend.PNG "Comprehend Example")

2. Automatically organizes a collection of text files by topic    
3. [Billed by units of 100 characters](https://aws.amazon.com/comprehend/pricing/)
    
## Rekognition
1. Image and Video analysis (classification)
    * when provided to the Rekognition API the service can identify objects, people, text, scenes, and activities
  
## MXNet
1. Fast and scalable training and inference framework with an easy-to-use/concise API for ML
2. Gluon interface allows quick learning access to deep learning on the cloud, edge devices, or mobile apps
3. Supports Python
