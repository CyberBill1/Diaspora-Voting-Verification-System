# Python Script for Diaspora Voting System Verification
# By Ifeanyi Barth
# The prospective voter is required to enter their full name as it appears in their passport
# They are also required to enter their passport number.
# The Program first matches the provided name and passport serial number to the data available in the database
# If the provided data is correct then the program goes ahead to check the age of the passport carrier as it is contained in its details.
# If the age is up to 18 years, they are allowed to vote else they are denied,

Name = input("Please enter your full name:")
passport_number = int (input("Please enter your passport serial number:"))
print("Reading from our Passport Database...")
import time
time.sleep(3) # Sleep for 3 seconds

 #Verifying eligibility from various Passport Numbers
if passport_number < 1000 : #Because our passport serial numbers starts from 1000
    print("You are not eligible to vote as you are not found in our Database")
elif passport_number > 10000 : #Because our passport serial numbers ends with 10000
    print("Sorry,you are too old to vote")
elif passport_number < 3000: #People less than 18 are giving SN of 1000-2999
    print("Sorry,you are too young to vote as you are less than 18")
else:
    print("You are eligible to vote \n"+
          "Proceed for Bimodal Accreditation")
    print(Name,",YOUR VOTE IS YOUR RIGHT,DON'T SELL IT!!!")
