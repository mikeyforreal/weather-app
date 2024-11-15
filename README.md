# Weather App

## Overview
This Weather App is a simple web application built using Flask and the OpenWeatherMap API. It provides users with real-time weather data for any city they search for, including temperature, humidity, and wind speed. The app is designed with a sleek, responsive user interface inspired by modern weather app designs to enhance the user experience.

## Features
- **Real-time Weather Updates**: Enter any city to get current weather data.
- **Detailed Weather Information**: Displays temperature, humidity, wind speed, and more.
- **Responsive and Modern UI**: An intuitive, mobile-friendly interface that resembles native weather apps.
- **Search Functionality**: Simple search input for quick city look-up.
- **Dynamic Visuals**: Animated clouds and attractive weather-related UI elements.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for Python.
- **HTML/CSS**: Custom styles for a modern, responsive design.
- **JavaScript**: Client-side logic for user interactions.
- **OpenWeatherMap API**: Used to fetch live weather data.
- **Python-dotenv**: To securely manage API keys with environment variables.

## Installation Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   - **Windows**: `venv\Scripts\activate`
   - **MacOS/Linux**: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file and add your OpenWeatherMap API key:
   ```
   API_KEY=your_actual_api_key_here
   ```
6. Run the Flask app:
   ```bash
   python app.py
   ```
7. Access the app at `http://127.0.0.1:5000/`.

## Usage
- Open the app in your web browser.
- Type the name of the city you want to check the weather for in the search box.
- Click the search button to view the current weather information.

## Screenshots
![Weather App Screenshot](link-to-screenshot.png)

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

---
Check out the live demo [here](link-to-live-demo).

