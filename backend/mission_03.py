# ═══════════════════════════════════════════════════════
# MISSION 03 — SOLUTION (Teacher Reference)
# ═══════════════════════════════════════════════════════

import time

# ── Helper functions from Mission 02 ────────────────
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


# ── TODO 1: 7-day simulation loop ───────────────────
def simulate_growth(ph, days=7):
    print(f"\n🌱 Starting experiment at pH {ph}")
    print("=" * 45)

    if not will_germinate(ph):
        print("❌ Seed did not germinate at this pH level.")
        print(f"   pH {ph} is outside the safe range (5.5 – 7.5)")
        return []

    print("✅ Seed germinated! Simulating growth...\n")
    print(f"{'Day':<5} | {'Height (cm)':<12} | Health")
    print("-" * 35)

    height = 0.0
    rate = daily_growth_rate(ph)
    results = []

    for day in range(1, days + 1):
        height += rate
        height = round(height, 1)
        status = health_status(ph)
        results.append({"day": day, "height": height, "status": status})
        print(f"{day:<5} | {height:<12} | {status}")
        time.sleep(0.5)

    return results


# ── TODO 2: Two experiments ──────────────────────────
print("🔬 EXPERIMENT A — Plain water (pH 6.5)")
results_a = simulate_growth(6.5)

print("\n🔬 EXPERIMENT B — Detergent water (pH 3.0)")
results_b = simulate_growth(3.0)


# ── TODO 3 BONUS: Final comparison summary ──────────
print("\n📊 FINAL COMPARISON")
print("=" * 45)

if results_a:
    final_a = results_a[-1]["height"]
    print(f"Experiment A (pH 6.5): final height = {final_a} cm")
else:
    print("Experiment A (pH 6.5): seed did not germinate")

if results_b:
    final_b = results_b[-1]["height"]
    print(f"Experiment B (pH 3.0): final height = {final_b} cm")
else:
    print("Experiment B (pH 3.0): seed did not germinate")
