import requests
import json
import os

key = os.environ.get('HUE_API')
group = "/groups/4/"
ipaddress = "http://192.168.1.198/api/"
light = ipaddress + key + "/groups/4/action"

sensor = "/sensors/46/"
sensorstate = ipaddress + key + sensor
sensor = ipaddress + key + sensor + "config/" +"on"

r = requests.get(light)
office_off = {'on':False}
requests.put(light, json.dumps(office_off))

sensoroff = {'on':True}
requests.put(sensor, json.dumps(sensoroff))
rofficesensor = requests.get(sensorstate)
officesensor = rofficesensor.json()['config']['on']
