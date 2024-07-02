# Installation

- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

# Python URL Shortener

This project aims to create a URL shortener with some additional features to enhance its functionality. The program will be developed in Python and include features such as custom short URLs, URL analytics, short URL expiration, and user authentication.

## Features

1. _URL Shortening:_

   - Generate a short URL for a given long URL.
   - Ensure the short URL is unique and redirects to the original long URL.

2. _Custom Short URLs:_

   - Allow users to specify custom short URLs.
   - Validate the uniqueness of custom short URLs and handle conflicts.

3. _URL Analytics:_

   - Track the number of times each short URL is accessed (clicked).
   - Provide a function to retrieve and display analytics for a given short URL.

4. _Expiration of Short URLs:_

   - Add an optional expiration feature for short URLs.
   - Short URLs should become invalid after the specified expiration date.

5. _User Authentication:_

   - Implement a simple authentication system.
   - Allow users to log in, view their created short URLs, and delete them if needed.

6. _User Interface:_

   - Create a command-line or web-based interface for users to interact with the URL shortener.
   - Display messages for successful URL shortening, analytics retrieval, and user authentication.

7. _Error Handling:_
   - Implement error handling for cases such as invalid URLs, duplicate custom short URLs, expired short URLs, etc.

## Running the project

1. _Installation:_

   - Clone the repository.
   - Install required dependencies (if any).

2. _Usage:_

   - Run the main Python script.
   - Interact with the URL shortener through the provided interface.

3. _Configuration:_
   - Modify configuration files for settings such as database connection, expiration rules, etc.

## Time Management

Set a timer to ensure the completion of the project within 2 hours.

## Contributor

- [Your Name]
