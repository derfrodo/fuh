"""Abschrift aus Skript."""

def main():
    '''Das was im Skript steht'''
    numbers = [1, 2, 3, 4, 5, 6, 7]
    sigma = [0, 4, 7, 6, 1, 2, 3, 5]
    for num in numbers:
        print
        current = num
        print current,
        while sigma[current] != num:
            current = sigma[current]
            print current,
            numbers.remove(current)

if __name__ == '__main__':
    main()
