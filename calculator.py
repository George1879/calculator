import re, operator

def main():
    command = ""
    print("Calculator 1.1 (beta)\n")
    while command != "quit":
        command = input("Enter a command: \n")
        split_input(command)

#Validate input (one day)
def is_valid(split_input):
    # Conceptually :
    # must have an input
    # must detedct -[number] as a negative number
    # must be an input for an operator. (what's the ratio ?)

    operators = ["**", "*", "/", "+", "-"]
    opCount = 0
    numCount = 0
    openCount = 0
    closedCount = 0
    i = 0

    if split_input == None:
        return False, "Please enter a valid input."

    while i < len(split_input):
        if split_input[i] == "-":
            #Figure out if it's a negative number..\
            if i == 0 or split_input[i-1] in ["(", "+", "-", "*", "/", "**"]:
                split_input[i+1] = - float(split_input[i+1])
                del split_input[i]
                i -= 1
            else:
                opCount += 1

        elif split_input[i] in operators:
            opCount += 1
        elif split_input[i] == "(":
            openCount += 1
        elif split_input[i] == ")":
            closedCount +=1 
        else:
            numCount += 1

        i+=1

    if opCount == 0:
        return False, "Please include an operator."
    else:
        if opCount == 1:
            if numCount < 2:
                return False, "Please Google how to use a calculator." #Change eventually
        else:
            if numCount - opCount < 1:
                return False, "Please include a valid ratio of operators to numbers."

    if openCount > 0 or closedCount > 0:
        if openCount != closedCount:
            return False, "Please include an appropriate number of brackets."

    return True, ""




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
    priority = [
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
    print("A take-away sign (-) directly to the left of a number will treat it as a negative one.")
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
        valid, message = is_valid(final)
        if valid == True:
            answer = perform_calculation(final)
            print(str(answer),"\n")
        else:
            print("ERROR:",message,"('help' for more info) \n")

main()
