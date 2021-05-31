"""This script prints the first repeating item in the list."""


def first_repeating(first_list):
    """Loops through the list and looks for repeating items.

    :param first_list: list
    :return: first duplicate item
    """
    two_list = []
    repeating_list = []
    if not first_list:
        return "Your list is empty."
    else:
        for i in first_list:
            if i not in two_list:
                two_list.append(i)
            else:
                repeating_list.append(i)

    if not repeating_list:
        return "No repeating elements."
    else:
        return repeating_list[0]


if __name__ == '__main__':
    my_list = ['a', 'b', 'c', 'c']
    print(first_repeating(my_list))
