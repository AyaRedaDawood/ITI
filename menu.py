
def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Parse access.log")
    print ("2. Directory monitoring")
    print ("3. scan a range of IPs")
    print ("4. Attack detection ")
    print ("5. Parse any link")
    print (67 * "-")
  
loop=True      
  
while loop:         
    print_menu()    
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:
        exec(open("Parsing.py").read())
        
    elif choice==2:
        exec(open("Watch_Dir.py").read())
      
    elif choice==3:
        exec(open("Scanner.py").read())
      
    elif choice==4:
        exec(open("lisener.py").read())

    elif choice ==5:
        exec(open("linl_Parsing.py").read())

        loop=False
    else:

        raw_input("Wrong option selection. Enter any key to try again..")
