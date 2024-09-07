from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.models import Sequential
import random
import json
import pickle
import numpy as np

# Natural Language Toolkit
# a Python library used for natural language processing tasks, such as tokenization, stemming, and lemmatization.
import nltk

#  WordNetLemmatizer class from the nltk.stem module, which is used for lemmatization. Lemmatization is the process of reducing a word to its base form (e.g. "running" to "run").
from nltk.stem import WordNetLemmatizer

# downloads the WordNet corpus, which is a large lexical database of English words and their relationships.
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
# Load the intents from the json file
intents = json.loads(open("intents.json").read())

words = []
classes = []
documents = []
ignore_letters = ['?', "!", ".", ","]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        #  creates a tuple containing the list of words and the conversation's class (like "greeting" or "goodbye"), and adds it to the documents list.
        documents.append((word_list, intent["tag"]))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmatizes each word and emoves any words that are in the ignore_letters list.
words = [lemmatizer.lemmatize(word)
         for word in words if word not in ignore_letters]

# Sorts the remaining words and removes any duplicates using the set() function.
words = sorted(set(words))

classes = sorted(set(classes))
# save the words and classes lists to files named "words.pkl" and "classes.pkl"
# This function serializes the Python objects and writes them to a file in a binary format, which can be loaded later using the pickle.load() function.
pickle.dump(words, open("words.pkl", 'wb'))
pickle.dump(classes, open("classes.pkl", 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(
        word.lower()) for word in word_patterns]
# For each word in the words list, we check if the word is in the word_patterns list. If it is, the program appends a 1 to the bag list; otherwise, it appends a 0.
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

# creates an output vector called output_row that has a 1 in the position corresponding to the class of the current document, and 0s elsewhere.
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
# Shuffling the training list is important because it ensures that the training data is presented to the model in a random order.
# This helps prevent the model from memorizing the order of the training data and overfitting to the training set.
train_x = np.array([x[0] for x in training])
train_y = np.array([x[1] for x in training])

# Building the AI model:
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
#  Dropout function is used after each Dense layer to prevent overfitting
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(32, activation="relu"))
# the number of classes in the output data
model.add(Dense(len(train_y[0]), activation="softmax"))
print("Length of the output: ",  len(train_y[0]))
model.compile(loss='categorical_crossentropy',
              optimizer="adam", metrics=['accuracy'])
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5')
print("Done")
