person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print(person)

print(person["name"])
print(person['hobby'])
person["surname"] = 'Nowak'
person["married"] = False
person['sex'] = 'male'
person["hobby"] += ['bicycle']
person['phone']['mobile'] = '313131444'