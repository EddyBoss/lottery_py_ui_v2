import random
import time     
class Existing_Lottery:
        
     def lottery_info():
        number_slot_1 = [[], [], [], []]
        number_slot_2 = [[], [], [], []]
        number_slot_3 = [[], [], [], []]
        print ("Write your last lottery numbers")
        print ("Please enter 4 numbers for the first slot")
        for i in range(4):
            number_slot_1[i] = input("Enter number: ").strip()
            if number_slot_1[i] == "" or number_slot_1[i] == " ": 
                number_slot_1[i] = input("Enter a number again!: ").strip()
            else : continue
        print ("Please enter 4 numbers for the second slot")
        for i in range(4):
            number_slot_2[i] = input("Enter number: ").strip()
            if number_slot_2[i] == "" or number_slot_2[i] == " ":
                number_slot_2[i] = input("Enter a number again!: ").strip()
            else : continue
        print ("Please enter 4 numbers for the third slot")
        for i in range(4):
            number_slot_3[i] = input("Enter number: ").strip()
            if number_slot_3[i] == "" or number_slot_3[i] == " ":
                number_slot_3[i] = input("Enter a number again!: ").strip()
            else : continue
        print ("Your last lottery numbers are: {} {} {}".format(number_slot_1, number_slot_2, number_slot_3))
        
        print("Calculating...")
        time.sleep(1)
        print("Your new numbers are: {} {} {}".format(random.choice(number_slot_1), random.choice(number_slot_2), random.choice(number_slot_3)))
        print("Good Luck, with your new numbers!")

"__init__" == "__main__ "
# Lottery()
Existing_Lottery.lottery_info()