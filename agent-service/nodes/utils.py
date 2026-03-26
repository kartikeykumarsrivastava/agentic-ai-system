# nodes/utils.py


import re

def extract_salary(query):
    match = re.search(r'\d+', query)
    return int(match.group()) * 100000 if match else 0
    if not match:
        return 0
