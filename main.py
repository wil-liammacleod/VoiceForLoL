import requests
import speech_recognition as sr

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
sr.__version__