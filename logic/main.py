# main.py — Entry Point & Main Game Loop


import sys
import gacha
import inventory
import save_system
import ui
from data import RARITY_DISPLAY

PRIMOGEM_PER_PULL    = 160
PRIMOGEM_PER_TEN     = 1600
STARTING_PRIMOGEM    = 6400  # 40 pulls buat demo

# ══════════════════════════════════════════
#  PLAYER STATE
# ══════════════════════════════════════════

player_name  = "Traveler"
primogem     = STARTING_PRIMOGEM
total_pulls  = 0
pull_history = []


# ══════════════════════════════════════════
#  STARTUP — NEW GAME / LOAD SAVE
# ══════════════════════════════════════════

def startup():
    global player_name, primogem, total_pulls, pull_history

    ui.clear()
    print()
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║          ✨  GACHA INVENTORY SIMULATOR  ✨           ║")
    print("  ║              Genshin-inspired Edition               ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print()

    if save_system.save_exists():
        print("  Save file ditemukan!")
        choice = input("  Load save? (y/n): ").strip().lower()
        if choice == "y":
            data = save_system.load_game()
            if data:
                player_name  = data.get("player_name",  player_name)
                primogem     = data.get("primogem",     primogem)
                total_pulls  = data.get("total_pulls",  0)
                pull_history = data.get("pull_history", [])
                inventory.set_inventory(data.get("inventory", []))
                gacha.set_pity_state(data.get("pity_state", {}))
                ui.pause()
                return

    # New game
    print()
    name = input("  Masukkan nama Traveler kamu: ").strip()
    player_name = name if name else "Traveler"
    print(f"\n  Selamat datang, {player_name}!")
    print(f"  Kamu memulai dengan {STARTING_PRIMOGEM} 💎 Primogem.")
    ui.pause()


# ══════════════════════════════════════════
#  PULL 1x
# ══════════════════════════════════════════

def handle_pull_one():
    global primogem, total_pulls

    pity_state = gacha.get_pity_state()
    ui.print_header(primogem, pity_state["pity_counter"], pity_state["is_guaranteed"])

    if primogem < PRIMOGEM_PER_PULL:
        print(f"\n  ✖  Primogem tidak cukup! (butuh {PRIMOGEM_PER_PULL} 💎)")
        ui.pause()
        return

    confirm = input(f"\n  Pull 1x seharga {PRIMOGEM_PER_PULL} 💎? (y/n): ").strip().lower()
    if confirm != "y":
        return

    primogem    -= PRIMOGEM_PER_PULL
    total_pulls += 1

    char   = gacha.pull_once()
    status = inventory.add_character(char)

    # Simpan ke history
    pull_history.append({
        "name":   char["name"],
        "rarity": char["rarity"],
        "status": status,
    })

    ui.animate_single_pull(char)

    if status == "duplicate":
        cons = inventory.search_by_name(char["name"])[0]["count"] - 1
        print(f"\n  (Sudah punya → Konstellasi C{cons})")

    pity_state = gacha.get_pity_state()
    print(f"\n  💎 Sisa Primogem: {primogem}  |  Pity: {pity_state['pity_counter']}/90")
    ui.pause()


# ══════════════════════════════════════════
#  PULL 10x
# ══════════════════════════════════════════

def handle_pull_ten():
    global primogem, total_pulls

    pity_state = gacha.get_pity_state()
    ui.print_header(primogem, pity_state["pity_counter"], pity_state["is_guaranteed"])

    if primogem < PRIMOGEM_PER_TEN:
        print(f"\n  ✖  Primogem tidak cukup! (butuh {PRIMOGEM_PER_TEN} 💎)")
        ui.pause()
        return

    confirm = input(f"\n  Pull 10x seharga {PRIMOGEM_PER_TEN} 💎? (y/n): ").strip().lower()
    if confirm != "y":
        return

    primogem    -= PRIMOGEM_PER_TEN
    total_pulls += 10

    chars   = gacha.pull_ten()
    results = inventory.add_characters_bulk(chars)

    # Simpan ke history
    for char, status in results:
        pull_history.append({
            "name":   char["name"],
            "rarity": char["rarity"],
            "status": status,
        })

    ui.animate_multi_pull(results)

    pity_state = gacha.get_pity_state()
    print(f"\n  💎 Sisa Primogem: {primogem}  |  Pity: {pity_state['pity_counter']}/90")
    ui.pause()


# ══════════════════════════════════════════
#  INVENTORY
# ══════════════════════════════════════════

def handle_inventory():
    pity_state = gacha.get_pity_state()
    ui.print_header(primogem, pity_state["pity_counter"], pity_state["is_guaranteed"])
    print("\n  ─── INVENTORY ───\n")
    inventory.display_inventory()
    print()
    ui.pause()


# ══════════════════════════════════════════
#  SEARCH
# ══════════════════════════════════════════

def handle_search():
    while True:
        pity_state = gacha.get_pity_state()
        ui.print_header(primogem, pity_state["pity_counter"], pity_state["is_guaranteed"])
        print("\n  ─── SEARCH ITEM ───")
        ui.print_search_menu()

        choice = input("  Pilih (0-3): ").strip()

        if choice == "0":
            break

        elif choice == "1":
            query   = input("  Nama karakter: ").strip()
            results = inventory.search_by_name(query)
            print(f"\n  Hasil pencarian '{query}':")
            inventory.display_inventory(results)
            ui.pause()

        elif choice == "2":
            print("  Elemen: Pyro / Hydro / Anemo / Electro / Dendro / Cryo / Geo")
            elem    = input("  Elemen: ").strip()
            results = inventory.search_by_element(elem)
            print(f"\n  Karakter elemen {elem}:")
            inventory.display_inventory(results)
            ui.pause()

        elif choice == "3":
            rarity  = input("  Rarity (SSR/SR/R): ").strip()
            results = inventory.search_by_rarity(rarity)
            print(f"\n  Karakter rarity {rarity.upper()}:")
            inventory.display_inventory(results)
            ui.pause()

        else:
            print("  Pilihan tidak valid.")
            ui.pause()


# ══════════════════════════════════════════
#  SORT
# ══════════════════════════════════════════

def handle_sort():
    while True:
        pity_state = gacha.get_pity_state()
        ui.print_header(primogem, pity_state["pity_counter"], pity_state["is_guaranteed"])
        print("\n  ─── SORT INVENTORY ───")
        ui.print_sort_menu()

        choice = input("  Pilih (0-4): ").strip()

        if choice == "0":
            break

        elif choice == "1":
            inventory.sort_by_rarity()
            print("\n  ✔  Sorted by Rarity (SSR → R)")
            inventory.display_inventory()
            ui.pause()

        elif choice == "2":
            inventory.sort_by_name()
            print("\n  ✔  Sorted by Name (A-Z)")
            inventory.display_inventory()
            ui.pause()

        elif choice == "3":
            inventory.sort_by_count()
            print("\n  ✔  Sorted by Konstellasi (terbanyak)")
            inventory.display_inventory()
            ui.pause()

        elif choice == "4":
            inventory.sort_by_element()
            print("\n  ✔  Sorted by Element (A-Z)")
            inventory.display_inventory()
            ui.pause()

        else:
            print("  Pilihan tidak valid.")
            ui.pause()


# ══════════════════════════════════════════
#  PROFILE
# ══════════════════════════════════════════

def handle_profile():
    pity_state = gacha.get_pity_state()
    ui.print_profile(
        player_name  = player_name,
        primogem     = primogem,
        total_pulls  = total_pulls,
        pity_state   = pity_state,
        inventory    = inventory.get_inventory(),
    )

    print()
    export = input("  Export pull history ke .txt? (y/n): ").strip().lower()
    if export == "y":
        save_system.export_pull_history(pull_history, player_name)

    ui.pause()


# ══════════════════════════════════════════
#  SAVE
# ══════════════════════════════════════════

def handle_save():
    pity_state = gacha.get_pity_state()
    save_system.save_game(
        player_name  = player_name,
        primogem     = primogem,
        inventory    = inventory.get_inventory(),
        pity_state   = pity_state,
        pull_history = pull_history,
    )
    ui.pause()


# ══════════════════════════════════════════
#  MAIN LOOP
# ══════════════════════════════════════════

def main():
    startup()

    while True:
        pity_state = gacha.get_pity_state()
        ui.print_header(primogem, pity_state["pity_counter"], pity_state["is_guaranteed"])
        ui.print_menu()

        choice = input("  Pilih menu (1-8): ").strip()

        if   choice == "1": handle_pull_one()
        elif choice == "2": handle_pull_ten()
        elif choice == "3": handle_inventory()
        elif choice == "4": handle_search()
        elif choice == "5": handle_sort()
        elif choice == "6": handle_profile()
        elif choice == "7": handle_save()
        elif choice == "8":
            print("\n  Sampai jumpa, Traveler! 🌟\n")
            sys.exit(0)
        else:
            print("  Pilihan tidak valid. Coba lagi.")
            ui.pause()


if __name__ == "__main__":
    main()
