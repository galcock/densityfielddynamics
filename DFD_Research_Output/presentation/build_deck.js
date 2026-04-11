const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const { FaRocket, FaAtom, FaBolt, FaShieldAlt, FaCogs, FaChartLine, FaGlobeAmericas, FaDollarSign, FaFlask, FaCheckCircle, FaClock, FaWeight, FaThermometerHalf, FaSatelliteDish, FaIndustry, FaBalanceScale, FaLock, FaLightbulb } = require("react-icons/fa");

function renderIconSvg(IconComponent, color, size = 256) {
  return ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
}

async function iconToBase64Png(IconComponent, color, size = 256) {
  const svg = renderIconSvg(IconComponent, color, size);
  const pngBuffer = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + pngBuffer.toString("base64");
}

async function main() {
  // ===== SETUP =====
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "Gary Thomas Alcock";
  pres.title = "Psi-Bubble Propulsion: Engineering the Next Age of Space Travel";

  // Colors
  const C = {
    navy: "0B1026",
    midnavy: "121A33",
    blue: "00B4D8",
    gold: "FFB703",
    white: "F0F0F0",
    dim: "7788AA",
    red: "FF4444",
    green: "22CC88",
    darkblue: "0A3D62",
  };

  // Preload icons
  const icons = {};
  const iconList = [
    ["rocket", FaRocket], ["atom", FaAtom], ["bolt", FaBolt], ["shield", FaShieldAlt],
    ["cogs", FaCogs], ["chart", FaChartLine], ["globe", FaGlobeAmericas], ["dollar", FaDollarSign],
    ["flask", FaFlask], ["check", FaCheckCircle], ["clock", FaClock], ["weight", FaWeight],
    ["thermo", FaThermometerHalf], ["satellite", FaSatelliteDish], ["industry", FaIndustry],
    ["balance", FaBalanceScale], ["lock", FaLock], ["lightbulb", FaLightbulb],
  ];
  for (const [name, component] of iconList) {
    icons[name + "_blue"] = await iconToBase64Png(component, "#00B4D8");
    icons[name + "_gold"] = await iconToBase64Png(component, "#FFB703");
    icons[name + "_white"] = await iconToBase64Png(component, "#F0F0F0");
    icons[name + "_red"] = await iconToBase64Png(component, "#FF4444");
    icons[name + "_green"] = await iconToBase64Png(component, "#22CC88");
  }

  // Helper: dark background
  const darkBg = (slide) => { slide.background = { color: C.navy }; };

  // ============================================================
  // ACT 1: THE HOOK
  // ============================================================

  // --- SLIDE 1: TITLE ---
  let s = pres.addSlide();
  darkBg(s);
  // Subtle circles
  for (let r = 4; r >= 0.5; r -= 0.5) {
    const t = Math.round(92 - r * 8);
    s.addShape(pres.shapes.OVAL, {
      x: 5 - r, y: 2.8125 - r, w: r * 2, h: r * 2,
      fill: { color: C.blue, transparency: t },
      line: { color: C.blue, width: 0.3, transparency: 80 },
    });
  }
  s.addText("PSI-BUBBLE PROPULSION", {
    x: 0.5, y: 1.4, w: 9, h: 0.9, fontSize: 40, fontFace: "Arial Black",
    color: C.white, align: "center", bold: true, charSpacing: 4,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3.5, y: 2.4, w: 3, h: 0, line: { color: C.gold, width: 2.5 },
  });
  s.addText("Engineering the Next Age of Space Travel", {
    x: 0.5, y: 2.6, w: 9, h: 0.5, fontSize: 18, fontFace: "Calibri",
    color: C.blue, align: "center", italic: true,
  });
  s.addText("Gary Thomas Alcock", {
    x: 0.5, y: 3.5, w: 9, h: 0.4, fontSize: 16, fontFace: "Calibri",
    color: C.white, align: "center",
  });
  s.addText("Density Field Dynamics", {
    x: 0.5, y: 3.9, w: 9, h: 0.35, fontSize: 12, fontFace: "Calibri",
    color: C.dim, align: "center",
  });

  // --- SLIDE 2: THE PROBLEM ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("95%", {
    x: 0.5, y: 0.6, w: 9, h: 2.8, fontSize: 120, fontFace: "Arial Black",
    color: C.red, align: "center", valign: "middle", bold: true,
  });
  s.addText("of every rocket is thrown away", {
    x: 0.5, y: 3.2, w: 9, h: 0.7, fontSize: 28, fontFace: "Calibri",
    color: C.white, align: "center", bold: true,
  });
  s.addText("Tsiolkovsky's equation constrains ALL chemical propulsion.\nThis has been true for 100 years.", {
    x: 1.5, y: 4.1, w: 7, h: 0.8, fontSize: 13, fontFace: "Calibri",
    color: C.dim, align: "center",
  });

  // --- SLIDE 3: THE COST ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Cost of Access to Space", {
    x: 0.5, y: 0.2, w: 9, h: 0.5, fontSize: 28, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  s.addChart(pres.charts.BAR, [{
    name: "$/kg to LEO",
    labels: ["SLS", "Atlas V", "Falcon 9", "Falcon Heavy", "Starship\n(target)"],
    values: [20000, 13200, 2720, 1500, 100],
  }], {
    x: 0.8, y: 0.9, w: 8.4, h: 4.0, barDir: "col",
    chartColors: [C.red, "DD5533", C.gold, "88BB44", C.green],
    chartArea: { fill: { color: C.midnavy }, roundedCorners: true },
    catAxisLabelColor: C.dim, catAxisLabelFontSize: 10,
    valAxisLabelColor: C.dim, valAxisLabelFontSize: 9,
    valGridLine: { color: "1E2D50", size: 0.5 },
    catGridLine: { style: "none" },
    showValue: true, dataLabelPosition: "outEnd", dataLabelColor: C.white,
    dataLabelFontSize: 10, showLegend: false,
    valAxisNumFmt: "$#,##0",
  });
  s.addText("Even Starship's revolutionary $100/kg is bounded by propellant mass fraction.", {
    x: 1, y: 5.0, w: 8, h: 0.4, fontSize: 11, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 4: THE TIME ---
  s = pres.addSlide();
  darkBg(s);
  s.addImage({ data: icons.clock_red, x: 4.5, y: 0.15, w: 0.6, h: 0.6 });
  const timeData = [
    ["Earth to Mars:", "7 months", 0.9],
    ["Earth to Jupiter:", "6 years", 2.0],
    ["Nearest star:", "75,000 years", 3.1],
  ];
  timeData.forEach(([label, time, y]) => {
    s.addText(label, {
      x: 0.8, y, w: 4.2, h: 0.7, fontSize: 22, fontFace: "Calibri",
      color: C.white, align: "right", valign: "middle", bold: true, margin: 0,
    });
    s.addText(time, {
      x: 5.2, y, w: 4, h: 0.7, fontSize: 36, fontFace: "Arial Black",
      color: C.red, align: "left", valign: "middle", bold: true, margin: 0,
    });
  });
  s.addText("Chemical propulsion makes the solar system large and the galaxy unreachable.", {
    x: 1, y: 4.4, w: 8, h: 0.5, fontSize: 13, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 5: BREAKTHROUGH ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("What if you didn't need\npropellant at all?", {
    x: 0.5, y: 1.2, w: 9, h: 1.5, fontSize: 36, fontFace: "Calibri",
    color: C.white, align: "center", bold: true,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3, y: 3.0, w: 4, h: 0, line: { color: C.gold, width: 2.5 },
  });
  s.addText("A propulsion system that modifies the local gravitational field\nrequires zero reaction mass.", {
    x: 1, y: 3.3, w: 8, h: 0.8, fontSize: 16, fontFace: "Calibri",
    color: C.blue, align: "center", italic: true,
  });

  // --- SLIDE 6: THE DEVICE ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Ferrite-Superconductor Resonant Shell", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Outer ellipse - ferrite (gold)
  s.addShape(pres.shapes.OVAL, {
    x: 2.5, y: 0.8, w: 5, h: 3.5,
    fill: { color: C.gold, transparency: 85 },
    line: { color: C.gold, width: 3 },
  });
  // Inner ellipse - superconductor (blue)
  s.addShape(pres.shapes.OVAL, {
    x: 3.0, y: 1.15, w: 4, h: 2.8,
    fill: { color: C.blue, transparency: 85 },
    line: { color: C.blue, width: 3 },
  });
  // Interior - dark
  s.addShape(pres.shapes.OVAL, {
    x: 3.5, y: 1.5, w: 3, h: 2.1,
    fill: { color: C.navy, transparency: 30 },
    line: { color: C.white, width: 0.5, transparency: 70 },
  });
  // Labels
  s.addText("Ferrite Layer\n(ε ≈ μ matched)", {
    x: 7.7, y: 1.0, w: 2, h: 0.6, fontSize: 10, fontFace: "Calibri",
    color: C.gold, align: "left", margin: 0,
  });
  s.addText("Superconductor\n(s-wave: Nb, MgB₂)", {
    x: 7.7, y: 1.9, w: 2, h: 0.6, fontSize: 10, fontFace: "Calibri",
    color: C.blue, align: "left", margin: 0,
  });
  s.addText("Payload\nZero g-force interior", {
    x: 4.0, y: 2.2, w: 2, h: 0.5, fontSize: 10, fontFace: "Calibri",
    color: C.white, align: "center", margin: 0,
  });
  s.addText("← ψ gradient →", {
    x: 0.3, y: 2.3, w: 2, h: 0.3, fontSize: 11, fontFace: "Calibri",
    color: C.gold, align: "center", bold: true, margin: 0,
  });
  s.addText("Rotating EM Field ↻", {
    x: 7.7, y: 2.8, w: 2, h: 0.3, fontSize: 10, fontFace: "Calibri",
    color: C.blue, align: "left", margin: 0,
  });
  // Bottom explanatory text
  s.addText([
    { text: "Ferrite: ", options: { color: C.gold, bold: true } },
    { text: "stores EM energy at maximum density (ε·μ optimized)    ", options: { color: C.dim } },
    { text: "Superconductor: ", options: { color: C.blue, bold: true } },
    { text: "provides quantum coherence (10²³ Cooper pairs)", options: { color: C.dim } },
  ], {
    x: 0.5, y: 4.6, w: 9, h: 0.6, fontSize: 11, fontFace: "Calibri", align: "center",
  });

  // --- SLIDE 7: HOW IT WORKS ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("How It Works", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 28, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const steps = [
    { label: "EM Energy\nInput", sub: "RF power into\nresonant cavity", color: C.blue, x: 0.3 },
    { label: "ψ Field\nModification", sub: "Cooper pairs modify\nlocal ψ density", color: C.gold, x: 2.7 },
    { label: "Gravitational\nGradient", sub: "Asymmetric ∇ψ\nproduces net force", color: C.green, x: 5.1 },
    { label: "Propellantless\nAcceleration", sub: "Vehicle accelerates\nwithout exhaust", color: C.white, x: 7.5 },
  ];
  steps.forEach((st, i) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: st.x, y: 1.0, w: 2.1, h: 1.5,
      fill: { color: st.color, transparency: 82 },
      line: { color: st.color, width: 2 },
      rectRadius: 0.12,
    });
    s.addText(st.label, {
      x: st.x, y: 1.1, w: 2.1, h: 0.9, fontSize: 13, fontFace: "Calibri",
      color: C.white, align: "center", valign: "middle", bold: true, margin: 0,
    });
    s.addText(st.sub, {
      x: st.x, y: 2.8, w: 2.1, h: 0.6, fontSize: 9, fontFace: "Calibri",
      color: C.dim, align: "center", margin: 0,
    });
    if (i < 3) {
      s.addText("→", {
        x: st.x + 2.1, y: 1.3, w: 0.6, h: 0.8, fontSize: 28, fontFace: "Arial",
        color: st.color, align: "center", valign: "middle", bold: true, margin: 0,
      });
    }
  });
  s.addText([
    { text: "Key insight: ", options: { color: C.blue, bold: true } },
    { text: "The EM field is the fuel. The cavity is the engine. There is no exhaust.", options: { color: C.white } },
  ], {
    x: 0.5, y: 4.2, w: 9, h: 0.5, fontSize: 15, fontFace: "Calibri", align: "center",
  });

  // --- SLIDE 8: ZERO G ---
  s = pres.addSlide();
  darkBg(s);
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: 0.6, w: 8.4, h: 1.8,
    fill: { color: C.blue, transparency: 88 },
    line: { color: C.blue, width: 2 },
  });
  s.addText("Zero g-forces on occupants.\nAt any acceleration.", {
    x: 1, y: 0.7, w: 8, h: 1.5, fontSize: 30, fontFace: "Calibri",
    color: C.white, align: "center", valign: "middle", bold: true,
  });
  s.addText("All matter inside the shell accelerates identically — exactly like gravitational freefall.", {
    x: 1, y: 2.7, w: 8, h: 0.5, fontSize: 14, fontFace: "Calibri", color: C.blue, align: "center",
  });
  const gComp = [
    ["Chemical rocket at 10g:", "crew is crushed", C.red, "●"],
    ["Psi-bubble at 10g:", "crew feels nothing", C.green, "●"],
    ["Psi-bubble at 1,000g:", "crew still feels nothing", C.green, "●"],
  ];
  gComp.forEach(([label, result, col, dot], i) => {
    const y = 3.5 + i * 0.5;
    s.addText(label, {
      x: 1.5, y, w: 4, h: 0.4, fontSize: 14, fontFace: "Calibri",
      color: C.white, align: "right", margin: 0,
    });
    s.addText(`${dot}  ${result}`, {
      x: 5.7, y, w: 3, h: 0.4, fontSize: 14, fontFace: "Calibri",
      color: col, align: "left", bold: true, margin: 0,
    });
  });

  // ============================================================
  // ACT 2: THE PHYSICS
  // ============================================================

  // --- SLIDE 9: SECTION DIVIDER ---
  s = pres.addSlide();
  darkBg(s);
  s.addImage({ data: icons.atom_blue, x: 4.5, y: 1.0, w: 1, h: 1 });
  s.addText("THE PHYSICS", {
    x: 0.5, y: 2.2, w: 9, h: 0.8, fontSize: 36, fontFace: "Arial Black",
    color: C.white, align: "center", charSpacing: 6,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3.5, y: 3.1, w: 3, h: 0, line: { color: C.blue, width: 2 },
  });

  // --- SLIDE 10: FIELD EQUATION ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Density Field Dynamics: The Master Equation", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Equation box
  s.addShape(pres.shapes.RECTANGLE, {
    x: 1.5, y: 0.8, w: 7, h: 1.2,
    fill: { color: C.midnavy },
    line: { color: C.blue, width: 2.5 },
  });
  s.addText("∇²ψ  =  (4πG / c²) · ρ_eff · μ(ψ)", {
    x: 1.5, y: 0.8, w: 7, h: 1.2, fontSize: 28, fontFace: "Calibri",
    color: C.white, align: "center", valign: "middle", bold: true,
  });
  // Term boxes
  const terms = [
    { label: "∇²ψ", desc: "Curvature of\nψ field", color: C.blue, x: 0.5 },
    { label: "4πG/c²", desc: "Gravitational\ncoupling", color: C.blue, x: 2.9 },
    { label: "ρ_eff", desc: "Effective energy\ndensity (incl. EM)", color: C.gold, x: 5.3 },
    { label: "μ(ψ)", desc: "MOND nonlinear\nresponse", color: C.red, x: 7.7 },
  ];
  terms.forEach(t => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: t.x, y: 2.3, w: 2.1, h: 1.1,
      fill: { color: t.color, transparency: 85 },
      line: { color: t.color, width: 1.5 },
    });
    s.addText(t.label, {
      x: t.x, y: 2.3, w: 2.1, h: 0.5, fontSize: 16, fontFace: "Calibri",
      color: C.white, align: "center", bold: true, margin: 0,
    });
    s.addText(t.desc, {
      x: t.x, y: 2.75, w: 2.1, h: 0.55, fontSize: 10, fontFace: "Calibri",
      color: C.dim, align: "center", margin: 0,
    });
  });
  s.addText("DFD generalizes Newtonian gravity: electromagnetic energy density directly sources the gravitational potential through a nonlinear coupling.", {
    x: 0.8, y: 3.7, w: 8.4, h: 0.5, fontSize: 12, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 11: COUPLING PROBLEM ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Coupling Problem", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  s.addText("10⁻⁴⁴", {
    x: 0.5, y: 0.8, w: 9, h: 2.2, fontSize: 96, fontFace: "Arial Black",
    color: C.red, align: "center", valign: "middle",
  });
  s.addText("m/J — gravitational effect per joule of electromagnetic energy", {
    x: 1, y: 3.0, w: 8, h: 0.4, fontSize: 14, fontFace: "Calibri",
    color: C.dim, align: "center",
  });
  s.addShape(pres.shapes.LINE, {
    x: 3, y: 3.6, w: 4, h: 0, line: { color: C.dim, width: 0.5 },
  });
  s.addText("This is why everyone assumed it was impossible.", {
    x: 1, y: 3.8, w: 8, h: 0.5, fontSize: 18, fontFace: "Calibri",
    color: C.white, align: "center", bold: true,
  });
  s.addText("But this is the classical, incoherent coupling. Three enhancement mechanisms change everything.", {
    x: 1, y: 4.4, w: 8, h: 0.5, fontSize: 13, fontFace: "Calibri",
    color: C.blue, align: "center",
  });

  // --- SLIDE 12: QUANTUM COHERENCE ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Enhancement 1: Quantum Coherence", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Left box - normal
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: 0.8, w: 4.2, h: 2.5,
    fill: { color: C.midnavy }, line: { color: C.dim, width: 1.5 },
  });
  s.addText("Normal Matter", {
    x: 0.5, y: 0.85, w: 4.2, h: 0.4, fontSize: 14, fontFace: "Calibri",
    color: C.dim, align: "center", bold: true, margin: 0,
  });
  s.addText("↗ ← ↙ → ↖ ↓ ↘ ↑\n→ ↙ ↗ ← ↖ ↓ ↗ ↘\n← ↑ → ↙ ↘ ↗ ↓ ←", {
    x: 0.8, y: 1.3, w: 3.6, h: 1.5, fontSize: 18, fontFace: "Arial",
    color: C.dim, align: "center", valign: "middle",
  });
  // Right box - coherent
  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.3, y: 0.8, w: 4.2, h: 2.5,
    fill: { color: C.midnavy }, line: { color: C.blue, width: 1.5 },
  });
  s.addText("Cooper Pair Condensate", {
    x: 5.3, y: 0.85, w: 4.2, h: 0.4, fontSize: 14, fontFace: "Calibri",
    color: C.blue, align: "center", bold: true, margin: 0,
  });
  s.addText("→ → → → → → → →\n→ → → → → → → →\n→ → → → → → → →", {
    x: 5.6, y: 1.3, w: 3.6, h: 1.5, fontSize: 18, fontFace: "Arial",
    color: C.blue, align: "center", valign: "middle",
  });
  // Arrow between
  s.addText("T < Tc", {
    x: 4.2, y: 1.7, w: 1.6, h: 0.3, fontSize: 11, fontFace: "Calibri",
    color: C.gold, align: "center", bold: true, margin: 0,
  });
  s.addText("⟹", {
    x: 4.3, y: 1.95, w: 1.4, h: 0.4, fontSize: 24, fontFace: "Arial",
    color: C.gold, align: "center", margin: 0,
  });
  // Enhancement
  s.addText("Enhancement: 10¹² — 10²⁷", {
    x: 0.5, y: 3.6, w: 9, h: 0.6, fontSize: 28, fontFace: "Calibri",
    color: C.gold, align: "center", bold: true,
  });
  s.addText("N ~ 10²³ particles acting as one quantum system. Phases add coherently, not randomly.", {
    x: 1, y: 4.3, w: 8, h: 0.4, fontSize: 12, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 13: MOND ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Enhancement 2: MOND Nonlinearity", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Simple representation of mu(x) curve
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: 0.8, w: 5.5, h: 3.2,
    fill: { color: C.midnavy }, line: { color: C.dim, width: 1 },
  });
  s.addText("μ(x)\n\n1.0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\n                    ╱\n                 ╱\n              ╱\n           ╱\n        ╱\n     ╱\n  ╱\n╱\n0  ─────────────────────── x\n     MOND          Newtonian\n     regime          regime", {
    x: 0.9, y: 0.8, w: 5.3, h: 3.2, fontSize: 10, fontFace: "Consolas",
    color: C.blue, align: "left", valign: "top", margin: 5,
  });
  // Annotation
  s.addShape(pres.shapes.RECTANGLE, {
    x: 6.8, y: 0.8, w: 2.8, h: 1.2,
    fill: { color: C.gold, transparency: 85 },
    line: { color: C.gold, width: 1.5 },
  });
  s.addText("Deep Space\nAdvantage", {
    x: 6.8, y: 0.85, w: 2.8, h: 0.55, fontSize: 14, fontFace: "Calibri",
    color: C.gold, align: "center", bold: true, margin: 0,
  });
  s.addText("10 — 1,000×\nenhancement", {
    x: 6.8, y: 1.4, w: 2.8, h: 0.5, fontSize: 12, fontFace: "Calibri",
    color: C.white, align: "center", margin: 0,
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 6.8, y: 2.3, w: 2.8, h: 0.8,
    fill: { color: C.blue, transparency: 88 },
    line: { color: C.blue, width: 1 },
  });
  s.addText("The device works\nBETTER far from\nmassive bodies", {
    x: 6.8, y: 2.3, w: 2.8, h: 0.8, fontSize: 11, fontFace: "Calibri",
    color: C.blue, align: "center", margin: 0,
  });
  s.addText("Near the MOND crossover (a ~ a₀ ≈ 1.2 × 10⁻¹⁰ m/s²), the nonlinear μ function amplifies small ψ perturbations.", {
    x: 0.5, y: 4.3, w: 9, h: 0.5, fontSize: 11, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 14: PARAMETRIC ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Enhancement 3: Parametric Amplification", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 1.5, y: 0.9, w: 7, h: 2.5,
    fill: { color: C.midnavy }, line: { color: C.green, width: 1.5 },
  });
  s.addText("Cavity Q > 10⁹", {
    x: 2, y: 1.1, w: 3, h: 0.5, fontSize: 20, fontFace: "Calibri",
    color: C.green, bold: true, margin: 0,
  });
  s.addText("Superconducting cavity walls (REBCO at 77K) achieve quality factors exceeding one billion.\n\nAt Q = 10⁹, the electromagnetic energy recirculates a billion times before dissipating.\n\nParametric coupling between EM modes and the ψ field is amplified by cavity resonance.", {
    x: 2, y: 1.7, w: 6, h: 1.5, fontSize: 12, fontFace: "Calibri",
    color: C.dim, margin: 0,
  });
  s.addText("Parametric Gain: 500 — 10⁵", {
    x: 0.5, y: 3.7, w: 9, h: 0.6, fontSize: 28, fontFace: "Calibri",
    color: C.green, align: "center", bold: true,
  });
  s.addText("e-folding time: 0.2 ms when parametric threshold is exceeded", {
    x: 1, y: 4.4, w: 8, h: 0.4, fontSize: 12, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 15: ENHANCEMENT BUDGET ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Total Enhancement Budget", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Waterfall as stacked horizontal bars
  const wf = [
    { label: "Classical coupling", val: "10⁻⁴⁴", color: C.red, w: 0.5 },
    { label: "+  Quantum coherence", val: "+20 orders", color: C.blue, w: 3.6 },
    { label: "+  MOND nonlinearity", val: "+3 orders", color: C.gold, w: 0.55 },
    { label: "+  Parametric amplification", val: "+4 orders", color: C.green, w: 0.7 },
    { label: "= Effective coupling", val: "10⁻¹⁷", color: C.white, w: 4.85 },
  ];
  let cumX = 0.7;
  wf.forEach((w, i) => {
    const y = 0.8 + i * 0.75;
    if (i < 4) {
      s.addShape(pres.shapes.RECTANGLE, {
        x: cumX, y, w: w.w, h: 0.5,
        fill: { color: w.color, transparency: 30 },
      });
      if (i > 0) cumX += w.w;
    } else {
      s.addShape(pres.shapes.RECTANGLE, {
        x: 0.7, y, w: w.w, h: 0.5,
        fill: { color: C.white, transparency: 75 },
        line: { color: C.white, width: 1.5 },
      });
    }
    s.addText(w.label, {
      x: 5.8, y, w: 2.5, h: 0.5, fontSize: 11, fontFace: "Calibri",
      color: w.color, align: "left", valign: "middle", bold: true, margin: 0,
    });
    s.addText(w.val, {
      x: 8.3, y, w: 1.3, h: 0.5, fontSize: 13, fontFace: "Calibri",
      color: C.white, align: "right", valign: "middle", bold: true, margin: 0,
    });
  });
  // Propulsion threshold line
  const threshX = 0.7 + 4.2; // roughly where -15 would be
  s.addShape(pres.shapes.LINE, {
    x: threshX, y: 0.8, w: 0, h: 3.8,
    line: { color: C.gold, width: 1.5, dashType: "dash" },
  });
  s.addText("← Propulsion\n    threshold", {
    x: threshX + 0.1, y: 2.0, w: 1.3, h: 0.6, fontSize: 9, fontFace: "Calibri",
    color: C.gold, margin: 0,
  });
  s.addText("27 orders of magnitude recovered. The gap from impossible to measurable is closed.", {
    x: 0.5, y: 4.6, w: 9, h: 0.4, fontSize: 13, fontFace: "Calibri", color: C.blue, align: "center", bold: true,
  });

  // --- SLIDE 16: SELF CONSISTENCY ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Rigorously Proven: Self-Consistent & Stable", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const checks = [
    ["Convergence ratio: 10⁻³³", "Exact to 33 decimal places — perturbation theory is definitive"],
    ["All eigenfrequencies stable", "No runaway instabilities under any laboratory conditions"],
    ["Energy conservation proven", "Via Noether's theorem from the DFD action principle"],
    ["Momentum carried by ψ-waves", "Recoil momentum radiated as ψ-field waves — NOT reactionless"],
  ];
  checks.forEach((c, i) => {
    const y = 0.85 + i * 1.0;
    s.addImage({ data: icons.check_green, x: 0.7, y: y + 0.05, w: 0.35, h: 0.35 });
    s.addText(c[0], {
      x: 1.2, y, w: 8, h: 0.4, fontSize: 16, fontFace: "Calibri",
      color: C.white, bold: true, margin: 0,
    });
    s.addText(c[1], {
      x: 1.2, y: y + 0.4, w: 8, h: 0.3, fontSize: 11, fontFace: "Calibri",
      color: C.dim, margin: 0,
    });
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 1.5, y: 4.6, w: 7, h: 0.5,
    fill: { color: C.red, transparency: 80 },
    line: { color: C.red, width: 1.5 },
  });
  s.addText("This is NOT perpetual motion.  It is NOT reactionless.  It is thermodynamically legal.", {
    x: 1.5, y: 4.6, w: 7, h: 0.5, fontSize: 12, fontFace: "Calibri",
    color: C.white, align: "center", valign: "middle", bold: true,
  });

  // --- SLIDE 17: VOLUME CANCELLATION ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Volume Cancellation Theorem", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Left: standing wave
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: 0.8, w: 4.2, h: 3.0,
    fill: { color: C.midnavy }, line: { color: C.red, width: 1.5 },
  });
  s.addText("Standing Wave", {
    x: 0.5, y: 0.85, w: 4.2, h: 0.4, fontSize: 16, fontFace: "Calibri",
    color: C.red, align: "center", bold: true, margin: 0,
  });
  s.addText("← → ← →\n→ ← → ←\n← → ← →", {
    x: 1.0, y: 1.4, w: 3.2, h: 1.2, fontSize: 22, fontFace: "Arial",
    color: C.dim, align: "center", valign: "middle",
  });
  s.addText("Symmetric: forces cancel\nNet force = 0", {
    x: 0.5, y: 2.8, w: 4.2, h: 0.6, fontSize: 12, fontFace: "Calibri",
    color: C.red, align: "center", margin: 0,
  });
  // Right: rotating wave
  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.3, y: 0.8, w: 4.2, h: 3.0,
    fill: { color: C.midnavy }, line: { color: C.green, width: 1.5 },
  });
  s.addText("Rotating Wave", {
    x: 5.3, y: 0.85, w: 4.2, h: 0.4, fontSize: 16, fontFace: "Calibri",
    color: C.green, align: "center", bold: true, margin: 0,
  });
  s.addText("→ → → →\n  → → → →\n    → → → →", {
    x: 5.8, y: 1.4, w: 3.2, h: 1.2, fontSize: 22, fontFace: "Arial",
    color: C.blue, align: "center", valign: "middle",
  });
  s.addText("Asymmetric: net directed force\nNet force  ⟹", {
    x: 5.3, y: 2.8, w: 4.2, h: 0.6, fontSize: 12, fontFace: "Calibri",
    color: C.green, align: "center", margin: 0,
  });
  s.addText("Only rotating (traveling wave) modes produce thrust. This is proven mathematically via parity arguments.", {
    x: 0.5, y: 4.2, w: 9, h: 0.5, fontSize: 12, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // ============================================================
  // ACT 3: THE ENGINEERING
  // ============================================================

  // --- SLIDE 18: SECTION DIVIDER ---
  s = pres.addSlide();
  darkBg(s);
  s.addImage({ data: icons.cogs_blue, x: 4.5, y: 1.0, w: 1, h: 1 });
  s.addText("THE ENGINEERING", {
    x: 0.5, y: 2.2, w: 9, h: 0.8, fontSize: 36, fontFace: "Arial Black",
    color: C.white, align: "center", charSpacing: 6,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3.5, y: 3.1, w: 3, h: 0, line: { color: C.gold, width: 2 },
  });

  // --- SLIDE 19: SHELL LAYERS ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Shell Architecture: 5 Precision Layers", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const layers = [
    { name: "YBCO Superconductor", dim: "5 mm", desc: "Cooper pair condensate, Meissner shielding", color: C.blue, h: 0.35 },
    { name: "MgO Buffer Layer", dim: "3 mm", desc: "Chemical barrier, CTE matching", color: C.dim, h: 0.25 },
    { name: "YIG Ferrite", dim: "50 mm", desc: "Matched ε≈μ, maximum EM energy density", color: C.gold, h: 1.0 },
    { name: "CFRP Overwrap", dim: "25 mm", desc: "Structural backup, carries tensile load", color: "445566", h: 0.6 },
    { name: "Aluminum Skin", dim: "5 mm", desc: "Vacuum jacket, outer EM boundary", color: "AABBCC", h: 0.35 },
  ];
  let layerY = 0.8;
  layers.forEach(l => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: 0.8, y: layerY, w: 5.5, h: l.h,
      fill: { color: l.color, transparency: 40 },
      line: { color: l.color, width: 1 },
    });
    s.addText(l.name, {
      x: 1.0, y: layerY, w: 3, h: l.h, fontSize: 11, fontFace: "Calibri",
      color: C.white, valign: "middle", bold: true, margin: 0,
    });
    s.addText(l.dim, {
      x: 6.6, y: layerY, w: 1, h: l.h, fontSize: 11, fontFace: "Calibri",
      color: C.white, valign: "middle", align: "center", bold: true, margin: 0,
    });
    s.addText(l.desc, {
      x: 7.7, y: layerY, w: 2.1, h: l.h, fontSize: 9, fontFace: "Calibri",
      color: C.dim, valign: "middle", margin: 0,
    });
    layerY += l.h + 0.08;
  });
  s.addText("Total wall thickness: 88 mm  |  Shell mass: 126,530 kg  |  Vehicle mass: 47,330 kg", {
    x: 0.5, y: 3.6, w: 9, h: 0.4, fontSize: 12, fontFace: "Calibri", color: C.blue, align: "center", bold: true,
  });

  // --- SLIDE 20: POWER ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Power Architecture", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const pSteps = [
    { label: "Nuclear\nReactor", sub: "50 MW thermal", color: C.red, x: 0.3 },
    { label: "Brayton\nTurbine", sub: "40% efficiency", color: C.gold, x: 2.2 },
    { label: "RF\nAmplifiers", sub: "GaN solid-state", color: C.green, x: 4.1 },
    { label: "Feed\nNetwork", sub: "Phase-locked", color: C.blue, x: 6.0 },
    { label: "Resonant\nShell", sub: "Q = 10⁹", color: C.white, x: 7.9 },
  ];
  pSteps.forEach((st, i) => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: st.x, y: 0.9, w: 1.6, h: 1.2,
      fill: { color: st.color, transparency: 82 },
      line: { color: st.color, width: 1.5 },
    });
    s.addText(st.label, {
      x: st.x, y: 0.95, w: 1.6, h: 0.7, fontSize: 11, fontFace: "Calibri",
      color: C.white, align: "center", valign: "middle", bold: true, margin: 0,
    });
    s.addText(st.sub, {
      x: st.x, y: 1.7, w: 1.6, h: 0.3, fontSize: 9, fontFace: "Calibri",
      color: C.dim, align: "center", margin: 0,
    });
    if (i < 4) {
      s.addText("→", {
        x: st.x + 1.6, y: 1.1, w: 0.6, h: 0.7, fontSize: 20, fontFace: "Arial",
        color: C.dim, align: "center", valign: "middle", margin: 0,
      });
    }
  });
  // Key callout
  s.addShape(pres.shapes.RECTANGLE, {
    x: 2, y: 2.7, w: 6, h: 1.0,
    fill: { color: C.blue, transparency: 85 },
    line: { color: C.blue, width: 2.5 },
  });
  s.addText([
    { text: "Only 13 kW ", options: { fontSize: 24, bold: true, color: C.gold } },
    { text: "maintains 1 MJ stored energy at Q = 10⁹", options: { fontSize: 16, color: C.white } },
  ], {
    x: 2, y: 2.7, w: 6, h: 1.0, align: "center", valign: "middle", fontFace: "Calibri",
  });
  s.addText("A compact gas turbine (23 kg) provides all the power needed. No nuclear reactor required for Scenario C.", {
    x: 0.5, y: 4.0, w: 9, h: 0.5, fontSize: 12, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 21: FLIGHT PERFORMANCE ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Flight Performance: The Numbers", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const perfHeader = [
    [
      { text: "Destination", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 12 } },
      { text: "Chemical", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 12 } },
      { text: "Psi-Bubble (1g)", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 12 } },
      { text: "Improvement", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 12 } },
    ],
    ["Moon", "3 days", "3.5 hours", { text: "20×", options: { color: C.green, bold: true } }],
    ["Mars", "7 months", "2.7 days", { text: "78×", options: { color: C.green, bold: true } }],
    ["Jupiter", "6 years", "5 days", { text: "438×", options: { color: C.green, bold: true } }],
    ["Saturn", "7 years", "6.8 days", { text: "375×", options: { color: C.green, bold: true } }],
    ["Alpha Centauri", "75,000 years", "3.6 years", { text: "20,000×", options: { color: C.gold, bold: true } }],
  ];
  s.addTable(perfHeader, {
    x: 0.8, y: 0.8, w: 8.4, colW: [2.2, 2, 2.2, 2],
    border: { pt: 0.5, color: "2A3555" },
    fill: { color: C.midnavy },
    color: C.white, fontSize: 12, fontFace: "Calibri",
    rowH: [0.45, 0.45, 0.45, 0.45, 0.45, 0.45],
    align: "center", valign: "middle",
  });
  s.addText("Continuous 1g acceleration with flip-and-brake trajectory. No propellant mass ratio constraint.", {
    x: 0.5, y: 3.8, w: 9, h: 0.4, fontSize: 11, fontFace: "Calibri", color: C.dim, align: "center",
  });

  // --- SLIDE 22: VEHICLE SPECS ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Vehicle Specifications", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const specs = [
    ["Vehicle mass", "47,330 kg"],
    ["Payload fraction", "50 — 75%"],
    ["Shell dimensions", "12.3m × 10.3m (prolate spheroid)"],
    ["RF maintenance power", "13 kW"],
    ["Cavity Q-factor", "> 10⁹"],
    ["Thrust vectoring bandwidth", "2.4 kHz (electronic, no moving parts)"],
    ["Operating temperature", "77 K (liquid nitrogen)"],
    ["Crew capacity", "4 (crewed variant)"],
  ];
  const specTable = specs.map(([param, val]) => [
    { text: param, options: { color: C.dim, fontSize: 12 } },
    { text: val, options: { color: C.white, bold: true, fontSize: 12 } },
  ]);
  s.addTable(specTable, {
    x: 1.5, y: 0.8, w: 7, colW: [3, 4],
    border: { pt: 0.5, color: "2A3555" },
    fill: { color: C.midnavy },
    fontFace: "Calibri", rowH: [0.45],
    valign: "middle",
  });

  // --- SLIDE 23: INTERSTELLAR ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Interstellar Mission Profiles", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const interHeader = [
    [
      { text: "Destination", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
      { text: "Distance", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
      { text: "1g Ship Time", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
      { text: "10g Ship Time", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
    ],
    ["Alpha Centauri", "4.37 ly", "3.58 years", { text: "0.75 years", options: { color: C.gold, bold: true } }],
    ["Tau Ceti", "12 ly", "5.2 years", { text: "1.1 years", options: { color: C.gold, bold: true } }],
    ["Galactic Center", "26,000 ly", "19.8 years", { text: "2.4 years", options: { color: C.gold, bold: true } }],
    ["Andromeda Galaxy", "2.5M ly", "28.6 years", { text: "3.3 years", options: { color: C.gold, bold: true } }],
    [{ text: "Observable Universe", options: { bold: true } }, "46B ly", "48 years", { text: "5.2 years", options: { color: C.green, bold: true } }],
  ];
  s.addTable(interHeader, {
    x: 0.6, y: 0.8, w: 8.8, colW: [2.5, 1.8, 2.2, 2.3],
    border: { pt: 0.5, color: "2A3555" },
    fill: { color: C.midnavy },
    color: C.white, fontSize: 11, fontFace: "Calibri",
    rowH: [0.42], align: "center", valign: "middle",
  });
  s.addText("At 10g (which occupants don't feel), the observable universe is reachable in a human lifetime.", {
    x: 0.5, y: 3.7, w: 9, h: 0.5, fontSize: 13, fontFace: "Calibri", color: C.gold, align: "center", bold: true,
  });

  // ============================================================
  // ACT 4: THE OPPORTUNITY
  // ============================================================

  // --- SLIDE 24: SECTION DIVIDER ---
  s = pres.addSlide();
  darkBg(s);
  s.addImage({ data: icons.chart_gold, x: 4.5, y: 1.0, w: 1, h: 1 });
  s.addText("THE OPPORTUNITY", {
    x: 0.5, y: 2.2, w: 9, h: 0.8, fontSize: 36, fontFace: "Arial Black",
    color: C.white, align: "center", charSpacing: 6,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3.5, y: 3.1, w: 3, h: 0, line: { color: C.gold, width: 2 },
  });

  // --- SLIDE 25: COST REVOLUTION ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Cost Per Kilogram to LEO", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Manual bars (log scale visual)
  const costBars = [
    { label: "Falcon 9", val: "$2,720", w: 7.5, color: C.red },
    { label: "Starship (target)", val: "$100", w: 3.0, color: C.gold },
    { label: "Psi-Bubble", val: "~$1", w: 0.3, color: C.green },
  ];
  costBars.forEach((b, i) => {
    const y = 0.8 + i * 1.3;
    s.addText(b.label, {
      x: 0.5, y, w: 2.5, h: 0.4, fontSize: 14, fontFace: "Calibri",
      color: C.white, bold: true, align: "right", margin: 0,
    });
    s.addShape(pres.shapes.RECTANGLE, {
      x: 3.2, y: y + 0.45, w: b.w, h: 0.5,
      fill: { color: b.color, transparency: 20 },
    });
    s.addText(b.val, {
      x: 3.2, y: y + 0.45, w: b.w, h: 0.5, fontSize: 16, fontFace: "Calibri",
      color: C.white, align: "center", valign: "middle", bold: true, margin: 0,
    });
  });
  s.addText("2,720× cost reduction. The floor is the cost of electricity.", {
    x: 0.5, y: 4.7, w: 9, h: 0.4, fontSize: 14, fontFace: "Calibri", color: C.gold, align: "center", bold: true,
  });

  // --- SLIDE 26: PAYLOAD ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Payload Fraction Revolution", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Left pie
  s.addText("Chemical Rocket", {
    x: 0.5, y: 0.7, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri",
    color: C.red, align: "center", bold: true, margin: 0,
  });
  s.addChart(pres.charts.PIE, [{
    name: "Chemical", labels: ["Propellant", "Structure", "Payload"],
    values: [95, 3, 2],
  }], {
    x: 0.8, y: 1.2, w: 3.8, h: 2.8,
    chartColors: [C.red, "666666", C.blue],
    showPercent: true, showLegend: true, legendPos: "b",
    legendColor: C.dim, legendFontSize: 10,
    dataLabelColor: C.white, dataLabelFontSize: 11,
  });
  // Right pie
  s.addText("Psi-Bubble", {
    x: 5, y: 0.7, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri",
    color: C.green, align: "center", bold: true, margin: 0,
  });
  s.addChart(pres.charts.PIE, [{
    name: "Psi-Bubble", labels: ["Shell + Power", "PAYLOAD"],
    values: [25, 75],
  }], {
    x: 5.3, y: 1.2, w: 3.8, h: 2.8,
    chartColors: [C.blue, C.gold],
    showPercent: true, showLegend: true, legendPos: "b",
    legendColor: C.dim, legendFontSize: 10,
    dataLabelColor: C.white, dataLabelFontSize: 11,
  });
  s.addText("From 2% useful payload to 75%. A 37× improvement in what actually gets delivered.", {
    x: 0.5, y: 4.4, w: 9, h: 0.4, fontSize: 13, fontFace: "Calibri", color: C.gold, align: "center", bold: true,
  });

  // --- SLIDE 27: MARKET ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Total Addressable Market", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const mktHeader = [
    [
      { text: "Market", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
      { text: "10-Year", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
      { text: "20-Year", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
      { text: "50-Year", options: { fill: { color: C.blue }, color: "FFFFFF", bold: true, fontSize: 11 } },
    ],
    ["Satellite Launch", "$10B", "$75B", "$500B"],
    ["Space Tourism", "$5B", "$50B", "$5T"],
    ["Asteroid Mining", "$50B", "$500B", "$50T"],
    ["Mars Colonization", "$10B", "$200B", "$10T"],
    ["P2P Earth Transport", "$30B", "$150B", "$2T"],
    ["Military/Government", "$20B", "$50B", "$200B"],
    [
      { text: "TOTAL / year", options: { bold: true, color: C.gold } },
      { text: "$125B", options: { bold: true, color: C.gold } },
      { text: "~$1T", options: { bold: true, color: C.gold } },
      { text: "~$70T", options: { bold: true, color: C.gold } },
    ],
  ];
  s.addTable(mktHeader, {
    x: 0.8, y: 0.7, w: 8.4, colW: [2.4, 1.8, 1.8, 2.4],
    border: { pt: 0.5, color: "2A3555" },
    fill: { color: C.midnavy },
    color: C.white, fontSize: 11, fontFace: "Calibri",
    rowH: [0.4], align: "center", valign: "middle",
  });

  // --- SLIDE 28: IP ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Intellectual Property Landscape", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  s.addImage({ data: icons.lock_green, x: 4.5, y: 0.7, w: 0.7, h: 0.7 });
  s.addText("ALL PAIS / US NAVY PATENTS: EXPIRED", {
    x: 0.5, y: 1.5, w: 9, h: 0.6, fontSize: 24, fontFace: "Calibri",
    color: C.green, align: "center", bold: true,
  });
  s.addText("The only prior art portfolio for EM-gravitational propulsion is unenforceable.", {
    x: 1, y: 2.1, w: 8, h: 0.4, fontSize: 13, fontFace: "Calibri", color: C.dim, align: "center",
  });
  const ipItems = [
    "8 patentable innovation clusters identified",
    "Freedom to operate assessment: FAVORABLE",
    "3-year patent program: $135 — 240K",
    "Provisional filing recommended within 30 days",
  ];
  ipItems.forEach((item, i) => {
    const y = 2.8 + i * 0.45;
    s.addImage({ data: icons.check_blue, x: 2.5, y: y + 0.03, w: 0.3, h: 0.3 });
    s.addText(item, {
      x: 3.0, y, w: 5, h: 0.35, fontSize: 13, fontFace: "Calibri",
      color: C.white, margin: 0,
    });
  });

  // --- SLIDE 29: WHY SPACEX ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Why SpaceX / Musk Portfolio", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const companies = [
    { name: "SpaceX", items: ["Vehicle manufacturing", "Flight operations", "Regulatory expertise", "Rapid iteration culture"], color: C.blue, x: 0.5 },
    { name: "Tesla", items: ["Power electronics", "Battery technology", "Thermal management", "Manufacturing at scale"], color: C.gold, x: 3.5 },
    { name: "Boring Co", items: ["Ground infrastructure", "P2P transport terminals", "Regulatory navigation", "Public-private partnerships"], color: C.green, x: 6.5 },
  ];
  companies.forEach(co => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: co.x, y: 0.7, w: 2.8, h: 3.2,
      fill: { color: co.color, transparency: 88 },
      line: { color: co.color, width: 1.5 },
    });
    s.addText(co.name, {
      x: co.x, y: 0.8, w: 2.8, h: 0.5, fontSize: 18, fontFace: "Calibri",
      color: co.color, align: "center", bold: true, margin: 0,
    });
    co.items.forEach((item, i) => {
      s.addText("•  " + item, {
        x: co.x + 0.2, y: 1.4 + i * 0.45, w: 2.4, h: 0.35, fontSize: 11, fontFace: "Calibri",
        color: C.white, margin: 0,
      });
    });
  });
  s.addText("Execution capability, not chemistry, is SpaceX's moat. This technology IS the successor to chemical rockets.", {
    x: 0.5, y: 4.2, w: 9, h: 0.6, fontSize: 13, fontFace: "Calibri", color: C.gold, align: "center", bold: true,
  });

  // --- SLIDE 30: DECISION TREE ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Decision", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 28, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Option A
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: 0.8, w: 3, h: 1.5,
    fill: { color: C.red, transparency: 80 }, line: { color: C.red, width: 1.5 },
  });
  s.addText("Do Nothing", {
    x: 0.5, y: 0.85, w: 3, h: 0.5, fontSize: 16, fontFace: "Calibri",
    color: C.red, align: "center", bold: true, margin: 0,
  });
  s.addText("Risk being disrupted.\nSpaceX becomes Kodak.", {
    x: 0.5, y: 1.35, w: 3, h: 0.7, fontSize: 11, fontFace: "Calibri",
    color: C.dim, align: "center", margin: 0,
  });
  // Option B
  s.addShape(pres.shapes.RECTANGLE, {
    x: 3.7, y: 0.8, w: 3, h: 1.5,
    fill: { color: C.green, transparency: 80 }, line: { color: C.green, width: 1.5 },
  });
  s.addText("Fund Phase 0: $2—4M", {
    x: 3.7, y: 0.85, w: 3, h: 0.5, fontSize: 14, fontFace: "Calibri",
    color: C.green, align: "center", bold: true, margin: 0,
  });
  s.addText("Null → lose $4M.\nPositive → proceed to Phase 1.", {
    x: 3.7, y: 1.35, w: 3, h: 0.7, fontSize: 11, fontFace: "Calibri",
    color: C.dim, align: "center", margin: 0,
  });
  // EV box
  s.addShape(pres.shapes.RECTANGLE, {
    x: 6.9, y: 0.8, w: 2.8, h: 1.5,
    fill: { color: C.gold, transparency: 70 }, line: { color: C.gold, width: 2 },
  });
  s.addText("Expected Value", {
    x: 6.9, y: 0.85, w: 2.8, h: 0.4, fontSize: 12, fontFace: "Calibri",
    color: C.gold, align: "center", bold: true, margin: 0,
  });
  s.addText("$10\nBILLION", {
    x: 6.9, y: 1.2, w: 2.8, h: 0.8, fontSize: 22, fontFace: "Arial Black",
    color: C.white, align: "center", valign: "middle",
  });
  s.addText("at just 0.1% probability of success", {
    x: 6.9, y: 2.0, w: 2.8, h: 0.3, fontSize: 9, fontFace: "Calibri",
    color: C.dim, align: "center", margin: 0,
  });
  // Roadmap
  s.addText("Development Roadmap", {
    x: 0.5, y: 2.7, w: 9, h: 0.4, fontSize: 16, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const phases = [
    { label: "Phase 0\nSQMS", cost: "$2—4M", dur: "1—2 yr", color: C.blue, w: 1.2 },
    { label: "Phase 1\nLab Demo", cost: "$10—50M", dur: "2—3 yr", color: C.green, w: 1.8 },
    { label: "Phase 2\nSubscale", cost: "$100—500M", dur: "3—5 yr", color: C.gold, w: 2.5 },
    { label: "Phase 3\nFull Vehicle", cost: "$1—5B", dur: "5—10 yr", color: C.white, w: 3.2 },
  ];
  let phX = 0.5;
  phases.forEach(ph => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: phX, y: 3.2, w: ph.w, h: 0.8,
      fill: { color: ph.color, transparency: 70 },
      line: { color: ph.color, width: 1 },
    });
    s.addText(ph.label, {
      x: phX, y: 3.2, w: ph.w, h: 0.5, fontSize: 9, fontFace: "Calibri",
      color: C.white, align: "center", bold: true, margin: 0,
    });
    s.addText(`${ph.cost} | ${ph.dur}`, {
      x: phX, y: 3.7, w: ph.w, h: 0.25, fontSize: 8, fontFace: "Calibri",
      color: C.dim, align: "center", margin: 0,
    });
    phX += ph.w + 0.1;
  });

  // --- SLIDE 31: THE ASK ---
  s = pres.addSlide();
  darkBg(s);
  s.addImage({ data: icons.flask_gold, x: 4.5, y: 0.6, w: 0.8, h: 0.8 });
  s.addText("The Ask", {
    x: 0.5, y: 1.5, w: 9, h: 0.6, fontSize: 32, fontFace: "Calibri",
    color: C.white, align: "center", bold: true,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3.5, y: 2.2, w: 3, h: 0, line: { color: C.gold, width: 2 },
  });
  s.addText("Fund the $200K MAGO parasitic experiment.", {
    x: 0.5, y: 2.6, w: 9, h: 0.6, fontSize: 22, fontFace: "Calibri",
    color: C.gold, align: "center", bold: true,
  });
  s.addText("Or the $10M dedicated SQMS measurement.", {
    x: 0.5, y: 3.2, w: 9, h: 0.5, fontSize: 18, fontFace: "Calibri",
    color: C.blue, align: "center",
  });
  s.addText("Either one answers the question definitively.", {
    x: 0.5, y: 4.0, w: 9, h: 0.5, fontSize: 16, fontFace: "Calibri",
    color: C.white, align: "center",
  });

  // ============================================================
  // ACT 5: CLOSE
  // ============================================================

  // --- SLIDE 32: KEY NUMBERS ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("Key Numbers at a Glance", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Calibri",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  const keyNums = [
    ["Classical coupling", "10⁻⁴⁴ m/J"],
    ["Enhanced coupling (full stack)", "10⁻¹⁷ m/J"],
    ["Energy for 1g (N scaling)", "~7 J"],
    ["Earth—Mars transit", "2.7 days"],
    ["Cost per kg to LEO", "~$1"],
    ["Prototype cost", "$1.2 — 3.1B"],
    ["Production cost", "$130 — 280M / unit"],
    ["Phase 0 experiment", "$2 — 4M"],
    ["TAM (50 year)", "$70T / year"],
    ["EV of Phase 0 at 0.1%", "$10 billion"],
  ];
  const knTable = keyNums.map(([p, v]) => [
    { text: p, options: { color: C.dim, fontSize: 12 } },
    { text: v, options: { color: C.white, bold: true, fontSize: 12 } },
  ]);
  s.addTable(knTable, {
    x: 1.5, y: 0.7, w: 7, colW: [3.5, 3.5],
    border: { pt: 0.5, color: "2A3555" },
    fill: { color: C.midnavy },
    fontFace: "Calibri", rowH: [0.4], valign: "middle",
  });

  // --- SLIDE 33: THE STAKES ---
  s = pres.addSlide();
  darkBg(s);
  s.addText("If this works, it is the most\nimportant technology\nin human history.", {
    x: 0.5, y: 0.8, w: 9, h: 2.2, fontSize: 30, fontFace: "Calibri",
    color: C.white, align: "center", valign: "middle", bold: true,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3, y: 3.2, w: 4, h: 0, line: { color: C.gold, width: 2 },
  });
  s.addText("If it doesn't, you lost less than\na fighter jet's landing gear.", {
    x: 0.5, y: 3.5, w: 9, h: 1.0, fontSize: 20, fontFace: "Calibri",
    color: C.gold, align: "center", valign: "middle",
  });

  // --- SLIDE 34: FINAL ---
  s = pres.addSlide();
  darkBg(s);
  // Subtle circles again
  for (let r = 3; r >= 0.5; r -= 0.5) {
    const t = Math.round(92 - r * 10);
    s.addShape(pres.shapes.OVAL, {
      x: 5 - r, y: 2.0 - r, w: r * 2, h: r * 2,
      fill: { color: C.blue, transparency: t },
    });
  }
  s.addText("∇²ψ  =  (4πG / c²) · ρ_eff · μ(ψ)", {
    x: 0.5, y: 1.5, w: 9, h: 0.8, fontSize: 26, fontFace: "Calibri",
    color: C.white, align: "center", bold: true,
  });
  s.addShape(pres.shapes.LINE, {
    x: 3, y: 2.5, w: 4, h: 0, line: { color: C.gold, width: 2 },
  });
  s.addText("The door is constrained but not locked.", {
    x: 0.5, y: 2.8, w: 9, h: 0.6, fontSize: 20, fontFace: "Calibri",
    color: C.gold, align: "center", italic: true,
  });
  s.addText("Gary Thomas Alcock", {
    x: 0.5, y: 3.8, w: 9, h: 0.4, fontSize: 14, fontFace: "Calibri",
    color: C.white, align: "center",
  });
  s.addText("Density Field Dynamics  |  densityfielddynamics.com", {
    x: 0.5, y: 4.2, w: 9, h: 0.35, fontSize: 11, fontFace: "Calibri",
    color: C.dim, align: "center",
  });
  s.addText("Technical appendix: 15-page Physical Review paper  •  12 engineering schematics  •  7 simulation codes  •  Complete IP analysis", {
    x: 0.5, y: 4.8, w: 9, h: 0.3, fontSize: 9, fontFace: "Calibri",
    color: C.dim, align: "center",
  });

  // ===== SAVE =====
  await pres.writeFile({ fileName: "/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/presentation/DFD_Psi_Bubble_Propulsion_Deck.pptx" });
  console.log("Deck saved: DFD_Psi_Bubble_Propulsion_Deck.pptx");
}

main().catch(err => { console.error(err); process.exit(1); });
