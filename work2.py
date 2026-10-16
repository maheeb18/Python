print("=== Daily Activity Planner ===")
print("Answer 3 quick questions and I will plan your evening!\n")
print("Please answer the following questions:")
time = int(input("What is your homework time in minutes? "))
if time < 60:
    print("You have plenty of time to finish your homework and enjoy your evening!")
else:
    print("You have a lot of homework to do! Make sure to manage your time wisely.")
free_time = input("Do you have free time after homework? (yes/no): ").strip().lower()
if free_time == "yes":
    print("Great! You can relax and enjoy your evening after finishing your homework.")
else:
    print("No worries! You can still have a productive evening by focusing on your homework first.")
print()
print("Plan complete! Have a great evening!") 