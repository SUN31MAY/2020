# AUTHOR : SHAMIRAN BEHERA
# NUDE NUMBER PROGRAM
# A NUDE NUMBER IS ANY POSITIVE INTEGER THAT IS DIVISIBLE BY ALL ITS DIGITS AND DOSEN'T CONTAIN ZERO


def check(n):
    """FUNCTION THAT CHECKS IF n IS A NUDE NUMBER OR NOT, n IS IN STRING FORMAT"""
    nude_num = f"{int(n)} IS A NUDE NUMBER\n".capitalize()  # PRINT THIS NUMBER IS NUDE NUMBER
    non_nude = f"{int(n)} IS NON NUDE NUMBER\n".capitalize()  # ELSE PRINT THIS
    if "0" in n or "-" in n:  # NUDE NUMBER SHOULD NOT CONTAIN ZERO IN IT AND SHOULD BE POSITIVE
        return non_nude  # RETURNING non_nude IF n CONTAINS ZERO
    else:
        for i in n:  # EVERY ELEMENT IN n, n IS STRING
            if int(n) % int(i) != 0:  # DIVIDING n WITH EACH DIGIT OF n BY CONVERTING TO INT
                return non_nude  # IF REMAINDER OCCURS IN THE ABOVE DIVISION RETURN non_nude
    return nude_num  # IF IT PASSES ALL IF CONDITIONS THEN RETURN nude_num


def try_again():
    """ THIS FUNCTION CHECKS IF USER WANTS TO TRY AGAIN """
    while 1:  # LOOPING IF INVALID KEY IS PRESSED
        choice = input("\nWANT TO CHECK ANOTHER NUMBER ?\nPRESS Y--> YES\t N--> NO :".capitalize()).lower()  # STORES USER INPUT
        if choice == "y" or choice == "n":  # USER INPUT SHOULD BE EITHER "Y" OR "N"
            return choice  # RETURNING CHOICE TO MAIN PROGRAM
        else:
            print("invalid!".capitalize())  # ELSE PRINTING INVALID AND LOOPING


# MAIN PROGRAM
while 1:  # RUNS IN A LOOPING FASHION
    try:  # TRY EXCEPT BLOCK TO PRINT EXCEPTION
        num = int(input("\nENTER A POSITIVE INTEGER : ".capitalize()))  # ASKING INPUT FROM USER
    except Exception as e:
        print(e)  # PRINTING EXCEPTION
        continue  # LOOPING BACK AND FOR ASKING USER INPUT
    print(check(str(num)))  # PASSING NUM AS STRING AND PRINTING OUTPUT
    if try_again() == "n":  # IF USER PRESSES N IN TRY_AGAIN FUNCTION WE BREAK THE LOOP
        break
print("BYE (^.^)".capitalize())  # PRINTING BYE
