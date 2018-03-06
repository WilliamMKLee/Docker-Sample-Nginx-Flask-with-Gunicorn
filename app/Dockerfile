FROM python:3-alpine

# Copying the requirements for installation to take
# advantage of the caching.
COPY requirements.txt .
RUN pip install -r ./requirements.txt && rm ./requirements.txt

WORKDIR /app

