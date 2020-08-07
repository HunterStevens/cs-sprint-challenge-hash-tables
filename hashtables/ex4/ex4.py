def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cahce_neg = {}
    cahce_pos = {}

    for i in a:
        if i < 0:
            if i in cahce_neg:
                pass
            else:
                cahce_neg[i] = -i
        elif i > 0:
            if i in cahce_pos:
                pass
            else:
                cahce_pos[i] = i
    for i in cahce_neg:
        if cahce_neg[i] in cahce_pos:
            result.append(cahce_neg[i])
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
