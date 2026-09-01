students = [ 
    {"name" : "Hermione", "house" : "Gryfinder", "patronus" : "Ottar"},
    {"name" : "Herry", "house" : "Gryfinder", "patronus" : "Stag"},
    {"name": "Ron" , "house" : "Gryfinder" , "patronus" : "jack Russell trrrier"},
    {"name" : "Draco", "house" :"Slytherion", "patronus": None},
]
for student in students :
    print (student["name"], student["house"], student["patronus"], sep=", ")