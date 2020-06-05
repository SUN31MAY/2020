# AUTHOR : SHAMIRAN BEHERA
# PROGRAM TO DETECT CORRECT PARENTHESIS STRING


def check(paren_str):
    """ THIS FUNCTION CHECKS THE PARENTHESIS STRING """
    correct = "input parenthesis string is correct\n".capitalize()  # THIS IS RETURNED IF PARENTHESIS STRING IS CORRECT
    incorrect = "input parenthesis string is in-correct\n".capitalize()  # RETURNED IF NOT CORRECT
    if len(paren_str) % 2 != 0:  # CLOSING BRACKETS SHOULD BE EQUAL TO OPEN BRACKETS HENCE SHOULD BE MULTIPLE OF 2
        return incorrect
    stack = []  # EMPTY LIST THAT ACTS AS A STACK
    bracket = {"(": ")", "{": "}", "[": "]"}  # DIFFERENT BRACKET TYPES
    for i in paren_str:  # CHECKING EACH ELEMENT OF PARENTHESIS STRING
        if i in bracket:
            stack.append(i)  # IF IT IS PRESENT AS KEY IN BRACKET DICTIONARY WE APPEND IT TO STACK LIST
        else:  # IF IT NOT PRESENT IN BRACKET DICTIONARY'S KEY
            if len(stack) != 0 and i == bracket[stack[(len(stack) - 1)]]:  # CHECKING IF IT MATCHES THE VALUE OF LAST
                # KEY OF BRACKET APPENDED TO STACK THEN WE POP THAT KEY FROM STACK AND THERE SHOULD BE AN ELEMENT TO POP
                stack.pop()
            else:  # IF THE VALUE DOSEN'T MATCH THE LAST KEY APPENDED TO STACK THEN RETURN INCORRECT
                return incorrect
    return correct if len(stack) == 0 else incorrect  # ALL STACK ELEMENTS SHOULD BE POPPED
    # RETURNING CORRECT IF THE PARENTHESIS STRING IS CORRECT AFTER PASSING THE IF CONDITIONS ELSE RETURNING INCORRECT


def play_again():
    """ FUNCTION THAT CHECKS IF USER WANTS TO TRY TRY AGAIN """
    while 1:  # USED FOR LOOPING IF INVALID BUTTON IS PRESSED
        try_again = input(
            "\nWANT TO TRY AGAIN ?\n PRESS Y--> YES\t N-->NO :".capitalize()).lower()  # STORES THE CHOICE OF USER
        if try_again == "y" or try_again == "n":  # IF IT IS EITHER YES OR NO
            return try_again  # RETURNING THE VALUE
        else:
            print("INVALID!".capitalize())  # PRINTING INVALID AND LOOPING


# MAIN PROGRAM
while 1:
    paren_str = input('\nENTER A PARENTHESIS STRING : ')  # STORES THE PARENTHESIS STRING
    print(check(paren_str))  # PRINTS THE FUNCTION RETURN VALUE, PAREN_STR IS PASSED TO CHECK FUNCTION
    if play_again() == "n":  # CHECKS PLAY AGAIN VALUE
        break  # COME OUT OF LOOP
print("BYE (^.^)".capitalize())
