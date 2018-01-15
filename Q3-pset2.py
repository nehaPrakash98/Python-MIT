'''
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)
Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!
The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

In short:
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
'''

def cal(bal, minPay, annualInterestRate):
    for i in range(0, 12):
        ub = bal - minPay
        interest = annualInterestRate/12
        bal = ub+(interest*ub)    
    return bal

bal = balance
MonthlyInterestRate = annualInterestRate/12
low = balance/12
high = balance*((1+MonthlyInterestRate)**12)/12
mid = (high + low)/2.0
while abs(bal)>= 0.01:
    bal = balance
    bal = cal(bal, mid, annualInterestRate)
    if bal>0:
        low = mid
    else:
        high = mid
    mid = (low+high)/2
print(round(mid, 2))
