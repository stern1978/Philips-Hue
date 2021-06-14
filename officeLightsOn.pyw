import requests
import json
import os


key = os.environ.get('HUE_API')
group = "/groups/4/"
ipaddress = "http://192.168.1.198/api/"
light = ipaddress + key + group + "action"
lightOn = ipaddress + key + group

sensor = "/sensors/46/"
sensorstate = ipaddress + key + sensor
sensor = ipaddress + key + sensor + "config/" +"on"

def state():
    while True:
        rstate = requests.get(lightOn)
        lightstate = rstate.json()['state']['any_on']
        bri = rstate.json()['action']['bri']
        if lightstate == False:
            office_on = {'on':True}
            requests.put(light, json.dumps(office_on))
        if bri < 255:
            requests.put(light, json.dumps({'bri':255}))
        sensoroff = {'on':False}
        requests.put(sensor, json.dumps(sensoroff))
        rofficesensor = requests.get(sensorstate)
        officesensor = rofficesensor.json()['config']['on']
        return

if __name__ == "__main__":
    state()
