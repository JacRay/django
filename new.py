class student:
    name = 'Tim'
    age = 21
    gender = 'male'


class person(student):
    pass 
p1 = person()
print(p1.name)
