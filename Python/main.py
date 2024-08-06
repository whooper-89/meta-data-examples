import csv
from weather import WeatherStation
from weather import WeatherData
weather_stations = dict()
weather_data_file_path = r"../data/weather_data.csv"
with open(weather_data_file_path, "rt") as file_obj:
    reader_obj = csv.reader(file_obj)
    for data_line in reader_obj:
        id = data_line[0]
        if id == "STATION": continue
        if not id in weather_stations:
            weather_stations[id] = WeatherStation(id, data_line[1], data_line[2], data_line[3], data_line[4])
        this_station = weather_stations[id]
        this_station.add_weather_data(data_line[5], data_line[6], data_line[7], data_line[8], data_line[9], data_line[10], data_line[11], data_line[12], data_line[13], data_line[14], data_line[15])
    file_obj.close()
w_count = 0
for w in weather_stations:
    if w_count > 5: break
    print(weather_stations[w])
    station_data = weather_stations[w].data
    data_keys = reversed(station_data.keys())
    d_count = 0
    for d in data_keys:
        if d_count > 7: break
        print(f"\t{d}\n\t\t{station_data[d]}")
        d_count += 1
    w_count += 1
    
