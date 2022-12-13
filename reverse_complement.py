def reverse(sequence):
    """
    The "reverse" function performs the conversion from a forward strand to a reverse strand
    :param sequence: DNA sequence entered by the user
    :return: returns the conversion
    """
    number_of_letters=0
    reverse=""
    for i in sequence:
        number_of_letters+=1
    for i in range(number_of_letters):
        reverse+=sequence[number_of_letters-1]
        number_of_letters-=1
    return reverse

def complement(sequence):
    """
    The "complement" function performs the conversion from forward strand to a complement strand
    :param sequence: DNA sequence entered by the user
    :return: returns the conversion
    """
    complement=""
    for i in sequence:
        if i=="T" or i=="t":
            complement+="A"
        elif i=="A" or i=="a":
            complement+="T"
        elif i=="C" or i=="c":
            complement+="G"
        elif i=="G" or i=="g":
            complement+="C"
    return complement

def program():
    """
    The "program" function is a menu with options, where the user enters a DNA sequence and chooses the conversion he wants to perform
    """
    program=True
    while program==True:
        letters = {"A", "T", "C", "G","a","t","c","g"}
        sequence=input("Enter the sequence: ")
        for i in sequence:
            if i in letters:
                program=False
    while True:
        try:
            menu=["Exit","Reverse-Complement","Reverse","Complement"]
            for i in range(len(menu)):
                print(i,menu[i],sep="-")
            print()
            option=int(input("Enter an option: "))
            if option<0 or option>3:
                print("Invalid option")
            elif option==0:
                break
            elif option==1:
                print("Reverse-Complement: ",complement(reverse(sequence)))
            elif option==2:
                print("Reverse: ",reverse(sequence))
            elif option==3:
                print("Complement: ",complement(sequence))
        except ValueError:
            print("Invalid option")

program()



