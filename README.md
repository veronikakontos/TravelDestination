# Travel Destination - a simple social media application
<!-- > Live demo [_here_](https://www.example.com). -->

## Table of Contents
- 
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Screenshots](#screenshots)
  - [Setup and Usage](#setup-and-usage)
  - [Project Status](#project-status)
  - [Room for Improvement](#room-for-improvement)
  - [Contact](#contact)

## General Information
This project is a full-stack web application built using Python, Css, Html, Flask, MySQL, and Api. 

After registering an account users can create new travel destinations, view and comment on posts from other users, as well as current weather in real-time using Weather API features.

Destintions allows users to create, edit , update or delete and share it with other registered user. User can choose country and cities in the prefered destiantion, travel date and cost.

<br>


## Technologies Used
- Python - version 3.11.1
- Flask - version 2.2.2
- MySQL - version 8.0.22 for macos10.15 on x86_64
- Python-socketio - version 5.7.2
- Flask-socketio - version 5.2.2
- Flask-bcrypt - version 1.0.1
- Bcrypt - version 4.0.1
- Pymysql - version 1.0.2

<br>


## Features
- Login and registration with validation and Bcrypt for password security
- File upload for profile photos
- Posts and comments
- Profile page
- Api weather (current weather)


<br>


## Screenshots
Login and Registration page with designated validations 
![Login and Registration](./site_images/LoginandReg.png)

Main Homepage where users can create and respond to posts
![View Destinations](./site_images/Homepage.png)

Real-time cweather from around the world
![API](./site_images/Chat.png)

Edit or Update your destination
![Edit/Update Profile](./site_images/EditProfile.png)

Delete your destination
![Delete Profile](./site_images/EditProfile.png)

<br>


## Setup and Usage
Project requirements/dependencies are located within Pipfile.lock file. 

        pipenv install 
        pipenv shell
        python3 server.py (for Mac users)
        pyhton server.py (windows users)

<br>


## Project Status
Project MVP: _Complete_. However, additional features planned.

<br>

## Room for Improvement

Room for improvement:
- CSS Responsiveness
> Aesthetic design and ease of use across a variety of device screen sizes 
- CSS File Organization
> Potentially allocate a CSS file for each HTML template page
<br>

<br>

## Contact
Created by [@veronikakontos](https://www.linkedin.com/in/veronika-kontogiannopoulos/) - feel free to contact me!