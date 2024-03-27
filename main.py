

def main():
    result = []

    numbers = list(map(int, (input().split())))
    start = 0
    end = -1
    
    for i in range(len(numbers)//2):
        result.append(numbers[start] + numbers[end])
        start +=1
        end -= 1
    """
    ########################################
    Code Your Program here
    ########################################
    """
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
