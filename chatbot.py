import random
import json
import spacy
import nltk
import ssl
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Download required resources
try:
    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context
except:
    pass
nltk.download('punkt')

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Tokenizers
def spacy_tokenizer(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if not token.is_punct and not token.is_space]

def nltk_tokenizer(text):
    return word_tokenize(text.lower())

# Choose tokenizer: 'spacy' or 'nltk'
tokenizer_choice = 'spacy'
tokenizer = spacy_tokenizer if tokenizer_choice == 'spacy' else nltk_tokenizer

# Load intents
with open("intents.json") as f:
    data = json.load(f)

corpus = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        corpus.append(pattern)
        labels.append(intent["tag"])

# Vectorization
vectorizer = CountVectorizer(tokenizer=tokenizer, lowercase=False)
X = vectorizer.fit_transform(corpus)

# Model training
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

# Chatbot response function with confidence threshold
def chatbot_response(text, threshold=0.5):
    text_vect = vectorizer.transform([text])
    probabilities = model.predict_proba(text_vect)[0]
    max_prob = max(probabilities)
    prediction = model.classes_[probabilities.argmax()]

    if max_prob < threshold:
        return random.choice([resp for intent in data["intents"] if intent["tag"] == "noanswer" for resp in intent["responses"]])

    for intent in data["intents"]:
        if intent["tag"] == prediction:
            return random.choice(intent["responses"])

# Chat loop
print("Start chatting with the bot (type 'quit' to stop):")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot_response(user_input))
