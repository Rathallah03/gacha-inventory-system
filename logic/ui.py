# ui.py — Animasi, Display, Terminal UI

import time
import os
import sys

PRIMOGEM_PER_PULL = 160


# ══════════════════════════════════════════
#  UTILITIES
# ══════════════════════════════════════════

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.03):
    """Print teks karakter per karakter (efek typewriter)."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def divider(char="═", width=52):
    print("  " + char * width)

def pause(msg="  Tekan Enter untuk melanjutkan..."):
    input(msg)


# ══════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════

def print_header(primogem, pity_counter, is_guaranteed):
    clear()
    rate_status = "✦ RATE ON" if is_guaranteed else "◆ Rate OFF"
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║          ✨  GACHA INVENTORY SIMULATOR  ✨           ║")
    print("  ╠══════════════════════════════════════════════════════╣")
    print(f"  ║  💎 Primogem : {primogem:<8}  🎯 Pity : {pity_counter:>2}/90   {rate_status:<12}║")
    print("  ╚══════════════════════════════════════════════════════╝")


# ══════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════

def print_menu():
    print()
    print("  ┌─────────────────────────────┐")
    print("  │         MAIN MENU           │")
    print("  ├─────────────────────────────┤")
    print("  │  1. Pull 1x   (160 💎)      │")
    print("  │  2. Pull 10x  (1600 💎)     │")
    print("  │  3. Inventory               │")
    print("  │  4. Search Item             │")
    print("  │  5. Sort Inventory          │")
    print("  │  6. Profile                 │")
    print("  │  7. Save Data               │")
    print("  │  8. Exit                    │")
    print("  └─────────────────────────────┘")
    print()


# ══════════════════════════════════════════
#  SPINNER ANIMASI
# ══════════════════════════════════════════

def spinner(duration=1.5, message="Melakukan pull"):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r  {frames[i % len(frames)]}  {message}...")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()


# ══════════════════════════════════════════
#  ANIMASI HASIL PULL (SINGLE)
# ══════════════════════════════════════════

def animate_single_pull(character):
    rarity = character["rarity"]
    name   = character["name"]
    elem   = character["element"]

    spinner(duration=1.2 if rarity == "SSR" else 0.7)

    if rarity == "SSR":
        # Flash effect
        for _ in range(3):
            clear()
            print("\n" * 4)
            print("       ✦  ✦  ✦  ✦  ✦  ✦  ✦")
            print("     ✦                       ✦")
            print("     ✦    ✨  G O L D E N  ✨  ✦")
            print("     ✦                       ✦")
            print("       ✦  ✦  ✦  ✦  ✦  ✦  ✦")
            time.sleep(0.18)
            clear()
            time.sleep(0.12)

        print("\n")
        divider("★")
        slow_print(f"  ✨✨  SSR OBTAINED!  ✨✨", delay=0.05)
        divider("★")
        print(f"\n  ★★★  {name}")
        print(f"       {elem}  |  {character['weapon']}  |  {character['region']}")
        divider("─")

    elif rarity == "SR":
        print()
        divider("─")
        print(f"  ★★   SR — {name}")
        print(f"       {elem}  |  {character['weapon']}  |  {character['region']}")
        divider("─")

    else:
        print()
        print(f"  ★    R  — {name}")
        print(f"       {elem}  |  {character['weapon']}")


# ══════════════════════════════════════════
#  ANIMASI HASIL PULL (10x)
# ══════════════════════════════════════════

def animate_multi_pull(results):
    """
    results: list of (character_dict, status)
    status: "new" atau "duplicate"
    """
    clear()
    spinner(duration=1.8, message="Melakukan 10x pull")
    clear()

    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║           ✨  10x PULL RESULT  ✨        ║")
    print("  ╚══════════════════════════════════════════╝\n")

    ssr_count = 0
    sr_count  = 0
    r_count   = 0

    for i, (char, status) in enumerate(results, 1):
        rarity = char["rarity"]
        name   = char["name"]
        dup    = " (duplikat)" if status == "duplicate" else ""

        if rarity == "SSR":
            ssr_count += 1
            time.sleep(0.6)
            print(f"  Pull #{i:>2}  >>>  ✨ ★★★  {name}{dup}  ✨  <<<")
        elif rarity == "SR":
            sr_count += 1
            time.sleep(0.25)
            print(f"  Pull #{i:>2}  >>>  ★★   {name}{dup}")
        else:
            r_count += 1
            time.sleep(0.15)
            print(f"  Pull #{i:>2}  >>>  ★    {name}{dup}")

    print()
    divider("─")
    print(f"  Ringkasan: ✨ SSR x{ssr_count}  |  ★★ SR x{sr_count}  |  ★ R x{r_count}")
    divider("─")


# ══════════════════════════════════════════
#  SORT MENU
# ══════════════════════════════════════════

def print_sort_menu():
    print()
    print("  Sort inventory berdasarkan:")
    print("  1. Rarity (SSR → R)")
    print("  2. Nama (A-Z)")
    print("  3. Konstellasi (terbanyak)")
    print("  4. Elemen (A-Z)")
    print("  0. Kembali")
    print()


# ══════════════════════════════════════════
#  SEARCH MENU
# ══════════════════════════════════════════

def print_search_menu():
    print()
    print("  Cari berdasarkan:")
    print("  1. Nama karakter")
    print("  2. Elemen")
    print("  3. Rarity (SSR/SR/R)")
    print("  0. Kembali")
    print()


# ══════════════════════════════════════════
#  PROFILE DISPLAY
# ══════════════════════════════════════════

def print_profile(player_name, primogem, total_pulls, pity_state, inventory):
    from data import RARITY_RANK

    clear()
    ssr_count = sum(1 for i in inventory if i["rarity"] == "SSR")
    sr_count  = sum(1 for i in inventory if i["rarity"] == "SR")
    r_count   = sum(1 for i in inventory if i["rarity"] == "R")
    rate_str  = "✦ RATE ON (guaranteed)" if pity_state["is_guaranteed"] else "◆ Rate OFF (50/50)"

    print()
    divider("═")
    print(f"  👤  {player_name}")
    divider("─")
    print(f"  💎  Primogem     : {primogem}")
    print(f"  🎯  Pity Counter : {pity_state['pity_counter']}/90")
    print(f"  🔄  SR Pity      : {pity_state['sr_pity']}/10")
    print(f"  ⚖️   Status 50/50 : {rate_str}")
    divider("─")
    print(f"  📊  Total Pulls  : {total_pulls}")
    print(f"  🗂️   Inventory    : {len(inventory)} karakter")
    print(f"       ✨ SSR: {ssr_count}  |  ★★ SR: {sr_count}  |  ★ R: {r_count}")
    divider("═")
