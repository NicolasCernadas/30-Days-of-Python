import statistics
numbers = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

#(20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26)/(11) = average numebr
print(format(statistics.mean(numbers), ".3f")) #format(number, ".Xf")

#[4, 20, 20, 20, 22, 22, 23, 24, 25, 26, 26] sorted list, 22 is the number in the middle
print(statistics.median(numbers))

#returns the number that repeats the most
print(statistics.mode(numbers))
