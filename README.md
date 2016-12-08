# alfred
DJANGO web application for coordinating take-out orders in UIUC ACM. Synchronised with SQLite database.

### Functions

Latest build contains two applications:
authpage
  Automatic redirect to authentication page if user has not supplied credentials
homepage
  Main user interface features client user interface to allow users to place orders
  Administrator screen eventually with user privileges to add users/venues
  Eventually Twilio integration and automatic forms to place orders at registered venues

### Usage

Download Python v2.7
Clone the repository onto local machine with git clone
Download the latest version of django for Python with: pip install django (for Windows)
Navigate to the folder with manage.py
Use command python manage.py runserver to run the server
Use command python manage.py flush to clear data

Navigate to localhost port 8000 (127.0.0.1:8000) to use the server.
Instructions to host on public-facing server available at the official django website
