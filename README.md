Event Manager

Event Manager is a Django-based web application for organizing and managing events. It enables users to create, update, and track events efficiently, whether it's a conference, meetup, workshop, or social gathering.

Features

User registration and login

Create, edit, and delete events

RSVP and attendee tracking

Event categories and tagging

Public and private event settings

Calendar and list views of upcoming events

Getting Started

Follow these steps to get Event Manager running locally on your system.

Prerequisites

Python 3.8+

Git (optional, for cloning the repo)

Installation

Clone the repository

git clone https://github.com/your-username/event-manager.git
cd event-manager

Create and activate a virtual environment

Mac/Linux:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

Install dependencies

pip install django

Apply migrations

python manage.py migrate

Run the development server

python manage.py runserver

Open in browser
Visit http://127.0.0.1:8000/ in your browser.

Contributing

Have ideas for features or improvements? Feel free to fork the project, make changes, and submit a pull request.



