while True:
    side_1 = int(input("Enter a side: ")) ** 2
    side_2 = int(input("Enter another side: ")) ** 2
    side_3 = int(input("Enter another side: ")) ** 2

    statement = "\nThis is a pythagorean triple."
    not_statement = "\nThis is not a pythagorean triple."

    triangle = [side_1, side_2, side_3]
    hypotenuse = max(triangle)

    triangle.remove(hypotenuse)

    if sum(triangle) == hypotenuse:
        print(statement)
    else:
        print(not_statement)

    count = input("\nWould you like to go again?")
    if count.lower() == 'n'or count.lower()=='no':
        break
    elif count.lower() == 'y'or count.lower()=='yes':
        continue
    else:
        print("Please answer in yes - no OR y-n")
        break

print("\nGoodbye!")
