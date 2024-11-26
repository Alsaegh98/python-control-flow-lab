# Example 1

def check_letter():

    letter = input("Enter a letter (a-z or A-Z): ")

    if len(letter) == letter.isalpha():

        letter = letter.lower()

        vowels = 'aeiou'

        if letter in vowels:
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")


check_letter()

# Example 2

while True:
    num = input('Enter a number:')
    print(f'The user entered {num}')

    if str(num) == "quit":
        break
    elif int(num) < 0 :
        print('please enter a non negative number')
    elif int(num) < 18:
        print('you are not allowed to vote ')
    else:
        print('your vote have been entered in the system')

# Example 3

def calculate_dog_years():

    dog_age = int(input("Input a dog's age: "))

    if dog_age <= 2:
        dog_years = dog_age * 10
    elif dog_age > 2:
        dog_years = dog_age * 7 + 6

    print(f"The dog's age in dog years is {dog_years}.")

calculate_dog_years()

# Example 4

def weather_advice():

    is_cold = input("Is it cold? (yes/no): ").lower()

    is_raining = input("Is it raining? (yes/no): ").lower()

    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == "no" and is_raining == "no":
        print("Wear light clothing.")
 

weather_advice()

# Example 5

def determine_season():
    while True:

        month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
        
        day = input("Enter the day of the month: ").strip()
        
        if month not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            print("Invalid month. Please enter a valid month (Jan - Dec).")
            continue
        
        if not day.isdigit() or not (1 <= int(day) <= 31):
            print("Invalid day. Please enter a valid day of the month (1 - 31).")
            continue
        
        day = int(day)
        season = ''

        if (month == 'Dec' and day >= 21) or month in ['Jan', 'Feb'] or (month == 'Mar' and day <= 19):
            season = 'Winter'
        elif (month == 'Mar' and day >= 20) or month in ['Apr', 'May'] or (month == 'Jun' and day <= 20):
            season = 'Spring'
        elif (month == 'Jun' and day >= 21) or month in ['Jul', 'Aug'] or (month == 'Sep' and day <= 21):
            season = 'Summer'
        elif (month == 'Sep' and day >= 22) or month in ['Oct', 'Nov'] or (month == 'Dec' and day <= 20):
            season = 'Fall'

        print(f"{month} {day} is in {season}.")
        break

determine_season()
