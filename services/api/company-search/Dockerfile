# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Copy the project files to the container
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-dev

# Copy the rest of your application code to the container
COPY . /app

# Make port 8000 available to the outside from this container
EXPOSE 8000

# Run the application using Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --reload"]