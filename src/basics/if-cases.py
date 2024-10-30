temperature = float(input("Enter temperature in Celsius: "))
pressure = int(input("Enter pressure in hPa: "))

if temperature > 30 and pressure > 1000:
    print("It's hot outside.")
elif temperature < 10 and pressure < 1000:
    print("It's cold outside.")
elif temperature > 20 and pressure < 1000:
    print("It's raining.")
else:
    print("The weather is pleasant.")

# match temperature:
#     case temperature if temperature > 30:
#         print("It's 30 degrees.")
#     case 20:
#         print("It's 20 degrees.")
#     case _:
#         print("It's neither 20 nor 30 degrees.")
