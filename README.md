## How to verify if it's working

### Python — run each file in the terminal

<python mission_01.py>

Type 6.5 when prompted. You should see:

Water type: neutral | Prediction: The seed will germinate well! 🌱

Try typing hello — it should say "That's not a number" and ask again.

python backend/mission_02.py

No input needed. You should see a table with 7 rows — pH 6.5 shows Healthy 🟢, pH 3.0 shows Failed 🔴.

python backend/mission_03.py

Watch it simulate day by day with a 0.5s delay. Experiment A (pH 6.5) reaches 8.4 cm by day 7. Experiment B (pH 3.0) prints "did not germinate."

python backend/mission_05.py

All 5 test cases should say ✅ HANDLES OK — none crash.


Frontend — open in browser

cd frontend
python -m http.server 5500


Open http://localhost:5500 and check:


Note on Mission 05 real data: The comparison currently shows ⚠️ No for all rows because the sample real data I filled in (0.0 → 6.8 cm) doesn't match the simulation rate of 1.2 cm/day. That's intentional — students replace those numbers with their actual notebook measurements. if their real plant grew slower than the simulation, that's a real scientific finding worth discussing!