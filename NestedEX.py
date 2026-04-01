age = int (input("Enter your age:"))
if age >=18:
    registered_voter= input("Are you a registered coter? (True/False):")
    registered_voter = registered_voter.lower()
    if registered_voter == "true":
        print("you are eligibel to vote.")
    else:
        print("you need to register to vote.")

else:
    print("You are not eligible to vote")        
