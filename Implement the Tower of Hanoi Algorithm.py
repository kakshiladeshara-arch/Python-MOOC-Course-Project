def hanoi_solver(n):
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []

    moves = []

    def record_state():
        moves.append(f"{rod1} {rod2} {rod3}")

    def move_disks(n, source, auxiliary, target):
        if n == 1:
            target.append(source.pop())
            record_state()
            return

        move_disks(n - 1, source, target, auxiliary)

        target.append(source.pop())
        record_state()

        move_disks(n - 1, auxiliary, source, target)

    record_state()
    move_disks(n, rod1, rod2, rod3)

    return "\n".join(moves)
