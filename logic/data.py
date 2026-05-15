# data.py — Character Database

# ══════════════════════════════════════════
#  CHARACTER POOL
#  Format: { "name", "rarity", "element", "weapon", "region" }
# ══════════════════════════════════════════

FEATURED_SSR = {
    "name": "SEA CHAN",
    "rarity": "SSR",
    "element": "Aqua",
    "weapon": "Data-Blade",
    "region": "Mondstadt",
}

STANDARD_SSR_POOL = [
    {"name": "Lyra Stellan",   "rarity": "SSR", "element": "Pyro",    "weapon": "Catalyst", "region": "Liyue"},
    {"name": "Kaelith Frost",  "rarity": "SSR", "element": "Cryo",    "weapon": "Bow",      "region": "Inazuma"},
    {"name": "Dravon Ashveil", "rarity": "SSR", "element": "Geo",     "weapon": "Claymore", "region": "Sumeru"},
    {"name": "Mirelle Dusk",   "rarity": "SSR", "element": "Hydro",   "weapon": "Sword",    "region": "Fontaine"},
    {"name": "Zephyr Cinder",  "rarity": "SSR", "element": "Electro", "weapon": "Polearm",  "region": "Natlan"},
]

SR_POOL = [
    {"name": "Soren Brightwell", "rarity": "SR", "element": "Pyro",    "weapon": "Sword",    "region": "Mondstadt"},
    {"name": "Nielle Vane",      "rarity": "SR", "element": "Hydro",   "weapon": "Catalyst", "region": "Liyue"},
    {"name": "Corvin Ashe",      "rarity": "SR", "element": "Cryo",    "weapon": "Bow",      "region": "Inazuma"},
    {"name": "Tessa Goldenleaf", "rarity": "SR", "element": "Dendro",  "weapon": "Polearm",  "region": "Sumeru"},
    {"name": "Aldric Emberveil", "rarity": "SR", "element": "Geo",     "weapon": "Claymore", "region": "Liyue"},
    {"name": "Fiora Mistwalker", "rarity": "SR", "element": "Anemo",   "weapon": "Sword",    "region": "Mondstadt"},
    {"name": "Breckon Surge",    "rarity": "SR", "element": "Electro", "weapon": "Polearm",  "region": "Natlan"},
]

R_POOL = [
    {"name": "Cedric Ironfoot",  "rarity": "R", "element": "Geo",     "weapon": "Claymore", "region": "Liyue"},
    {"name": "Willa Ferngrove",  "rarity": "R", "element": "Pyro",    "weapon": "Bow",      "region": "Mondstadt"},
    {"name": "Oswin Saltmere",   "rarity": "R", "element": "Hydro",   "weapon": "Polearm",  "region": "Fontaine"},
    {"name": "Petra Coldsnap",   "rarity": "R", "element": "Cryo",    "weapon": "Sword",    "region": "Inazuma"},
    {"name": "Davin Sparkholt",  "rarity": "R", "element": "Electro", "weapon": "Catalyst", "region": "Sumeru"},
    {"name": "Rinna Mosswhirl",  "rarity": "R", "element": "Dendro",  "weapon": "Bow",      "region": "Sumeru"},
    {"name": "Tobren Ashenford", "rarity": "R", "element": "Anemo",   "weapon": "Sword",    "region": "Mondstadt"},
]

# ══════════════════════════════════════════
#  RARITY CONFIG
# ══════════════════════════════════════════

RARITY_DISPLAY = {
    "SSR": "✦ SSR ✦",
    "SR":  "★ SR ★",
    "R":   "◆ R ◆",
}

RARITY_RANK = {"SSR": 3, "SR": 2, "R": 1}  # untuk sorting

ELEMENT_COLORS = {
    "Pyro":    "🔴",
    "Hydro":   "🔵",
    "Anemo":   "🟢",
    "Electro": "🟣",
    "Dendro":  "🌿",
    "Cryo":    "⚪",
    "Geo":     "🟡",
}

# ══════════════════════════════════════════
#  GACHA RATES
# ══════════════════════════════════════════

BASE_SSR_RATE  = 0.006   # 0.6%
BASE_SR_RATE   = 0.051   # 5.1%
SOFT_PITY_START = 74
HARD_PITY       = 90

# 50/50 config
FIFTYFIFTY_SR_START = 9   # SR guaranteed every 10 pulls (soft)
HARD_PITY_SR        = 10  # SR guaranteed at pull 10
