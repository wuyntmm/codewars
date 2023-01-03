def multiplaer(symbol_end, arr, begin):
    end = 0
    i = begin
    for ch in arr[begin::]:
        if ch == symbol_end:
            end = i
            break
        i += 1
    if end != len(arr) - 1:
        if str(arr[end + 1]).isdigit():
            for i, x in enumerate(arr):
                if str(x).isdigit() and begin < i < end:
                    arr[i] = str(int(arr[i]) * int(arr[end + 1]))
            arr.pop(end + 1)
            arr.pop(end)
            arr.pop(begin)
        else:
            arr.pop(end)
            arr.pop(begin)
    else:
        arr.pop(end)
        arr.pop(begin)
    return arr


def parse_molecule(formula):
    opposite = {'[': ']',
                '(': ')',
                '{': '}'}
    arr = list(formula)

    for ind, el in enumerate(arr):
        if str(arr[ind]).isalpha():
            if ind != len(arr) - 1:
                if arr[ind + 1].islower():
                    arr[ind] += arr[ind + 1]
                    arr.pop(ind + 1)
            if ind == len(arr) - 1:
                arr.append('1')
            elif str(arr[ind + 1]).isdigit():
                continue
            else:
                arr.insert(ind + 1, '1')
        elif arr[ind].isdigit():
            if ind != len(arr) - 1:
                if arr[ind + 1].isdigit():
                    arr[ind] += arr[ind + 1]
                    arr.pop(ind + 1)
    flag = True
    while flag:
        for y in arr:
            flag = False
            if y in opposite.keys():
                flag = True
                break
        for ind, char in enumerate(arr[::-1]):
            if char in list(opposite.keys()):
                multiplaer(opposite.get(char), arr, len(arr) - ind - 1)
                break
    result = {}
    for ind, el in enumerate(arr):
        if el.isalpha():
            if result.get(el) is None:
                result[el] = int(arr[ind + 1])
            else:
                temp = int(result.get(el))
                result[el] = int(temp + int(arr[ind + 1]))
    return result


print(parse_molecule('{[Co(NH3)4(OH)2]3Co}(SO4)3'))
