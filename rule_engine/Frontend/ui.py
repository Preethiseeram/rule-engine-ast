import requests
import json

def create_rule():
    rule = input("Enter rule string: ")
    response = requests.post('http://localhost:5000/create_rule', json={"rule": rule})
    print(response.json())

def evaluate_rule():
    rule = input("Enter rule string to evaluate: ")
    try:
        # Raw input from the user
        data_input = input("Enter user data in JSON format (e.g., {'age': 35, 'department': 'Sales'}): ")
        
        # Print raw input for debugging
        print(f"Raw input: {data_input}")
        
        # Safely parse the user data as JSON
        data = json.loads(data_input)  # Convert the input string to a Python dictionary
        
        # Print parsed JSON for debugging
        print(f"Parsed JSON: {data}")

        # Send rule and data to the backend API for evaluation
        response = requests.post('http://localhost:5000/evaluate_rule', json={"rule": rule, "data": data})
        
        # Print the evaluation result
        print(response.json())

    except json.JSONDecodeError as e:
        print(f"Invalid JSON input: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the API: {e}")

def view_rules():
    response = requests.get('http://localhost:5000/rules')
    print(response.json())

if __name__ == "_main_":
    while True:
        print("\n1. Create Rule\n2. Evaluate Rule\n3. View Rules\n4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            create_rule()
        elif choice == 2:
            evaluate_rule()
        elif choice == 3:
            view_rules()
        else:
            break