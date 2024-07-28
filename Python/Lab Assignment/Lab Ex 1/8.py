people = [
{"name": "John Doe", "age": 30, "blood_group": "A+"},
{"name": "Jane Smith", "age": 25, "blood_group": "B-"},
{"name": "Emily Davis", "age": 40, "blood_group": "O+"},
{"name":"Michael Brown","age": 35, "blood_group": "AB-"},
{"name": "William Johnson", "age": 28, "blood_group": "A-"},
{"name": "Emma Wilson", "age": 22,"blood_group": "B+"}]

for x in people:
    print("Name:",x.get("name"),"\n")
    print("Age:",x.get("age"),"\n")
    print("Blood Group:",x.get("blood_group"),"\n")
    print("____________________________________________")