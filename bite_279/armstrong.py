"""In this bite, you will try to solve the Armstrong number question: given an integer, determine if it is an armstrong number
  153 = (1^3) + (5^3) + (3^3)= 153. True
  """
def is_armstrong(n: int) -> bool:
    adder = 0

    if n <=9:
        return True
    else:
        conv = [x for x in str(n)]

        for ele in range(0, len(conv)):
            adder += int(conv[ele])**len(conv)

        if adder == n:
            return True
        else:
            return False