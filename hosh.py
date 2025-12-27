from heapq import heappop, heappush

# تعریف گراف اولیه
city_map = {
    'Home': {'School': 10, 'Market': 15, 'Hospital': 20},
    'School': {'Home': 10, 'Library': 5},
    'Market': {'Home': 15, 'Hospital': 25},
    'Hospital': {'Home': 20, 'Market': 25, 'Library': 10},
    'Library': {'School': 5, 'Hospital': 10}
}

# تابع برای تغییر هزینه‌ها به صورت پویا
def update_costs(city_map, factor):
    for node, neighbors in city_map.items():
        for neighbor, weight in neighbors.items():
            # افزایش یا کاهش هزینه‌ها بر اساس فاکتور
            city_map[node][neighbor] = max(1, weight + factor)  # هزینه‌ها حداقل 1 باشند

# UCS: یافتن مسیر کم‌هزینه
def ucs(city_map, start, goal):
    priority_queue = [(0, start, [start])]  # (هزینه، گره فعلی، مسیر طی‌شده)
    visited = set()

    while priority_queue:
        (cost, node, path) = heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return (cost, path)

        for neighbor, weight in city_map[node].items():
            if neighbor not in visited:
                heappush(priority_queue, (cost + weight, neighbor, path + [neighbor]))

    return None

# اجرای کد با گراف پویا
start, goal = 'Home', 'Library'
factor = 5  # تغییر هزینه‌ها
update_costs(city_map, factor)  # به‌روزرسانی هزینه‌ها
result = ucs(city_map, start, goal)

if result:
    cost, path = result
    print(f"کم‌هزینه‌ترین مسیر از {start} به {goal}: {path} با هزینه {cost}")
else:
    print(f"مسیر از {start} به {goal} یافت نشد.")
