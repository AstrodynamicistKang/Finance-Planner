print("Annualized Return Rate Calculator for a Sum of Annuity with Sales Charge\n")

while True:

    #x = eval(input("Enter annualized return rate, r; number of years, N and sales charge, s.\n\n"))

    x = 0.1, 10, 0.0175

    print("\n" + str(x))

    k = (((1+((x[0])/12))**(x[1]*12))-1)/((x[0])/12*(1-x[2]))

    print("\n")
    print("{0:.5f}".format(k))

    #T = eval(input("Enter a test value for the expected annualized rate of return over the period defined.\n\n"))

    T = 0.1030769

    LHS = 1+(k*(T/12))

    RHS = (1+(T/12))**(x[1]*12)

    print("{0:.5f}\n{1:.5f}\n{2:.5f}\n".format(LHS, RHS, LHS-RHS))
    
    ask = input("Would you like to continue? Y/N")
    
    if (ask.lower() == "y") or (ask.lower() == "Y"):
        continue
    
    else:
        print()
        break

print("Income Growth Simulator\n")

while True:

    y = eval(input("Enter initial working age and retirement age.\n"))

    print()

    z = eval(input("Enter expenses increment ratio (in % percent) and maximum monthly expenses.\n"))

    print()

    x = input("Select annual (a) or monthly (m).\n")

    print()

    if (x.lower() == "annual") or (x.lower() == "a"):
        inputs = eval(input("Enter annual starting salary, increment ratio (in % percent), and initial expenses.\n"))
        print()

    elif (x.lower() == "monthly") or (x.lower() == "m"):
        inputs = eval(input("Enter monthly starting salary, increment ratio (in % percent), and initial expenses.\n"))
        print()
        inputs = (inputs[0]*12, inputs[1], inputs[2]*12)

    new = inputs[0]
    cr = (inputs[1])/100 + 1
    exp = (inputs[2])/12
    cre = z[0]/100 + 1
    cum = 0

    print("Age     Annual Salary   Monthly Salary   Monthly Expenses    Monthly Savings      Annual Savings     Cumulative Annual Savings")

    for n in range(0,y[1]+1-y[0]):
      new = new * cr
      if exp < z[1]:
        exp = exp * cre
      else:
        exp = z[1] 
      cum = (new)-(exp*cre*12) + cum
      print("{:3} {:15,.2f} {:15,.2f} {:17,.2f} {:18,.2f} {:20,.2f} {:25,.2f}".format(n+y[0], new, (new/12), (exp*cre) , ((new/12) - (exp*cre)), ((new)-(exp*cre*12)), cum))

    print()
    print(126*"-" + 2*"\n")
