# ═══════════════════════════════════════════════════════
# MISSION 01 — SOLUTION (Teacher Reference)
# ═══════════════════════════════════════════════════════

# ── TODO 1: classify_ph ─────────────────────────────
def classify_ph(ph):
    if ph < 6.0:
        return "acidic"
    elif ph <= 7.5:
        return "neutral"
    else:
        return "alkaline"


# ── TODO 2: predict_growth ──────────────────────────
def predict_growth(ph):
    if 6.0 <= ph <= 7.0:
        return "The seed will germinate well! 🌱 pH is in the optimal range."
    elif 5.5 <= ph < 6.0:
        return "The seed may struggle. 🟡 Water is slightly too acidic."
    elif 7.0 < ph <= 7.5:
        return "The seed may struggle. 🟡 Water is slightly too alkaline."
    elif ph < 5.5:
        return "The seed will likely fail. 🔴 Water is too acidic."
    else:
        return "The seed will likely fail. 🔴 Water is too alkaline."


# ── TODO 3: Safe input from user ────────────────────
print("🌱 Seed Germination pH Simulator")
print("=" * 35)

while True:
    try:
        ph = float(input("Enter the pH of your water (1-14): "))
        if 0 <= ph <= 14:
            break
        else:
            print("⚠️  Please enter a number between 0 and 14.")
    except ValueError:
        print("⚠️  That's not a number. Please try again.")

water_type = classify_ph(ph)
prediction = predict_growth(ph)

print(f"\npH entered  : {ph}")
print(f"Water type  : {water_type}")
print(f"Prediction  : {prediction}")
