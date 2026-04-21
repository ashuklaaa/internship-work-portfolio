import json
import os

class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone 
        self.email= email 

    def to_dict(self):
        return{
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

class Contact_Book:
    def __init__(self,filename="contacts.json"):
        self.filename=filename 
        self.contacts=[]
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as file:
                self.contacts=json.load(file)
        else:
            self.contacts=[]

    def save_contacts(self):
        with open(self.filename,"w") as file:
            json.dump(self.contacts,file,indent=4)

    def add_contacts(self,name,phone,email):
        contact=Contact(name,phone,email)
        self.contacts.append(contact.to_dict())
        self.save_contacts()
        print("\n Contact added successfully.\n")

    def search_contacts(self,keyword):
        keyword=keyword.lower()
        results= []
        for c in self.contacts:
            if (keyword in c["name"].lower() or
                keyword in c["phone"].lower() or
                keyword in c["email"].lower()) :
                results.append(c)

        return results
    
    def display_all(self):
        if not self.contacts:
            print("\n No Contacts Found. \n")
            return
        print("ALL CONTACTS")
        for i,c in enumerate(self.contacts,start=1):
            print(f"{i}.{c["name"]}   |   {c["phone"]}   |   {c["email"]}")
            print()

    def delete_contact(self,name):
        original_count=len(self.contacts)

        self.contacts=[
            c for c in self.contacts
            if c["name"].lower() !=name.lower()
        ]
        self.save_contacts
        if len(self.contacts) < original_count:
            print("\n Contact Deleted Successfully.\n")
        else:
            print("\n No Contact Found \n")



def main():
    book = Contact_Book()
    while True:
        print("\n CONTACT BOOK \n")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice=input("Ennter Choice: ")

        if choice == "1":
            name=input("Enter Name: ")
            phone=input("Enter Phone No.: ")
            email=input("Enter Email: ")
            book.add_contacts(name,phone,email)

        elif choice == "2":
            keyword = input("Enter search keyword: ")
            result = book.search_contacts(keyword)
            if result:
                print(f"\n(len(result)) contact(s) found: \n")
                for i,c in enumerate(result, start=1):
                    print(f"{i}.{c["name"]}    |    {c["phone"]}    |    {c["email"]}")
        
        elif choice == "3":
            book.display_all()

        elif choice == "4":
            name = input("Enter exact name of contact to delete: ")
            book.delete_contact(name)

        elif choice == "5":
            print("Exiting Program")

        else:
            print("Invalid Entry")



if __name__=="__main__":
    main()




