import re

# email = input()
email = "name@test.gmail.com"
match = re.search(rf"^(\w+)@(\w+\.)?gmail\.com$", email, re.IGNORECASE)
test = 1
print(match.group(2))

    # if expression:
    #     print(expression)
    #     print("Valid")
    # else:
    #     print(expression)
    #     # print("Invalid")