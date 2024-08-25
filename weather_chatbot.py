import aiml
import requests

# Initialize AIML kernel
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

# Function to get weather information
def get_weather(city):
    api_key = "f7efff2c055cf4815a2b09b14dea96af"  # Insert your actual API key here
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    
    print("API Response :",data)
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        return f"The weather in {city} is {weather_desc} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't find the weather information for that location."

# Chat loop
while True:
    input_text = input(">Human: ")
    if "WEATHER IN" in input_text.upper():
        city = input_text.split("in")[-1].strip()
        weather_info = get_weather(city)
        print(f">Bot: {weather_info}")
    else:
        response = kernel.respond(input_text)
        print(f">Bot: {response}")