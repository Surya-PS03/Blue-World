import requests

base_url = "http://api.weatherstack.com/current?"


def temp(cty, key, Base_url):
    url = Base_url + "access_key=" + key + "&query=" + cty
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        city = data['location']['name']
        tempe = data['current']['temperature']
        time = data['location']['localtime']
        humid = data['current']['humidity']
        uv = data['current']['uv_index']
        visi = data['current']['visibility']
        print(f"The city: {city}")
        print(f"The temperature: {tempe}")
        print(f"The time: {time}")
        print(f"The humidity: {humid}")
        print(f"The uv index: {uv}")
        print(f"The visibility: {visi}")
    else:
        print(f"error:{response.status_code}")


citi = input("Enter city name: ")
access_key = input("Enter the access_key: ")
temp(citi, access_key, base_url)
