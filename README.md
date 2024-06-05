# ChatGPT Integration Website

This repository contains the code for a simple web application that integrates with the ChatGPT API using the Django framework, HTML, CSS, and JavaScript.

## Table of Contents
- [Overview](#overview)
- [Pages](#pages)
  - [Chat Page](#chat-page)
- [Technologies Used](#technologies-used)
- [Database Models](#database-models)
- [Django Views](#django-views)

## Overview
This project is a web application that allows users to interact with ChatGPT. Users can type messages into a chat interface, and the application sends these messages to the ChatGPT API, receiving and displaying the responses.

## Pages

### Chat Page
The Chat Page includes:
- A chat interface for users to type and send messages
- Display of user messages and chatbot responses

## Technologies Used
- Django
- HTML
- CSS
- JavaScript
- Axios (for making HTTP requests)

## Database Models
This project does not use any custom database models. All interactions are handled through API calls to the ChatGPT service.

## Django Views
The project includes the following Django views and functions:

### Chatbot Response View
- **URL**: `/chatbot_response/`
- **Function**: `chatbot_response`
- **Description**: Handles POST requests containing user messages, sends the messages to the ChatGPT API, and returns the chatbot's response.

### Index View
- **URL**: `/`
- **Function**: `index`
- **Description**: Renders the chat interface page.

