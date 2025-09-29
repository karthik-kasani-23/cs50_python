

while True:
    try:
        first_number = int(input("first number : "))#input will convertt to string
        second_number =int(input("second number: "))
        add = first_number + second_number
        sum_string = f"the additon of {first_number + second_number}"
        print(sum_string)
        break   # exit loop when valid
    except ValueError:
         print("❌ Invalid input! Please enter a valid integer.")
    finally:
        print("this is finally block it will run always")
