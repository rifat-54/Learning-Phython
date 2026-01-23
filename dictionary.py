info={
    "name":"astha",
    "subject":["python","C","Go"],
    "topics":("dict","set"),
    "age":34,
    "is_adult":True,
    12:343.34
}

# print(type(info))

# info["name"]=45
# info["surname"]="fatacasto"
# print(info)

# null_dict={}
# null_dict["name"]="rifat"
# print(null_dict)

student={
    "name":"rifat",
    "subject":{
        "phy":34,
        "chem":54,
        "math":46
    }
}

# print(student["subject"]["chem"]) 
# print(len(list(student.keys())))
# print(list(student.values()))

# print(list(student.items()))
# pairs=list(student.items())

# print(pairs[0])

# print(student["name2"])   # return error if not found
# print(student.get("name2"))   # return none if not found


# student.update({"name":"pagla"})

new_dict={
    "city":"dhaka",
    "age":14
}

student.update(new_dict)

print(student)