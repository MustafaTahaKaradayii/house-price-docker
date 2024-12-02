House Price Prediction with Docker

This project demonstrates a simple machine learning pipeline for predicting house prices using the California Housing Dataset. It involves training a model using Linear Regression and deploying the model using a web application built with Flask. The project uses Docker to manage two containers: one for training the model and another for hosting the prediction service.

Project Structure

->app.py: Flask application for serving the prediction model.

->train_model.py: Script to train the model using the California Housing Dataset.

->Dockerfile.train: Dockerfile for creating a container to train the model.

->Dockerfile.host: Dockerfile for creating a container to host the Flask application.

->docker-compose.yml: Docker Compose file to orchestrate both training and hosting containers.

->requirements.txt: Python dependencies for both training and hosting.

->output/: Directory to store the trained model (house_price_model.pkl).



Prerequisites

->Docker and Docker Compose must be installed.

->Git must be installed to clone the repository.

Setup Instructions

Clone the Repository:

->git clone <repository_url>
->cd house-price-docker

Directory Structure:
The repository should have the following structure after cloning:

house-price-docker/
|-- app.py
|-- train_model.py
|-- Dockerfile.train
|-- Dockerfile.host
|-- docker-compose.yml
|-- requirements.txt
|-- output/
    |-- house_price_model.pkl (generated after training)
|-- README.md

Build and Run the Docker Containers:
Use Docker Compose to build and run the containers. This will first train the model and then deploy the Flask application.

docker-compose up --build

Access the Application:

Once the containers are up, the Flask application will be running on http://localhost:8080.

You can access it using your browser or use tools like Postman or curl to test predictions.

Application Features

Training: The trainer container (house-price-trainer) trains a Linear Regression model using the California Housing Dataset. The trained model is saved in output/house_price_model.pkl.

Hosting: The host container (house-price-host) runs a Flask web application that allows users to enter features of a house and get a predicted price.

Example Usage

Open the Web Interface:
Navigate to http://localhost:8080/ in your browser. You will see a form where you can enter details like Median Income, House Age, Number of Rooms, etc.

Get Predictions:

Fill out the form fields.

Click Predict Price.

The predicted price will be displayed on the page.

Technical Details

Model: The model used is Linear Regression from scikit-learn.

Dataset: The California Housing Dataset is used to train the model. It provides information on median home prices in California.

Flask App: The Flask app has a simple HTML form for user input and displays predictions.

Troubleshooting

Port Conflict: If port 8080 is already in use, change the port mapping in docker-compose.yml:

ports:
  - "<new_port>:5000"

Firewall: Make sure any firewall allows incoming traffic on the port you're using.

Docker Issues: Ensure that Docker is running and that the necessary images are built without errors.

How to Clean Up

To stop and remove the containers and network created by Docker Compose:

docker-compose down

Sources

Dataset: The California Housing Dataset from scikit-learn.

Technologies Used: Flask, scikit-learn, Docker.

Additional Notes

This project is intended as a simple demonstration of deploying a machine learning model with Docker. For a production environment, additional considerations should be made, including using a production-grade WSGI server, adding security measures, etc.

This setup is configured to run locally. To make the application accessible over the internet, additional configurations such as ngrok or cloud deployment would be required.