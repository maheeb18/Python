temperature = int(input("Enter today's temperature in Celsius: "))
if temperature < 20:
    outfit = "jacket"
    print("Its cold today.")
    print("You should wear a", outfit)
else:
    outfit = "t-shirt"
    print("Its warm today.")
    print("You should wear a", outfit)
is_raining = input("Is it raining today? (yes/no): ")
if is_raining == "yes":
    print("Bring an umbrella!") 
wind_speed = int(input("Enter today's wind speed in km/h: "))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It's windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("The wind is calm today.")
    print("You don't need a windbreaker over your", outfit)
has_puddles = input("Are there puddles on the ground? (yes/no): ")
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)
print("")
print("Weather check complete!")
print("====== WEATHER OUTFIT PICKER ======")
print("Today's temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("===================================")