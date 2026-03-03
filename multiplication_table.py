def generate_table(number):
    #loop 1 to 12
    for i in range(1, 13):        
        result = number * i
        print(f"{number} x {i} = {result}")
    #print formatted string 

    def main():
        while True:
            # input
            user_input = input("Enter a number to see its multiplication table (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Goodbye.")
                break
            # validation 
            try:
                number = int(user_input)
                generate_table(number)
            except ValueError:
                print("Please enter a valid integer or 'q' to quit.")


    if __name__ == "__main__":        
        main()
