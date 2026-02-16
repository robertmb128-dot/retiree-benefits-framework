# Synthetic data generator example
import json

sample_data = [
    {"id": 1, "name": "John Doe", "benefit_status": "active"},
    {"id": 2, "name": "Jane Smith", "benefit_status": "inactive"}
]

with open('examples/sample1.json', 'w') as f:
    json.dump(sample_data, f, indent=2)
print("Synthetic data generated.")