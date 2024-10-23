#!/usr/bin/env python
# coding: utf-8

# #                            Rule Engine With AST

# # Step-1: Define the Node class for AST

# In[2]:


class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left  # left child node
        self.right = right  # right child node
        self.value = value  # value for operand nodes (conditions)


# # Step-2: Function to create AST from rule string

# In[3]:


def create_rule(rule_string):
    # Simulated: Parsing the rule string manually for this example
    if "AND" in rule_string or "OR" in rule_string:
        operator = "AND" if "AND" in rule_string else "OR"
        left_part, right_part = rule_string.split(f" {operator} ")
        return Node("operator", create_rule(left_part), create_rule(right_part), operator)
    else:
        # Operand: Handle simple conditions like "age > 30" or "department = 'Sales'"
        return Node("operand", value=rule_string.strip())


# # Step-3: Combine multiple ASTs into one

# In[4]:


def combine_rules(rules):
    if not rules:
        return None
    combined_rule = create_rule(rules[0])
    for rule in rules[1:]:
        combined_rule = Node("operator", combined_rule, create_rule(rule), "AND")
    return combined_rule


# # Step-4: Evaluate the rule against the user's data

# In[5]:


def evaluate_rule(node, data):
    if node.type == "operand":
        condition = node.value.replace(" ", "")
        
        # Check and handle various comparison operators
        if ">" in condition:
            key, value = condition.split(">")
            return data[key] > int(value)
        elif "<" in condition:
            key, value = condition.split("<")
            return data[key] < int(value)
        elif ">=" in condition:
            key, value = condition.split(">=")
            return data[key] >= int(value)
        elif "<=" in condition:
            key, value = condition.split("<=")
            return data[key] <= int(value)
        elif "=" in condition:
            key, value = condition.split("=")
            return data[key] == value.strip("'")
        else:
            raise ValueError("Invalid condition format")
    
    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == "OR":
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)


# # Step-5: Test the solution with sample data and rules

# In[6]:


if __name__ == "__main__":
    # Example rules
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "age < 25 AND department = 'Marketing'"
    
    # Create AST for individual rules
    ast_rule1 = create_rule(rule1)
    ast_rule2 = create_rule(rule2)
    
    # Combine rules into a single AST
    combined_ast = combine_rules([rule1, rule2])
    
    # Test evaluation with sample data
    data1 = {"age": 35, "department": "Sales"}
    data2 = {"age": 22, "department": "Marketing"}
    
    print("Data1 matches rule1:", evaluate_rule(ast_rule1, data1))  # Expected: True
    print("Data2 matches rule2:", evaluate_rule(ast_rule2, data2))  # Expected: True
    print("Combined rule with Data1:", evaluate_rule(combined_ast, data1))  # Combined evaluation

