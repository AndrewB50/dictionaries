#1: How to output a value from a dictionary using a key. 

emp_name_dict = {1: "Michael Jones", 2: "Andrew B.", 3: "Tamas W.", 4: "Rimington Steel"}

def get_emp_name(num):
  return emp_name_dict[num]

print(get_emp_name(2))

'''
Here, I used the key (2) to grab the value of two. Notice that with dictionaries, it asks for the key, not the position of of key:value. 
'''

#2: How to output a dictionary with multiple values per key. 

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id];


print(get_employee_from_dict(12458));

'''
Here, you can see that multiple values can belong to the same key. 
'''
