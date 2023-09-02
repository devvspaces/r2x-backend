# RoadFlow - Generative Learning Platform for Tech Skills

Welcome to the ATRONS GitHub repository! Roadflow is an online learning platform designed to provided users with a seamless and personalized experience for learning tech skills using generative AI. This repository contains the source code and development history of the RoadFlow Platform API.

This is the backend api for RoadFlow. It uses DRF for api development and MindsDB for user reviews classification, sentiment analysis and generating texts. The API follows REST API requirements. It can be tested from the Swagger documentation or any client.

## Structure

The repository structure is as follows:

- `src` - This directory contains the backend code of the Roadflow platform, including the API endpoints, database models, and business logic implemented in Python using the Django Rest framework.
- `docs` - This directory contains the documentation for the Roadflow platform, including the API documentation, database schema, and other relevant information.
- `src/models` - This directory contains the AI models used by the Roadflow platform, including the MindsDB models for user reviews classification, sentiment analysis and generating texts.

## Purpose

The purpose of this project is to provide a platform for users to learn tech skills using generative AI and personalized test feedback. The platform will provide users with a seamless and personalized experience for learning tech skills using generative AI. We aim to create a platform that allows users to learn by following a personalized and curated learning path. Ensuring they are learning the right topics at the right time and accordingly.

## How Generative AI Models are Solving the Problem

Roadflow leverages Generative AI models to enhance the it's core functionality, especially the learning experience for users in the domain of Question and Answering. This is built in such a way that the application domain is not coupled with the model used. This allows for easy swapping of models in the future without affecting the core functionality of the platform.

MindsDB is currently used to utilize open ai and hugging face models for the following:

- User reviews classification
- Sentiment analysis
- Generating texts

By incorporating Generative AI models into Roadflow using MindsDB allows the platform to train and fine-tune the models based on the data accumulated over time. This allows the platform to provide a personalized experience for users. Users can get detailed feedback on their tests and learn from their mistakes. This is done by using the generative AI models to generate feedback for the user based on their test results. Allowing for dynamic but curated learning paths for users. Users can be assured that they are learning the right topics at the right time and accordingly no matter what tech skill they are learning.


## Figma Design

Here is a link to the [figma](https://www.figma.com/file/4sWAOaXGdd16N5AlyFVSBl/RoadTrack-Project?node-id=10-39&t=J5xBuuZrD2TIcSLZ-0).

## DB Diagram Design

Here is a db diagram for the project database - [Diagram](https://dbdiagram.io/d/6437cb1c8615191cfa8d9bc1)

![](./Roadflow%20DB.png)

## Prerequisites

- Python 3
- MindsDB Python SDK
- Redis

## Installing

A step by step series of examples that tell you how to get a development environment running.

> First you have to clone the project on your machine

- Setup virtual enviroment

    Debian

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    Windows

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

- Install dependencies in the project root dir

    ```bash
    pip install -r requirements.txt
    cd src
    mkdir logs
    ```

- Setup the env file

    ```bash
    cp env.example .env
    ```

    For the email config:

    This is not required, for it is used to send OTP for account registration. Email sending is disabled by default in development.

    For MINDSDB config:

    Create a [MindsDB](https://mindsdb.com/) account. If you don't have one, sign up for a free account at [cloud.mindsdb.com](http://cloud.mindsdb.com/).

    Set `MINDSDB_SERVER_USERNAME` to your email, and `MINDSDB_SERVER_PASSWORD` to your password.

    Redis config:

    If you don't have redis installed you can configure `settings/base.py` to use Django Memcache. Cache is used for OTP verification.

- Run migrations

    ```bash
    python manage.py migrate
    ```

> The site is configured to run with SQLite but you can configure it to use postgress in production.

## Running the API

To run the API on your machine. Make sure you are in the `src` directory before you run the command below.

```bash
python manage.py runserver
```

API server will run on `http://localhost:8000/`. Visit [Swagger](http://localhost:8000/docs/) to read the Swagger API documentation.

## ⛏️ Built Using

- [Django](https://www.djangoproject.com/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Building Web APIs
- [Redis](https://redis.io/) - In-memory data store
- [Python](https://www.python.org/) - Programming Language
