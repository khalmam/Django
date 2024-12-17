# Weather Prediction App ️🌦️

The Weather Prediction App allows users to view real-time weather updates for cities around the world. Built using Django for the backend and Bootstrap for the frontend, this app integrates the OpenWeatherMap API to deliver weather forecasts, real-time data, and alerts.

## Project Overview

* **Purpose:** To display real-time weather updates, forecasts, and alerts based on user-provided locations.
* **Time Taken:** 2 weeks
* **Complexity:** Intermediate
* **Technology Stack:**
    * Django 4.2
    * Bootstrap 4
    * OpenWeatherMap API
    * SQLite / PostgreSQL

## Features 

* Location-Based Search: Users can search weather details by city.
* Real-Time Updates: Fetches the latest weather data from the OpenWeatherMap API.
* Weather Forecast: Provides detailed weather predictions.
* Weather Alerts: Displays warnings for extreme weather conditions.
* User Preferences: Saves user search histories and favorite cities (if configured).

## Live Demo

To experience the live app, click here. (Add your live URL when deployed)

### Installation Guide 

Follow these steps to set up and run the Weather Prediction App on your local machine:

#### Clone the Repository

```bash
git clone [invalid URL removed]
cd weather-app
```

## Installation Guide 💻
Follow these steps to set up and run the Weather Prediction App on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```
### 2. Install Dependencies
Ensure you have Python and pip installed. Run the following command:

```bash
pip install -r requirements.txt
```
### 3. Configure the Database
By default, the app uses SQLite. If you want to switch to MySQL or PostgreSQL:

Open the settings.py file.
Update the following database settings:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Change to 'postgresql' for PostgreSQL
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',  # Use 5432 for PostgreSQL
    }
}
```

### 4. Apply Migrations
Run the following commands to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Start the Development Server

```bash
python manage.py runserver
```
Open your browser and navigate to:

```
http://127.0.0.1:8000
```
## Deployment Options ☁️
You can deploy this app on:

..* **Heroku** (quick setup for small projects)

..* **AWS** (scalable for production-ready deployments)

## API Integration 🌐
The app integrates with the **OpenWeatherMap API** to fetch weather data. To configure the API key:

1. Sign up on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your API key.

2. Add the API key in your settings file or .env file:
```python
OPENWEATHER_API_KEY = 'your_api_key_here'
```
## Learning Outcomes 📘
By building this app, you will learn:

- How to integrate and consume external APIs.
- Real-time data fetching and processing.
- Storing user preferences in databases like SQLite or PostgreSQL.
- Presenting data in a clean, graphical format using Bootstrap and JavaScript.

## Screenshots


## Contributing 🤝
Contributions are welcome! If you find bugs or have suggestions, feel free to fork this repository and create a pull request.

## License 📄
This project is licensed under the MIT License.

## Contact
For any queries or support, contact: 

- Name: Ibrahim Imam
- Email: imamkhaleel2@gmail.com
- GitHub: https://github.com/khalmam
#
Enjoy using the Weather Prediction App! ☀️🌧️


