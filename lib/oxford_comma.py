def oxford_comma(arr):
    if not str:
        return ""
    elif len(arr)==1:
        return arr[0]
    elif len(arr)==2:
        return " and ".join(arr)
    else:
        return ", ".join(arr[:-1])+ f", and {arr[-1]}"
