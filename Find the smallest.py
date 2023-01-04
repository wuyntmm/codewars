def smallest(n):
    grab, drop, minimal = None, None, n
    for took in range(len(str(n))):
        for place in range(len(str(n))):
            arr = list(str(n))
            arr.insert(place, arr.pop(took))
            if int(''.join(arr)) < minimal:
                minimal = int(''.join(arr))
                grab, drop = took, place
    return [minimal, grab, drop]

print(smallest(935855753))
