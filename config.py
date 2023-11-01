BOT_API_TOKEN = '6336550320:AAFv0Nmr4V5VVZf9azY0n-WcWeM4QvKjP3g'
WEATHER_API_KEY = 'd556e725fa526dc0adf5a8a40fb6069e'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)