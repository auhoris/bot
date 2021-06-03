def count_yes(tuple):
    stupid = 0
    c_of_yes = 0
    for _, value in tuple.items():
        if (value == "Да"):
            if (stupid != 0):
                c_of_yes += 1
        stupid += 1
    return c_of_yes
