def calculate(num1, num2, operator):
    # logic here
    if operator == "+":
        return num1 + num2   
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")


def main():
    while True: 
        # get input
        parts = user_input.split()
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        result = calculate(num1, num2, operator)
        print(result)
    
        

    if __name__ == "__main__":
        main()