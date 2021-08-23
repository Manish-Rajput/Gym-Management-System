

import shutil
import sys
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date


columns = shutil.get_terminal_size().columns
    

Members = {}
Regimen = {'Regimen 1':{'Mon': 'Chest', 'Tue': 'Biceps','Wed': 'Rest','Thu': 'Back',
'Fri': 'Triceps', 'Sat': 'Rest', 'Sun': 'Rest'}, 'Regimen 2': {'Mon': 'Chest', 'Tue': 'Biceps',
'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Legs', 'Sun': 'Rest'}, 'Regimen 3':
    {'Mon': 'Chest', 'Tue': 'Biceps','Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps',
     'Sat': 'Legs','Sun':'Cardio'}, 'Regimen 4': {'Mon': 'Chest', 'Tue': 'Biceps','Wed': 'Cardio',
                'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Cardio', 'Sun':'Cardio'}}



def add_member(name, Age, Gender, phoneNo, email, BMI, duration):
    today_date = date.today()
    next_date = date.today() + relativedelta(months=+int(duration))
    Members[phoneNo] = {}
    Members[phoneNo]['name'] = name
    Members[phoneNo]['Age'] = Age
    Members[phoneNo]['Gender'] = Gender
    Members[phoneNo]['email'] = email
    Members[phoneNo]['BMI'] = BMI
    Members[phoneNo]['joinDate'] = today_date.strftime("%d/%m/%Y")
    Members[phoneNo]['Subscription End date'] = next_date.strftime("%d/%m/%Y")

def update_member(phone_check3):
    action = input("\nPress 1 to extend the membership\n\nPress 2 to revoke the membership - ")
    if action == '1':
        end = Members[phone_check3]['Subscription End date']
        print(f"\ncurrent subscription of member ends ---> {end}")
        extention = input("\nEnter the extention in 1,3,6 or 12 months - ")
        temp_date = datetime.strptime(end,"%d/%m/%Y")
        temp_next = temp_date + relativedelta(months=int(extention))
        next_final = temp_next.strftime("%d/%m/%Y")
        Members[phone_check3]['Subscription End date'] = next_final
        print("\n\t\t\tMembership has been extended successfully")
        print(f"\n\t\t\tcurrent subscription of member ends ---> {Members[phone_check3]['Subscription End date']}")

    elif action == '2':
        del Members[phone_check3]
        print("\n\t\t\tMembership revoked succesfully....")

    else:
        print("\n\t\t\tInvalid input")
        menu()


def create_regimen(reg_name):
    Regimen[reg_name] = {}
    Regimen[reg_name]['Mon'] = input("Enter workout for Monday - ")
    Regimen[reg_name]['Tue'] = input("Enter workout for Tuesday - ")
    Regimen[reg_name]['Wed'] = input("Enter workout for Wednesday - ")
    Regimen[reg_name]['Thu'] = input("Enter workout for Thursday - ")
    Regimen[reg_name]['Fri'] = input("Enter workout for Friday - ")
    Regimen[reg_name]['Sat'] = input("Enter workout for Saturday - ")
    Regimen[reg_name]['Sun'] = input("Enter workout for Sunday - ")

def update_regimen(reg_name2):
    Regimen[reg_name2] = {}
    Regimen[reg_name2]['Mon'] = input("Enter workout for Monday - ")
    Regimen[reg_name2]['Tue'] = input("Enter workout for Tuesday - ")
    Regimen[reg_name2]['Wed'] = input("Enter workout for Wednesday - ")
    Regimen[reg_name2]['Thu'] = input("Enter workout for Thursday - ")
    Regimen[reg_name2]['Fri'] = input("Enter workout for Friday - ")
    Regimen[reg_name2]['Sat'] = input("Enter workout for Saturday - ")
    Regimen[reg_name2]['Sun'] = input("Enter workout for Sunday - ")

def regimen_selection(phoneNo, BMI):
    if BMI < 18.5:
        Members[phoneNo]['Regimen Assigned'] = 'Regimen 1'
        print('\n\t\t\tRegimen 1 has been assigned to the member')

    elif BMI > 18.5 and BMI <25:
        Members[phoneNo]['Regimen Assigned'] = 'Regimen 2'
        print('\n\t\t\tRegimen 2 has been assigned to the member')

    elif BMI > 25 and BMI <30:
        Members[phoneNo]['Regimen Assigned'] = 'Regimen 3'
        print('\n\t\t\tRegimen 3 has been assigned to the member')

    else:
        Members[phoneNo]['Regimen Assigned'] = 'Regimen 4'
        print('\n\t\t\tRegimen 4 has been assigned to the member')

def menu():
    print("\n")
    print("   *****Edyoda Gym Management System*****")
    print("Hello Admin, please select a choice from the menu\n\n")
    print("1. Create Member")
    print("2. View Member")
    print("3. Delete Member")
    print("4. Update Member")
    print("5. Create Regimen")
    print("6. View Regimen")
    print("7. Delete Regimen")
    print("8. Update Regimen")
    print("9. To go back to login screen")
    while True:
        i = input("Enter your choice:  ")
        if i == '1':
            name = input("Enter full name - ")
            Age = input("Enter age - ")
            Gender = input("Enter Gender M for male and F for female - ")
            phoneNo = input("Enter phone no. - ")
            email = input("Enter email id - ")
            duration = input("Enter Membership duration in 1,3,6,12 months - ")
            BMI = float(input("Enter BMI - "))
            add_member(name, Age, Gender, phoneNo, email, BMI, duration)
            regimen_selection(phoneNo, BMI)
            print("\n\t\t\tMember created successfully")

        elif i == '2':
            phone_check = input("Enter the phone number of Member - ")
            if phone_check in Members:
                x = phone_check
                print("\n\n{:<15} {:<5} {:<8} {:<12} {:<25} {:<5} {:<15} {:<10}".format('Name', 'Age', 'Gender', 'Mobile No', 'Email Id', 'BMI', 'Join date', 'Subs End date'))
                print("{:<15} {:<5} {:<8} {:<8} {:<27} {:<5} {:<15} {:<10}".format(Members[x]['name'], Members[x]['Age'], Members[x]['Gender'], x, Members[x]['email'], Members[x]['BMI'], Members[x]['joinDate'], Members[x]['Subscription End date']))
            else:
                print("\n\t\t\tMember not found")


        elif i == '3':
            phone_check2 = input("Enter the phone number of Member - ")
            if phone_check2 in Members:
                del Members[phone_check2]
                print("\n\t\t\tMember deleted successfully.......")

            else:
                print("\n\t\t\tMember not found")

        elif i == '4':
            phone_check3 = input("Enter the phone number of Member - ")
            if phone_check3 in Members:
                update_member(phone_check3)
                print("\n\t\t\tMember updated successfully......")

        elif i == '5':
            reg_name = input("Enter the name of regimen - ")
            if reg_name not in Regimen:
                create_regimen(reg_name)
                print("\n\t\t\tRegimen has been created successfully...... ")
            else:
                print("\n\t\t\tRegimen name already exists.....")

        elif i == '6':
            print("\n{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Regimen', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
            for k in Regimen:
                print("\n{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(k, Regimen[k]['Mon'], Regimen[k]['Tue'], Regimen[k]['Wed'], Regimen[k]['Thu'], Regimen[k]['Fri'], Regimen[k]['Sat'], Regimen[k]['Sun']))

        elif i == '7':
            reg_name = input("Enter the name of Regimen - ")
            if reg_name in Regimen:
                del Regimen[reg_name]
                print("\n\t\t\tRegimen has been deleted......")
            else:
                print("\n\t\t\tRegimen is not present.......")

        elif i == '8':
            reg_name2 = input("Enter the name of Regimen - ")
            if reg_name2 in Regimen:
                del Regimen[reg_name2]
                update_regimen(reg_name2)
                print("\n\t\t\tRegimen has been updated successfully......")
            else:
                print("\n\t\t\tRegimen is not present.......")

        elif i == '9':
            login_screen()
            
        else:
            print("Wrong Input\n")

        menu()

def member_menu():
    print("\n")
    print("   *****Edyoda Gym Management System*****")
    print("Hello Member, please select a choice from the menu\n\n")
    print("1. My Regimen")
    print("2. My Profile")
    print("3. To go back to login screen")
    while True:
        i = input("Enter your choice:  ")
        if i == '1':
            mob_no = input("Enter the mobile No - ")
            if mob_no in Members:
                m = Members[mob_no]['Regimen Assigned']
#                 print(m)
                print("\n{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Regimen', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(m, Regimen[m]['Mon'], Regimen[m]['Tue'], Regimen[m]['Wed'], Regimen[m]['Thu'], Regimen[m]['Fri'], Regimen[m]['Sat'], Regimen[m]['Sun']))
                
            else:
                print("\n\t\t\tMember not found")

        elif i == '2':
            mob_no2 = input("Enter the mobile No - ")
            if mob_no2 in Members:
                print("\n\n{:<15} {:<5} {:<8} {:<12} {:<25} {:<5} {:<15} {:<10}".format('Name', 'Age', 'Gender', 'Mobile No', 'Email Id', 'BMI', 'Join date', 'Subs End date'))
                print("{:<15} {:<5} {:<8} {:<8} {:<27} {:<5} {:<15} {:<10}".format(Members[mob_no2]['name'], Members[mob_no2]['Age'], Members[mob_no2]['Gender'], mob_no2, Members[mob_no2]['email'], Members[mob_no2]['BMI'], Members[mob_no2]['joinDate'], Members[mob_no2]['Subscription End date']))
                
                
            else:
                print("\n\t\t\tMember not found")

        elif i == '3':
            member = 0
            login_screen()

        member_menu()
        
def login_screen():        
    print("Press 1 for Admin and Press 2 for Member\n".center(columns))
    print("Press 3 to exit the program".center(columns))
    login_Response = input()   

    if login_Response == '1':
        print("\n")
        menu()   


    elif login_Response == '2':
            print("\n")
            member_menu()

    elif login_Response == '3':
        sys.exit()

    else:
        print("\n\t\t\tWrong Input\n")
        login_screen()
        
login_screen()