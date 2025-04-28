def unique_in_order(seq):
    if len(seq) == 0:
        return []
    result = [seq[0]]

    for x in seq[1:]:
        if x != result[-1]:
            result.append(x)

    return result

if __name__ == '__main__':
    string = "AAAABBBCCDAABBB"

    print(unique_in_order(string))