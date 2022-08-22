def calculator():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print('Operations: "add" "substract" "multiply" "divide"')
    OP=input('Enter The operation You Want to Perform:')
    if OP=='add' or OP=='Add':
        print("Addition is:"+n1+n2)
    elif OP=='substract' or OP=='Substract':
        print("Substraction is:"+n1-n2)
    elif OP=='Multiply' or OP=='M':
        print("multiplication is:"+n1*n2)
    elif OP=='devide' or OP=='Divide':
        print("Division is:"+n1/n2)
    else:
        print('Operation Not Available....!')

calculator()