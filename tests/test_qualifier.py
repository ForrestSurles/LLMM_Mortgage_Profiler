# Import 'Path' from 'pathlib' to create a workable filepath
from pathlib import Path
from app import find_qualifying_loans, save_qualifying_loans

#Import 'fileio' functions from 'loc_fun.utils' which include 'load_csv' and 'save_csv'
from loc_fun.utils.fileio import *

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
    csvpath = Path('.\data\output\output_data.csv')
    test_data = []
    temp_list = []
    for i in range(10):
        for j in range(10):
            temp_list.append(j)
            if j == 0:
                test_data.append(list(temp_list))
                temp_list.clear()
    save_csv(csvpath, test_data)
    assert csvpath.exists() == True

def test_calculate_monthly_debt_ratio():
    assert calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculate_loan_to_value_ratio(210000, 250000) == 0.84


def test_filters():
    bank_data = load_csv(Path('data\daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375
    loan_to_value_ratio = 0.84

    qualifying_loans = find_qualifying_loans(
        bank_data, current_credit_score, debt, income, loan, home_value)
    compare_against = []
    compare_against.append(['Bank of Big - Premier Option','300000','0.85','0.47','740','3.6'])
    compare_against.append(['Bank of Fintech - Premier Option','300000','0.9','0.47','740','3.15'])
    compare_against.append(['Prosper MBS - Premier Option','400000','0.85','0.42','750','3.45'])
    compare_against.append(['Bank of Big - Starter Plus','300000','0.85','0.39','700','4.35'])
    compare_against.append(['FHA Fredie Mac - Starter Plus','300000','0.85','0.45','550','4.35'])
    compare_against.append(['iBank - Starter Plus','300000','0.9','0.4','620','3.9'])
    assert qualifying_loans == compare_against