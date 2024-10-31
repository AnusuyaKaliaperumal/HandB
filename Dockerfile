# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the Python scripts and required data files into the container
COPY . .

# Run all steps in sequence, followed by the tests
CMD ["bash", "-c", "python Step1.py && python Step2.py && python Step3.py && python Step4.py && python Step5.py && pytest Test1.py"]
