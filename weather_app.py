from flask import Flask, render_template_string, request, jsonify
import requests
import datetime

app = Flask(__name__)

API_KEY = '0e520e348508ad0b00d7c664e228906d'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Arial', sans-serif; }
        body { background: linear-gradient(135deg, #162d50 0%, #1a2b4b 100%); min-height: 100vh; color: white; padding: 20px; }
        .container { max-width: 400px; margin: 0 auto; }
        .search-box { position: relative; margin-bottom: 20px; }
        .search-box input { width: 100%; padding: 15px 20px; background: rgba(255, 255, 255, 0.1); border: none; border-radius: 15px; color: white; font-size: 16px; backdrop-filter: blur(10px); }
        .search-box input::placeholder { color: rgba(255, 255, 255, 0.7); }
        .search-box button { position: absolute; right: 10px; top: 50%; transform: translateY(-50%); background: none; border: none; color: white; cursor: pointer; font-size: 20px; }
        .weather-display { text-align: center; padding: 20px; position: relative; overflow: hidden; }
        .cloud { position: absolute; opacity: 0.7; }
        .cloud-1 { top: 20px; left: 20px; animation: float 6s infinite ease-in-out; }
        .cloud-2 { top: 60px; right: 40px; animation: float 8s infinite ease-in-out; }
        @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
        .temperature { font-size: 72px; font-weight: bold; margin: 20px 0; position: relative; z-index: 1; }
        .location { font-size: 24px; margin-bottom: 10px; }
        .date { color: #8e9bae; margin-bottom: 30px; }
        .forecast { margin-top: 40px; }
        .forecast h2 { text-align: left; margin-bottom: 20px; }
        .forecast-cards { display: flex; overflow-x: auto; gap: 15px; padding: 10px 0; -ms-overflow-style: none; scrollbar-width: none; }
        .forecast-cards::-webkit-scrollbar { display: none; }
        .forecast-card { background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 15px; min-width: 80px; text-align: center; backdrop-filter: blur(10px); }
        .forecast-card .time { font-size: 14px; margin-bottom: 10px; }
        .forecast-card .icon { font-size: 24px; margin: 10px 0; }
        .forecast-card .temp { font-size: 18px; font-weight: bold; }
        .weather-details { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 30px; }
        .detail-card { background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 15px; backdrop-filter: blur(10px); }
        .detail-card .title { color: #8e9bae; font-size: 14px; margin-bottom: 5px; }
        .detail-card .value { font-size: 18px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <div class="search-box">
            <input type="text" placeholder="Search for a city..." id="searchInput">
            <button onclick="searchWeather()"><i class="fas fa-search"></i></button>
        </div>

        <div class="weather-display">
            <div class="cloud cloud-1">☁️</div>
            <div class="cloud cloud-2">☁️</div>
            <div class="location" id="location">{{ location }}</div>
            <div class="date" id="date">{{ date }}</div>
            <div class="temperature" id="temperature">{{ temperature }}°</div>
        </div>

        <div class="weather-details">
            <div class="detail-card">
                <div class="title">Humidity</div>
                <div class="value" id="humidity">{{ humidity }}%</div>
            </div>
            <div class="detail-card">
                <div class="title">Wind Speed</div>
                <div class="value" id="windSpeed">{{ wind_speed }} km/h</div>
            </div>
            <div class="detail-card">
                <div class="title">UV Index</div>
                <div class="value" id="uvIndex">N/A</div>
            </div>
        </div>
    </div>

    <script>
        async function searchWeather() {
            const searchInput = document.getElementById('searchInput').value;
            if (!searchInput) return;

            const response = await fetch(`/weather?city=${searchInput}`);
            const data = await response.json();

            if (data.success) {
                document.getElementById('location').textContent = data.location;
                document.getElementById('temperature').textContent = `${data.temperature}°`;
                document.getElementById('humidity').textContent = `${data.humidity}%`;
                document.getElementById('windSpeed').textContent = `${data.wind_speed} km/h`;
            } else {
                alert('City not found');
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, location='Montreal', date=datetime.datetime.now().strftime('%B %d, %Y'), temperature='19', humidity='62', wind_speed='12')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'success': False, 'error': 'No city provided'})

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'success': True,
            'location': data['name'],
            'temperature': round(data['main']['temp']),
            'humidity': data['main']['humidity'],
            'wind_speed': round(data['wind']['speed'] * 3.6)  # Convert m/s to km/h
        })
    else:
        return jsonify({'success': False, 'error': 'City not found'})

if __name__ == '__main__':
    app.run(debug=True)
