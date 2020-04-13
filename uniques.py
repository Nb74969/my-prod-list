def find_non_duplicates(list_of_int):
    """find uniques."""
    new_list = []
    for i in  list_of_int:
        count =  list_of_int.count(i)
        if count == 1:
            new_list.append(i)
    return(new_list)


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 3, 2, 4, 11]
    non_duplicate = find_non_duplicates(list1)
    print(non_duplicate)