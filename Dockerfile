FROM --platform=linux/amd64 python:3.11-slim-buster


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files to the container
COPY . .


# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


# build commands
# docker build -t insta-api .
# docker run -d --name insta-api -p 80:8000 insta-api
# docker stop insta-api
# docker tag insta-api:latest pavankoushik22/insta-api:latest
# docker push pavankoushik22/insta-api:latest
