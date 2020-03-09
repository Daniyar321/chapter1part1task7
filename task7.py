def biggest_guy(one, two, three):
    if one > two > three:
        return one
    elif one < two > three:
        return two
    else:
        return three

func = biggest_guy(1,3,2)
print(func)