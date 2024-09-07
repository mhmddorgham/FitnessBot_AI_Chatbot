## Introduction:
The use of Artificial Intelligence (AI) in the health and fitness industry has gained considerable attention in recent years. AI-powered chatbots have been developed to assist individuals in achieving their fitness goals by providing personalized workout and diet plans(Yu, Beam & Kohane 2018). These chatbots use deep learning and natural language processing techniques to understand and respond to user queries, thereby providing a more personalized and effective fitness experience(Sqalli et al. 2021).

The development of AI-powered chatbots in the health and fitness industry has the potential to transform the way individuals approach their fitness goals(Wahl et al. 2018). By providing personalized workout and diet plans based on a user's BMI, these chatbots can help individuals achieve their fitness goals in a more efficient and effective manner. Additionally, chatbots can provide general information on fitness, health, nutrition, weight loss/gain, and motivational advice, making them a valuable resource for individuals looking to improve their overall health(Yu, Beam & Kohane 2018).


The use of neural networks, a crucial aspect of deep learning, is at the core of the Fatness Chatbot's capabilities(Chowdhury 2003). The chatbot uses neural networks to handle and analyze massive volumes of data using frameworks like TensorFlow or PyTorch, allowing it to learn from practical situations and derive insightful conclusions(Halácsy 2006). These networks provide the chatbot the ability to discern trends in user input, find pertinent keywords, and produce context-sensitive answers. The chatbot continually improves its comprehension and answer creation as it converses with more people, resulting in a unique and useful user experience.

## Design Process and Methodology :
The problem we are trying to solve with our AI fitness chatbot is the lack of personalized guidance and support for individuals who are trying to achieve their fitness goals(Lamb, Brodie & Roberts 1988). Many people find it challenging to develop and maintain a fitness routine that is effective and sustainable, especially if they have limited knowledge or experience in this area (Lamb, Brodie & Roberts 1988) .

Traditional fitness programs and personal trainers can be expensive and inaccessible for many individuals, making it difficult for them to get the guidance and support they need(Eackles 2020). Furthermore, generic fitness plans that do not take into account the user's specific needs, preferences, and limitations may not be effective or sustainable in the long term(Eackles 2020).

Our AI fitness chatbot addresses these issues by providing personalized recommendations that are tailored to the user's BMI, fitness goals, preferences, and limitations. By using deep learning and natural language processing techniques, the chatbot can understand the user's needs and provide tailored recommendations that are specific to their goals and limitations. This personalized approach can help individuals achieve their fitness goals in a more effective and sustainable way, without the need for expensive personal trainers or generic fitness programs.

## Data Collection:
We collected a dataset of user profiles that included information such as age, weight, height, gender, and fitness goals. We also collected data on workout plans and diet plans that were recommended by fitness experts for individuals with specific BMIs. In addition to sourced our data from various publicly available sources, including fitness blogs, websites, and forums. We also collected data from fitness apps and wearable devices that track user activity and provide personalized recommendations.

## Data Preprocessing:
We used Tensorflow, Keras, and NLTK. Our data were stored in a JSON file named "intents.json". We loads the intents from this file and extracts the words, classes, and documents from the intent patterns. Each document is a tuple containing the list of words in the intent pattern and the corresponding tag (class) for that pattern.

The words are then lemmatized and cleaned by removing any irrelevant characters, such as punctuation marks. The remaining words are sorted and saved to a file named "words.pkl". The classes are also sorted and saved to a file named "classes.pkl". This preprocessing step ensures that the data is in a suitable format for training the deep learning model.
Lemmatization and tokenization are two important techniques used in natural language processing to preprocess textual data for machine learning models(Halácsy 2006).

Tokenization involves breaking up a sentence or a document into individual words or tokens. This is often the first step in the preprocessing pipeline, as it allows the text to be converted into a format that can be more easily processed by machine learning algorithms(Chowdhury 2003). There are several techniques for tokenization, including simple whitespace splitting, rule-based techniques, and machine learning-based techniques(Halácsy 2006).

Lemmatization, on the other hand, is the process of reducing a word to its base or dictionary form, known as a lemma. This process is important because it allows different forms of the same word to be treated as the same word, which can improve the accuracy of machine learning models(Halácsy 2006). For example, the words "running," "ran," and "runs" can all be reduced to the lemma "run".

The lemmatization process typically involves using a dictionary or a set of rules to map each word to its lemma. This can be a challenging task, as many words can have multiple lemmas depending on their context. However, advances in natural language processing have led to the development of sophisticated algorithms that can accurately perform lemmatization in most cases(Chowdhury 2003).

Next, we created a training set by creating a bag of words for each document. The bag of words is a binary vector indicating whether each word in the "words" list is present in the document or not. This step involves iterating over each document and checking if each word in the "words" list is present in the document. If a word is present, a 1 is added to the bag of words for that document; otherwise, a 0 is added. The training set is then shuffled to prevent overfitting(Aleedy, Shaiba & Bezbradica 2019).

The deep learning model is developed using the Keras Sequential API. The model consists of three dense layers with 128, 64, and 32 units respectively, and each layer is followed by a dropout function to prevent overfitting. The output layer has a number of units equal to the number of classes in the training data and uses the softmax activation function to output a probability distribution over the classes(Schmidhuber 2015).

The model is compiled using the categorical cross-entropy loss function, the Adam optimizer, and the accuracy metric(Chowdhury 2003). The model is then trained on the training set for 200 epochs with a batch size of 5. The trained model is saved to a file named "chatbot_model.h5".


## Model Implementation:
After we trained the model, the model is loaded using the TensorFlow Keras library, which provides a high-level API for building and training deep learning models(Schmidhuber 2015).

Once the model is loaded, we use it to predict the most likely intent for the user's input sentence. To do this, the  a "bag of words" is created representation of the input sentence, which is a numerical vector that represents the presence or absence of each word in the chatbot's vocabulary(Aleedy, Shaiba & Bezbradica 2019). The bag of words representation is then passed through the deep learning model using the model's predict() method, which generates a probability distribution over the possible intents.

The program then uses a threshold value to filter out low-probability intents and sorts the remaining intents in descending order of probability. The most likely intent is then selected, and the chatbot generates an appropriate response based on the selected intent.

Calculating BMI and provide Diet and workout plans:
When the user requests to calculate their BMI, the Chatbot retrieves the relevant response from the intents.json file. The Chatbot prompts the user to enter their weight, height, and age, which are then passed to a function that calculates the BMI using the standard formula: BMI = weight (kg) / height^2 (m^2). The resulting BMI value is used to determine the user's current health status(Eackles 2020). 

The Chatbot uses another function that takes the user's BMI and fitness level (beginner, intermediate, or advanced) to recommend the best workout plan for the user. It recommends a personalized workout plan based on the user's fitness level, the BMI. The workout plan includes specific exercises, sets, and repetitions, as well as rest periods and recovery techniques(Eackles 2020).
In addition, FitnessBot recommends a personalized diet plan based on the user's BMI and dietary goals, such as losing weight, gaining weight, or maintaining weight. The Chatbot uses a function that takes into account the user's BMI and  fitness level. The diet plan may include specific foods, portion sizes, meal timings, and nutritional supplements. 

Furthermore, we created two functions in Python that provide general workout and diet plans based on the user's fitness level, without considering BMI. The fitness level can be specified as 'beginner', 'intermediate', or 'advanced'.

The create_workout_plan function takes the fitness level as an input and returns a workout plan as a string. The workout plan includes a combination of cardio and strength training exercises, with the number of repetitions and duration of each exercise increasing with the user's fitness level(Eackles 2020).

The create_diet_plan function also takes the fitness level as an input and returns a diet plan as a string. The diet plan includes tips for healthy eating habits and a sample meal plan based on the user's goals, such as weight loss or muscle gain. The meal plan consists of whole, nutrient-dense foods and suggests tracking food intake to ensure macronutrient and calorie goals are met.

However, both functions emphasize the importance of calculating BMI and knowing one's body condition to tailor the workout and diet plans to the individual's needs. 

## Flask Python Server: 
Flask is a web framework for building web applications using the Python programming language. It is a lightweight and flexible framework that allows developers to quickly and easily build web applications(Vogel et al. 2017). Flask provides a set of tools and libraries for routing, templating, and database integration, making it a popular choice for developers who want to create web applications with minimal setup and configuratio(Aslam et al. 2015) .
We used a Python Flask web application that provides a chatbot interface for users to interact with. Handling different intents such as creating personalized workout or diet plans, or calculating BMI values.
The code defines two routes, "/" and "/get". The first route renders a HTML template for the chat interface. The second route handles user input from the chat interface, where the method can be either "GET" or "POST". The user's message is extracted from the request and is then passed to a function called "predict_class" to determine the intent of the user's message.

If the user's intent is to create a personalized workout or diet plan, the corresponding intent is stored in the session and the chatbot waits for additional input from the user before generating a plan. If the user enters values to calculate their BMI, the values are extracted from the message and passed to a function called "calculate_bmi" to obtain the user's BMI value and category. The BMI category is then stored in the session.

If the user enters a fitness level, such as "beginner", "intermediate", or "advanced", the chatbot will check if a BMI category has been stored in the session. If a BMI category is available, a personalized plan will be generated using the user's fitness level and BMI category. If no BMI category is available, a plan will be generated without considering the user's BMI category.

If the user's intent does not match any of the above cases, the chatbot will generate a response based on the user's intent using the "get_response" function. Finally, if the code is run directly (not imported), the Flask application is started and run on the local machine.


## Graphical User Interface:
We created the graphical user interface (GUI) using HTML and CSS, and JavaScript. The interface is designed to be responsive and user-friendly, with a clean and modern look.
The interface is structured using the Bootstrap CSS framework, which provides a grid-based system for laying out the various components of the interface. The interface is divided into a header, a body, and a footer, with the chatbot interface itself occupying the body(Aslam et al. 2015).
The body of the chat interface is divided into two sections, one for displaying the chat history and one for entering new messages. The chat history section is represented using a div element with the ID "messageFormeight", which is initially empty. The new message section is represented using a form element with the ID "messageArea", which includes an input field for entering messages and a send button for submitting them.
The JavaScript code included in the HTML file provides the functionality for sending and receiving messages. When the user submits a new message using the "messageArea" form, the JavaScript code processes the message, adds it to the chat history section, and sends an AJAX request to the server to process the message. When the server responds with a message, the JavaScript code updates the chat history section with the response.


