for Task A --> check the code file task A.py
for Task B --> check the code file app.py
for task C read below


# Time Difference Calculation Application



This application calculates the time difference between pairs of timestamps with diffrent time zones.

## Overview

The Time Difference Calculation Application allows users to provide pairs of timestamps and get the absolute difference in seconds for each pair.

## Dependencies

- Python
- Flask

## Setup and Usage


2. Install the required dependencies: `pip install flask`
3. Start the Flask server: `python app.py` and write the code. I have included my code in app.py
4. Install Docker: Visit the Docker website (https://www.docker.com/) and download Docker for your specific operating system. Follow the installation instructions to complete the installation.
5. Create a Dockerfile: In the root directory of your Flask application, create a file named 'Dockerfile' (without all files types file extension).
6. Build the Docker image: Open a terminal or command prompt, navigate to the root directory of your Flask application (where the Dockerfile is located), and run the following command to build the Docker image: "docker build -t flask-app" .
7.     Start the containers: Open a terminal or command prompt, navigate to the root directory of your project (where the docker-compose.yml file is located), and run the following command to start the containers:"docker-compose up"
7. Open your web browser and navigate to `http://localhost:5000`

## API Endpoints

- `/time-difference` [POST]: Calculate the time difference between pairs of timestamps.

  Request Body:
{
"timestamps": [
["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"],
["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]
]
}



Response Body:
Id	"Acer" -- (Muneeb's Node ID)
[25200, 88200]