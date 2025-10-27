# Test cases for the price calculation function
This repository contains test cases for the price calculation function defined in `main.py`. The test cases are stored in a CSV file named `w3_test_cases.csv`, and the tests are implemented using the `pytest` framework in `test.py`.
## Test Cases
The test cases are defined in the `w3_test_cases.csv` file with the following columns:
- `V`: The value input for the price calculation function.
- `S`: The status input for the price calculation function.
- `Expected`: The expected output from the price calculation function.
## Running the Tests
To run the tests, ensure you have `pytest` installed. You can install it using pip:
```bashpip install pytest```
Then, you can run the tests using the following command:
```bashpytest -v test.py```
This will execute all the test cases defined in `w3_test_cases.csv` and report any failures or errors.
## Adding New Test Cases
To add new test cases, simply edit the `w3_test_cases.csv` file and add new rows with the desired `V`, `S`, and `Expected` values. Save the file, and the new test cases will be automatically included the next time you run the tests.