def check_if_good(t, function_type, msg):
    while True:
        t = input(msg)

        try:
            t = function_type(t)
            return t
        except:
            print('Wrong data format! Did you provide correct value?')
            continue
