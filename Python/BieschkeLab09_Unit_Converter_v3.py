#Lab9 Unit Converter 
'''
Version 3
Allow the user to also enter the units. Then depending on the units, 
convert the distance into meters. The units we'll allow are feet, miles, 
meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
1 yard is 0.9144 m
1 inch is 0.0254 m
'''

print("Hello! We're converting distances to meters!")
units = input("What kind of distance are we converting today?\n>")
units = units.lower()
distance = input(f"How many {units} are we converting today?\n>")
distance = int(distance)
meter = 0

if units not in ["km", "kilo", "kilometer", "kilometers",
                 "mile", "miles", "mi", "feet", "ft", "m", "meter", 
                 "meters", "in", "inch", "inches", "yd", "yard", "yards"]:
    print("Just basic distances today please.")

else:
    if units in ["km", "kilo", "kilometer", "kilometers"]:
        meter = distance * 1000

    elif units in ["mile", "miles", "mi"]:
        meter = distance * 1609.34

    elif units in ["feet", "ft"]: 
        meter = distance * 0.3048

    elif units in ["m", "meter", "meters"]:
        print("That's meters already!")

    elif units in ["in", "inch", "inches"]:
        meter = distance * 0.0254

    elif units in ["yd", "yard", "yards"]:
        meter = distance * 0.9144

    else:
        print("Hey! That's not a number!")
        

    print(f"Fab! Your distance is {meter} meters!") 