print("welcome to the tip calculator")
bill=input("what is the total bill? ")
bill_as_float=float(bill)
tip=input("what percentage of tips you want to give? 10 12 15 20 percentage")

tip_as_int=int(tip)

total_bill = (bill_as_float * tip_as_int)/100 + bill_as_float
people = input("How many people to split the bill?")
total_people = int(people)
split = total_bill/total_people
final_amount = round(split, 2)
print("Each person should pay: "+str(final_amount))