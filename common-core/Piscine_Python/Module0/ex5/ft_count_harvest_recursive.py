def ft_count_harvest_recursive(current_day=1, total_days=None):
    if total_days is None:
        total_days = int(input("Days until harvest: "))

    if current_day > total_days:
        print("Harvest time!")
        return

    print(f"Day {current_day}")
    ft_count_harvest_recursive(current_day + 1, total_days)
