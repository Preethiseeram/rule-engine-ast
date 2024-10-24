
# Rule Engine with AST

This project implements a 3-tier rule engine using an Abstract Syntax Tree (AST) to determine user eligibility based on attributes like age, department, income, and experience. The rule engine allows for dynamic creation, combination, and evaluation of rules via a simple API.

## Features
- **AST-based Rule Representation**: Use an AST to define and combine rules.
- **Dynamic Rule Creation**: Supports the creation of custom rules from input strings.
- **Rule Evaluation**: Evaluate user data against dynamically created rules.
- **API Endpoints**: Expose APIs to create rules, combine multiple rules, and evaluate rules against user data.

---

## Project Structure

```
.
├── backend
│   └── api.py         # Main API for the rule engine (Flask app)
├── frontend
│   └── ui.py          # Simple command-line interface (CLI) for rule entry
├── tests
│   └── test_api.py    # Test cases for API endpoints
└── README.md          # Project documentation
```

---

## Prerequisites

- **Python 3.7+**: Make sure Python is installed on your machine.
- **Flask**: The backend API is built using Flask.
- **Requests**: The frontend uses the requests library to interact with the API.

You can install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

---

## Setup

1. **Install Dependencies**

   Navigate to the project directory and install the required Python packages:

   ```bash
   cd rule-engine-ast
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should include:
   ```
   Flask==2.0.1
   requests==2.26.0
   ```

2. **Running the Backend (API)**

   To start the Flask API server, navigate to the `backend/` directory and run the following command:

   ```bash
   python backend/api.py
   ```

   The API will be accessible at `http://127.0.0.1:5000/`.

3. **Running the Frontend (CLI)**

   In another terminal, navigate to the `frontend/` directory and run the `ui.py` script to interact with the API:

   ```bash
   python frontend/ui.py
   ```

---

## API Endpoints

### 1. `POST /create_rule`

Create an AST from a rule string.

- **URL**: `/create_rule`
- **Method**: `POST`
- **Request Body**: JSON object with the rule string.
  
  Example:
  ```json
  {
    "rule": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))"
  }
  ```

- **Response**: The generated AST representing the rule.

### 2. `POST /combine_rules`

Combine multiple rules into a single AST.

- **URL**: `/combine_rules`
- **Method**: `POST`
- **Request Body**: JSON array of rule strings.

  Example:
  ```json
  {
    "rules": [
      "age > 30 AND department = 'Sales'",
      "salary > 50000 OR experience > 5"
    ]
  }
  ```

- **Response**: Combined AST of the rules.

### 3. `POST /evaluate_rule`

Evaluate a user’s data against a rule.

- **URL**: `/evaluate_rule`
- **Method**: `POST`
- **Request Body**: JSON object with rule and user data.
  
  Example:
  ```json
  {
    "rule": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))",
    "data": {
      "age": 35,
      "department": "Sales",
      "salary": 60000,
      "experience": 3
    }
  }
  ```

- **Response**: Boolean (`True` or `False`) indicating if the user satisfies the rule.

---

## Testing

Test cases are included in the `tests/` folder. You can run the tests using the following command:

```bash
python -m unittest discover tests
```

---

## Example Usage

1. **Run the Backend**:
   ```bash
   python backend/api.py
   ```

2. **Use the CLI**:
   ```bash
   python frontend/ui.py
   ```

3. **Create and Evaluate Rules**: Use the CLI to input rules and user data in JSON format to test the rule engine.

Example interaction:

- **Rule**: `"((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))"`
- **User Data**: `{"age": 35, "department": "Sales", "salary": 60000, "experience": 3}`

---

## Contributing

Feel free to fork this project, submit issues, and contribute to improving the rule engine.

---

## Contact

For any questions or issues, contact:

- **Your Name**: preethi.bttr@gmail.com
- **GitHub**: [Preethiseeram](https://github.com/Preethiseeram)
