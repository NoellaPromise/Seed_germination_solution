// ═══════════════════════════════════════════════════════
// SOLUTION app.js (Teacher Reference)
// Includes all TODOs + Bonus SVG plant
// ═══════════════════════════════════════════════════════

const slider = document.getElementById('phSlider');
const phDisplay = document.getElementById('phDisplay');
const phLabel = document.getElementById('phLabel');

// ── TODO 1: Connect the pH Slider ───────────────────
slider.addEventListener('input', function() {
    const ph = parseFloat(this.value);
    phDisplay.textContent = ph.toFixed(1);
    const info = classifyPH(ph);
    phLabel.textContent = info.label;
    document.body.style.backgroundColor = info.bgColor;
});


// ── TODO 2: classifyPH ──────────────────────────────
function classifyPH(ph) {
    if (ph < 6.0) return { label: "Acidic",   bgColor: "#fde8e8" };
    if (ph <= 7.5) return { label: "Neutral",  bgColor: "#d8f3dc" };
    return              { label: "Alkaline", bgColor: "#dbeafe" };
}


// ── TODO 3: getDailyRate ─────────────────────────────
function getDailyRate(ph) {
    if (ph >= 6.0 && ph <= 7.0) return 1.2;
    if (ph >= 5.5 && ph < 6.0)  return 0.7;
    if (ph > 7.0 && ph <= 8.0)  return 0.5;
    return 0.0;
}


// ── TODO 4: getHealthStatus ──────────────────────────
function getHealthStatus(ph) {
    if (ph >= 6.0 && ph <= 7.0) return { label: "Healthy 🟢",    color: "#2d6a4f" };
    if ((ph >= 5.5 && ph < 6.0) || (ph > 7.0 && ph <= 8.0))
                                 return { label: "Struggling 🟡", color: "#b45309" };
    return                              { label: "Failed 🔴",     color: "#dc2626" };
}


// ── TODO 5: runSimulation ────────────────────────────
async function runSimulation() {
    const ph = parseFloat(slider.value);
    const rate = getDailyRate(ph);
    const tbody = document.getElementById('resultsBody');

    tbody.innerHTML = '';
    updatePlantStage(0, ph);  // reset plant

    let height = 0;

    for (let day = 1; day <= 7; day++) {
        height = Math.round((height + rate) * 10) / 10;
        const status = getHealthStatus(ph);

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${day}</td>
            <td>${height.toFixed(1)}</td>
            <td style="color:${status.color}; font-weight:600">${status.label}</td>
        `;
        tbody.appendChild(row);

        updatePlantStage(day, ph);

        await new Promise(resolve => setTimeout(resolve, 600));
    }
}


// ── BONUS: SVG illustrated plant ────────────────────
function updatePlantStage(day, ph) {
    const svg = document.getElementById('plantSvg');
    const failed = getDailyRate(ph) === 0;
    const cx = 60;    // center x
    const base = 155; // soil line y

    // Colors
    const stemColor  = failed ? "#8B4513" : "#2d6a4f";
    const leafColor  = failed ? "#a0522d" : "#52b788";
    const budColor   = failed ? "#cd853f" : "#95d5b2";
    const flowerColor = "#f4a261";

    // Stem height grows each day
    const stemH = failed ? 30 : Math.min(day * 18, 130);
    const stemTop = base - stemH;

    let content = "";

    // Always draw the stem
    content += `<line x1="${cx}" y1="${base}" x2="${cx}" y2="${stemTop}"
                  stroke="${stemColor}" stroke-width="5" stroke-linecap="round"/>`;

    if (failed) {
        // Wilted drooping curve
        content += `<path d="M${cx} ${stemTop} Q${cx + 20} ${stemTop + 10} ${cx + 30} ${stemTop + 30}"
                      stroke="${stemColor}" stroke-width="4" fill="none" stroke-linecap="round"/>`;
        content += `<ellipse cx="${cx + 30}" cy="${stemTop + 35}" rx="10" ry="6"
                      fill="${leafColor}" transform="rotate(30 ${cx + 30} ${stemTop + 35})"/>`;
    } else {
        // Day 1 — tiny sprout nub
        if (day >= 1) {
            content += `<ellipse cx="${cx}" cy="${stemTop}" rx="5" ry="8"
                          fill="${leafColor}" opacity="0.8"/>`;
        }

        // Day 3 — left leaf
        if (day >= 3) {
            content += `<ellipse cx="${cx - 18}" cy="${stemTop + 20}" rx="14" ry="7"
                          fill="${leafColor}" transform="rotate(-30 ${cx - 18} ${stemTop + 20})"/>`;
            content += `<line x1="${cx}" y1="${stemTop + 24}" x2="${cx - 18}" y2="${stemTop + 20}"
                          stroke="${stemColor}" stroke-width="2"/>`;
        }

        // Day 4 — right leaf
        if (day >= 4) {
            content += `<ellipse cx="${cx + 18}" cy="${stemTop + 35}" rx="14" ry="7"
                          fill="${leafColor}" transform="rotate(30 ${cx + 18} ${stemTop + 35})"/>`;
            content += `<line x1="${cx}" y1="${stemTop + 38}" x2="${cx + 18}" y2="${stemTop + 35}"
                          stroke="${stemColor}" stroke-width="2"/>`;
        }

        // Day 5 — bud at top
        if (day >= 5) {
            content += `<ellipse cx="${cx}" cy="${stemTop - 8}" rx="7" ry="9"
                          fill="${budColor}"/>`;
        }

        // Day 6 — second left leaf
        if (day >= 6) {
            content += `<ellipse cx="${cx - 20}" cy="${stemTop + 55}" rx="14" ry="7"
                          fill="${leafColor}" transform="rotate(-20 ${cx - 20} ${stemTop + 55})"/>`;
            content += `<line x1="${cx}" y1="${stemTop + 58}" x2="${cx - 20}" y2="${stemTop + 55}"
                          stroke="${stemColor}" stroke-width="2"/>`;
        }

        // Day 7 — flower blooms
        if (day >= 7) {
            const fx = cx, fy = stemTop - 16;
            // Petals
            for (let i = 0; i < 6; i++) {
                const angle = (i * 60) * Math.PI / 180;
                const px = fx + Math.cos(angle) * 12;
                const py = fy + Math.sin(angle) * 12;
                content += `<ellipse cx="${px}" cy="${py}" rx="6" ry="4"
                              fill="${flowerColor}"
                              transform="rotate(${i * 60} ${px} ${py})"/>`;
            }
            // Center
            content += `<circle cx="${fx}" cy="${fy}" r="7" fill="#e9c46a"/>`;
        }
    }

    svg.innerHTML = content;
}


// ── Initialize on page load ──────────────────────────
slider.value = 7;
phDisplay.textContent = "7.0";
phLabel.textContent = "Neutral";
document.body.style.backgroundColor = "#d8f3dc";
updatePlantStage(0, 7);
