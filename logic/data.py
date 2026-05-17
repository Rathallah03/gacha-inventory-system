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
    {"name": "Prof. Caspian",  "rarity": "SSR", "element": "Plasma",  "weapon": "Module",     "region": "Engine Room"},
    {"name": "Marina Frost",   "rarity": "SSR", "element": "Cryogen", "weapon": "Blaster",    "region": "Bio-Wing"},
    {"name": "Atlas Reef",     "rarity": "SSR", "element": "Terra",   "weapon": "Breaker",    "region": "Surface Hub"},
    {"name": "Coralie Stream", "rarity": "SSR", "element": "Aqua",    "weapon": "Data-Blade", "region": "Fluid Dynamics"},
    {"name": "Zephyr Gale",    "rarity": "SSR", "element": "Aero",    "weapon": "Harpoon",    "region": "Data Archive"},
]

SR_POOL = [
    {"name": "Corvin Glaze",   "rarity": "SR", "element": "Cryogen", "weapon": "Blaster",    "region": "Deep Core"},
    {"name": "Tessa Kelp",     "rarity": "SR", "element": "Bio",      "weapon": "Harpoon",    "region": "Data Archive"},
    {"name": "Aldric Fathom",  "rarity": "SR", "element": "Terra",   "weapon": "Breaker",    "region": "Bio-Wing"},
    {"name": "Fiora Gulf",     "rarity": "SR", "element": "Aero",    "weapon": "Data-Blade", "region": "Surface Hub"},
    {"name": "Breckon Surge",  "rarity": "SR", "element": "Volt",    "weapon": "Harpoon",    "region": "Engine Room"},
]

R_POOL = [
    {"name": "Cedric Shoal",   "rarity": "R", "element": "Terra",   "weapon": "Breaker",    "region": "Bio-Wing"},
    {"name": "Willa Crest",    "rarity": "R", "element": "Plasma",  "weapon": "Blaster",    "region": "Surface Hub"},
    {"name": "Oswin Eddy",     "rarity": "R", "element": "Aqua",    "weapon": "Harpoon",    "region": "Fluid Dynamics"},
    {"name": "Petra Rime",     "rarity": "R", "element": "Cryogen", "weapon": "Data-Blade", "region": "Deep Core"},
    {"name": "Rinna Bloom",    "rarity": "R", "element": "Bio",      "weapon": "Blaster",    "region": "Data Archive"},
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
