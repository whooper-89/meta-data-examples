class WeatherStation:
    def __init__(self, id, name, latitude, longitude, elevation):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.data = dict()

    def __str__(self):
        return f"{self.name}: ({self.latitude}, {self.longitude}) @ {self.elevation} metres."

    def add_weather_data(self, date, prcp, prcp_att, snwd, snwd_att, tavg, tavg_att, tmax, tmax_att, tmin, tmin_att):
        self.data[date] = WeatherData(prcp, prcp_att, snwd, snwd_att, tavg, tavg_att, tmax, tmax_att, tmin, tmin_att)


class WeatherData:
    def __init__(self, precipitation, prcp_att, snow_depth, snwd_att, temp_avg, tavg_att, temp_max, tmax_att, temp_min, tmin_att):
        self.precipitation = precipitation
        self.prcp_att = prcp_att
        self.snow_depth = snow_depth
        self.snwd_att = snwd_att
        self.temp_avg = temp_avg
        self.tavg_att = tavg_att
        self.temp_min = temp_min
        self.tmin_att = tmin_att
        self.temp_max = temp_max
        self.tmax_att = tmax_att

    def __str__(self):
        return (f"Precipitation: {self.precipitation}mm ({self.prcp_att})\n"
                f"\t\tSnow depth: {self.snow_depth}mm ({self.snwd_att})\n"
                f"\t\tAverage temp: {self.temp_avg} ({self.tavg_att})\n"
                f"\t\tMinimum temp: {self.temp_min} ({self.tmin_att})\n"
                f"\t\tMaximum temp: {self.temp_max} ({self.tmax_att})")
