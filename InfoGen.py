# © 2025 Fr0zst. All rights reserved. 
# Unauthorized copying prohibited.

import pyfiglet
import secrets
import string
import random

# Banner
banner = pyfiglet.figlet_format("LIBTARD", font="larry3d")
print(banner)
print("Made by, Fr0zst\n")

# Menu
def menu():
    print("\nSelect an option:")
    print("1. Temporary Email")
    print("2. Temporary Gmail")
    print("3. Temporary Number")
    print("4. Password Generator")
    print("5. Exit")

# Simulated Temp Emails
def temp_email():
    domains = ["@tempmail.org", "@emailnator.com", "@internxt.com"]
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(domains)
    print(f"\nGenerated temporary email: {username}{domain}")

# Simulated Gmail
def temp_gmail():
    username_length = random.randint(6, 12)
    username_chars = string.ascii_lowercase + string.digits + "_"
    username = ''.join(random.choices(username_chars, k=username_length))
    print(f"\nGenerated temporary Gmail: {username}@gmail.com")

# Temporary Numbers by Country
def temp_number():
    country_codes = {
        "US": "+1",
        "UK": "+44",
        "CA": "+1",
        "AU": "+61",
        "IN": "+91"
    }

    print("\nSelect a country for the temporary number:")
    for i, country in enumerate(country_codes.keys(), 1):
        print(f"{i}. {country}")
    choice = input("Enter number: ")

    try:
        country_list = list(country_codes.keys())
        country_selected = country_list[int(choice)-1]
        code = country_codes[country_selected]
        number = ''.join([str(random.randint(0,9)) for _ in range(10)])
        print(f"Generated temporary number ({country_selected}): {code}{number}")
    except:
        print("Invalid choice.")

# Password Generator
def generate_password():
    length = int(input("Enter password length: "))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    print(f"Generated password: {password}")

# Main loop
while True:
    menu()
    option = input("Enter your choice: ")
    if option == "1":
        temp_email()
    elif option == "2":
        temp_gmail()
    elif option == "3":
        temp_number()
    elif option == "4":
        generate_password()
    elif option == "5":
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")

