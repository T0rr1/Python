# Import classes needed for the project
import math
import argparse
import sys

parser = argparse.ArgumentParser(description='A credit Calculator')
parser.add_argument('--type', choices=['diff', 'annuity'], required=True, type=str,
                    help='The type of payment either "diff" or "annuity"')
parser.add_argument('--payment', type=float, help='Monthly payment')
parser.add_argument('--principal', type=int, help='The credit principal')
parser.add_argument('--periods', type=int,
                    help='The number of months and/or years needed to repay the credit')
parser.add_argument('--interest', type=float, help='input the interest rate without the percentage sign')
args = parser.parse_args()
type = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest


class CreditCalculator:
    def __init__(self):
        self.principal = principal
        self.period = periods
        self.payment = payment
        self.interest = interest
        self.type = type

    # Convert months into years and remaining months
    def convert_months(self, months):
        years = months / 12
        if months % 12 == 0:
            print('')
            print(f'You need {int(years)} years to repay this credit!')
        else:
            year = [int(months / 12), months % 12]
            print('')
            print(f'You need {year[0]} years and {year[1]} months to repay this credit!')

    # Main method that calculates the credit based on the principal,interest and period

    def calculate_credit(self):
        if self.type == 'diff':
            if self.principal > 0 and self.interest > 0 and self.period > 0:
                nominal = (self.interest / 12) / 100
                num_months = range(1, self.period + 1)
                total_paid = 0
                for i in range(len(num_months)):
                    payout = math.ceil((self.principal / (len(num_months))) + nominal * (
                            self.principal - (self.principal * (num_months[i] - 1) / (len(num_months)))))
                    total_paid += payout
                    print(f'Month {num_months[i]}: paid out {payout}')
                print()
                print(f'Overpayment = {total_paid - self.principal}')
            else:
                print('Incorrect parameters.')
        elif self.type == 'annuity':
            if self.principal is not None and self.period is not None and self.interest is not None:
                nominal = (self.interest / 12) / 100
                annuity = int(math.ceil(self.principal * (
                        (nominal * ((1 + nominal) ** self.period)) / (
                        ((1 + nominal) ** self.period) - 1))))
                print('')
                print(f'Your annuity payment = {annuity}!')
                print(f'Overpayment = {(annuity * self.period) - self.principal}')
            elif self.principal is not None and self.payment is not None and self.interest is not None:
                nominal = (self.interest / 12) / 100
                count_periods = math.ceil(
                    math.log((self.payment / (self.payment - nominal * self.principal)), 1.0 + nominal))
                self.convert_months(count_periods)
                print(f"Overpayment = {int((count_periods * self.payment) - self.principal)}")
            elif self.payment is not None and self.period is not None and self.interest is not None:
                nominal = (self.interest / 12) / 100
                credit_principal = int(self.payment / (
                        (nominal * ((1 + nominal) ** self.period)) / (
                        ((1 + nominal) ** self.period) - 1)))
                print(f'Your credit principal = {credit_principal}!')
                print(f"Overpayment = {int((self.period * self.payment) - credit_principal)}")


if len(sys.argv) != 4:
    new = CreditCalculator()
    new.calculate_credit()
else:
    print('Incorrect parameters.')
