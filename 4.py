'''
feet=5
inches=2
f2i=feet*12 #5x12=60
ti=f2i+inches #60+2(given inches)
tc=ti*2.54
print("Total Height of 5 feet and 2 inches into centimeter is:",tc)
'''
#x1,x2,y1,y2=eval(input("Enter value of x1,x2,y1,y2:"))
'''
food=input("Enter your fav food:").capitalize()
print("Let me see if i can find you a",food)
'''
'''==
>
<
!=
<=
>=

and
or
not
'''

print("PET Suggestion","\nlet us know, which type of pet you want?")
size=input("Enter a size of pet you want? (small/large)").lower()
activity=input("Enter an activity of pet you want? (playful/calm)").lower()
if size=="small" and activity=="playful":
    pet="A Playful kitten 🐱"
elif size=="small" and activity=="calm":
    pet="A calm hamster 🐹"
elif size=="large" and activity=="playful":
    pet="A Dog 🐶"
elif size=="large" and activity=="calm":
    pet="Goat 🐐"
    
else:
    pet="Fish is a low maintanance pet for you"
    
print(pet)
    






