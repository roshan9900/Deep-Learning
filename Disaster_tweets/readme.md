# **Project Title:** BERT-Powered Disaster Tweet Classifier

**Project Description:**

Welcome to my portfolio project, "BERT-Powered Disaster Tweet Classifier." In this project, I harnessed the formidable capabilities of BERT (Bidirectional Encoder Representations from Transformers) to develop a highly accurate and efficient model for classifying tweets as either describing real disasters or not. This project represents a compelling application of state-of-the-art natural language processing (NLP) techniques to real-world data.

#### Architecture of the Model
<img width="300" alt="image" src="https://github.com/roshan9900/Deep-Learning/assets/115538447/b45f2491-6000-48e5-a375-a4aa6f0b12db">


**Key Components and Achievements:**

1. **Data Collection and Exploration:**
   - I got the dataset from kaggle, which contains tweets with labels indicating whether they pertain to real disasters.

2. **Data Preprocessing and Cleaning:**
   - A rigorous data preprocessing phase was conducted, addressing challenges such as missing values and tokenization to prepare the text for BERT input.

3. **Choosing BERT Architecture:**
   - The choice of the 'bert-base-uncased' architecture was made for fine-tuning, based on its well-established performance in NLP tasks.

4. **Fine-Tuning BERT:**
   - Utilizing TensorFlow and the Hugging Face Transformers library, the pretrained BERT model was fine-tuned on the disaster tweet classification task. This process involved setting up the model architecture, attention masks, and training pipelines.

5. **Handling Class Imbalance:**
   - To address class imbalance in the dataset, techniques like SMOTE and class-weighted loss were implemented to ensure that the model learned effectively for both disaster and non-disaster tweets.
   - But after training the model on the whole dataset gave better results than training on the balanced dataset.

6. **Hyperparameter Tuning:**
   - Extensive hyperparameter tuning experiments were conducted to optimize the model's performance. This included adjusting learning rates, batch sizes, and dropout rates.

**Evaluation and Kaggle Achievement:**

- The project achieved a notable top 25% ranking on Kaggle.

### Classification Report Metrics:
<img width="300" alt="image" src="https://github.com/roshan9900/Deep-Learning/assets/115538447/64cb0f6f-e3b9-4a5d-b6de-33f1c104932b">



**Conclussion**:
- In summary, our BERT-Powered Disaster Tweet Classifier demonstrates strong performance, with precision rates of 0.83 for non-disaster tweets and 0.91 for disaster tweets. These results indicate the model's effectiveness in distinguishing between the two categories. Additionally, high recall values of 0.95 for non-disaster and 0.73 for disaster tweets underscore its ability to capture relevant content. The overall accuracy of 85% reflects the model's proficiency in classifying tweets. These findings establish the classifier as a valuable tool for real-world applications, particularly in disaster monitoring and response efforts.
