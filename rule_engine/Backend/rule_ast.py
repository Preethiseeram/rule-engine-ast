class Node:
    def _init_(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left  # Left child (Node)
        self.right = right  # Right child (Node)
        self.value = value  # Operand value (for comparisons)

def create_rule(rule_string):
    """Creates an AST from a rule string."""
    import ast
    # Use Python's ast module to parse the rule string
    # This is simplified for illustration; you'll need to handle complex rules manually
    return ast.parse(rule_string, mode='eval')

def evaluate_node(node, data):
    """Evaluate the AST node based on user data."""
    if node.type == 'operand':
        # Assuming the node value is a string like 'age > 30'
        key, operator, value = node.value.split()
        if operator == '>':
            return data[key] > int(value)
        elif operator == '<':
            return data[key] < int(value)
        elif operator == '=':
            return data[key] == value.strip("'")
    elif node.type == 'operator':
        if node.value == 'AND':
            return evaluate_node(node.left, data) and evaluate_node(node.right, data)
        elif node.value == 'OR':
            return evaluate_node(node.left, data) or evaluate_node(node.right, data)
    return False

def evaluate_rule(ast, data):
    """Evaluate the entire AST."""
    return evaluate_node(ast.body, data)

# Example of a Node for testing
example_rule = Node('operator', 
                    Node('operand', value='age > 30'),
                    Node('operand', value="department = 'Sales'"),
                value='AND')