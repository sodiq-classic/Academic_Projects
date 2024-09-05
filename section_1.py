"""
ASSIGNMENT_6: SECTION_1
-----------------------------------------------
Writing a program for student enrolment platform showing desicion structures, 
loops and functions in the code.

@author: Sodiq
@date: Tue Nov 28, 2023
"""

#check if user has an account
has_account = input("Do you have an account? Answer with True or False: ")

# This line prints the sign_up message
if has_account == "True":
    print("Login")

# This line prompts user to login
    login = input("Enter 'Login':")
else:
    print("Sign up")

#This line prompts user to sign up
    sign_up = input("Enter 'sign up': ")
    
#PART A, defining functions
def create_candidate():
    print("Create candidate")
    print("Fill in your contact information")

    contact_information = []
    fields = ["full name", 
              "email", 
              "phone number", 
              "home address", 
              "date of birth"
              ]

    for field in fields:
        value = input(f"Enter your {field}: ")
        contact_information.append(value)

    print("Your contact information is as follows:", contact_information)
    print("Your candidate ID is: 12AD")
    print("Proceed to upload required documents by choosing option 2.")


def upload_documents(candidate_id):
    print("Proceed to upload required documents")
    print("Each document should not be more than 25kb")

    documents = ["international passport", 
                 "high school final grades", 
                 "school testimonial", 
                 "bank statement"
                 ]

    for doc in documents:
        upload = input(f"Upload your {doc}: ")

    print("You have been approved! Proceed to pay initial tuition fee by" 
          " choosing option 3.")


def make_tuition_payment(candidate_id):
    print("Make initial tuition payment")

    # Tuition fee summary for year one

    # Prompt user to pay tuition fee
    initial_tuition_payment = input("Make initial tuition payment: ")

    # Display you have been enrolled
    print("Congratulations, you have been enrolled")
    print("Check your email regularly as your acceptance letter will be" 
          " sent in due time")

#PART B, loop structure
while True:
    menu_option = input("Enter menu option (1, 2, 3,): ")

    if menu_option == '1':
        create_candidate()
    
    elif menu_option == '2':
        print("Enter candidate ID")
        candidate_id = input("Enter candidate ID: ")
        if candidate_id == "12AD":
            upload_documents(candidate_id)
        else:
            print("Candidate not found")
            print("Go to choice 1 to create a candidate")
    
    elif menu_option == '3':
        print("Enter candidate ID")
        candidate_id = input("Enter candidate ID: ")
        if candidate_id == "12AD":
            make_tuition_payment(candidate_id)
            break
        else:
            print("Candidate not found")
    
    else:
        print("You chose a wrong option.")
