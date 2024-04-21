# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /container_app

# Copy the current directory contents into the container at /app
COPY . .

# Install anu needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]