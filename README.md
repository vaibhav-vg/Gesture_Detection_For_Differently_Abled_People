# Gesture Detection For Differently-Abled People
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Overview
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project focuses on creating a gesture detection system to empower differently-abled individuals with seamless interaction experiences. Using machine learning, computer vision, and Python, we've developed a solution that recognizes gestures for intuitive device control.

Features
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Inclusivity: Recognizes a diverse set of gestures to cater to different user needs.
High Accuracy: Achieved an impressive 97% accuracy using a Random Forest Classifier.
Real-time Interaction: Provides real-time gesture processing for instant responsiveness.
User-Friendly Interface: An intuitive and easy-to-use interface for users to interact with the system effortlessly.
Customization: Allows users to easily customize and add new gestures based on personal preferences.
Cross-Platform Compatibility: Supports multiple platforms, ensuring accessibility for a wide range of devices.

How it Works
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The heart of our gesture detection lies in the implementation of a Random Forest Classifier. Here's a brief overview of the process:

Data Collection: We collected a dataset of various gestures performed by individuals, ensuring diversity and inclusivity. Users can contribute by placing their collected images in the data folder.

Create Dataset:

Execute the create_dataset.py file to create your own dataset using the collected images.
Name the dataset file as data.pickle.

Train the Model:

Train the classifier model using the created dataset (data.pickle) by running the training script.
Save the trained model as model.p.

Run Inference:

Navigate to the inference classifier folder.
Run the script to initiate the gesture detection window for testing.

Note: To enhance the accuracy and adapt the system to personal preferences, users are encouraged to create and use their own gesture datasets during both training and real-time usage.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage
Clone the repository: git clone https://github.com/your-username/gesture-detection.git

Install dependencies: pip install -r requirements.txt

Follow the steps mentioned above for data collection, dataset creation, model training, and inference testing.
Additional Features and Functionalities
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Gesture Logging: Option to log recognized gestures for further analysis or integration with other applications.

Real-time Feedback: Provides visual or audio feedback in real-time for recognized gestures.

Multi-Gesture Support: Recognizes and processes multiple gestures simultaneously for advanced interactions.

API Integration: Allows developers to integrate the gesture detection functionality into their own applications.

Contributing
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We welcome contributions! If you have ideas for improvement, open an issue or submit a pull request.
