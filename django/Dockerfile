FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# work directory
WORKDIR /django/

# Install dependencies
COPY ./requirements.txt /django/
RUN pip install --upgrade pip && pip install -r ./requirements.txt 

# Copy project
COPY . /django/