def mean_median(array_input):
    mean = 1.0
    median = 1
    if not array_input:
        return None
    
    sorted_array = sorted (array_input)
    length = len(sorted_array)

    mean = sum(sorted_array) / length

    if length % 2 == 0 :
        median = (sorted_array[length // 2 - 1] + sorted_array[length // 2]) / 2

    else:
        median = sorted_array[length // 2]

    return (mean, median)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)