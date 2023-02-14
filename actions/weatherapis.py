import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()

show_dict = {
    'Latitude': 'latitude',
    'Longitude': 'longitude',
    'Resolved Address': 'resolvedAddress',
    'Address': 'address',
    'Timezone': 'timezone',
    'Timezone Offset': 'tzoffset',
    'Alerts': 'alerts',
    'Date time': 'datetime',
    'Temperature Maximum': 'tempmax',
    'Temperature Minimum': 'tempmin',
    'Temperature': 'temp',
    'Feels like Maximum': 'feelslikemax',
    'Feels like Minimum': 'feelslikemin',
    'Feels like': 'feelslike',
    'Humidity': 'humidity',
    'Precipitation': 'precip',
    'Precipitation Type': 'preciptype',
    'Snow': 'snow',
    'Snow Depth': 'snowdepth',
    'Wind Gust': 'windgust',
    'Wind Speed': 'windspeed',
    'Wind Direction': 'winddir',
    'Sea Level Pressure': 'pressure',
    'Cloud cover': 'cloudcover',
    'Visibility': 'visibility',
    'Solar radiation': 'solarradiation',
    'Solar energy': 'solarenergy',
    'UV Index': 'uvindex',
    'Severe Risk': 'severerisk',
    'Sunrise time': 'sunrise',
    'Sunset time': 'sunset',
    'Moonphase': 'moonphase',
    'Short text about the weather': 'conditions',
    'Description of the weather for the day': 'description',
    'A weather icon': 'icon'
}

string_print_dict = {
    'latitude': "\tLatitude: {dynamic}\n",
    'longitude': "\tLongitude: {dynamic}\n",
    'resolvedAddress': "\tResolved Address: {dynamic}\n",
    'address': "\tAddress: {dynamic}\n",
    'timezone': "\tTimezone: {dynamic}\n",
    'tzoffset': "\tTimezone Offset: {dynamic}\n",
    'alerts': "\tAlerts: {dynamic}\n",
    'datetime': "\tDate time: {dynamic}\n",
    'tempmax': "\tTemperature Maximum: {dynamic}°C\n",
    'tempmin': "\tTemperature Minimum: {dynamic}°C\n",
    'temp': "\tTemperature: {dynamic}°C\n",
    'feelslikemax': "\tFeels like Maximum: {dynamic}°C\n",
    'feelslikemin': "\tFeels like Minimum: {dynamic}°C\n",
    'feelslike': "\tFeels like: {dynamic}°C\n",
    'humidity': "\tHumidity: {dynamic}%\n",
    'precip': "\tPrecipitation: {dynamic} mm\n",
    'preciptype': "\tPrecipitation Type: {dynamic}\n",
    'snow': "\tSnow: {dynamic} cm\n",
    'snowdepth': "\tSnow Depth: {dynamic} cm\n",
    'windgust': "\tWind Gust: {dynamic} kph\n",
    'windspeed': "\tWind Speed: {dynamic} kph\n",
    'winddir': "\tWind Direction: {dynamic}° from true north\n",
    'pressure': "\tSea Level Pressure: {dynamic} mb\n",
    'cloudcover': "\tCloud cover: {dynamic}%\n",
    'visibility': "\tVisibility: {dynamic} km\n",
    'solarradiation': "\tSolar radiation: {dynamic} W/sq.m\n",
    'solarenergy': "\tSolar energy: {dynamic} WJ/sq.m\n",
    'uvindex': "\tUV Index: {dynamic}/10.0 \n",
    'severerisk': "\tSevere Risk: {dynamic}\n",
    'sunrise': "\tSunrise time: {dynamic}\n",
    'sunset': "\tSunset time: {dynamic}\n",
    'moonphase': "\tMoonphase: {dynamic}\n",
    'conditions': "\tShort text about the weather: {dynamic}\n",
    'description': "\tDescription of the weather for the day: {dynamic}\n",
    'icon': "\tA weather icon: {dynamic}\n"
}


def moon_phase_function(moon_phase_digit):
    moon_phase = moon_phase_digit
    if moon_phase_digit == 0:
        moon_phase = 'New Moon'
    elif 0 < moon_phase_digit < 0.25:
        moon_phase = 'Waxing Crescent'
    elif moon_phase_digit == 0.25:
        moon_phase = 'First Quarter'
    elif 0.25 < moon_phase_digit < 0.5:
        moon_phase = 'Waxing Gibbous'
    elif moon_phase_digit == 0.5:
        moon_phase = 'Full Moon'
    elif 0.5 < moon_phase_digit < 0.75:
        moon_phase = 'Waning Gibbous'
    elif moon_phase_digit == 0.75:
        moon_phase = 'Last Quarter'
    elif 0.75 < moon_phase_digit <= 1:
        moon_phase = 'Waning Crescent'
    return moon_phase


def clearing_data(json_data: dict):
    for key, value in json_data.items():
        if key == 'moonphase':
            json_data[key] = moon_phase_function(moon_phase_digit=json_data[key])
        elif type(json_data[key]) is str or type(json_data[key]) is int or key in ['latitude', 'longitude', 'tzoffset']:
            continue
        elif type(json_data[key]) is float:
            json_data[key] = str(round(value))
        elif type(json_data[key]) is dict:
            clearing_data(value)
        elif type(json_data[key]) is list:
            if len(json_data[key]) > 0:
                if type(json_data[key][0]) is dict:
                    for i in range(len(json_data[key])):
                        clearing_data(value[i])
                elif type(json_data[key]) is list and len(json_data[key]) > 0:
                    json_data[key] = ', '.join(json_data[key])
                elif type(json_data[key]) is list:
                    json_data[key] = json_data[key][0]
                else:
                    continue
            else:
                continue
        elif json_data[key] is None:
            json_data[key] = '--'
        else:
            continue
    return json_data


def finding_location(call_location):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={call_location}&key={os.getenv('GOOGLE_API_KEY')}"
    response = requests.request("GET", url, headers={}, data={})
    location_details = response.json()
    if location_details.get('status') == "ZERO_RESULTS":
        print("Its not a valid location")
        return None
    elif location_details.get('status') == "OK":
        print("Its a valid location.", location_details['results'][0].get('formatted_address'))
        return location_details['results'][0].get('formatted_address')


# finding_location('porbandar')


def finding_weather(call_location, call_day_range='today'):
    data = '/today'
    main_link = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
    location = f'{call_location}'
    day_range = f'{data}'
    unit_group = 'unitGroup=metric'
    key = f"key={os.getenv('VISUAL_CROSSING_WEATHER_API_KEY')}"
    content_type = 'contentType=json'
    includes = 'include=obs,remote,statsfcst,fcst,days,events,alerts,current'  # stats,
    utils_elements = 'datetime,name,address,resolvedAddress,latitude,longitude,'
    temperature_elements = 'tempmax,tempmin,temp,feelslikemax,feelslikemin,feelslike,'
    atmosphere_elements = 'humidity,precip,preciptype,snow,snowdepth,windgust,windspeed,winddir,pressure,cloudcover,visibility,'
    sun_moon_elements = 'solarradiation,solarenergy,uvindex,sunrise,sunset,moonphase,'
    data_elements = 'conditions,description,icon'
    link = f"{main_link}{location}{day_range}?{unit_group}&{key}&{content_type}&{includes}&elements={utils_elements}{temperature_elements}{atmosphere_elements}{sun_moon_elements}{data_elements}"
    result = requests.get(link)
    print(result.url)
    if result.status_code == 200:
        return_data = {
            "status_code": result.status_code,
            "message": "request was successful",
            "payload": clearing_data(result.json())
        }
    elif result.status_code == 400:
        return_data = {
            "status_code": result.status_code,
            "message": "request was unsuccessful, your requests is invalid in some way (invalid dates, bad location parameter etc).",
            "payload": result.text
        }
    elif result.status_code == 401:
        return_data = {
            "status_code": result.status_code,
            "message": "You are not authorized to perform this action!",
            "payload": result.text
        }
    elif result.status_code == 429:
        return_data = {
            "status_code": result.status_code,
            "message": "You have exceed your plan concurrency limits or daily or monthly cost limits.",
            "payload": result.text
        }
    elif result.status_code == 500:
        return_data = {
            "status_code": result.status_code,
            "message": "Sorry! we are using 3rd party API for weather search, and there is some server error from their side.",
            "payload": result.text
        }
    else:
        return_data = {
            "status_code": result.status_code,
            "message": "Unexpected error has been occurred!",
            "payload": result.text
        }
    return return_data


# print(finding_weather('New York'))


def pass_all_details(json_data):
    fetch_list = ['latitude', 'longitude', 'resolvedAddress', 'address', 'timezone', 'tzoffset', 'alerts', 'datetime',
                  'tempmax',
                  'tempmin', 'temp', 'feelslikemax', 'feelslikemin', 'feelslike', 'humidity', 'precip', 'preciptype',
                  'snow', 'snowdepth', 'windgust',
                  'windspeed', 'winddir', 'pressure', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy',
                  'uvindex', 'severerisk', 'sunrise',
                  'sunset', 'moonphase', 'conditions', 'description', 'icon']
    general = f"General location details:\n"
    current = f"Current weather condition:\n"
    days = [f"Average weather throughout the day{count + 1}\n" for count in
            range(len(json_data.get('payload').get('days')))]
    print(days)
    for detail in fetch_list:
        if detail != 'moonphase':
            if detail in json_data.get('payload'):
                general += string_print_dict[detail].format(dynamic=json_data.get('payload').get(detail))
                continue
            if detail in json_data.get('payload').get('currentConditions'):
                current += string_print_dict[detail].format(
                    dynamic=json_data.get('payload').get('currentConditions').get(detail))
            if detail in json_data.get('payload').get('days')[0]:
                for count in range(len(json_data.get('payload').get('days'))):
                    if detail in json_data.get('payload').get('days')[count]:
                        days[count] += string_print_dict[detail].format(
                            dynamic=json_data.get('payload').get('days')[count].get(detail))
        else:
            current += string_print_dict[detail].format(
                dynamic=moon_phase_function(json_data.get('payload').get('currentConditions').get(detail)))
            for count in range(len(json_data.get('payload').get('days'))):
                days[count] += string_print_dict[detail].format(
                    dynamic=moon_phase_function(json_data.get('payload').get('days')[count].get(detail)))
    return {'General Details:': general, 'Current Details:': current, 'Throughout the Day:': days[0]}
