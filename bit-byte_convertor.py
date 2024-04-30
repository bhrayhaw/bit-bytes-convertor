"""
Elijah will handle the display of the introductory message
Jemima will handle the user input
Justice will handle the bytes to bit conversion
Tracy will handle the bits to bytes conversion
Martha will handle the exiting of the program
Nana Ama will handle the invalid choice
"""
print(" ********************************************* \n\tWelcome to our bit byte convertor\n ********************************************* \n")
print("1. Bits-Bytes Conversion \n2. Bytes-Bits Conversion \n3. Exit \n")


#Check user choice and perform corresponding conversion

if choice == '2':
        #Bits to bytes conversion
        bits_value = float(input("Enter the value in bits: "))
        bytes_value = bits_value // 8 
        print(f"{bits_value} bits is equal to {bytes_value} bytes.\n")
else: 
    print("invalid choice please enter 1,2,3")