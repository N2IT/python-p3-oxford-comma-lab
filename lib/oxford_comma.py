def oxford_comma(items):

    # if a single element return untouched
    
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    # if more than two elements return el 1 AND el 2
    elif len(items) >= 3:
        last = items.pop(-1)
        pen_ult = items.pop(-1)
        new_list = [ pen_ult, last ]
        new_new_list = ", and ".join(new_list)
        items.append(new_new_list)
        last_list = ", ".join(items)
        return last_list
