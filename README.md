# Optimized Django App Setup in Windows VSCode 🚀🐍🛠️ 

This is the source code for a tutorial I'm writing on Dev.to that guides you through the process of setting up a new Django web app. The app itself interacts with the Internet Archive's Wayback Machine API, and allows users to input a URL, and then check if the Wayback Machine has a snapshot of that URL available. If a snapshot exists, the app displays the archived content; if not, it informs the user that the URL isn't available in the Wayback Machine.

The tutorial covers everything from installing Python and Django to creating a virtual environment and generating a requirements.txt file. You'll also learn how to add basic HTML and CSS to your app, and how to Dockerize it.

## Requirements

    Python 3.x
    Django
    Docker (optional)

## Installation

    Clone or download this repository to your local machine.
    Navigate to the project directory in a terminal or command prompt.
    Create a new virtual environment using python -m venv venv.
    Activate the virtual environment using .\venv\Scripts\Activate (Windows) or source venv/bin/activate (macOS/Linux).
    Install the required packages using pip install -r requirements.txt.
    Start the development server using python manage.py runserver.
    Open a web browser and go to http://localhost:8000/wayback_app/ to see the app running.
    
OR - Build it from scratch yourself following the guide [here](https://dev.to/siwhelan/optimized-django-app-setup-in-windows-vscode-lg2)

## Usage

The index view function in wayback_app/views.py handles both GET and POST requests. If it receives a POST request, it retrieves the URL and timestamp from the request, checks the Wayback Machine for a snapshot, and renders the appropriate template based on the availability of the URL.

You can modify and extend the app's functionality by editing the existing code or adding new views, models, and templates.

## Dockerization

To run the app in a Docker container, follow these steps:

    Install Docker on your system.
    Build the Docker image using docker build -t wayback-app ..
    Run the Docker container using docker run -p 8000:8000 wayback-app.
    Open a web browser and go to http://localhost:8000/wayback_app/ to see the app running in the container.
    
## Credits

This tutorial was created by Simon Whelan and is based on the official [Django](https://www.djangoproject.com/start/overview/) documentation and various online resources, as well as personal knowledge. Feel free to use and share it under the MIT License.
