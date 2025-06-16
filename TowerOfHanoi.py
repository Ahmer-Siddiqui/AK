def tower_of_hanoi(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary using target as auxiliary
    tower_of_hanoi(n - 1, source, aux, target)

    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move n-1 disks from auxiliary to target using source as auxiliary
    tower_of_hanoi(n - 1, aux, target, source)

n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')