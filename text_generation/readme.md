# Title: Text Generation Web Application using Flask and Keras

<img width="958" alt="image" src="https://github.com/roshan9900/Deep-Learning/assets/115538447/9ade89cf-faa1-43df-8344-193f856f812d">


## Description:
The "Text Generation Web Application" is a project that showcases the integration of machine learning, particularly Natural Language Processing (NLP), with web development. The application utilizes Python's Flask framework for creating a user-friendly web interface that generates text based on a pre-trained language model. The text generation model, implemented using Keras and TensorFlow, predicts and generates new words or sentences based on a seed text provided by the user.

## Key Components:
1. **Machine Learning Model:**
   The core of the project is a machine learning model that generates text. This model has two main parts:
   
   - **Architecture (model.json):** The architecture of the text generation model, stored in a JSON file. This includes the layers, activation functions, and other parameters of the neural network.
   
   - **Weights (model_weights.h5):** The trained weights of the model, stored in an HDF5 file. These weights capture the knowledge learned during training.

2. **Tokenizer:**
   A tokenizer is used to process and convert text data into numerical sequences that the model can understand. The tokenizer is pre-trained and stored as a pickle file (tokenizer.pkl). It's loaded to encode input text and decode the generated output.

3. **Web Application:**
   The web application is built using Flask, a micro web framework in Python. Flask allows you to create routes (URL endpoints) and render HTML templates. The key routes are:
   
   - **Home Route (/):** Renders the main page of the web application where users can enter the seed text and number of words to generate.
   
   - **Generate Route (/generate):** Handles the generation process. It takes user input, uses the model to predict the next words, and displays the generated text on the same page.

4. **User Interface (HTML Templates):**
   HTML templates are used to create the user interface of the web application. The main template (index.html) contains a form where users can input the seed text and number of words. The generated text is displayed below the form.

5. **Text Generation Process:**
   When a user enters the seed text and number of words, the web application processes this input. It tokenizes the seed text, pads it to the appropriate length, and then uses the pre-trained model to predict the next words. The most probable word is selected, and this process is repeated for the desired number of words.

6. **Model Output:**
   The generated text is displayed in a user-friendly format on the web interface. The application ensures that the generated text resembles natural language.

7. **Deployment:**
   The application can be locally deployed. Create a virtual environment, install requirements and run using python main.py command.
   
9. **Warning Suppression:**
   The warnings related to TensorFlow and other libraries are suppressed to avoid cluttering the console output.

10. **Interactive and Engaging:**
   The project demonstrates how to create an interactive and engaging web application that leverages machine learning to generate human-like text based on user input. This type of application could be used for creative writing prompts, text completion, or even simple chatbots.

Overall, the "Text Generation Web Application" project showcases the seamless integration of machine learning and web development, allowing users to experience the capabilities of NLP and AI in a user-friendly and accessible manner.
