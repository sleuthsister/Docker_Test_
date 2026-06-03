

    #Start with a lightweight LINUX computer that has python pre installed 
    FROM python:3.11-slim

    # Create a folder inside the container called app
    WORKDIR /app

    #Copy the requirements list into the container and install them
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    #Copy all python scripts into the container
    COPY . .
