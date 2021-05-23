# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    
    month = month + 1

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra
        total_paid = total_paid + payment + extra
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(month, total_paid, principal)

print('Total paid', total_paid) 
print('Months', month)
