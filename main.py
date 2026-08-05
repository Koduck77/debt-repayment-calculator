def get_number(message, allow_zero=False):
    while True:
        try:
            number = float(input(message))

            if number < 0:
                print("Please enter a positive number.")
            elif number == 0 and allow_zero == False:
                print("Please enter a number greater than zero.")
            else:
                return number
        except ValueError:
            print("Please enter a number.")


def calculate_repayment(balance, yearly_interest, monthly_payment):
    monthly_interest_rate = yearly_interest / 100 / 12

    if monthly_payment <= balance * monthly_interest_rate:
        return None

    months = 0
    total_interest = 0
    total_paid = 0

    while balance > 0:
        interest = balance * monthly_interest_rate
        balance = balance + interest
        total_interest = total_interest + interest

        if monthly_payment > balance:
            payment = balance
        else:
            payment = monthly_payment

        balance = balance - payment
        total_paid = total_paid + payment
        months = months + 1

    return months, total_interest, total_paid


def main():
    print("Debt Repayment Calculator")

    balance = get_number("Current debt balance: $")
    interest = get_number("Yearly interest rate: ", True)
    payment = get_number("Monthly payment: $")

    result = calculate_repayment(balance, interest, payment)

    if result == None:
        print("Your monthly payment is too low to reduce the debt.")
    else:
        months, total_interest, total_paid = result
        years = months // 12
        extra_months = months % 12

        print("\nRepayment result")
        print("Time:", years, "year(s) and", extra_months, "month(s)")
        print(f"Total interest: ${total_interest:.2f}")
        print(f"Total paid: ${total_paid:.2f}")


if __name__ == "__main__":
    main()
