def validateColor(input):

    c = ['#''0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']

    output = [i for i in input if i not in c]



    if (output == []):

        print("Hex code is correct")

    else:

        print("Hex code is not correct")



# Main program

hex_number = str(input("Input Hex Number\t\t:"))

validateColor(hex_number)