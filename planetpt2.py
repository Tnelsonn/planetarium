
from planet import planet
Mars = planet("Mars ", "6.4171×1023 kg", " -82 F", "1000ft", "141.6 million mi")
Earth = planet("Earth", "5.972 * 10^24 Kg","70 F", "3389.5 Km"," 92.96 million mi")
Jupiter = planet("Jupiter", "1.898 × 10^27 kg (317.8 M⊕)","108 C","43,441 mi","483.8 million mi")
Neptune = planet("Neptune", "1.024 × 10^26 kg (17.15 M⊕)", "-201 C", "15,299 mi", "2.793 billion mi")

print("What planet would you like to see?")
p = input()

if(p == "Mars"):
    print(Mars)
if(p == "Earth"):
    print(Earth)
if(p == "Jupiter"):
    print(Jupiter)
if(p == "Neptune"):
    print(Neptune)
