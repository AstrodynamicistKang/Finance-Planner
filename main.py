import locale
print("Finance Planner\n")

while True:

    y = eval(input("Enter initial working age and retirement age.\n"))

    print()

    z = eval(input("Enter maximum monthly expenses.\n"))

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
    cum = 0

    print("Age     Annual Salary   Monthly Salary   Monthly Expenses    Monthly Savings      Annual Savings     Cumulative Annual Savings")

    for n in range(0,y[1]+1-y[0]):
      new = new * cr
      if exp < z:
        exp = exp * cr
      else:
        exp = z 
      cum = (new)-(exp*cr*12) + cum
      print("{:3} {:15,.2f} {:15,.2f} {:17,.2f} {:18,.2f} {:20,.2f} {:25,.2f}".format(n+y[0], new, (new/12), (exp*cr) , ((new/12) - (exp*cr)), ((new)-(exp*cr*12)), cum))

    print()
    print(126*"-" + 2*"\n")

