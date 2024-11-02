'''
x1,x2,y1,y2=eval(input("Enter values for x1,x2,x3,x4:"))
Distance=pow(pow(x2-x1, 2)+pow(y2-y1,2),1/2)
print(Distance)

(-b+(b2-4ac)^1/2)/2a
(-b+(b**2-4*a*c)**1/2)/2*a
'''
'''
food=eval(input("Enter a food you like:"))
print("Let me see if i can find you a",food.upper())
'''
'''
==
>
<
>=
<=
!=
'''
print("Welcome to pet suggestions point")
print("Answer a few questions and i'll suggest you a good pet for you,\n")
size=input("Enter a size of pet you want? (small/large):").lower()
activity=input("Enter an activity you want? (playful/calm):").lower()

if size== "small" and activity=="playful":
    pet = "A playful Kitten 🐱"
elif size=="small" and activity =="calm":
    pet = "A calm hamster 🐹"
elif size=="large" and activity =="playful":
    pet = "A playful Dog 🐶"
elif size=="large" and activity == "calm":
    pet = "A Turtle 🐢"  
else:
    pet ="A low maintanance fish 🐟 is a perfect for any lifestyle"  
print(f"A perfect suggestion for you to have a pet = {pet}")









