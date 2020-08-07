def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    intersect = {}
    num_of_arr = len(arrays)
    # print(num_of_arr)
    for i in range(0, len(arrays)):
        # print(i)
        # print("\n")
        for j in arrays[i]:
            if j in intersect:
                intersect[j] += 1
                # print(j)
                # print(intersect[j])
                # print("\n")
            else:
                intersect[j] = 1
    
    for i in intersect:
        # print(len(intersect[i]))
        if intersect[i] == num_of_arr:
            result.append(i)
            
    # print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
