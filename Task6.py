#You need to return a string that looks like a diamond shape when printed on the screen, 
#using asterisk (*) characters. Trailing spaces should be removed, and every line must be 
#terminated with a newline character (\n). 

#Return null/nil/None/... if the input is an even number or negative, as it is not 
#possible to print a diamond of even or negative size. 

def main():

    test_diamond = int(input("Enter desired size:"))

    def diamond(size):
        if size % 2 == 0 or size < 0:
            return(None)

        #Where the max width of the diamond is created, after this we must decrease
        inflection_index = ((size//2 + 1))

        for i in range(1, size+1):
            if i > inflection_index:
                stars_to_remove = (i-inflection_index)
                print("*" * (i-(stars_to_remove*2)))
                continue

            print("*" * i)


    diamond(test_diamond)


if __name__ == "__main__":
    main()