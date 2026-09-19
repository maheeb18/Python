name = input("Enter your real name, Agent: ")
gadget = input("Enter your favorite gadget, Agent: ")
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True
print("Name: ", name, "-> type:", type(name))
print("Gadget: ", gadget, "-> type:", type(gadget))
print("Agent Number: ", agent_number, "-> type:", type(agent_number))
print("Speed Rating: ", speed_rating, "-> type:", type(speed_rating))
print("Mission Count: ", mission_count, "-> type:", type(mission_count))
print("Height (m): ", height_m, "-> type:", type(height_m))
print("Is Active: ", is_active, "-> type:", type(is_active))
agent_number_text = str(agent_number)
print("Agent Number as text:", agent_number_text, "-> type:", type(agent_number_text))
print("Mission Count as text:", str(mission_count), "-> type:", type(str(mission_count)))
print("Speed Rating as text:", str(speed_rating), "-> type:", type(str(speed_rating)))
status_text = str(is_active)
print("Status as text:", status_text, "-> type:", type(status_text))
first_three = name[0:3]
last_letter = name[-1]
code_name = first_three + last_letter
print("First three letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Code name:", code_name)
reversed_gadget = gadget[::-1]
print("Reversed Gadget Name", reversed_gadget)
badge_line_1 = "AGENT " + code_name.upper()
badge_line_2 = "ID: " + agent_number_text
badge_line_3 = "MISSIONS: " + str(mission_count)
badge_line_4 = "SPEED: " + str(speed_rating)
badge_line_5 = "ACTIVE: " + status_text
badge_line_6 = "SECRET GADGET CODE: " + reversed_gadget.upper()
print("")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print(badge_line_5)
print(badge_line_6)
print("===============================")