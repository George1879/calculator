import re, operator

def main():
    command = ""
    print("Calculator 1.0 (beta)\n")
    while command != "q":
        command = input("Enter a command: \n")
        if is_valid(command) == True:
                split_input(command)

def is_valid(command):
    return True

def perform_calculation(split_list):
    print(split_list)
    priority = ["(", "**", "*", "/", "+", "-"]

    #print(operations["+"](5,10))
    temp_answer = BODMAS(priority, split_list)

    answer = "We don't know the answer gang"

    return answer

def BODMAS(priority, split_list, process_brackets = True):
    for i in range(0, len(priority)):
        if priority[i] == "(" and not process_brackets:
            continue
        for d in range(0, len(split_list)):
            if priority[i] == split_list[d]:
                index = split_list.index(priority[i])
                calc = smaller_calc(priority[i],split_list, index)
                return calc

def smaller_calc(operatorz, split_list, o_index):
    print("Operator",operatorz,"detected\n")
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

    return answer

def brackets(first, split_list):
    #Time to panic
    priority = ["(", "**", "*", "/", "+", "-"]
    expression = []

    for i in range(first, len(split_list)):
        print("Test x"+str(i))
        if split_list[i] == "(":
            brackets(i + 1, split_list)

        elif split_list[i] == ")":
            end = i
            for h in range(first, end):
                expression.append(split_list[h])
                print(split_list[h])

            Correct_vers = BODMAS(priority, expression, False)
            print("Maybe sorted ? ")
            print(Correct_vers)

            print("Expression achieved:",expression)
            split_list[first - 1:end + 1] = [str(Correct_vers)]

            if "(" not in expression:
                print("FINAL VERSION!!!")
                return 

            return i





def split_input(command):
    operators = ["*", "-", "+", "/"]
    detected_o = []
    detected_num = []

    command = command.replace(" ", "")
    final = re.findall(r'\d+(?:\.\d+)?|\*\*|[+\-*/()]', command)

    answer = perform_calculation(final)

    print(str(answer))

main()