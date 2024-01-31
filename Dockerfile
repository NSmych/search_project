# Use the official Python image as a base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project dependencies and requirements.txt into the container
COPY src/ ./src/
COPY tests/ ./tests/
COPY requirements.txt .
COPY .env .

# Install the project dependencies
RUN pip install -r requirements.txt

# Run your application
CMD ["python", "src/main.py"]
