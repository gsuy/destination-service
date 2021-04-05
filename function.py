import math
import json
import numpy as np
from keras.models import load_model


model = load_model('data/find_destination_model.h5')
min_max = {"maxLong":0.07807520000001489 , "minLong":-0.2694200999999907 , "maxLat":0.18197406000000171 , "minLat":-0.14342057999999724}
f = open('data/grid_info.json')
grid_info = json.loads(f.read())
f.close()
day_table = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

def scaleup(x):
    x_pre = ((x[0] - 0.1)/(0.9))*(min_max['maxLong']-min_max['minLong'])+min_max['minLong']-114
    y_pre = ((x[1] - 0.1)/(0.9))*(min_max['maxLat']-min_max['minLat'])+min_max['minLat']+51
    return [x_pre,y_pre]

def findDistance(x,y):
    x = np.array(x)
    y = np.array(y)
    return math.sqrt(sum((x-y)**2))

def findNearGrid(x):
    name = None
    min_distance = None
    for key in grid_info:
        temp_distance = findDistance([grid_info[key]["longitude"],grid_info[key]["latitude"]],x)
        if name == None:
            name = key
            min_distance = temp_distance
        elif min_distance > temp_distance:
                name = key
                min_distance = temp_distance
    return name

def convert_data_to_model(tripInfo):
    day_list = [0]*7
    hour_list = [0]*24
    day_target = day_table.get(tripInfo.dayofweek.lower(), False)
    if type(day_target) != bool:
        hour_list[tripInfo.hour] = 1
        day_list[day_target] = 1
        latitude =  (((tripInfo.latitude-51) - min_max['minLat'])/(min_max['maxLat']-min_max['minLat']))*(0.9)+0.1
        longitude = (((tripInfo.longitude+114) - min_max['minLong'])/(min_max['maxLong']-min_max['minLong']))*(0.9)+0.1
        result = day_list+ hour_list
        result.append(longitude)
        result.append(latitude)
        return np.array([result])
    return False