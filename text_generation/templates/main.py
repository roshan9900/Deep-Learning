import numpy as np
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import model_from_json
import pickle
from flask import Flask, render_template, request


with open('model.json', 'r') as json_file:
    loaded_model_json = json_file.read()
model = model_from_json(loaded_model_json)
model.load_weights("model_weights.h5")

with open('tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)
max_sequence_len = 44

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate',methods=['POST'])
def generate():
    features = [x for x in request.form.values()]
    seed_text = features[0]
    next_words = int(features[1])
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted_probs = model.predict(token_list)
        predicted_class_index = np.argmax(predicted_probs)

        output_word = ''
        for word, index in tokenizer.word_index.items():
            if index == predicted_class_index:
                output_word = word
                break
        seed_text += ' ' + output_word

    seed_text = seed_text.capitalize()
    

    return render_template('index.html', prediction=seed_text)


if __name__ == "__main__":
    app.run(debug=True)