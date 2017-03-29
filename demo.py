from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY

poller = MiFloraPoller("C4:7C:8D:60:8F:E6")
print("Getting data from Mi Flora")
print("FW: {}".format(poller.firmware_version()))
print("Name: {}".format(poller.name()))
print("Temperature: {}".format(poller.parameter_value("temperature")))
print("Moisture: {}".format(poller.parameter_value(MI_MOISTURE)))
print("Light: {}".format(poller.parameter_value(MI_LIGHT)))
print("Conductivity: {}".format(poller.parameter_value(MI_CONDUCTIVITY)))
print("Battery: {}".format(poller.parameter_value(MI_BATTERY)))

#data to write into the json file
data = {}
data['miflora'] = []
data['miflora'].append({
    'Firmware': format(poller.firmware_version()),
    'Nom': format(poller.name()),
    'Température': format(poller.parameter_value("temperature")),
    'Humidité': format(poller.parameter_value(MI_MOISTURE)),
    'Lumière': format(poller.parameter_value(MI_LIGHT)),
    'Conductivité': format(poller.parameter_value(MI_CONDUCTIVITY)),
    'Batterie': format(poller.parameter_value(MI_BATTERY))
})

#open destination file, and use json.dump to write data
with open('data.json','w') as outfile:
    json.dump(data,outfile)

#open destination file, and use json.load to read data
#with open('data.json') as json_file:
#    data = json.load(json_file)
#    for p in data['miflora']:
#        print(p) 
