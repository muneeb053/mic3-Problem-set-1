# Use a base Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application code and requirements
COPY app.py .
COPY requirements.txt .

# Install the required dependencies
RUN pip install -r requirements.txt

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the entrypoint command to run the Flask app
CMD ["python", "app.py"]
