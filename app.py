from flask import session
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from functions import calculate_bmi, create_workout_plan_with_BMI, create_diet_plan_with_BMI, create_workout_plan, create_diet_plan
app = Flask(__name__)
nltk.download('punkt')
nltk.download('wordnet')
app.secret_key = "my-secret-key"
cors = CORS(app)

lemmatizer = WordNetLemmatizer()

intents = json.loads(open("intents.json").read())

words = pickle.load(open("words.pkl", 'rb'))
classes = pickle.load(open("classes.pkl", 'rb'))


model = load_model("chatbot_model.h5")


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


@app.route("/")
def index():
    session["bmi_category"] = " "
    session["order"] = ""
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    print("Inside Chat function")
    msg = request.form["msg"]
    input = msg
    ints = predict_class(input)
    print(input)
    print(ints)
    print(ints[0]['intent'])
    print(session["bmi_category"])  # Accessing stored value
    print(session["order"])  # Accessing stored value

    if ints[0]['intent'] == 'personalized_workout_plan' or ints[0]['intent'] == 'personalized_diet_plan':
        session["order"] = ints[0]['intent']
        print(session["order"])

    # If user enter values to calculate his / her bmi
    if "," in input:
        input = input.split(',')
        weight, height, age = map(float, input)
        result = calculate_bmi(weight, height, age)
        response = result[0]  # Get the response only
        session["bmi_category"] = result[1]  # Get the bmi_category only
        return response

    if input.lower() in ["beginner", "intermediate", "advanced"]:
        print("inside the if beginner")
        print(ints)
        print(ints[0]['intent'])

        if session["order"] == 'personalized_workout_plan':
            print("inside personalized_workout_plan")
            print(session["bmi_category"])
            print(input)
            if session["bmi_category"] != "":
                response = create_workout_plan_with_BMI(
                    input.lower(), session["bmi_category"])

            if session["bmi_category"] == " ":
                print("Workout with no BMI")
                response = create_workout_plan(input)
            return response

        elif session["order"] == 'personalized_diet_plan':
            print("inside personalized_diet_plan")
            print(session["bmi_category"])
            print(input)
            if session["bmi_category"] != "":
                response = create_diet_plan_with_BMI(
                    input, session["bmi_category"])

            if session["bmi_category"] == " ":
                print("diet with no BMI")
                response = create_diet_plan(input)
            return response

    response = get_response(ints, intents)
    return response


if __name__ == '__main__':
    app.run()
