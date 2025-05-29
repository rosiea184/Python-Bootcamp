def sum_of_squares(num):
    sum = 0
    try:
        num = int(num)
        if num < 1:
            return "Invalid Negative Number"
        else:
            for i in range(1,num+1):
                sum += i*i
        return sum
    except ValueError:
        return "That is not a valid number!"    


print(sum_of_squares(6))
print(sum_of_squares(-1))
print(sum_of_squares("g"))