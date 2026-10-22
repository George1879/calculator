import re, operator

def main():
    command = ""
    print("Calculator 1.1 (beta)\n")
    while command != "quit":
        command = input("Enter a command: \n")
        split_input(command)

#Validate input (one day)
def is_valid(split_input):
    valid_ops = [
        "**","*","/","+","-"
    ]
    brackets = ["(", ")"]

    valid = False
    #Check that every item in the list is valid
    for i in range(0,len(split_input)):
        if split_input[i].isdigit() or split_input[i] in valid_ops or split_input[i] in brackets:
            valid = True
        else:
            valid = False
            return valid
    digiCount = 0 
    opCount = 0
    #Check that it goes item -> operator -> item 
    for d in range(0, len(split_input)):
        if split_input[d] in brackets:
            continue #Eventually check brackets are completed.. or do in brackets()
        elif split_input[d].isdigit():
            #Must be an operator for every two numbers. Checked at the end.
            digiCount += 1
            pass #Do something here :D
        elif split_input[d] in valid_ops:
            #Must be an operator
            print("Operator detected:", split_input[d])
            opCount += 1
            print("d+1 =",d+1,"len of list =",len(split_input))
            print("Split list:",split_input)
            if (d+1) >= len(split_input):
                print("Item after operator isn't a number!")
                valid = False
                return valid

            if split_input[d-1].isdigit() == False:
                print("Item before operator must be a number!")
                valid = False
                return valid
            elif split_input[d+1].isdigit() == False:
                print("Item after operator isn't a number!")
                valid = False
                return valid
            else:
                print("Oh hell naw\nHow did you even get this error?")
            
    if opCount > 0:
        if (digiCount / opCount) != 2:
            print("Must be an operator for every two numbers.\n")
            valid = False
            return valid
    else:
        print("Must include an operator!\n")
        valid = False
        return valid
    
    return valid

#Loop through and perform the overall calculation
def perform_calculation(split_list):
    priority = [
    ["("],
    ["**"],
    ["*", "/"],
    ["+", "-"]
    ]

    #print(operations["+"](5,10))
    temp_answer = BODMAS(priority, split_list)


    return temp_answer

#Apply BODMAS to the input
def BODMAS(priority, split_list, process_brackets = True):
    for i in range(0, len(priority)):
        #Ignore processing brackets if we need
        if "(" in priority[i] and not process_brackets:
            continue
        
        #I should've commented this while writing :/ 
        for d in range(0, len(split_list)):
            if split_list[d] in priority[i]:
                index = d
                #Calls smaller calc with the operator, list, and index of the number to be calculated
                calc = smaller_calc(split_list[index], split_list, index)
                return calc

#Actually performs calculations
def smaller_calc(operatorz, split_list, o_index):
    priority = [
    ["("],
    ["**"],
    ["*", "/"],
    ["+", "-"]
    ]
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow
    }


    if operatorz == "(":
        n_index = split_list.index("(")
        return brackets(n_index, split_list)

    left = float(split_list[o_index - 1])
    right = float(split_list[o_index + 1])

    answer = operations[operatorz](left, right)
    #Replacing the list with the answer
    split_list[o_index - 1:o_index + 2] = [str(answer)]

    BODMAS(priority, split_list, False)
    answer = float(split_list[0])

    return answer

#Loops through recursivley when every ( is detected, finishing with ) to get nested brackets
def brackets(first, split_list):
    #Time to panic
    prinaliority = [
    ["("],
    ["**"],
    ["*", "/"],
    ["+", "-"]
    ]
    expression = []
    i = first + 1

    while i < len(split_list):
    
        if split_list[i] == "(":
            brackets(i, split_list)
            
        elif split_list[i] == ")":
            end = i
            for h in range(first + 1, end):
                expression.append(split_list[h])

            Correct_vers = BODMAS(priority, expression, False)
                
            split_list[first:end + 1] = [str(Correct_vers)]
            
            return Correct_vers
        
        i += 1
    

def help():
    print("The valid operators are: () (brackets), ** (power), * (multiply), / (divide), + (add), and - (take-away)")
    print("Type 'quit' to exit.\n")

#Split the original input into seperate items in split_list
def split_input(command):
    if command == "quit":
        quit()
    elif command == "help":
        help()
    else:
        command = command.replace(" ", "")
        final = re.findall(r'\d+(?:\.\d+)?|\*\*|[+\-*/()]', command)
        #Forgot how to modify re.findall so we use a seperate list with everything included to validate
        temp = list(command)
        valid = is_valid(temp)
        if valid == True:
            answer = perform_calculation(final)
            print(str(answer),"\n")
        else:
            print("ERROR: invalid input ('help' for command list)\n")

main()
