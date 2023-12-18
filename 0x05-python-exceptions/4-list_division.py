#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    finalList = []
    for a in range(list_length):
        try:
            div_res = my_list_1[a] / my_list_2[a]
        except (ZeroDivisionError):
            print("division by 0")
            div_res = 0
        except (TypeError):
            print("wrong type")
            div_res = 0
        except (IndexError):
            print("out of range")
            div_res = 0
        finally:
            finalList.append(div_res)
    return finalList
