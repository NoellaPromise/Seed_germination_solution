# ═══════════════════════════════════════════════════════
# MISSION 05 — SOLUTION (Teacher Reference)
# ═══════════════════════════════════════════════════════

import time

# ── All helper functions ─────────────────────────────
def will_germinate(ph):
    return 5.5 <= ph <= 7.5

def daily_growth_rate(ph):
    if 6.0 <= ph <= 7.0:
        return 1.2
    elif 5.5 <= ph < 6.0:
        return 0.7
    elif 7.0 < ph <= 8.0:
        return 0.5
    else:
        return 0.0

def health_status(ph):
    if 6.0 <= ph <= 7.0:
        return "Healthy 🟢"
    elif (5.5 <= ph < 6.0) or (7.0 < ph <= 8.0):
        return "Struggling 🟡"
    else:
        return "Failed 🔴"

def simulate_growth(ph, days=7):
    if not will_germinate(ph):
        print(f"❌ Seed did not germinate at pH {ph}.")
        return []
    height = 0.0
    rate = daily_growth_rate(ph)
    results = []
    for day in range(1, days + 1):
        height = round(height + rate, 1)
        results.append({"day": day, "height": height, "status": health_status(ph)})
    return results


# ── TODO 1: Test cases ───────────────────────────────
test_cases = [0, 14, 6.5, -1, 100]

print("🧪 RUNNING ALL TEST CASES")
print("=" * 50)

for ph in test_cases:
    print(f"\nTesting pH = {ph}...")
    try:
        result = simulate_growth(ph)
        if result:
            print(f"  ✅ HANDLES OK — final height: {result[-1]['height']} cm")
        else:
            print(f"  ✅ HANDLES OK — seed did not germinate (expected)")
    except Exception as e:
        print(f"  ❌ CRASHED: {e}")


# ── TODO 2: safe_input ───────────────────────────────
def safe_input():
    while True:
        try:
            ph = float(input("Enter pH (0–14): "))
            if 0 <= ph <= 14:
                return ph
            else:
                print("⚠️  pH must be between 0 and 14. Try again.")
        except ValueError:
            print("⚠️  Please enter a number, not a word!")


# ── TODO 3: Real vs simulated comparison ─────────────
# Sample real data — students replace these with their actual measurements
real_data = {
    "day_1": 0.0,
    "day_2": 1.1,
    "day_3": 2.3,
    "day_4": 3.4,
    "day_5": 4.6,
    "day_6": 5.7,
    "day_7": 6.8,
}

real_ph = 6.5
simulated = simulate_growth(real_ph)

print("\n📊 REAL vs SIMULATED COMPARISON")
print(f"Experiment pH: {real_ph}")
print("=" * 55)
print(f"{'Day':<5} | {'Real (cm)':<12} | {'Simulated (cm)':<16} | Close?")
print("-" * 55)

for i, result in enumerate(simulated):
    day_key = f"day_{result['day']}"
    real_val = real_data.get(day_key)
    sim_val = result["height"]

    if real_val is not None:
        diff = abs(real_val - sim_val)
        match = "✅ Yes" if diff <= 0.5 else "⚠️  No"
        print(f"{result['day']:<5} | {real_val:<12} | {sim_val:<16} | {match}")
    else:
        print(f"{result['day']:<5} | {'N/A':<12} | {sim_val:<16} | —")
