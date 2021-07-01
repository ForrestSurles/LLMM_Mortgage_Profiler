# Import pathlib
from pathlib import Path
from app import find_qualifying_loans, save_qualifying_loans

#Import fileio
from loc_fun.utils.fileio import *
#from loc_fun.utils.fileio import load_csv, save_csv

# Import Calculators
from loc_fun.utils.calculators import *
#from loc_fun.utils.calculators import calculate_monthly_debt_ratio, calculate_loan_to_value_ratio

# Import Filters
#from loc_fun.filters import *

from loc_fun.filters.credit_score import filter_credit_score
from loc_fun.filters.debt_to_income import filter_debt_to_income
from loc_fun.filters.loan_to_value import filter_loan_to_value
from loc_fun.filters.max_loan_size import filter_max_loan_size


def test_save_csv():
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    csvpath = Path('..\data\output\output_data.csv')
    test_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    save_csv(csvpath, test_data)
    assert csvpath.exists() == True

def test_calculate_monthly_debt_ratio():
    assert calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculate_loan_to_value_ratio(210000, 250000) == 0.84

'''
def test_filters():
    bank_data = load_csv(Path('data\daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
'''