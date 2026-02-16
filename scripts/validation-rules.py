# Simple validation example
import json

def validate_benefit_status(file_path):
    with open(file_path) as f:
        data = json.load(f)
    for record in data:
        assert record['benefit_status'] in ['active', 'inactive']
    print("All records valid.")

validate_benefit_status('../examples/sample1.json')