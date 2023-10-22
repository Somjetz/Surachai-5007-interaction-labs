import re

def split_my_info(my_info):
    search_result = re.split("My name:| and My ID is ", my_info)

    name = search_result[1]
    id_number = search_result[2]
    
    print(f"My name is {name}")
    print(f"My ID is {id_number}")

if __name__ == "__main__":
    my_info = "My name:Surachai Visetla and My ID is 653040500-7"
    split_my_info(my_info)
