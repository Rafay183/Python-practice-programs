print(":::::Welcome to Pet Shop::::::")
print("Please Answer some quetions so that ican suggest you a pet")

size=input("Enter a size of pet you want? (small/large)").lower()
activity=input("Enter an activity of pet you want? (playful/calm)").lower()

if size=="small" and activity=="playful":
    pet="A playful Kitten 🐱"
elif size=="small" and activity=="calm":
    pet="A calm hamster 🐹"
elif size=="large" and activity=="playful":
    pet="A playful Dog 🐶"
elif size=="large" and activity=="calm":
    pet="A calm panda 🐼"
    
else:
    pet="Fish 🐠 is a low maintainance pet you can have!"
    
print(f"Your pet suggestion is {pet}")    
