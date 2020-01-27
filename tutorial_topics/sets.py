def set_print(some_set):
    for se in some_set: print(se, end=' ')


def compare_sets(set_1, set_2):
    subset_res = set_1 <= set_2
    superset_res = set_1 >= set_2
    if subset_res and superset_res:
        print("First and Second are equal")
        return
    if subset_res:
        print("First is a SubSet of Second")
        return
    if superset_res:
        print("Second is a SubSet of First")
        return
    print("Neither of those sets is a subset of the other.")
    return


""" 0. Creating a set """
months = set(["Jan", "Feb", "Mar"])
weekdays = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
dates = {21, 22, 27, 12, 6}

print("\n\nSet of months:\t\t", months)
print("Set of weekdays:\t", weekdays)
print("Set of dates:\t\t", dates)

""" 1. Accessing values in a Set """
print("\nWeekdays: ", end='')
set_print(weekdays)

""" 2. Adding elements to the set """
print("\n\nBEFORE Adding: ", end='')
set_print(weekdays)
weekdays.add("All")
print("\nAFTER Adding: ", end='')
set_print(weekdays)

""" 3. Removing elements from the set """
print("\n\nBEFORE Removing: ", end='')
set_print(weekdays)
weekdays.discard("All")
print("\nAFTER Removing: ", end='')
set_print(weekdays)

""" ---- ---- ---- ---- ---- ---- """
weekdays_a = {'Mon', 'Thu', 'Sun', 'Fri'}
weekdays_b = {'Sun', 'Fri', 'Tue', 'Wed', 'Sat'}

""" 4. Union of Sets """
print("\n\nFirst set: ", end='')
set_print(weekdays_a)
print("\nSecond set: ", end='')
set_print(weekdays_b)
print("\nUNION of Sets: ", end='')
weekdays_union = weekdays_a | weekdays_b
set_print(weekdays_union)

""" 5. Intersection of Sets """
print("\n\nFirst set: ", end='')
set_print(weekdays_a)
print("\nSecond set: ", end='')
set_print(weekdays_b)
print("\nINTERSECTION of Sets: ", end='')
weekdays_intersection = weekdays_a & weekdays_b
set_print(weekdays_intersection)

""" 6. Difference of Sets """
print("\n\nFirst set: ", end='')
set_print(weekdays_a)
print("\nSecond set: ", end='')
set_print(weekdays_b)
weekdays_diff_ab = weekdays_a - weekdays_b
weekdays_diff_ba = weekdays_b - weekdays_a
print("\nDIFFERENCE of <a> and <b> : ", end='')
set_print(weekdays_diff_ab)
print("\nDIFFERENCE of <a> and <b> : ", end='')
set_print(weekdays_diff_ba)

""" 7. Compare Sets """
print("\n\n\t\t___ The first way ___")
print("First set: ", end='')
set_print(weekdays_a)
print("\nSecond set: ", end='')
set_print(weekdays_b)
print()
compare_sets(weekdays_a, weekdays_b)

print("\t\t___ The second way ___")
someset_1 = {1, 2, 5, 7, 11}
someset_2 = {1, 2}
print("First set: ", end='')
set_print(someset_1)
print("\nSecond set: ", end='')
set_print(someset_2)
print()
compare_sets(someset_1, someset_2)
