## Steps to run this project

### Python — run each file in the terminal

```python mission_01.py```

- Type `6.5` when prompted. You should see:

`Water type: neutral | Prediction: The seed will germinate well! 🌱`

Try typing `hello` — it should say "That's not a number" and ask again.

`python backend/mission_02.py`

- No input needed. You should see a table with 7 rows — pH 6.5 shows Healthy 🟢, pH 3.0 shows Failed 🔴.

```python backend/mission_03.py```

Watch it simulate day by day with a 0.5s delay. Experiment A (pH 6.5) reaches 8.4 cm by day 7. Experiment B (pH 3.0) prints "did not germinate."

```python backend/mission_05.py```

All 5 test cases should say ✅ HANDLES OK — none crash.

## Frontend — Open in browser
```
cd frontend
python -m http.server 5500


Open http://localhost:5500 and check:
```
