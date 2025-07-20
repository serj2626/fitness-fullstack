FROM python:3.10-slim

# Set the environment variable to prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Set the environment variable to make Python output unbuffered
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000

# Run the command to start the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]