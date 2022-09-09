import random
from tkinter import *
from PIL import ImageTk, Image

# Create App Layout
# Lottery = Tk()
# Lottery.geometry('800x360')
# Lottery.title('Lottery Number Generator')
# Lottery.iconbitmap("ticket.ico")

# num_input = input(f"Please enter a value: \n", a , b , c , d)


def random_generator(): 
    a, b, c, d = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9) 
    print("Random Number Generator is running!")
    print(f"Your random numbers are: {a} {b} {c} {d} \n", end="", flush=True, file=open("output.txt", "a"), sep=" ")

def fix_generator():
    a, b, c, d = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9) 
    print("Fix Number Generator is running!")
    counter = (random.randint(0, 9) + random.randint(0, 9)) / 2
    a, b , c , d = ({(a + counter) /2} , {(b + counter)/2} , {(c + counter) / 2} , {(d + counter)/2})
    print(f"Your fix numbers are: {a} {b} {c} {d} \n", end="", flush=True, file=open("fixput.txt", "a"), sep=" ")
    
   
    

# def initialize(): 
#     random_generator()


"__init__" == "__main__ "
random_generator()
fix_generator()
