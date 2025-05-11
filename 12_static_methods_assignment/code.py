class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

cs_value= TemperatureConverter.celsius_to_fahrenheit(37)
print(cs_value)
cs_value= TemperatureConverter.celsius_to_fahrenheit(90)
print(cs_value)
