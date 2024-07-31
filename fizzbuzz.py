# scope = range(1, 101)

# for num in scope:
#     if num % 3 == 0 and num % 5 == 0:
#         print('Fizzbuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else: print(num)

def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('Fizzbuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

def main():
    print(fizzbuzz(1, 100))





if __name__ == "__main__":
    main()



