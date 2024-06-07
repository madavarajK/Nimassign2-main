import requests

API_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather():
    response = requests.get(API_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_temperature_data(data, tar_datetime):
    for entry in data["list"]:
        if entry["dt_txt"] == tar_datetime:
            return entry["main"]["temp"]
    return None

def get_wind_speed_data(data1, tar1_datetime):
    for entry in data1["list"]:
        if entry["dt_txt"] == tar1_datetime:
            return entry["wind"]["speed"]
    return None

def get_pressure_data(data2, tar2_datetime):
    for entry in data2["list"]:
        if entry["dt_txt"] == tar2_datetime:
            return entry["main"]["pressure"]
    return None

def main():
    data = get_weather()
    if not data:
        return

    while True:
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "0":
            print("Terminating the program.")
            break
        elif choice == "1" or choice == "2" or choice == "3":
            target_datetime = input("Enter the date with time (YYYY-MM-DD HH:MM:SS): ")
            if choice == "1":
                temperature = get_temperature_data(data, target_datetime)
                if temperature is not None:
                    print(f"Temperature at {target_datetime}: {temperature} K")
                else:
                    print("Data not found for the specified date and time.")
            elif choice == "2":
                wind_speed = get_wind_speed_data(data, target_datetime)
                if wind_speed is not None:
                    print(f"Wind Speed at {target_datetime}: {wind_speed} m/s")
                else:
                    print("Data not found for the specified date and time.")
            elif choice == "3":
                pressure = get_pressure_data(data, target_datetime)
                if pressure is not None:
                    print(f"Pressure at {target_datetime}: {pressure} hPa")
                else:
                    print("Data not found for the specified date and time.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
