# inventory.py — Inventory Management, Sort, Search

from data import RARITY_RANK, ELEMENT_COLORS, RARITY_DISPLAY

# ══════════════════════════════════════════
#  INVENTORY STATE
#  Format list of dict:
#  { name, rarity, element, weapon, region, count }
# ══════════════════════════════════════════

inventory = []

# ══════════════════════════════════════════
#  ADD CHARACTER
# ══════════════════════════════════════════

def add_character(character):
    """
    Tambah karakter ke inventory.
    Kalau sudah ada → tambah count (konstellasi/eidolon).
    """
    for item in inventory:
        if item["name"] == character["name"]:
            item["count"] += 1
            return "duplicate"   # sudah punya, nambah konstellasi

    new_entry = dict(character)
    new_entry["count"] = 1
    inventory.append(new_entry)
    return "new"                 # karakter baru


def add_characters_bulk(characters):
    """Tambah list karakter sekaligus (untuk 10x pull)."""
    results = []
    for char in characters:
        status = add_character(char)
        results.append((char, status))
    return results


# ══════════════════════════════════════════
#  SEARCHING
# ══════════════════════════════════════════

def search_by_name(query):
    """
    Cari karakter di inventory berdasarkan nama (partial, case-insensitive).
    Returns: list of matching characters
    """
    query = query.lower().strip()
    results = [item for item in inventory if query in item["name"].lower()]
    return results


def search_by_element(element):
    """Filter inventory berdasarkan elemen."""
    element = element.capitalize()
    return [item for item in inventory if item["element"] == element]


def search_by_rarity(rarity):
    """Filter inventory berdasarkan rarity (SSR/SR/R)."""
    rarity = rarity.upper()
    return [item for item in inventory if item["rarity"] == rarity]


# ══════════════════════════════════════════
#  SORTING
# ══════════════════════════════════════════

def sort_by_rarity(descending=True):
    """Sort inventory berdasarkan rarity (SSR dulu)."""
    inventory.sort(
        key=lambda x: RARITY_RANK[x["rarity"]],
        reverse=descending
    )

def sort_by_name():
    """Sort inventory A-Z berdasarkan nama."""
    inventory.sort(key=lambda x: x["name"].lower())

def sort_by_count(descending=True):
    """Sort berdasarkan jumlah duplikat (konstellasi terbanyak dulu)."""
    inventory.sort(key=lambda x: x["count"], reverse=descending)

def sort_by_element():
    """Sort berdasarkan elemen (alphabetical)."""
    inventory.sort(key=lambda x: x["element"])


# ══════════════════════════════════════════
#  DISPLAY HELPERS
# ══════════════════════════════════════════

def format_character(item, index=None):
    """Format satu baris karakter untuk ditampilkan di terminal."""
    elem_icon = ELEMENT_COLORS.get(item["element"], "⬜")
    rarity    = RARITY_DISPLAY.get(item["rarity"], item["rarity"])
    cons      = f"C{item['count'] - 1}" if item["count"] > 1 else "C0"
    prefix    = f"{index:>3}. " if index is not None else "  "

    return (
        f"{prefix}{elem_icon} {item['name']:<20} "
        f"{rarity:<10} {item['weapon']:<10} "
        f"{item['region']:<12} [{cons}]"
    )

def display_inventory(chars=None):
    """
    Tampilkan inventory ke terminal.
    Params: chars — list karakter (default: semua inventory)
    """
    chars = chars if chars is not None else inventory

    if not chars:
        print("  [ Inventory kosong ]")
        return

    print(f"\n  {'#':<4} {'  Name':<22} {'Rarity':<10} {'Weapon':<10} {'Region':<12} [Const]")
    print("  " + "─" * 70)
    for i, item in enumerate(chars, 1):
        print(format_character(item, index=i))
    print(f"\n  Total: {len(chars)} karakter")


# ══════════════════════════════════════════
#  GETTER/SETTER — untuk save/load
# ══════════════════════════════════════════

def get_inventory():
    return inventory

def set_inventory(data):
    global inventory
    inventory.clear()
    inventory.extend(data)
