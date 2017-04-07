from stack import Stack

tower = Stack()

def move_tower(height, from_pole, to_pole, with_pole):
    while height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height -1, with_pole, to_pole, from_pole)
        tower.push(move_tower)

def move_disk(fp, tp):
    print("moving disk from", fp, "to", tp)


(move_tower(3, "A", "B", "C"))
