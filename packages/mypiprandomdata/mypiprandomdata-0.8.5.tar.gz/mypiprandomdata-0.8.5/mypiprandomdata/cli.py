import random
import string
import json
import re
import pkg_resources
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

class RandomData:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, user_agent, email, password,emailo,tempm,plixup,hotmail,gmail,outlook,tempm_simple,email_simpleo,email_simple):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.user_agent = user_agent
        self.email = email
        self.password = password
        self.emailo = emailo
        self.tempm = tempm
        self.plixup = plixup
        self.hotmail = hotmail
        self.gmail = gmail
        self.outlook = outlook
        self.tempm_simple = tempm_simple
        self.email_simple = email_simple
        self.email_simpleo = email_simpleo
        

def generate_realistic_random_email(first_name, last_name, random_number, selected_domain):
    methods = ["normal_order", "reverse_order", "mix_letters", "initials", "randomized", "initials_with_number"]
    probabilities = [0.35, 0.35, 0.05, 0.1, 0.05, 0.1]
    choice = random.choices(methods, probabilities)[0]

    if choice == "normal_order":
        email = f"{first_name}{last_name}{random_number}@{selected_domain}"
    elif choice == "reverse_order":
        email = f"{last_name}{first_name}{random_number}@{selected_domain}"
    elif choice == "mix_letters":
        email = f"{first_name[:3]}{last_name}{random_number}@{selected_domain}"
    elif choice == "initials":
        email = f"{first_name[0]}{last_name}{random_number}@{selected_domain}"
    elif choice == "randomized":
        email = f"{first_name}{last_name[:3]}{random_number}@{selected_domain}"
    elif choice == "initials_with_number":
        email = f"{first_name[0]}{last_name[0]}{random_number}@{selected_domain}"
    return email

def extract_filtered_emails(url='https://tempm.com/'):
    try:
        with urlopen(url) as response:
            html_code = response.read().decode('utf-8')
            email_pattern = re.compile(r'\b(?:[A-Za-z0-9-]+\.)+(?:com|net)\b')
            emails = re.findall(email_pattern, html_code)
            filtered_emails = [email for email in emails if not any(x in email for x in ['tempm', 'jsdelivr', 'google', 'fake', 'your-domain'])]
            filtered_emails = list(set(filtered_emails))
            return filtered_emails

    except HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_random_data():
    data_dir = pkg_resources.resource_filename('mypiprandomdata', 'data')

    with open(data_dir + '/data.json', 'r') as file:
        data = json.load(file)

    random_generator = random.randint(0, len(data) - 1)
    addresses = data[random_generator]['addresses']

    random_generator2 = random.randint(0, len(addresses) - 1)

    random_data = {
        "address": addresses[random_generator2]['street'],
        "city": addresses[random_generator2]['city'],
        "state": addresses[random_generator2]['state'],
        "zip_code": addresses[random_generator2]['zipcode'],
        "phone_number": addresses[random_generator2]['phone_number']
    }



    num_digits = random.randint(3, 7)
    random_number = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)

    Tempm_Mail_list = extract_filtered_emails()
    random_email_domain = random.choice(['gmail.com', 'hotmail.com', 'outlook.com'])
    random_email_domain_o = random.choice(['yahoo.com', 'icloud.com'])
    

    Tempm_Mail = random.choice(Tempm_Mail_list)
    # Tempm_Mail = f'@{Tempm_Mail}'

    
    first_name = get_random_name_from_file(data_dir, 'FirstName.txt', split_by=',')
    last_name = get_random_name_from_file(data_dir, 'LastName.txt', split_by=',')
    user_agent = get_random_name_from_file(data_dir, 'UserAgent.txt', split_by='\n')
    
    email = f"{first_name.lower()}{last_name.lower()}{random_number}{random.choice(['@gmail.com', '@hotmail.com', '@outlook.com'])}"
    gmail = f"{first_name.lower()}{last_name.lower()}{random_number}{random.choice(['@gmail.com'])}"
    hotmail = f"{first_name.lower()}{last_name.lower()}{random_number}{random.choice(['@hotmail.com'])}"
    outlook = f"{first_name.lower()}{last_name.lower()}{random_number}{random.choice(['@outlook.com'])}"
    


    plixup = f"{first_name.lower()}{last_name.lower()}{random_number}{random.choice(['@plixup.com'])}"
    email_simple = f"{first_name.lower()}{last_name.lower()}{random_number}@{random_email_domain}"
    email_simpleo = f"{first_name.lower()}{last_name.lower()}{random_number}@{random_email_domain_o}"
    email = generate_realistic_random_email(first_name.lower(), last_name.lower(), random_number, random_email_domain)
    emailo = generate_realistic_random_email(first_name.lower(), last_name.lower(), random_number, random_email_domain_o)



    tempm_simple = f"{first_name.lower()}{last_name.lower()}{random_number}@{Tempm_Mail}"
    tempm = generate_realistic_random_email(first_name.lower(), last_name.lower(), random_number, Tempm_Mail)

    password = generate_random_password()

    random_data = RandomData(first_name, last_name, random_data['address'], random_data['city'],
                             random_data['state'], random_data['zip_code'], random_data['phone_number'],
                             user_agent, email, password,emailo,tempm,plixup,hotmail,gmail,outlook,tempm_simple,email_simpleo,email_simple)

    return random_data

def get_random_name_from_file(directory, filename, split_by=None):
    file_path = directory + '/' + filename
    with open(file_path, 'r') as file:
        names = file.read().strip().split(split_by) if split_by else file.readlines()
    return random.choice(names).strip().strip('",')

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = random.randint(8, 12)
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

def main():
    random_data = get_random_data()
    print("Randomly Generated Data:")
    print("First Name:", random_data.first_name)
    print("Last Name:", random_data.last_name)
    print("Email:", random_data.email)
    print("Password:", random_data.password)
    print("Address:", random_data.address)
    print("City:", random_data.city)
    print("State:", random_data.state)
    print("Zip Code:", random_data.zip_code)
    print("Phone Number:", random_data.phone_number)
    print("User Agent:", random_data.user_agent)

if __name__ == '__main__':
    main()
