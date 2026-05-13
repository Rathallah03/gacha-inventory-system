# gacha.py — Pull Logic, Pity System, 50/50

import random
from data import (
    FEATURED_SSR, STANDARD_SSR_POOL, SR_POOL, R_POOL,
    BASE_SSR_RATE, BASE_SR_RATE,
    SOFT_PITY_START, HARD_PITY, HARD_PITY_SR
)

# ══════════════════════════════════════════
#  PITY STATE
#  (akan di-load dari save file saat startup)
# ══════════════════════════════════════════

pity_counter  = 0    # counter menuju SSR (max 90)
sr_pity       = 0    # counter menuju SR (max 10)
is_guaranteed = False  # True = rate ON (guaranteed featured SSR)


# ══════════════════════════════════════════
#  RATE CALCULATION
# ══════════════════════════════════════════

def get_ssr_rate(pity):
    """
    Hitung rate SSR berdasarkan pity counter.
    - Pull 1-73  : base rate 0.6%
    - Pull 74-89 : soft pity, naik +6% per pull
    - Pull 90    : hard pity, 100%
    """
    if pity < SOFT_PITY_START:
        return BASE_SSR_RATE
    else:
        bonus = (pity - SOFT_PITY_START + 1) * 0.06
        return min(BASE_SSR_RATE + bonus, 1.0)


# ══════════════════════════════════════════
#  RESOLVE RARITY
# ══════════════════════════════════════════

def resolve_rarity():
    """
    Tentukan rarity hasil pull berdasarkan rate & pity.
    Returns: "SSR", "SR", atau "R"
    """
    global pity_counter, sr_pity

    pity_counter += 1
    sr_pity      += 1

    ssr_rate = get_ssr_rate(pity_counter)
    roll     = random.random()

    # — SSR check (hard pity di 90) —
    if pity_counter >= HARD_PITY or roll < ssr_rate:
        pity_counter = 0
        sr_pity      = 0
        return "SSR"

    # — SR check (guaranteed tiap 10 pull) —
    if sr_pity >= HARD_PITY_SR or roll < BASE_SR_RATE:
        sr_pity = 0
        return "SR"

    return "R"


# ══════════════════════════════════════════
#  RESOLVE CHARACTER
# ══════════════════════════════════════════

def resolve_character(rarity):
    """
    Pilih karakter berdasarkan rarity.
    Untuk SSR: terapkan sistem 50/50.
    """
    global is_guaranteed

    if rarity == "SSR":
        # 50/50 system
        if is_guaranteed or random.random() < 0.5:
            is_guaranteed = False
            return dict(FEATURED_SSR)         # featured (rate ON → win)
        else:
            is_guaranteed = True              # rate OFF → next guaranteed
            return random.choice(STANDARD_SSR_POOL).copy()

    elif rarity == "SR":
        return random.choice(SR_POOL).copy()

    else:
        return random.choice(R_POOL).copy()


# ══════════════════════════════════════════
#  SINGLE PULL
# ══════════════════════════════════════════

def pull_once():
    """
    Lakukan 1x pull.
    Returns: dict karakter hasil pull
    """
    rarity    = resolve_rarity()
    character = resolve_character(rarity)
    return character


# ══════════════════════════════════════════
#  MULTI PULL (10x)
# ══════════════════════════════════════════

def pull_ten():
    """
    Lakukan 10x pull sekaligus.
    Returns: list of 10 karakter
    """
    results = []
    for _ in range(10):
        results.append(pull_once())
    return results


# ══════════════════════════════════════════
#  GETTER — untuk save/load & display
# ══════════════════════════════════════════

def get_pity_state():
    return {
        "pity_counter":  pity_counter,
        "sr_pity":       sr_pity,
        "is_guaranteed": is_guaranteed,
    }

def set_pity_state(state):
    global pity_counter, sr_pity, is_guaranteed
    pity_counter  = state.get("pity_counter",  0)
    sr_pity       = state.get("sr_pity",       0)
    is_guaranteed = state.get("is_guaranteed", False)
