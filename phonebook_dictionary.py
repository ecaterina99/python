people=[
    {"name":"Ecaterina", "number":"069703999", "gmail":"tricolicikatea1999@gmail.com"},
    {"name":"Alex", "number":"069722626", "gmail":"tricolicialex@gmail.com"},
    {"name":"Dorin", "number":"069758903", "gmail":"bjrdorin@gmail.com"},
    ]
    
name=input("Name: ")
    
for person in people:
     if person["name"]==name:
         number=person["number"]
         gmail=person["gmail"]
         print(f"Found! Number: {number}, gmail: {gmail}")
         break
else:
     print("Not found")