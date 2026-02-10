# ft_inventory_system.py

import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inv: dict[str, int] = dict()
    for token in args:
        parts = token.split(":")
        if len(parts) != 2:
            continue
        name = parts[0]
        try:
            qty = int(parts[1])
        except ValueError:
            continue
        if qty < 0:
            continue
        inv[name] = inv.get(name, 0) + qty
    return inv


def total_items(inv: dict[str, int]) -> int:
    total = 0
    for q in inv.values():
        total += q
    return total


def sorted_items_by_qty_desc(inv: dict[str, int]) -> str:
    # no sorted()/list(): repeated max selection
    used: dict[str, int] = dict()
    out = ""
    done = 0

    while done < len(inv):
        best_item = ""
        best_qty = -1

        for item, qty in inv.items():
            if used.get(item, 0) == 1:
                continue
            if qty > best_qty:
                best_item = item
                best_qty = qty

        if best_item == "":
            break

        used.update({best_item: 1})
        done += 1

        if out == "":
            out = best_item + ":" + str(best_qty)
        else:
            out = out + "," + best_item + ":" + str(best_qty)

    return out


def percent_1_decimal(qty: int, total: int) -> str:
    if total <= 0:
        return "0.0"
    tenths = (qty * 1000 + total // 2) // total  # percent * 10 (rounded)
    return (
        str(tenths // 10)
        + "."
        + str(tenths % 10)
    )


def most_and_least(
    inv: dict[str, int],
) -> tuple[str, int, str, int]:
    most_item = ""
    most_qty = -1
    least_item = ""
    least_qty = -1

    for item, qty in inv.items():
        if most_item == "" or qty > most_qty:
            most_item = item
            most_qty = qty
        if least_item == "" or qty < least_qty or least_qty == -1:
            least_item = item
            least_qty = qty

    return most_item, most_qty, least_item, least_qty


def categorize(
    inv: dict[str, int],
) -> tuple[dict[str, int], dict[str, int]]:
    moderate: dict[str, int] = dict()
    scarce: dict[str, int] = dict()
    for item, qty in inv.items():
        if qty >= 5:
            moderate.update({item: qty})
        else:
            scarce.update({item: qty})
    return moderate, scarce


def restock_list_str(inv: dict[str, int]) -> str:
    s = "["
    first = 1
    for item, qty in inv.items():
        if qty <= 1:
            if first:
                s += "'" + item + "'"
                first = 0
            else:
                s += ", '" + item + "'"
    s += "]"
    return s


def keys_list_str(inv: dict[str, int]) -> str:
    s = "["
    first = 1
    for k in inv.keys():
        if first:
            s += "'" + k + "'"
            first = 0
        else:
            s += ", '" + k + "'"
    s += "]"
    return s


def values_list_str(inv: dict[str, int]) -> str:
    s = "["
    first = 1
    for v in inv.values():
        if first:
            s += str(v)
            first = 0
        else:
            s += ", " + str(v)
    s += "]"
    return s


def main() -> None:
    inv = parse_inventory(sys.argv[1:])
    total = total_items(inv)

    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total)
    print("Unique item types:", len(inv))
    print()
    print("=== Current Inventory ===")
    order = sorted_items_by_qty_desc(inv)
    if order != "":
        for pair in order.split(","):
            item, _qty_str = pair.split(":")
            qty = inv.get(item, 0)
            pct = percent_1_decimal(qty, total)
            print(item + ":", qty, "units (" + pct + "%)")
    print()
    print("=== Inventory Statistics ===")
    most_item, most_qty, least_item, least_qty = most_and_least(inv)
    if most_item != "":
        print("Most abundant:", most_item, "(", most_qty, "units)", sep="")
        print("Least abundant:", least_item, "(", least_qty, "units)", sep="")
    else:
        print("Most abundant:  (0 units)")
        print("Least abundant:  (0 units)")
    print()
    print("=== Item Categories ===")
    moderate, scarce = categorize(inv)
    print("Moderate:", moderate)
    print("Scarce:", scarce)
    print()
    print("=== Management Suggestions ===")
    print("Restock needed:", restock_list_str(inv))
    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", keys_list_str(inv))
    print("Dictionary values:", values_list_str(inv))
    print(
        "Sample lookup - 'sword' in inventory:",
        inv.get("sword") is not None,
    )


if __name__ == "__main__":
    main()
