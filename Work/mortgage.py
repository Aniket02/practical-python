# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        new_payment = payment + extra_payment
    else:
        new_payment = payment
    total_left = principal * (1+rate/12)
    if total_left < new_payment:
        new_payment = total_left
    principal = total_left - new_payment
    total_paid = total_paid + new_payment
    print(f"{month} {total_paid} {principal}")
    month += 1

print('Total paid', total_paid)
print('Months', month - 1)