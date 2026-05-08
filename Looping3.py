import time


# Example 1: while-else loop for checking password
# loop 3 attempts. If password correct, break
def check_password():
    for i in range(3):
        correct = "1234"
        attempts = 3
        timeLeft = 10
        success = False

        while attempts > 0:
            pw = input("Enter password: ")
            if pw == correct:
                print("Access granted")
                success = True
                break     # it breaks the while loop if pw == correct
            else:
                print("wrong password. Please try again.")
                attempts -= 1
        else:
            # this else clause will be triggered if the loop managed to run till completion
            if not i == 2:
                print("Attempts over. Please try again in 10 seconds.")
                while timeLeft > 0:
                    time.sleep(1)
                    timeLeft -= 1
                print("You now have 3 new attempts.")

        if success:
            break   # it breaks the for loop if success == True

    else:
        print("device disabled permanently.")



check_password()