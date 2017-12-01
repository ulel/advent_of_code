def main():
    
    with open('input') as input_file:
        puzzle_input = input_file.readline()

    first = puzzle_input[1]
    current = ''

    total = 0

    for i in puzzle_input.strip():
        if i == current:
            total += int(i)
        current = i

    if current == first:
        total += int(current)

    print(total)


if __name__ == '__main__':
    main()
