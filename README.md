# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: GOWTHAM N

*INTERN ID*: CT04DF178

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

*DESCRIPTION*:

         For Task 3 of the CodTech Python Internship, I was assigned the development of an **AI-powered chatbot** using Python and natural language processing (NLP) libraries such as **NLTK (Natural Language Toolkit)** or **spaCy**. The primary objective of this task was to build an interactive chatbot that could understand user queries and respond in a human-like manner. This task simulated real-world applications where AI chatbots are used for customer service, virtual assistance, educational helpdesks, and more. It required a combination of skills in data preprocessing, natural language understanding, machine learning fundamentals, and user interaction design.

To begin this task, I first designed the **intents file** — a JSON file containing multiple categories or “intents” that the chatbot should recognize and respond to. Each intent contained a “tag” (which acts as a label), several “patterns” (user inputs), and relevant “responses.” For example, an intent like `"greeting"` would include patterns such as “Hello,” “Hi,” or “Good morning,” and responses such as “Hello! How can I assist you today?” The JSON structure acts as the knowledge base for the chatbot’s conversation model. I created multiple intents covering various domains like greetings, jokes, farewells, and queries related to time or information. Next, I used **NLTK** to perform natural language preprocessing. This included **tokenization** (breaking down input text into words), **stemming** (reducing words to their root forms), and **bag-of-words encoding**, which transformed the user’s input into a numerical format that the model could understand. The intent classification model was built using a simple **feedforward neural network** with the help of libraries like **PyTorch** or **TensorFlow/Keras** (depending on implementation). I divided the data into training and testing sets, converted input patterns into numerical vectors, and trained the model to predict the appropriate tag based on user input.

Once the model was trained, I developed the response mechanism. When a user inputs a message, the chatbot preprocesses it, predicts the intent using the trained model, and then selects a random response from the associated intent category. To enhance interactivity, I implemented a loop that continuously takes user input and breaks when the user says “bye” or “exit.” During testing, I made sure to handle edge cases — such as unknown inputs or ambiguous phrases — by introducing fallback responses like “I’m not sure I understand. Could you rephrase?” In addition to NLTK, I experimented with **spaCy** for advanced NLP capabilities. SpaCy offers better tokenization and named entity recognition (NER), which can be useful for more sophisticated bots. However, for a lightweight and educational chatbot, NLTK proved sufficient. I also implemented basic error handling to prevent issues like missing tags in the intent file or empty user input. Throughout the script, I added comments and organized the code into functions for better readability and maintainability. The chatbot was executed successfully in a command-line environment using Visual Studio Code (VS Code). It was able to answer basic questions, tell jokes, greet the user, and exit politely when requested. This task helped me develop a strong understanding of how chatbots process language and how machine learning models are trained to categorize and respond to text input. It also exposed me to real-world practices such as intent mapping, conversational design, and NLP preprocessing pipelines.

In conclusion, Task 3 was one of the most engaging and intellectually rewarding assignments of the internship. It provided me with practical knowledge of how AI chatbots work behind the scenes and how natural language understanding can be implemented using Python. By building this chatbot from scratch, I learned how to integrate data, train models, and manage conversations in a meaningful way. This task not only deepened my understanding of Python and machine learning but also prepared me to work on more advanced NLP projects in the future, such as sentiment analysis, text summarization, or context-aware conversation systems.


