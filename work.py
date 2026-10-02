print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")
day     = input("What day is it? (Monday to Sunday):").strip().capitalize()
weather = input("What is the weather like? (sunny, rainy, cloudy): ").strip().lower()
homework = input("Is your homework done? (yes/no): ").strip().lower()
print()
print(f"=== Your plan for {day} ===")
print("-" * 35)
if day in ("Saturday", "Sunday"):
    print("Its the weekend! Enjoy your free time!")
elif day == "Monday":
    print("Day type    : First day of the week.")
elif day == "Friday":
    print("Day type  : Last school day of the week! Remember to return library books.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type  : A regular school day.")
else:
    print("Day type : Day not recognized. Please enter a valid day of the week.")
if weather == "sunny" and homework == "yes":
    print("After school : Head to the park - great weather and homework is done!")
if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your umbrella - it may get wet outside.")
if not (homework == "yes"):
    print("Homework: Not done yet. Make sure to complete it before going out to play.")
if weather == "rainy" and not (homework == "yes"):
    print("Best plan: Stay in, finish your homework, and then you can do whatever you want while staying indoors.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan: All set for a school day! Enjoy your classes and have fun after school!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - You got this!")
print()
print("Plan complete! Have a great day!")  