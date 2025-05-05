
age= input("what is your age?")
age_as_int= int(age)
year_remaining= 100-age_as_int
days_remaining =year_remaining*365
weeks_remaining = year_remaining*52
months_remaining = year_remaining*12
message = f"your remainig days {days_remaining},your remaining weeks {weeks_remaining},your months remaining {months_remaining}"
print(message)