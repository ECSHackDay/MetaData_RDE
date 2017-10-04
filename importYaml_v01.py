#Sample Yaml file import

import yaml
from io import open
import os
#import matplotlib.pyplot as plt



def importYaml(fileName):
    with open("%s\\%s.yaml" % (os.getcwd(), fileName), 'r') as stream:
        try:
            doc = yaml.load(stream)

        except yaml.YAMLError as exc:
            print(exc)

    data = doc["datapoints"]

    del doc["datapoints"]

    return data, doc

def extractData(dataDict):
    time = []
    current = []
    voltage = []
    for point in data:
        time.append(point["time"].split(' ')[0])
        current.append(point["current"].split(' ')[0])
        voltage.append(point["voltage"].split(' ')[0])

    return time,current,voltage


data, metaData =importYaml("RDEtest_100mV")

time,current,voltage = extractData(data)

print(time)
print(current)
print(voltage)



