names = ["jake", "zac", "ian", "ron", "sam", "dave"] 

#I made a list, Function to check if the user input exists in the list and a way to check.

def search_name(name_list, search_term):
    if search_term in name_list:
        print(f"{search_term} found in the list!")
    else:
        print(f"{search_term} not found in the list.")

def main():
  
    search_term = input("Enter the name to search: ")  
    search_term = search_term.lower()
    search_name(names, search_term)

main()