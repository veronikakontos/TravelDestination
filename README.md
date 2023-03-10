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
- Python
- Flask
- MySQL 
- Flask-bcrypt 
- Bcrypt
- Pymysql 
- API
- Html5
- CSS

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
![Login and Registration](/screenshots/logreg.png)

Main Homepage where each user can see all destinations created by user or other users. Delete destination can only creator of the destination.
![All Destinations](/screenshots/alldest.png)
![All Destinations](/screenshots/deletedest.png)

Welcome page where user who is log in, will see his/her/their name and can see destination and all info about the trip
![All Destinations](/screenshots/welcomedest.png)

Real-time weather from choosen city destination
![API](/screenshots/apiweather.png)

Edit or Update destination
![Edit/Update Profile](/screenshots/createdest.png)

Popular destination is preview as video(repeating 5sec)
![Video of popular destination](/screenshots/video.png)

<br>


## Setup and Usage
Project requirements/dependencies are located within Pipfile.lock file. 

        pipenv install 
        pipenv shell
        python3 server.py (for Mac users)
        python server.py (windows users)

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