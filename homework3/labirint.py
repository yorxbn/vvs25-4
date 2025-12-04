import random

rooms = ["пусто", "сундук", "монстр", "ключ", "портал", "ловушка"]
equip = ["скороходы", "аптечка", "меч"]
N = 5
area = [[rooms[0] for _ in range(N)] for _ in range(N)]
visible = [[False for _ in range(N)] for _ in range(N)]
health = 10
pos = [0, 0]
inventory = []
has_key = False
visible[0][0] = True

objects_count = {"сундук": 3, "монстр": 1, "ключ": 1, "портал": 1, "ловушка": 2}
for obj_type, count in objects_count.items():
    for _ in range(count):
        while True:
            i, j = random.randint(0, N-1), random.randint(0, N-1)
            if area[i][j] == rooms[0] and (i, j) != (0, 0):
                area[i][j] = obj_type
                break
symbols = {"пусто": "_", "сундук": "S", "монстр": "M", "ключ": "K", "портал": "E", "ловушка": "_"}

def print_area():
    print(f"Здоровье: {health}, Инвентарь: {inventory}")
    for i in range(N):
        for j in range(N):
            if [i, j] == pos:
                print("*", end=" ")
            elif visible[i][j]:
                print(symbols[area[i][j]], end=" ")
            else:
                print("?", end=" ")
        print()
print_area()

while health > 0:
    move = input().upper()
    dx, dy = 0, 0
    if move == "W": dx = -1
    elif move == "S": dx = 1
    elif move == "A": dy = -1
    elif move == "D": dy = 1
    else:
        print("Используйте W/A/S/D")
        continue
    
    new_x, new_y = pos[0] + dx, pos[1] + dy
    if not (0 <= new_x < N and 0 <= new_y < N):
        print("Стена!")
        health -= 1
        print_area()
        continue
    
    pos = [new_x, new_y]
    visible[new_x][new_y] = True
    room = area[new_x][new_y]
    
    if room == "сундук":
        if equip:
            item = random.choice(equip)
            equip.remove(item)
            inventory.append(item)
            print(f"Нашли {item}!")
            if item == "аптечка":
                health += 5
                inventory.remove(item)
                print("+5 HP!")
            
            area[new_x][new_y] = "пусто"
    
    elif room == "монстр":
        if "меч" in inventory:
            print("Победили монстра мечом!")
            area[new_x][new_y] = "пусто"
        else:
            health -= 9
            print("Монстр атаковал!")
    elif room == "ключ":
        has_key = True
        inventory.append("ключ")
        area[new_x][new_y] = "пусто"
        print("Нашли ключ!")
    elif room == "портал":
        if has_key:
            print("Победа! Вышли через портал.")
            break
        else:
            print("Нужен ключ!")
    elif room == "ловушка":
        health -= 5
        area[new_x][new_y] = "пусто"
        print("Ловушка! -5 HP")
    elif room == "пусто":
        print("Пустая комната")
    print_area()

if health <= 0:
    print("Вы проиграли!")
