# Capstone-Final-AlphaVantage
This program allows a user to search for a specific Stock Ticker Symbol and Interval (time), to view InterDay information about that certain Stock.

It is a Django app and running on a local host at the moment.

It includes a requirements.txt that has all packages/libraries that the app needs.

It uses the AlphaVantage API, there is an API key needed. You can get a free one at this link:
https://www.alphavantage.co/support/#api-key

-Add it into the 'ALPHA_VANTAGE_KEY' enviornment varible.
-Example Key to use: 0B7Z2RG55NXJOCF3

DB: Just using the Django db, 
-python manage.py migrate
-python manage.py makemigrations
