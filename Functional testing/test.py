import csv
import pytest
from main import calculate_price

def load_test_cases(csv_file="w3_test_cases.csv"):
    cases = []
    with open(csv_file, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            V = int(row["V"])
            S = int(row["S"])
            expected_str = row["Expected"].strip()
            expected = int(expected_str) if expected_str.isdigit() else None
            cases.append((V, S, expected))
    return cases

@pytest.mark.parametrize("V,S,expected", load_test_cases())
def test_calculate_price(V, S, expected):
    result = calculate_price(V, S)
    print(f"Test case: V={V}, S={S} | result={result}, expected={expected}")
    assert result == expected, f"Failed for V={V}, S={S}: got {result}, expected {expected}"
