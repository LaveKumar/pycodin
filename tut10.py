# Dictionary is nothing but key value pairs
d1= {}
print(type(d1))
"""d2=[]
print(type(d2))
d3=()
print(type(d3))"""
d2= {"Lucky": "Burger","Rohan": "Fish","SkillF":"Roti","Shubham": {"B":"maggie","L": "Roti","D": "Kaddu"} }
print(d2)
d2["Ankit"]= "Junk Food"
d2[420]= "Kabbab"
print(d2["Lucky"])
print(d2["Shubham"]["B"])
# Functions in Dictionary
del d2[420] # remove d2
print(d2.copy())
# Copy() returns copy of d2
d3=d2   # remove Lucky from d2 as well as d3 d3=d2 did not make any copy

del d3["Lucky"]
print(d2.get("Lucky"))
d2.update({"Leena":"Toffee"}) # update()= adda key value

#print(d2.keys())
print(d2.items()) # .items() gives key value pairs
print("This is vaibhav here!")
