# Project Title

The Face Mask Detection Web Application is a tool designed to detect whether individuals in images are wearing face masks or not. Developed by Viet Duc, this web application utilizes machine learning models to analyze images and provide real-time feedback on the presence of face masks.

## Prerequisites

Before getting started, make sure you have the following:

- Docker installed on your machine
- Basic knowledge of Python programming

## Getting Started

To start learning Python with Docker, follow these steps:

1. Create a new directory for your project.
2. Navigate to the project directory.
3. Create a new Python file.
4. Create **requirements.txt** file.
5. Open the Python file in a text editor and start writing your Python code.

## Running Python Code in Docker

To run your Python code in Docker, follow these steps:

1. Create a **Dockerfile** in the project directory.
2. Create a **compose.yaml** file
3. Run:
```
   docker compose up --build
```
4. Verify by browse the website at http://localhost:5000/

## Pushing Docker Image to Docker Hub

1. Log in to Docker Hub.
Before you can push images to Docker Hub, you need to log in to your Docker Hub account using the `docker login` command:
```
    docker login
```
2. List Docker Images.
List all the Docker images on your local machine using the following command:
```
    docker images
```
Identify the image that you want to push to Docker Hub. Make note of its repository name and tag.

3. Tag the Docker Image.
Tag the Docker image with your Docker Hub username and the desired repository name using the following command:
```
    docker tag <image_id> <dockerhub_username>/<repository_name>:<tag>
```
Replace '<image_id>' with the ID of the Docker image you want to push, '<dockerhub_username>' with your Docker Hub username, '<repository_name>' with the name of the repository on Docker Hub, and '<tag>' with the desired tag for the image.

4. Push the Docker Image
Finally, push the tagged Docker image to Docker Hub using the following command:
```
    docker push <dockerhub_username>/<repository_name>:<tag>
```
This command uploads the Docker image to your Docker Hub account, making it available for others to pull and use.

5. Verify Image on Docker Hub
Once the push is successful, you can verify that the Docker image is available on Docker Hub by visiting the repository page on Docker Hub in your web browser.

## Deploy to Microsoft Azue using Azure App Service Web App
1. Navigate to https://portal.azure.com/#home
2. Select **App Services**
<kbd>![Explore Photos](https://raw.githubusercontent.com/levietduc0712/Docker_Python/master/screenshots/S1.png?raw=true)</kbd>

3. Enter a name for your new web app, and create a new Resource Group. Select Linux for the Operating System.
<kbd>![Explore Photos](https://raw.githubusercontent.com/levietduc0712/Docker_Python/master/screenshots/S2.png?raw=true)</kbd>

4. Enter the docker image name.
<kbd>![Explore Photos](https://raw.githubusercontent.com/levietduc0712/Docker_Python/master/screenshots/S3.png?raw=true)</kbd>

5. Select Review and create. Review your configuration, and select Create when you are done.
