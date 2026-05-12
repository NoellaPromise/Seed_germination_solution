# ═══════════════════════════════════════════════════════
# MISSION 02 — SOLUTION (Teacher Reference)
# ═══════════════════════════════════════════════════════

# ── TODO 1: will_germinate ───────────────────────────
def will_germinate(ph):
    return 5.5 <= ph <= 7.5


# ── TODO 2: daily_growth_rate ────────────────────────
def daily_growth_rate(ph):
    if 6.0 <= ph <= 7.0:
        return 1.2
    elif 5.5 <= ph < 6.0:
        return 0.7
    elif 7.0 < ph <= 8.0:
        return 0.5
    else:
        return 0.0


# ── TODO 3: health_status ────────────────────────────
def health_status(ph):
    if 6.0 <= ph <= 7.0:
        return "Healthy 🟢"
    elif (5.5 <= ph < 6.0) or (7.0 < ph <= 8.0):
        return "Struggling 🟡"
    else:
        return "Failed 🔴"


# ── Test table ───────────────────────────────────────
test_values = [3.0, 5.5, 6.0, 6.5, 7.0, 8.0, 11.0]

print("pH    | Germinates? | Growth/day  | Health")
print("-" * 55)
for ph in test_values:
    g = will_germinate(ph)
    r = daily_growth_rate(ph)
    h = health_status(ph)
    print(f"{ph:<5} | {str(g):<11} | {r} cm/day   | {h}")
