currency = input("Pick a cuurency: USD = 1 OR ZAR = 2: ")

conv = int(currency)



bill = input("What is the amount of the bill: ")
tip = input(f"what percentage do you want the tip to be: ")
people = input("How many people are you sharing the tip amongst: ")


if conv == 1:
    tip_total = int(bill)*int(tip)/100
    answer = tip_total
    final_ans = tip_total/int(people)
    print(int(final_ans), "Dollars per person")
elif conv == 2:
    tip_total = int(bill)*int(tip)/100
    answer = tip_total
    final_ans = tip_total/int(people)
    print(int(final_ans), "Rand per person") 
else:
    print("There was a problem with the information please try again")