# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install dependencies for building
RUN apt-get install -y curl

# Install Poetry using the official installer
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the project files to the container
COPY pyproject.toml poetry.lock* /app/

# Copy the rest of your application code to the container
COPY . /app

# Install project dependencies without dev dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev


# Make port 8000 available to the outside from this container
EXPOSE 8000

# Run the application using Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --reload"]
