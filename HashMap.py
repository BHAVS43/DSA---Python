hashmap = {
    "Student1" : "Bhavana",
    "RollNo1" : 478,
    "Student2" : "Tulsi",
    "RollNo2" : 413,
    "Student3" : "Amulya",
    "RollNo3" : 411
    }
print("The list: ", hashmap)  #printing the commplete hashmap

print(hashmap["Student1"])

hashmap["RollNo3"] = 412
print(hashmap["RollNo3"])   #to access the values of unique keys


print(hashmap.get("RollNo3")) #to get the values of the key

hashmap.pop(("RollNo2"))  #to delete the key and value pair
print(hashmap) 

hashmap.clear() #to delete the complete hashmap
print(hashmap)
