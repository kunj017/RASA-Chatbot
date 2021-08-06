# RASA-Chatbot

### Problem Statement
To design a chatbot assistant for patients in need of emotional attention. To monitor, analyse and suppress any negative thoughts and help getting psychiatric assistance if required.

### Why Chatbots ?
The popularity of live chat applications has been growing over the past few
years. And as the AI trend keeps rising, chatbots become more a
must-have rather than a nice to have part of the business. The increasing
demand for chats continues to grow so to keep the customer satisfaction
rate high; companies must find ways to cope with the rising volumes of
inquiries coming every day to all their communication channels.

![image](https://user-images.githubusercontent.com/44698183/128494749-aac45c35-47f1-460f-8a21-040040988ade.png)

### What is RASA ?
Rasa is an open-source machine learning framework for building contextual AI assistants and chatbots.

To make complete AI-based chatbot it has to handle two things:

- Understanding the user’s message which is done through Rasa NLU.
- The bot should be able to carry dialogue with context which is done by Rasa Core.

![image](https://user-images.githubusercontent.com/44698183/128495389-1965cbe0-d5c4-4c00-b0f6-3334f66d0f5e.png)

### What happens under the hood?

Now let’s understand how the brain of chatbot works. It’s called NLU(Natural 
language understanding) unit where it’s components do the job. 
Component includes as follows.
- Tokenization: We read and understand the sentence word by word, right? 
Similarly, tokenizer will break the sentence into words(called word tokenizer).
- Entity Extraction: These are a chunk of information we extract from 
sentences to complete the action. For example when one says, I want to 
travel from Hyderabad to Mumbai by flight. Here the intent is “travel_flight" 
and to fetch information we need to know source i.e Hyderabad and 
destination i.e Mumbai and couple more entities like date of travel etc.
- Classifier: Now you know the meaning(features) of the sentence(words 
through tokenization). It’s time to classify to its appropriate category. For e.g I 
want to travel by cab should classify to travel_cab and I want to travel by 
flight travel_flight. All this is done by using Machine learning or Deep 
learning classifier.


![image](https://user-images.githubusercontent.com/44698183/128495595-6ba6136b-61b2-4f67-a9b6-abba4fa82f07.png)

![image](https://user-images.githubusercontent.com/44698183/128495621-1314c7f3-0970-4c6f-9854-4647883eb85c.png)

### Development And Analysis

Steps involved in development and testing are:
- Creating Domain
- Making a conversational flow
- Making NLU data for the intent and entity extraction.
- Making test stories to train the Model
- Making appropriate actions

### Testing our NLU data
Rasa generates an intent confusion matrix based on the test stories we create.

This helps us to pin point the data that is clashing or might need more NLU data.
![image](https://user-images.githubusercontent.com/44698183/128495939-fa32e6f4-f9c3-4bdb-9d05-afaa03f3d61c.png)

We get a description of each intent and its prediction cofidence.


![image](https://user-images.githubusercontent.com/44698183/128495972-790e9228-b7b9-4b90-b5e6-2c979df03184.png)

### Using RASA Interactive to generate stories

Full phase of testing can be done by alpha users provided them with the feature of RASA Interactive where the can conversely chat with the bot and guide it the way they intent to be. At the end several story paths are generated to incorporate the new conversation path chosen by the user and the model can consistently train and learn from more usage.
![image](https://user-images.githubusercontent.com/44698183/128496005-bc796e48-4f17-4b78-b982-4c8bafb587b8.png)
