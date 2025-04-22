fahrenheit_temps = [32, 68, 100, 212]  
celsius_temps = [(temp - 32) * 5/9 for temp in fahrenheit_temps]

print("Celsius Temperatures:", celsius_temps)
