from faker import Faker


class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"
    
    def contact(self):
        return f"Contacting {self.name} {self.surname} at {self.email}"
    
    @property
    def name_surname_length(self):
        return len(self.name) + len(self.surname)


class BusinessContact(BaseContact):
   def __init__(self, company, title, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.title = title
        self.work_phone = work_phone

    
fake = Faker()

def create_business_card(type, amount):
    cards = []
    for _ in range(amount):
        name = fake.name()
        surname = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        company = fake.company()
        title = fake.job()
        work_phone = fake.phone_number()

        if type == "business":
            card = BusinessContact(company, title, work_phone, name, surname, phone, email)
        else:
            card = BaseContact(name, surname, phone, email)

        cards.append(card)
    return cards




def main():

    amount = int(input("Enter the number of contacts to create: "))
    type = input("Enter the type of contact (business or personal): ").strip().lower()
    
    if type not in ["business", "personal"]:
        print("Invalid contact type. Please enter 'business' or 'personal'.")
        return
    
    contacts = create_business_card(type, amount)
    
    for contact in contacts:
        print(contact)
        print(contact.contact())
        print(f"Name and surname length: {contact.name_surname_length}")
        print("-" * 40)
 
main()


