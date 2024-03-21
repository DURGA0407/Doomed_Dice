def undoom_dice(Die_A, Die_B):
    filtered_Die_A = [val for val in Die_A if val <= 4]
    New_Die_A = filtered_Die_A
    New_Die_B = Die_B[:len(Die_B)] + [0] * (len(filtered_Die_A) - len(Die_B))

    return New_Die_A, New_Die_B

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
