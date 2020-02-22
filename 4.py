def validateColor(input):

    c = ['9','2','5','2','1','1','2','2','4','4,']

    output = [i for i in input if i not in c]



    if (output == []):

        print("input yang di terima adalah string")

    else:

        print("input yang di terima bukan string")



# Main program

hex_number = str(input("Input Hex Number\t\t:"))

validateColor(hex_number)