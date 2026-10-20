import re, operator

def main():
    command = ""
    print("Calculator 1.1 (beta)\n")
    while command != "q":
        command = input("Enter a command: \n")
        if is_valid(command) == True:
                split_input(command)

#Validate input (one day)
def is_valid(command):
    return True

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
    
        if split_list[i] == "(":#
            brackets(i, split_list)
            
        elif split_list[i] == ")":
            end = i
            for h in range(first + 1, end):
                expression.append(split_list[h])

            Correct_vers = BODMAS(priority, expression, False)
                
            split_list[first:end + 1] = [str(Correct_vers)]
            
            return Correct_vers
        
        i += 1
    



#Split the original input into seperate items in split_list
def split_input(command):
    command = command.replace(" ", "")
    final = re.findall(r'\d+(?:\.\d+)?|\*\*|[+\-*/()]', command)

    answer = perform_calculation(final)

    print(str(answer),"\n")

main()