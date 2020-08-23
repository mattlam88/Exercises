# Write your solution here
def tower_of_hanoi(n , from_rod, to_rod, aux_rod):
    if n > 0:
        tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
        while len(from_rod) > 0:
            to_rod.append(from_rod.pop())
        
        return tower_of_hanoi(n-1, to_rod,aux_rod, from_rod)


# from_rod = [1,2,3]
# to_rod = []
# aux_rod = []
# tower_of_hanoi(len(from_rod),from_rod,to_rod,aux_rod)

# print(from_rod, to_rod, aux_rod)