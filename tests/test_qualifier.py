"""
==========================================================================================
VITAL NOTE: to everyone else, and me in 6 months.
==========================================================================================
WHERE YOU RUN 'pytest' FROM WILL MAKE OR BREAK THESE TESTS
SO BE SURE TO HAVE YOUR CURRENT WORKING DIRECTORY BE THE 'tests' SUB-FOLDER
THAT'S LOCATED IN THE 'challenge' PARENT FOLDER.
OTHERWISE, YOU'RE GONNA HAVE A BAD TIME.
==========================================================================================
"""

# Import from the 'pathlib' library, and the main 'app.py'
from pathlib import Path
from app import find_qualifying_loans, save_qualifying_loans

#Import 'fileio' -- 'load_csv' and 'save_csv'
from loc_fun.utils.fileio import *

# Import Calculators -- calculate_monthly_debt_ratio & calculate_loan_to_value_ratio
from loc_fun.utils.calculators import *

# Import Filters
from loc_fun.filters.credit_score import filter_credit_score
from loc_fun.filters.debt_to_income import filter_debt_to_income
from loc_fun.filters.loan_to_value import filter_loan_to_value
from loc_fun.filters.max_loan_size import filter_max_loan_size

# test to make sure a csv with the output is saved out
def test_save_csv():
    # yet we shall still remember to cherish in our hearts the original filename of 'plz_data.csv'
    csvpath = Path('../data/output/test_save.csv')     # identify the target directory for saving
    
    # ============================================================
    # generate test data for saving out to a csv
    test_data = []
    temp_list = []
    for i in range(10):
        for word in ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']:
            temp_list.append(word)
            if word == 'Interest Rate':
                test_data.append(list(temp_list))
                temp_list.clear()
    # ============================================================
    save_csv(csvpath, test_data)        # save the test data to 'csvpath'
    assert csvpath.exists() == True     # check the file was generated w/ '.exists()'

# test function - calculate_monthly_debt_ratio
def test_calculate_monthly_debt_ratio():
    assert calculate_monthly_debt_ratio(1500, 4000) == 0.375

# test function - calculate_loan_to_value_ratio
def test_calculate_loan_to_value_ratio():
    assert calculate_loan_to_value_ratio(210000, 250000) == 0.84

# test to make sure all of the filters work together
def test_filter_scenario():
    # load the list of bank loans
    bank_data = load_csv(Path('../data/daily_rate_sheet.csv'))
    
    # ========================================
    # ======= DATA WITH A KNOWN OUTPUT =======
    # ========================================
    
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375
    loan_to_value_ratio = 0.84
    
    # run the 'find qualifying loans' function and set the filtered output to the 'qualifying_loans' list
    qualifying_loans = find_qualifying_loans(
        bank_data, current_credit_score, debt, income, loan, home_value)
    
    # ========================================
    # ==== GENERATE LIST OF KNOWN OUTPUT =====
    # ========================================

    compare_against = []
    compare_against.append(['Bank of Big - Premier Option','300000','0.85','0.47','740','3.6'])
    compare_against.append(['Bank of Fintech - Premier Option','300000','0.9','0.47','740','3.15'])
    compare_against.append(['Prosper MBS - Premier Option','400000','0.85','0.42','750','3.45'])
    compare_against.append(['Bank of Big - Starter Plus','300000','0.85','0.39','700','4.35'])        
    compare_against.append(['FHA Fredie Mac - Starter Plus','300000','0.85','0.45','550','4.35'])
    compare_against.append(['iBank - Starter Plus','300000','0.9','0.4','620','3.9'])

    # compare the test input to the known output
    assert qualifying_loans == compare_against

# ========================================================
# ~~~~~~~~~~~~~~~~~~ BONUS - EXTENSION ~~~~~~~~~~~~~~~~~~~
# ========================================================

# test each of the filters in succession simulating the output of each stage
def test_all_filters():
    # load the list of bank loans
    bank_data = load_csv(Path('../data/daily_rate_sheet.csv'))
    
    # ========================================
    # ======= DATA WITH A KNOWN OUTPUT =======
    # ========================================

    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375
    loan_to_value_ratio = 0.84

    # ========================================
    # ==== GENERATE LIST OF KNOWN OUTPUT =====
    # ========================================

    compare_against = []
    compare_against.append(['Bank of Big - Premier Option','300000','0.85','0.47','740','3.6'])
    compare_against.append(['West Central Credit Union - Premier Option','400000','0.9','0.35','760','2.7'])
    compare_against.append(['FHA Fredie Mac - Premier Option','600000','0.9','0.43','790','3.6'])
    compare_against.append(['FHA Fannie Mae - Premier Option','500000','0.9','0.47','780','3.6'])
    compare_against.append(['General MBS Partners - Premier Option','400000','0.95','0.35','790','3.0'])
    compare_against.append(['Bank of Fintech - Premier Option','300000','0.9','0.47','740','3.15'])
    compare_against.append(['iBank - Premier Option','500000','0.85','0.46','780','3.15'])
    compare_against.append(['Goldman MBS - Premier Option','500000','0.8','0.4','770','3.6'])
    compare_against.append(['Citi MBS - Premier Option','400000','0.9','0.47','780','3.6'])
    compare_against.append(['Prosper MBS - Premier Option','400000','0.85','0.42','750','3.45'])
    compare_against.append(['Developers Credit Union - Premier Option','300000','0.85','0.47','770','3.45'])
    compare_against.append(['Bank of Stodge & Stiff - Premier Option','500000','0.9','0.41','790','3.15'])
    compare_against.append(['Bank of Big - Starter Plus','300000','0.85','0.39','700','4.35'])
    compare_against.append(['West Central Credit Union - Starter Plus','300000','0.8','0.44','650','3.9'])
    compare_against.append(['FHA Fredie Mac - Starter Plus','300000','0.85','0.45','550','4.35'])
    compare_against.append(['General MBS Partners - Starter Plus','300000','0.85','0.36','670','4.05'])
    compare_against.append(['iBank - Starter Plus','300000','0.9','0.4','620','3.9'])
    compare_against.append(['Citi MBS - Starter Plus','300000','0.8','0.39','740','4.05'])

    # test that filter_max_loan_size works as expected
    qualifying_loans = filter_max_loan_size(loan,bank_data)
    assert qualifying_loans == compare_against

    # modify generated list of known output to match/check filter_credit_score works as expected
    compare_against.remove(['West Central Credit Union - Premier Option','400000','0.9','0.35','760','2.7'])
    compare_against.remove(['Goldman MBS - Premier Option','500000','0.8','0.4','770','3.6'])
    compare_against.remove(['Developers Credit Union - Premier Option','300000','0.85','0.47','770','3.45'])
    compare_against.remove(['FHA Fannie Mae - Premier Option','500000','0.9','0.47','780','3.6'])
    compare_against.remove(['iBank - Premier Option','500000','0.85','0.46','780','3.15'])
    compare_against.remove(['Citi MBS - Premier Option','400000','0.9','0.47','780','3.6'])
    compare_against.remove(['FHA Fredie Mac - Premier Option','600000','0.9','0.43','790','3.6'])
    compare_against.remove(['General MBS Partners - Premier Option','400000','0.95','0.35','790','3.0'])
    compare_against.remove(['Bank of Stodge & Stiff - Premier Option','500000','0.9','0.41','790','3.15'])

    # test that filter_credit_score works as expected
    qualifying_loans = filter_credit_score(current_credit_score, qualifying_loans)
    assert qualifying_loans == compare_against

    # modify generated list of known output to match/check filter_debt_to_income works as expected
    compare_against.remove(['General MBS Partners - Starter Plus','300000','0.85','0.36','670','4.05'])

    # test that filter_debt_to_income works as expected
    qualifying_loans = filter_debt_to_income(monthly_debt_ratio, qualifying_loans)
    assert qualifying_loans == compare_against

    # modify generated list of known output to match/check filter_loan_to_value works as expected
    compare_against.remove(['West Central Credit Union - Starter Plus','300000','0.8','0.44','650','3.9'])
    compare_against.remove(['Citi MBS - Starter Plus','300000','0.8','0.39','740','4.05'])

    # test that filter_loan_to_value works as expected
    qualifying_loans = filter_loan_to_value(loan_to_value_ratio, qualifying_loans)
    assert qualifying_loans == compare_against