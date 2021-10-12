#!/usr/bin/python3
import os, time, pwd

USERNAME = pwd.getpwuid(os.getuid())[0]
CONFIG_PATH = f"/home/{USERNAME}/.config/"
BUILD_PATH = "/usr/local/bin/"
B_PATH = CONFIG_PATH + "buckets.txt"

buckets_list = ["A. OPEN BUCKETS", "B. ADD BUCKETS", "C. EXIT BUCKETS"]

def switchCase(args):
    case = {"a" : open_buckets, "A" : open_buckets,
            "b" : add_buckets, "B" : add_buckets,
            "c" : exit, "C" : exit}
    return case[args]()

# function that checks whether we have buckets.txt or Not
def check():

    # basically does an $ls and the further process is to check whether buckets.txt is present
    items = [files for files in os.listdir(path=CONFIG_PATH)] 

    if "buckets.txt" in items:
        main()
    else: 
        create_buckets = str(input("Buckets Text File Not Found, would you like to create it? (Y/n) "))

        # checks if the user wants to use the program to make buckets.txt 
        # this is meant for users who wants to use another text editor to write the list 
        if create_buckets == "n" or create_buckets == "N":
            exit()
        else:
            with open(B_PATH, "x") as f:
                f.write("(Based on Priorities)\n")
            main()

def main():

    os.system('clear')  # clears the screen, obviously 

    print("---------------------------------------------------------\n")
    print("              BUCKETS - TODO LISTS IN PYTHON             \n")
    print("                      by bangkemono                      \n")
    print("---------------------------------------------------------")

    for options in buckets_list:
        print(options)

    # I use the try block just so that if i use ^C (Ctrl-C) it doesn't raise
    # an error before I quit, it's just a tiny detail, but i hate it lmao 

    try:
        main_input = input("\n$")
        
        try:
            switchCase(main_input)
        except Exception:
            os.system('clear')
            print("Invalid Input! ")
            input("\nPress any key to continue.... ")
            return main()

    except(KeyboardInterrupt):
        print(" ^C\n")
        exit()

def numbering_buckets(args):
 
    with open(B_PATH, "a") as bappend, open(B_PATH) as blist: # opens buckets.txt twice, for appending and for reading

        for numbering, contents in enumerate(blist, 1): # bad auto-numbering system smh
            pass
        bappend.write(f"{str(numbering).zfill(2)}. {args} | {time.asctime().split()[2]}/{time.asctime().split()[1]}/{time.asctime().split()[4]} {time.asctime().split()[3]}\n")

def remove_add_buckets(args):

    # think of it as buffers i guess... first it stores our first data within a list
    # Then it also stores the new data from into a list but it's only the "removed line"
    with open(B_PATH) as blist_old, open(B_PATH) as blist:

        old_buff = [i for i in blist_old.read().split("\n")]
        remov_buff = "".join([word for word in blist.read().split("\n") if word.startswith(args)])

    # Using the Try/Except Block to prevent any form of errors, usually it's just whitespace errors
    try:
        del old_buff[0] # somehow old_buff.remove("Based on Priorities") doesn't work. WTF??
        old_buff.remove(remov_buff)
        old_buff.remove("")
    except(ValueError):
        pass
    
    new_buff = "\n".join([f"{str(nums).zfill(2)}. {chars[4:]}" for nums, chars in enumerate(old_buff, 1)]) # yes, i know... it's ugly

    # appends the previously said new data, into our buckets.txt file
    with open(B_PATH, "w") as blist_new:
        if new_buff.startswith("01") == True:
            blist_new.write(f"(Based on Priorities)\n{new_buff}\n")
        else:
            blist_new.write(f"(Based on Priorities)\n{new_buff}")

def add_buckets():
    
    os.system('clear')
    print("-----------------------")
    print("\n     THINGS TO DO      \n")
    print("-----------------------")

    with open(B_PATH) as blist:
        print(blist.read())

    print("\nWhat would you like to add?")
    print("To go back to main menu, please Type \'$exit\'\n")

    add_buckets_inp = input("$")
    
    if add_buckets_inp == "exit":
        main()
        
    else: # as long as the user doesn't use '$exit' it will append the input
        numbering_buckets(add_buckets_inp)
        add_buckets() 

def open_buckets():

    os.system('clear')
    print("-----------------------")
    print("\n     THINGS TO DO      \n")
    print("-----------------------")

    with open(B_PATH) as blist:
        print(blist.read())

    print("\nTo Remove a Task from Buckets type in \'$*line number to remove*\'")
    print("To Remove all Task from Buckets type in \'$purge\'")
    print("To go back to the main menu, please type \'$exit\'\n")

    remove_input = input("$")
    
    if remove_input == "exit":
        main()

    elif remove_input == "purge": # for debugging purposes, or if you finished all of your stuffs
        with open(B_PATH, 'w') as purger:
            purger.write("(Based on Priorities)\n")
        open_buckets()

    # gives a range for maximum nums inputted, so the things added in buckets.txt have a max value of 100 ?
    elif remove_input not in [str(i).zfill(2) for i in range(1, 101)]:
        print("Please enter a valid number")
        input("Press any key to continue ")
        open_buckets() 

    else: # if the user doesn't give a spesific value ($purge, $exit, etc) it'll just call the remove_add_buckets function

        remove_add_buckets(str(remove_input))
        open_buckets()

if __name__ == '__main__':
    check()
        
