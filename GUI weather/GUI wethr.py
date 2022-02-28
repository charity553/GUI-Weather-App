import tkinter as tk
import json
import requests


LIGHT_GREY = '#F5F5F5'
WHITE = '#FFF'
OFF_WHITE = '#F8FAFF'
LIGHT_BLUE = '#CCEDFF'
BLUE = '#80c1ff'
SMALL_FONT = ('Arial', 10)
LARGE_FONT = ('Arial', 40, 'bold')
HEIGHT = 500
WIDTH = 600


def clicked(value):
    print('Value entered: ', value)


def format_response(weather):
    country = weather['sys']['country']
    city = weather['name']
    description = weather['weather'][0]['description']
    temperature = weather['main']['temp']
    temp = str(temperature)

    return f'Country: {country}\nCity: {city}\nDescription: {description}\nTemperature: {temp}°C'


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    weather_key = '767661b8552b44abc293432d9a9a999d'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    try:
        response = requests.get(url, params=params)
        weather = response.json()
        print(weather)
    except:
        label['text'] = 'Invalid Entry!!'
    else:
        label['text'] = format_response(weather)


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

back_image = tk.PhotoImage(file='background.png')
back_label = tk.Label(root, image=back_image)
back_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg=BLUE, bd=5,)
upper_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

entry = tk.Entry(upper_frame, font=SMALL_FONT)
entry.place(relwidth=0.70, relheight=1)

button = tk.Button(upper_frame, text='Get Weather', font=SMALL_FONT, command=lambda: get_weather(entry.get()))
button.place(relx=0.72, relwidth=0.28, relheight=1)

lower_frame = tk.Frame(root, bg=BLUE, bd=5)
lower_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6, )

label = tk.Label(lower_frame,)
label.place(relwidth=1, relheight=1)

root.mainloop()