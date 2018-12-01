def check_if_good(t, function_type, msg):
    """
    Function to check if user input is correct and with agreement to the program functionality.
    :param t: it is name of variable, that user need to provide;
    :param function_type: it is a function that is executed to evaluate whether user input is correct or not.
    It is connected to t parameter as command that is going to be executed is: function_type(t).
    Need to be provided without brackets!
    Examples of parameters and what they will execute float -> float(t), int -> int(t)
    :param msg: It is a message that you want to ask user, when asking for input.
    :return: Returning value of user input.
    """
    while True:
        t = input(msg)
        try:
            t = function_type(t)
            return t
        except:
            print('Wrong data format! Did you provide correct value?')
            continue


def main():
    check_if_good()


if __name__ == "__main__":
    main()
