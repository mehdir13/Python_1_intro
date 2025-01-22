### 1.0 Hello World!
# Printa ut "Hello World" till konsolen.

print("Hello World")


### 1.1 Ålderskontroll
# Skriv en funktion som tar in användarens ålder och sedan skriver ut om de är minderåriga (under 18 år), vuxna (mellan 18 och 65) eller pensionärer (över 65).

def age_function():
    age = int(input("Please enter your age: "))
    
    if age < 30:
        print("Why are you such a baby ?!")
    elif 30 <= age <= 65:
        print("You are an adult.")
    else:
        print("You are obsolete bro!")

# Call the function to test:
age_function()


### 1.2 Jämnt eller udda
# Skriv en funktion som tar in en enskild siffra och skriver ut om den är udda eller jämn.

def OddEvenNumber_function():
    number = int(input("Please enter your favourite number: "))
    
    if number %2 == 0:
        print(f"{number} is even like De Sitter Space.")
    else:
        print(f"{number} is odd like a bearded woman in circus!")

# Call the function to test:
OddEvenNumber_function()


### 1.3 - Intervall
# Skapa funktionen `in_range(lower, upper)` som avgör ifall ett tal är inom det angivna intervallet. Om talet finns i ändpunkterna räknas det som inom intervallet.

def INrange_function():
    lower = int(input("Please enter the lower endpoint of the range: "))
    upper = int(input("Please enter the upper endpoint of the range: "))
    number = int(input("Please enter a number to check: "))
    
    if lower <= number <= upper:
        print(f"HURRAY !!!! {number} is within the range [{lower}, {upper}].")
    else:
        print(f"Shit of Stick !!! {number} is outside the range [{lower}, {upper}].")

# Call the function to test:
INrange_function()
