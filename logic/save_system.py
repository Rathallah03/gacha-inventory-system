# save_system.py — Save & Load Player Data

import json
import os

SAVE_DIR  = "save"
SAVE_FILE = os.path.join(SAVE_DIR, "player_data.json")

# ══════════════════════════════════════════
#  INIT
# ══════════════════════════════════════════

def init_save_dir():
    """Buat folder save/ kalau belum ada."""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)


# ══════════════════════════════════════════
#  SAVE
# ══════════════════════════════════════════

def save_game(player_name, primogem, inventory, pity_state, pull_history):
    """
    Simpan semua progress ke file JSON.

    Params:
        player_name  : str
        primogem     : int
        inventory    : list of dict (dari inventory.py)
        pity_state   : dict (dari gacha.py)
        pull_history : list of dict
    """
    init_save_dir()

    data = {
        "player_name":  player_name,
        "primogem":     primogem,
        "inventory":    inventory,
        "pity_state":   pity_state,
        "pull_history": pull_history,
    }

    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\n  ✔  Data berhasil disimpan ke '{SAVE_FILE}'")
        return True
    except Exception as e:
        print(f"\n  ✖  Gagal menyimpan data: {e}")
        return False


# ══════════════════════════════════════════
#  LOAD
# ══════════════════════════════════════════

def load_game():
    """
    Load progress dari file JSON.
    Returns: dict data player, atau None kalau file tidak ada.
    """
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"  ✔  Data berhasil dimuat untuk: {data.get('player_name', '???')}")
        return data
    except Exception as e:
        print(f"  ✖  Gagal memuat data: {e}")
        return None


# ══════════════════════════════════════════
#  EXPORT PULL HISTORY
# ══════════════════════════════════════════

def export_pull_history(pull_history, player_name="player"):
    """
    Export pull history ke file .txt yang readable.
    """
    init_save_dir()
    filename = os.path.join(SAVE_DIR, f"{player_name}_history.txt")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"=== Pull History — {player_name} ===\n")
            f.write(f"Total pulls: {len(pull_history)}\n")
            f.write("=" * 40 + "\n\n")

            for i, entry in enumerate(pull_history, 1):
                rarity = entry.get("rarity", "?")
                name   = entry.get("name", "Unknown")
                status = entry.get("status", "")   # "new" atau "duplicate"
                f.write(f"#{i:>4}  [{rarity:<3}]  {name:<22}  {status}\n")

        print(f"  ✔  Pull history diekspor ke '{filename}'")
        return True
    except Exception as e:
        print(f"  ✖  Gagal ekspor history: {e}")
        return False


# ══════════════════════════════════════════
#  CHECK SAVE EXISTS
# ══════════════════════════════════════════

def save_exists():
    return os.path.exists(SAVE_FILE)
