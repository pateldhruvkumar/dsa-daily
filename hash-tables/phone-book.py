BUCKET_SIZE = 100
phoneNumberList = [[] for _ in range(BUCKET_SIZE)]

def hash_function(name):
    sum_of_char = 0
    for char in name:
        sum_of_char = sum_of_char + ord(char)

    return sum_of_char % BUCKET_SIZE

def add_contact(name, phoneNumber, email, age):
    index = hash_function(name)
    for contact in phoneNumberList[index]:
        if contact["name"] == name:
            print("Contact already exists")
            return
    phoneNumberList[index].append({"name": name, "phoneNumber": phoneNumber, "email": email, "age": age})


def find_contact(name):
    index = hash_function(name)
    for contact in phoneNumberList[index]:
        if contact["name"] == name:
            return contact
    print("Contact not found")

def delete_contact(name):
    index = hash_function(name)
    for contact in phoneNumberList[index]:
        if contact["name"] == name:
            phoneNumberList[index].remove(contact)
            return
    print("Contact not found")

add_contact("Bob", "123-456", "bob@gmail.com", 25)
add_contact("Bob", "999-999", "bob2@gmail.com", 26)
print("phoneNumberList", phoneNumberList)
print(find_contact("Bob"))  # which Bob gets returned?
delete_contact("Bob")
find_contact("Bob")
