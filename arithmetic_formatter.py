def arithmetic_arranger(problems, solve=False):
    # We define the lines
    first = ""
    second = ""
    lines = ""
    sumx = ""
    # Maximal problems is five
    if len(problems) >= 6:
        return "Error: Too many problems."
    # We split the problem in components for each line
    for i in problems:
        a = i.split()
        n1 = a[0]
        op = a[1]
        n2 = a[2]
        # Check the lenght of the numbers, max allowed is 4 digits
        if (len(n1) > 4 or len(n2) > 4):
            return "Error: Numbers cannot be more than four digits."
        # Check for valid digits
        if not n1.isnumeric() or not n2.isnumeric():
            return "Error: Numbers must only contain digits."

        # Check the valid operators
        if (op == "+" or op == "-"):
            if op == "+":
                sums = str(int(n1) + int(n2))
            else:
                sums = str(int(n1) - int(n2))
            # Set lenght of top, bottom, lines and res
            l = max(len(n1), len(n2)) + 2
            top = str(n1).rjust(l)
            bot = op + str(n2).rjust(l - 1)
            line = "-" * l
            res = str(sums).rjust(l)

            # Add to the overall string
            if i != problems[-1]:
                first += top + (" " * 4)
                second += bot + (" " * 4)
                lines += line + (" " * 4) 
                sumx += res + (" " * 4)
            else:
                first += top
                second += bot
                lines += line
                sumx += res  
        else:
            return "Error: Operator must be '+' or '-'." 
    if solve:
        arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        arranged_problems = first + "\n" + second + "\n" + lines 
    return arranged_problems





print(arithmetic_arranger(["32 / 698", "3801 - 2", "45 + 43", "123 + 49"]))
