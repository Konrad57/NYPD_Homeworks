# Exercise 1
print("Exercise 1")


def create_phone_book():
    return {}


def insert_number(phone_book, name, number):
    if name in phone_book:
        phone_book[name].append(number)
    else:
        phone_book[name] = [number]


def retrieve_number(phone_book, name):
    if name in phone_book:
        return phone_book[name][0]  # Return any number for the indicated person, it is not specified which one or
        # whether user should say which one
    else:
        return None


def delete_number(phone_book, name, number):
    if name in phone_book:
        if number in phone_book[name]:
            phone_book[name].remove(number)
            if len(phone_book[name]) == 0:  # Let's delete also a person from the book when she has no number assigned
                del phone_book[name]


def print_phone_book(phone_book):
    for name, numbers in phone_book.items():
        print(f"{name}: {', '.join(numbers)}")


# Testing the phone book
phone_book = create_phone_book()

# Inserting numbers
insert_number(phone_book, "Ala Wesołowska", "+048 513 056 121")
insert_number(phone_book, "Ala Wesołowska", "22-848-34-21")
insert_number(phone_book, "John Smith", "469-452-199")
insert_number(phone_book, "John Smith", "0800 241 6331")
insert_number(phone_book, "Susan Brown", "315-728-3639")

# Retrieving a number
print("Number for John Smith:", retrieve_number(phone_book, "John Smith"))

# Deleting a number
delete_number(phone_book, "John Smith", "469-452-199")

# Printing the phone book
print("\nPhone Book:")
print_phone_book(phone_book)

# Exercise 2
print()
print("Exercise 2 \n")

phone_book["Ala Wesołowska"] = ["+048 513 056 121", "22-848-34-21"]

# I used a string representation in the original solution so it is not changing anything

phone_book[("Ala", "Wesołowska")] = ["+048 513 056 121", "22-848-34-21"]


# The tuple seems to work as well but probably this would require different approach to printing the phone book
# However, tuple (also as list) in most cases would be more desired due to the fact that they are more flexible and
# easy to work with than strings

# phone_book[["Ala", "Wesołowska"]] = ["+048 513 056 121", "22-848-34-21"]

# The list is not working because it can not function as a value in the python dict raising an 'not hashable type' error


def create_phone_book2():
    return {}


# b) To use labeling of the phone numbers I am using the dict as a value in the phone_book dict.

# c) No, the current structure allows inserting the same phone number several times for one person.
# To prevent this from happening, we can check if the phone number already exists in the list before inserting it.

# d) Yes, the current structure allows inserting the same phone number several times, maybe for different people.
# To prevent this from happening, we could use a set to store unique phone numbers and associate each phone number
# with a list of people.


def insert_number2(phone_book, name, label, number):
    if name in phone_book:
        if label in phone_book[name]:
            phone_book[name][label].append(number)
        else:
            phone_book[name][label] = [number]
    else:
        phone_book[name] = {label: [number]}


def retrieve_number2(phone_book, name):
    if name in phone_book:
        return phone_book[name]


def delete_number2(phone_book, name, label, number):
    if name in phone_book:
        if label in phone_book[name]:
            if number in phone_book[name][label]:
                phone_book[name][label].remove(number)
                if len(phone_book[name][label]) == 0:
                    del phone_book[name][label]
                    if len(phone_book[name]) == 0:
                        del phone_book[name]


def print_phone_book2(phone_book):
    for name, labels_numbers in phone_book.items():
        print(name + ":", end=" ")
        for label, numbers in labels_numbers.items():
            print(label + ":", end=" ")
            print(", ".join(numbers), end="; ")
        print()


# Testing the phone book
phone_book = create_phone_book2()

# Inserting numbers
insert_number2(phone_book, "Ala Wesołowska", "main", "+048 513 056 121")
insert_number2(phone_book, "Ala Wesołowska", "home", "22-848-34-21")
insert_number2(phone_book, "John Smith", "main", "0800 241 6331")
insert_number2(phone_book, "John Smith", "work", "469-452-199")
insert_number2(phone_book, "Susan Brown", "work", "315-728-3639")

# Retrieving numbers
print("Numbers for John Smith:", retrieve_number2(phone_book, "John Smith"))

# Deleting a number
delete_number2(phone_book, "John Smith", "work", "469-452-199")

# Printing the phone book
print("\nPhone Book:")
print_phone_book2(phone_book)

# Exercise 3
print("Exercise 3")


# I will use the list

def eratosthenes_sieve(n):
    primes = []
    sieve = [True] * (n + 1)
    # print(sieve)

    for num in range(2, n + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                sieve[multiple] = False

    # print(sieve)
    return primes


# Testing the algorithm
n = 11
print(f"Primes up to {n}: {eratosthenes_sieve(n)}")


# Exercise 4
print("Exercise 4")

def pos(word, text):
    for i in range(0, len(text)):
        if text[i] == word[0]:
            test_string = ""
            for j in range(i, i + 2*len(word), 2):
                test_string += text[j]
                # print(test_string)
            if test_string == word:
                return i

    return -1


print(f"pos('a', '') == {pos("a", "")}")
print(f"pos('hsal', 'Mary has a little lamb') == {pos("hsal", "Mary has a little lamb")}")
print(pos("dil", "godzilla minus one"))

# Exercise 5
def sublist(lst1, lst2):
    if not lst1:
        return True

    if not lst2:
        return False

    index = 0
    for item in lst2:
        if item == lst1[index]:
            index += 1
            if index == len(lst1):
                return True

    return False


# Test cases
print(sublist([], []))  # Output: True
print(sublist([], [1, 2, 3]))  # Output: True
print(sublist([2], [1, 2, 3]))  # Output: True
print(sublist([1, 3, 4], [1, 2, 3, 4, 5]))  # Output: True
print(sublist([1, 4, 3], [1, 2, 3, 4, 5]))  # Output: False
