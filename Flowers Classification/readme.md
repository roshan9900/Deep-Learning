
# Flowers Classification Using Transfer Learning

## 1. Project Overview

### Problem Statement
The objective of this project is to classify images of flowers into five categories: daisy, dandelion, rose, sunflower, and tulip, using deep learning and transfer learning techniques.

### Dataset
The dataset contains 3,670 images of flowers, divided into five categories. The images are stored in TensorFlow’s `flower_photos` dataset, which is used for model training and validation.

---

## 2. Data Preparation

### Steps Taken
1. **Image Loading and Preprocessing**:
   - Used the TensorFlow library to load the dataset and split it into training and validation sets.
   - Resized images to 180x180 pixels for uniform input dimensions.
   - Set up categorical labels for the five flower classes.

2. **Training and Validation Split**:
   - The data was split into an 80-20 ratio, with 2,936 images used for training and 734 images for validation.

---

## 3. Model Architecture

### Model Used: Transfer Learning with ResNet50
- **Architecture**: The model uses ResNet50 pre-trained on ImageNet as a base for feature extraction. The top layers are removed, and custom dense layers are added for flower classification.
- **Layers Added**:
   - Flatten layer to transform the output of ResNet50 to a 1D feature vector.
   - Dense layer with 512 neurons and ReLU activation.
   - Output layer with 5 neurons (one for each flower class) and softmax activation for categorical classification.
- **Parameters**:
   - Total parameters: 24,639,365
   - Trainable parameters: 1,051,653
   - Non-trainable parameters: 23,587,712

### Compilation
- **Optimizer**: Adam with a learning rate of 0.001
- **Loss Function**: Categorical cross-entropy
- **Metrics**: Accuracy

---

## 4. Model Training

### Training Process
- The model was trained for 10 epochs using the training dataset, with validation accuracy and loss monitored at each epoch.
- **Training Results**:
  - **Epoch 1**: Accuracy = 77.15%, Validation Accuracy = 84.88%
  - **Final Epoch (Epoch 10)**: Accuracy = 100%, Validation Accuracy = 88.01%

### Evaluation
- After training, the model achieved a high validation accuracy of 88.01%, with minor fluctuations in validation loss, indicating a well-generalized model.

---

## 5. Model Performance

### Performance Metrics
- **Training Accuracy**: Reached 100% by the last epoch, showing strong learning ability.
- **Validation Accuracy**: Stable at approximately 88%, indicating robust performance across unseen data.

### Training and Validation Loss and Accuracy Plots
Plots were generated to visualize the model’s accuracy and loss over each epoch, showing smooth convergence with minimal overfitting.

---

## 6. Model Prediction Example

### Example Prediction
A test image of a rose was loaded and preprocessed for prediction. The model output probabilities for each class, with the highest probability corresponding to the class `rose`.

### Prediction Output
- **Class Prediction**: Rose
- **Confidence**: 99.99%

---

## 7. Conclusion

This flower classification model successfully leverages transfer learning with ResNet50, achieving an impressive validation accuracy of around 88%. The use of a pre-trained model significantly enhanced performance with limited training data.

---

## 8. Future Work
1. **Hyperparameter Tuning**: Experiment with learning rates, batch sizes, and optimizers to improve accuracy.
2. **Data Augmentation**: Implement data augmentation techniques to increase variability and further improve model generalization.
3. **Testing with Other Architectures**: Try additional architectures like VGG16 or Inception for comparison.

