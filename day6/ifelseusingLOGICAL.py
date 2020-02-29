numbers = list(range(11))

if not(len(numbers) == 10 or len(numbers) == 11 and numbers[0]%2 == 0):
    print(True)
else:
    print(False)
