const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const path = require("path");
const { FaCheckCircle } = require("react-icons/fa");

function renderIconSvg(IconComponent, color, size = 256) {
  return ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
}
async function iconPng(IconComponent, color, size = 256) {
  const svg = renderIconSvg(IconComponent, color, size);
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

const IMG = (name) => path.join(__dirname, "images", name);

async function main() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10" x 5.625"
  pres.author = "Gary Thomas Alcock";
  pres.title = "Psi-Bubble Propulsion";

  // Premium palette — muted, sophisticated
  const C = {
    bg: "080E1A",       // near-black navy
    card: "0F1628",     // slightly lighter card bg
    accent: "4EA8DE",   // muted steel blue (NOT childish cyan)
    gold: "C8963E",     // muted warm gold (NOT neon yellow)
    white: "EAEAEA",
    dim: "6B7A94",
    red: "C0392B",
    green: "27AE60",
    midgray: "2A3550",
  };

  const checkIcon = await iconPng(FaCheckCircle, "#27AE60");

  // Helper: photo background with dark overlay
  function photoBg(slide, imgFile, overlayOpacity) {
    slide.background = { path: IMG(imgFile) };
    slide.addShape(pres.shapes.RECTANGLE, {
      x: 0, y: 0, w: 10, h: 5.625,
      fill: { color: "000000", transparency: 100 - overlayOpacity },
    });
  }

  // Helper: solid dark bg
  function darkBg(slide) { slide.background = { color: C.bg }; }

  // Helper: thin gold accent line
  function goldLine(slide, y) {
    slide.addShape(pres.shapes.LINE, {
      x: 3.8, y, w: 2.4, h: 0, line: { color: C.gold, width: 1.5 },
    });
  }

  // Helper: bottom dim caption
  function caption(slide, text) {
    slide.addText(text, {
      x: 0.8, y: 4.9, w: 8.4, h: 0.4, fontSize: 10, fontFace: "Georgia",
      color: C.dim, align: "center", italic: true,
    });
  }

  let s;

  // ============================================================
  // SLIDE 1: TITLE
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "space_stars.jpg", 70);
  s.addText("PSI-BUBBLE", {
    x: 0.8, y: 1.0, w: 8.4, h: 1.0, fontSize: 48, fontFace: "Georgia",
    color: C.white, align: "center", bold: true,
  });
  s.addText("PROPULSION", {
    x: 0.8, y: 1.85, w: 8.4, h: 0.8, fontSize: 40, fontFace: "Georgia",
    color: C.gold, align: "center",
  });
  goldLine(s, 2.75);
  s.addText("Engineering the Next Age of Space Travel", {
    x: 0.8, y: 3.0, w: 8.4, h: 0.5, fontSize: 16, fontFace: "Georgia",
    color: C.dim, align: "center", italic: true,
  });
  s.addText("Gary Thomas Alcock  |  Density Field Dynamics", {
    x: 0.8, y: 3.8, w: 8.4, h: 0.4, fontSize: 12, fontFace: "Calibri Light",
    color: C.dim, align: "center",
  });

  // ============================================================
  // SLIDE 2: THE PROBLEM — 95%
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "rocket_launch.jpg", 75);
  s.addText("95%", {
    x: 0.5, y: 0.5, w: 9, h: 2.8, fontSize: 140, fontFace: "Georgia",
    color: C.red, align: "center", valign: "middle", bold: true,
  });
  s.addText("of every rocket is thrown away", {
    x: 0.5, y: 3.1, w: 9, h: 0.6, fontSize: 26, fontFace: "Georgia",
    color: C.white, align: "center",
  });
  caption(s, "Tsiolkovsky's equation constrains all chemical propulsion. This has been true for 100 years.");

  // ============================================================
  // SLIDE 3: COST BAR CHART
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Cost of Access to Space", {
    x: 0.8, y: 0.2, w: 8.4, h: 0.5, fontSize: 24, fontFace: "Georgia",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  s.addChart(pres.charts.BAR, [{
    name: "$/kg to LEO",
    labels: ["SLS", "Atlas V", "Falcon 9", "Falcon Heavy", "Starship\n(target)"],
    values: [20000, 13200, 2720, 1500, 100],
  }], {
    x: 0.8, y: 0.9, w: 8.4, h: 4.0, barDir: "col",
    chartColors: [C.red, "A0522D", C.gold, "6B8E23", C.green],
    chartArea: { fill: { color: C.card }, roundedCorners: true },
    catAxisLabelColor: C.dim, catAxisLabelFontSize: 10, catAxisLabelFontFace: "Calibri Light",
    valAxisLabelColor: C.dim, valAxisLabelFontSize: 9,
    valGridLine: { color: C.midgray, size: 0.5 },
    catGridLine: { style: "none" },
    showValue: true, dataLabelPosition: "outEnd", dataLabelColor: C.white,
    dataLabelFontSize: 10, showLegend: false,
    valAxisNumFmt: "$#,##0",
  });
  caption(s, "Even Starship's revolutionary $100/kg is bounded by propellant mass fraction.");

  // ============================================================
  // SLIDE 4: THE TIME
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "mars.jpg", 78);
  const timeData = [
    ["Earth to Mars", "7 months", 0.8],
    ["Earth to Jupiter", "6 years", 1.8],
    ["Nearest star", "75,000 years", 2.8],
  ];
  timeData.forEach(([label, time, y]) => {
    s.addText(label, {
      x: 0.8, y, w: 4, h: 0.7, fontSize: 20, fontFace: "Georgia",
      color: C.dim, align: "right", valign: "middle", margin: 0,
    });
    s.addText(time, {
      x: 5.0, y, w: 4, h: 0.7, fontSize: 32, fontFace: "Georgia",
      color: C.red, align: "left", valign: "middle", bold: true, margin: 0,
    });
  });
  caption(s, "Chemical propulsion makes the solar system large and the galaxy unreachable.");

  // ============================================================
  // SLIDE 5: BREAKTHROUGH
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "earth_space.jpg", 72);
  s.addText("What if you didn't need\npropellant at all?", {
    x: 0.8, y: 1.2, w: 8.4, h: 1.5, fontSize: 32, fontFace: "Georgia",
    color: C.white, align: "center", bold: true,
  });
  goldLine(s, 2.9);
  s.addText("A propulsion system that modifies the local gravitational field\nrequires zero reaction mass.", {
    x: 1.5, y: 3.2, w: 7, h: 0.8, fontSize: 15, fontFace: "Georgia",
    color: C.accent, align: "center", italic: true,
  });

  // ============================================================
  // SLIDE 6: THE DEVICE
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Ferrite-Superconductor Resonant Shell", {
    x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia",
    color: C.white, bold: true, align: "center", margin: 0,
  });
  // Visual shell diagram using shapes
  s.addShape(pres.shapes.OVAL, { x: 2.2, y: 0.8, w: 5.6, h: 3.5, fill: { color: C.gold, transparency: 82 }, line: { color: C.gold, width: 2.5 } });
  s.addShape(pres.shapes.OVAL, { x: 2.8, y: 1.15, w: 4.4, h: 2.8, fill: { color: C.accent, transparency: 82 }, line: { color: C.accent, width: 2.5 } });
  s.addShape(pres.shapes.OVAL, { x: 3.4, y: 1.5, w: 3.2, h: 2.1, fill: { color: C.bg, transparency: 20 }, line: { color: C.dim, width: 0.5 } });
  s.addText("PAYLOAD\nZero g-force", { x: 3.8, y: 2.1, w: 2.4, h: 0.8, fontSize: 11, fontFace: "Calibri Light", color: C.white, align: "center", margin: 0 });
  // Labels
  s.addText("Ferrite\n(ε ≈ μ matched)", { x: 7.9, y: 1.0, w: 1.8, h: 0.5, fontSize: 10, fontFace: "Calibri Light", color: C.gold, margin: 0 });
  s.addText("Superconductor\n(s-wave: Nb, MgB₂)", { x: 7.9, y: 1.8, w: 1.8, h: 0.5, fontSize: 10, fontFace: "Calibri Light", color: C.accent, margin: 0 });
  s.addText("Rotating EM ↻", { x: 7.9, y: 2.6, w: 1.8, h: 0.3, fontSize: 10, fontFace: "Calibri Light", color: C.white, margin: 0 });
  s.addText("ψ gradient →", { x: 0.3, y: 2.3, w: 1.8, h: 0.3, fontSize: 10, fontFace: "Calibri Light", color: C.gold, bold: true, margin: 0 });
  // Bottom
  s.addText([
    { text: "Ferrite ", options: { color: C.gold, bold: true } },
    { text: "stores EM energy at maximum density     ", options: { color: C.dim } },
    { text: "Superconductor ", options: { color: C.accent, bold: true } },
    { text: "provides quantum coherence (10²³ Cooper pairs)", options: { color: C.dim } },
  ], { x: 0.5, y: 4.6, w: 9, h: 0.5, fontSize: 10, fontFace: "Calibri Light", align: "center" });

  // ============================================================
  // SLIDE 7: HOW IT WORKS
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("How It Works", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const steps = [
    { label: "EM Energy\nInput", sub: "RF power into\nresonant cavity", color: C.accent, x: 0.3 },
    { label: "ψ Field\nModification", sub: "Cooper pairs modify\nlocal ψ density", color: C.gold, x: 2.7 },
    { label: "Gravitational\nGradient", sub: "Asymmetric ∇ψ\nproduces net force", color: C.green, x: 5.1 },
    { label: "Propellantless\nAcceleration", sub: "Vehicle accelerates\nwithout exhaust", color: C.white, x: 7.5 },
  ];
  steps.forEach((st, i) => {
    s.addShape(pres.shapes.RECTANGLE, { x: st.x, y: 1.0, w: 2.1, h: 1.4, fill: { color: st.color, transparency: 85 }, line: { color: st.color, width: 1.5 } });
    s.addText(st.label, { x: st.x, y: 1.05, w: 2.1, h: 0.85, fontSize: 13, fontFace: "Calibri Light", color: C.white, align: "center", valign: "middle", bold: true, margin: 0 });
    s.addText(st.sub, { x: st.x, y: 2.6, w: 2.1, h: 0.5, fontSize: 9, fontFace: "Calibri Light", color: C.dim, align: "center", margin: 0 });
    if (i < 3) s.addText("→", { x: st.x + 2.1, y: 1.2, w: 0.6, h: 0.8, fontSize: 24, fontFace: "Georgia", color: C.dim, align: "center", valign: "middle", margin: 0 });
  });
  s.addText([
    { text: "The EM field is the fuel. ", options: { color: C.accent, bold: true } },
    { text: "The cavity is the engine. There is no exhaust.", options: { color: C.white } },
  ], { x: 0.5, y: 4.0, w: 9, h: 0.5, fontSize: 14, fontFace: "Georgia", align: "center" });

  // ============================================================
  // SLIDE 8: ZERO G
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "dark_abstract.jpg", 80);
  s.addText("Zero g-forces on occupants.\nAt any acceleration.", {
    x: 0.8, y: 0.8, w: 8.4, h: 1.4, fontSize: 28, fontFace: "Georgia",
    color: C.white, align: "center", valign: "middle", bold: true,
  });
  s.addText("All matter inside accelerates identically — exactly like gravitational freefall.", {
    x: 1, y: 2.4, w: 8, h: 0.4, fontSize: 13, fontFace: "Georgia", color: C.accent, align: "center", italic: true,
  });
  const gComp = [
    ["Chemical rocket at 10g:", "crew is crushed", C.red],
    ["Psi-bubble at 10g:", "crew feels nothing", C.green],
    ["Psi-bubble at 1,000g:", "crew still feels nothing", C.green],
  ];
  gComp.forEach(([label, result, col], i) => {
    s.addText(label, { x: 1.5, y: 3.2 + i * 0.5, w: 3.8, h: 0.4, fontSize: 13, fontFace: "Calibri Light", color: C.dim, align: "right", margin: 0 });
    s.addText(result, { x: 5.5, y: 3.2 + i * 0.5, w: 3, h: 0.4, fontSize: 13, fontFace: "Calibri Light", color: col, align: "left", bold: true, margin: 0 });
  });

  // ============================================================
  // SLIDE 9: PHYSICS SECTION DIVIDER
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "dark_abstract.jpg", 85);
  s.addText("THE PHYSICS", {
    x: 0.5, y: 1.8, w: 9, h: 0.9, fontSize: 36, fontFace: "Georgia",
    color: C.white, align: "center", bold: true,
  });
  goldLine(s, 2.85);
  s.addText("Three enhancement mechanisms close a 44-order-of-magnitude gap", {
    x: 1, y: 3.1, w: 8, h: 0.5, fontSize: 14, fontFace: "Georgia",
    color: C.dim, align: "center", italic: true,
  });

  // ============================================================
  // SLIDE 10: FIELD EQUATION
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Master Equation", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  s.addShape(pres.shapes.RECTANGLE, { x: 1.5, y: 0.8, w: 7, h: 1.1, fill: { color: C.card }, line: { color: C.accent, width: 2 } });
  s.addText("∇²ψ  =  (4πG / c²) · ρ_eff · μ(ψ)", {
    x: 1.5, y: 0.8, w: 7, h: 1.1, fontSize: 26, fontFace: "Georgia", color: C.white, align: "center", valign: "middle", bold: true,
  });
  const terms = [
    { label: "∇²ψ", desc: "Curvature of ψ field", color: C.accent },
    { label: "4πG/c²", desc: "Gravitational coupling", color: C.accent },
    { label: "ρ_eff", desc: "Energy density (incl. EM)", color: C.gold },
    { label: "μ(ψ)", desc: "MOND nonlinear response", color: C.red },
  ];
  terms.forEach((t, i) => {
    const x = 0.5 + i * 2.35;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 2.2, w: 2.15, h: 0.9, fill: { color: t.color, transparency: 87 }, line: { color: t.color, width: 1 } });
    s.addText(t.label, { x, y: 2.2, w: 2.15, h: 0.45, fontSize: 14, fontFace: "Georgia", color: C.white, align: "center", bold: true, margin: 0 });
    s.addText(t.desc, { x, y: 2.6, w: 2.15, h: 0.4, fontSize: 9, fontFace: "Calibri Light", color: C.dim, align: "center", margin: 0 });
  });
  caption(s, "DFD generalizes Newtonian gravity: EM energy density directly sources the gravitational potential.");

  // ============================================================
  // SLIDE 11: 10^-44
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Coupling Problem", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  s.addText("10⁻⁴⁴", { x: 0.5, y: 0.7, w: 9, h: 2.2, fontSize: 96, fontFace: "Georgia", color: C.red, align: "center", valign: "middle", bold: true });
  s.addText("m/J — gravitational effect per joule of electromagnetic energy", { x: 1, y: 2.9, w: 8, h: 0.4, fontSize: 13, fontFace: "Calibri Light", color: C.dim, align: "center" });
  s.addText("This is why everyone assumed it was impossible.", { x: 1, y: 3.6, w: 8, h: 0.5, fontSize: 18, fontFace: "Georgia", color: C.white, align: "center", bold: true });
  s.addText("But this is the classical, incoherent coupling. Three mechanisms change everything.", { x: 1, y: 4.2, w: 8, h: 0.4, fontSize: 12, fontFace: "Georgia", color: C.accent, align: "center", italic: true });

  // ============================================================
  // SLIDE 12: QUANTUM COHERENCE
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Enhancement 1: Quantum Coherence", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  // Two panels
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.8, w: 4.2, h: 2.2, fill: { color: C.card }, line: { color: C.dim, width: 1 } });
  s.addText("Normal Matter", { x: 0.5, y: 0.85, w: 4.2, h: 0.35, fontSize: 13, fontFace: "Georgia", color: C.dim, align: "center", bold: true, margin: 0 });
  s.addText("↗  ←  ↙  →  ↖  ↓  ↘  ↑\n→  ↙  ↗  ←  ↖  ↓  ↗  ↘\n←  ↑  →  ↙  ↘  ↗  ↓  ←", { x: 0.7, y: 1.3, w: 3.8, h: 1.2, fontSize: 16, fontFace: "Consolas", color: C.dim, align: "center", valign: "middle" });
  s.addShape(pres.shapes.RECTANGLE, { x: 5.3, y: 0.8, w: 4.2, h: 2.2, fill: { color: C.card }, line: { color: C.accent, width: 1.5 } });
  s.addText("Cooper Pair Condensate", { x: 5.3, y: 0.85, w: 4.2, h: 0.35, fontSize: 13, fontFace: "Georgia", color: C.accent, align: "center", bold: true, margin: 0 });
  s.addText("→  →  →  →  →  →  →  →\n→  →  →  →  →  →  →  →\n→  →  →  →  →  →  →  →", { x: 5.5, y: 1.3, w: 3.8, h: 1.2, fontSize: 16, fontFace: "Consolas", color: C.accent, align: "center", valign: "middle" });
  s.addText("⟹", { x: 4.3, y: 1.5, w: 1.4, h: 0.5, fontSize: 28, fontFace: "Georgia", color: C.gold, align: "center", margin: 0 });
  s.addText("T < Tc", { x: 4.35, y: 1.2, w: 1.3, h: 0.3, fontSize: 10, fontFace: "Calibri Light", color: C.gold, align: "center", bold: true, margin: 0 });
  s.addText("Enhancement:  10¹²  —  10²⁷", { x: 0.5, y: 3.3, w: 9, h: 0.5, fontSize: 26, fontFace: "Georgia", color: C.gold, align: "center", bold: true });
  caption(s, "N ~ 10²³ particles acting as one quantum system. Phases add coherently, not randomly.");

  // ============================================================
  // SLIDE 13: MOND
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Enhancement 2: MOND Nonlinearity", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 0.8, w: 5.2, h: 3.0, fill: { color: C.card }, line: { color: C.dim, width: 1 } });
  s.addText("μ(x)\n\n  1.0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\n                      ╱\n                   ╱\n                ╱\n            ╱\n         ╱\n      ╱\n   ╱\n  0 ───────────────────── x\n      MOND        Newtonian", {
    x: 0.9, y: 0.8, w: 5, h: 3.0, fontSize: 10, fontFace: "Consolas", color: C.accent, valign: "top", margin: 8,
  });
  s.addShape(pres.shapes.RECTANGLE, { x: 6.5, y: 0.8, w: 3, h: 1.3, fill: { color: C.gold, transparency: 87 }, line: { color: C.gold, width: 1.5 } });
  s.addText("Deep Space\nAdvantage", { x: 6.5, y: 0.85, w: 3, h: 0.6, fontSize: 16, fontFace: "Georgia", color: C.gold, align: "center", bold: true, margin: 0 });
  s.addText("10 — 1,000×", { x: 6.5, y: 1.5, w: 3, h: 0.4, fontSize: 14, fontFace: "Calibri Light", color: C.white, align: "center", margin: 0 });
  s.addShape(pres.shapes.RECTANGLE, { x: 6.5, y: 2.3, w: 3, h: 0.7, fill: { color: C.accent, transparency: 88 }, line: { color: C.accent, width: 1 } });
  s.addText("Device works BETTER\nfar from massive bodies", { x: 6.5, y: 2.3, w: 3, h: 0.7, fontSize: 11, fontFace: "Georgia", color: C.white, align: "center", margin: 0 });

  // ============================================================
  // SLIDE 14: PARAMETRIC
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Enhancement 3: Parametric Amplification", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  s.addShape(pres.shapes.RECTANGLE, { x: 1.5, y: 0.8, w: 7, h: 2.4, fill: { color: C.card }, line: { color: C.green, width: 1.5 } });
  s.addText("Cavity Q  >  10⁹", { x: 2, y: 1.0, w: 6, h: 0.5, fontSize: 22, fontFace: "Georgia", color: C.green, bold: true, margin: 0 });
  s.addText("Superconducting cavity walls (REBCO at 77K) achieve quality\nfactors exceeding one billion. Energy recirculates 10⁹ times\nbefore dissipating. Parametric coupling between EM modes\nand the ψ field is amplified by cavity resonance.", {
    x: 2, y: 1.6, w: 6, h: 1.2, fontSize: 12, fontFace: "Calibri Light", color: C.dim, margin: 0,
  });
  s.addText("Parametric Gain:  500  —  10⁵", { x: 0.5, y: 3.5, w: 9, h: 0.5, fontSize: 26, fontFace: "Georgia", color: C.green, align: "center", bold: true });

  // ============================================================
  // SLIDE 15: ENHANCEMENT BUDGET WATERFALL
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Total Enhancement Budget", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const wf = [
    { label: "Classical coupling", val: "10⁻⁴⁴", color: C.red, barW: 0.4 },
    { label: "+ Quantum coherence", val: "+20 orders", color: C.accent, barW: 3.2 },
    { label: "+ MOND nonlinearity", val: "+3 orders", color: C.gold, barW: 0.5 },
    { label: "+ Parametric amplification", val: "+4 orders", color: C.green, barW: 0.65 },
    { label: "= Effective coupling", val: "10⁻¹⁷", color: C.white, barW: 4.75 },
  ];
  let cumX = 0.8;
  wf.forEach((w, i) => {
    const y = 0.8 + i * 0.7;
    if (i < 4) {
      s.addShape(pres.shapes.RECTANGLE, { x: cumX, y, w: w.barW, h: 0.45, fill: { color: w.color, transparency: 30 } });
      if (i > 0) cumX += w.barW;
    } else {
      s.addShape(pres.shapes.RECTANGLE, { x: 0.8, y, w: w.barW, h: 0.45, fill: { color: C.white, transparency: 80 }, line: { color: C.white, width: 1.5 } });
    }
    s.addText(w.label, { x: 6, y, w: 2.3, h: 0.45, fontSize: 11, fontFace: "Calibri Light", color: w.color, align: "left", valign: "middle", bold: true, margin: 0 });
    s.addText(w.val, { x: 8.3, y, w: 1.2, h: 0.45, fontSize: 12, fontFace: "Georgia", color: C.white, align: "right", valign: "middle", bold: true, margin: 0 });
  });
  // threshold line
  s.addShape(pres.shapes.LINE, { x: 4.5, y: 0.8, w: 0, h: 3.5, line: { color: C.gold, width: 1, dashType: "dash" } });
  s.addText("← Propulsion\n   threshold", { x: 4.6, y: 1.8, w: 1.2, h: 0.5, fontSize: 8, fontFace: "Calibri Light", color: C.gold, margin: 0 });
  s.addText("27 orders of magnitude recovered. The gap from impossible to measurable is closed.", { x: 0.5, y: 4.3, w: 9, h: 0.4, fontSize: 13, fontFace: "Georgia", color: C.accent, align: "center" });

  // ============================================================
  // SLIDE 16: SELF CONSISTENCY
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Rigorously Proven", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const checks = [
    ["Convergence: 10⁻³³", "Exact to 33 decimal places"],
    ["All eigenfrequencies stable", "No runaway instabilities"],
    ["Energy conservation proven", "Via Noether's theorem"],
    ["Momentum: ψ-wave radiation", "Not reactionless — has \"exhaust\""],
  ];
  checks.forEach((c, i) => {
    s.addImage({ data: checkIcon, x: 0.8, y: 0.85 + i * 0.95, w: 0.3, h: 0.3 });
    s.addText(c[0], { x: 1.3, y: 0.8 + i * 0.95, w: 8, h: 0.35, fontSize: 16, fontFace: "Georgia", color: C.white, bold: true, margin: 0 });
    s.addText(c[1], { x: 1.3, y: 1.15 + i * 0.95, w: 8, h: 0.25, fontSize: 11, fontFace: "Calibri Light", color: C.dim, margin: 0 });
  });
  s.addShape(pres.shapes.RECTANGLE, { x: 1.2, y: 4.5, w: 7.6, h: 0.45, fill: { color: C.red, transparency: 82 }, line: { color: C.red, width: 1 } });
  s.addText("NOT perpetual motion.  NOT reactionless.  Thermodynamically legal.", { x: 1.2, y: 4.5, w: 7.6, h: 0.45, fontSize: 11, fontFace: "Calibri Light", color: C.white, align: "center", valign: "middle", bold: true });

  // ============================================================
  // SLIDE 17: ENGINEERING SECTION
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "circuit.jpg", 82);
  s.addText("THE ENGINEERING", { x: 0.5, y: 1.8, w: 9, h: 0.9, fontSize: 36, fontFace: "Georgia", color: C.white, align: "center", bold: true });
  goldLine(s, 2.85);
  s.addText("Complete specifications for a buildable device", { x: 1, y: 3.1, w: 8, h: 0.5, fontSize: 14, fontFace: "Georgia", color: C.dim, align: "center", italic: true });

  // ============================================================
  // SLIDE 18: SHELL LAYERS
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Shell Architecture", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const layers = [
    { name: "YBCO Superconductor", dim: "5 mm", color: C.accent, h: 0.32 },
    { name: "MgO Buffer Layer", dim: "3 mm", color: C.dim, h: 0.22 },
    { name: "YIG Ferrite", dim: "50 mm", color: C.gold, h: 1.1 },
    { name: "CFRP Overwrap", dim: "25 mm", color: "445566", h: 0.6 },
    { name: "Aluminum Skin", dim: "5 mm", color: "8899AA", h: 0.32 },
  ];
  let ly = 0.8;
  layers.forEach(l => {
    s.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: ly, w: 5.5, h: l.h, fill: { color: l.color, transparency: 40 }, line: { color: l.color, width: 1 } });
    s.addText(l.name, { x: 1.0, y: ly, w: 3, h: l.h, fontSize: 11, fontFace: "Calibri Light", color: C.white, valign: "middle", bold: true, margin: 0 });
    s.addText(l.dim, { x: 6.6, y: ly, w: 1, h: l.h, fontSize: 11, fontFace: "Georgia", color: C.white, valign: "middle", align: "center", bold: true, margin: 0 });
    ly += l.h + 0.06;
  });
  s.addText("Total: 88 mm  |  Shell: 126,530 kg  |  Vehicle: 47,330 kg", { x: 0.5, y: 3.5, w: 9, h: 0.35, fontSize: 12, fontFace: "Georgia", color: C.accent, align: "center" });

  // ============================================================
  // SLIDE 19: POWER — KEY NUMBER
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Power Architecture", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const pSteps = [
    { label: "Reactor", color: C.red },
    { label: "Turbine", color: C.gold },
    { label: "RF Amps", color: C.green },
    { label: "Feed Net", color: C.accent },
    { label: "Shell", color: C.white },
  ];
  pSteps.forEach((st, i) => {
    const x = 0.4 + i * 1.95;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 0.8, w: 1.6, h: 0.9, fill: { color: st.color, transparency: 82 }, line: { color: st.color, width: 1.5 } });
    s.addText(st.label, { x, y: 0.8, w: 1.6, h: 0.9, fontSize: 12, fontFace: "Calibri Light", color: C.white, align: "center", valign: "middle", bold: true });
    if (i < 4) s.addText("→", { x: x + 1.6, y: 0.9, w: 0.35, h: 0.6, fontSize: 18, color: C.dim, align: "center", valign: "middle", margin: 0 });
  });
  s.addShape(pres.shapes.RECTANGLE, { x: 1.5, y: 2.2, w: 7, h: 1.2, fill: { color: C.accent, transparency: 88 }, line: { color: C.accent, width: 2.5 } });
  s.addText([
    { text: "Only 13 kW ", options: { fontSize: 28, bold: true, color: C.gold, fontFace: "Georgia" } },
    { text: "maintains 1 MJ at Q = 10⁹", options: { fontSize: 18, color: C.white, fontFace: "Georgia" } },
  ], { x: 1.5, y: 2.2, w: 7, h: 1.2, align: "center", valign: "middle" });
  caption(s, "A 23 kg gas turbine provides all the power. No nuclear reactor required for Scenario C.");

  // ============================================================
  // SLIDE 20: FLIGHT PERFORMANCE
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Flight Performance", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const perfRows = [
    [{ text: "Destination", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 11 } }, { text: "Chemical", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 11 } }, { text: "Psi-Bubble (1g)", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 11 } }, { text: "Factor", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 11 } }],
    ["Moon", "3 days", "3.5 hours", { text: "20×", options: { color: C.green, bold: true } }],
    ["Mars", "7 months", "2.7 days", { text: "78×", options: { color: C.green, bold: true } }],
    ["Jupiter", "6 years", "5 days", { text: "438×", options: { color: C.green, bold: true } }],
    ["Alpha Centauri", "75,000 years", "3.6 years", { text: "20,833×", options: { color: C.gold, bold: true } }],
  ];
  s.addTable(perfRows, { x: 0.8, y: 0.8, w: 8.4, colW: [2.2, 2, 2.2, 2], border: { pt: 0.5, color: "1A2540" }, fill: { color: C.card }, color: C.white, fontSize: 12, fontFace: "Calibri Light", rowH: [0.42], align: "center", valign: "middle" });

  // ============================================================
  // SLIDE 21: INTERSTELLAR
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "galaxy.jpg", 75);
  s.addText("Interstellar Missions", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const interRows = [
    [{ text: "Destination", options: { fill: { color: "000000", transparency: 30 }, color: "FFFFFF", bold: true, fontSize: 10 } }, { text: "Distance", options: { fill: { color: "000000", transparency: 30 }, color: "FFFFFF", bold: true, fontSize: 10 } }, { text: "1g Ship Time", options: { fill: { color: "000000", transparency: 30 }, color: "FFFFFF", bold: true, fontSize: 10 } }, { text: "10g Ship Time", options: { fill: { color: "000000", transparency: 30 }, color: "FFFFFF", bold: true, fontSize: 10 } }],
    ["Alpha Centauri", "4.37 ly", "3.58 yr", { text: "0.75 yr", options: { color: C.gold, bold: true } }],
    ["Galactic Center", "26,000 ly", "19.8 yr", { text: "2.4 yr", options: { color: C.gold, bold: true } }],
    ["Andromeda", "2.5M ly", "28.6 yr", { text: "3.3 yr", options: { color: C.gold, bold: true } }],
    [{ text: "Observable Universe", options: { bold: true } }, "46B ly", "48 yr", { text: "5.2 yr", options: { color: C.green, bold: true } }],
  ];
  s.addTable(interRows, { x: 0.6, y: 0.8, w: 8.8, colW: [2.5, 1.8, 2.2, 2.3], border: { pt: 0.5, color: "1A2540" }, fill: { color: "000000", transparency: 40 }, color: C.white, fontSize: 11, fontFace: "Calibri Light", rowH: [0.4], align: "center", valign: "middle" });
  s.addText("At 10g — which occupants don't feel — the observable universe is reachable in a human lifetime.", { x: 0.5, y: 3.5, w: 9, h: 0.4, fontSize: 13, fontFace: "Georgia", color: C.gold, align: "center", bold: true });

  // ============================================================
  // SLIDE 22: OPPORTUNITY SECTION
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "earth_space.jpg", 80);
  s.addText("THE OPPORTUNITY", { x: 0.5, y: 1.8, w: 9, h: 0.9, fontSize: 36, fontFace: "Georgia", color: C.white, align: "center", bold: true });
  goldLine(s, 2.85);

  // ============================================================
  // SLIDE 23: COST REVOLUTION
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Cost Per Kilogram to LEO", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const costBars = [
    { label: "Falcon 9", val: "$2,720/kg", w: 6.5, color: C.red },
    { label: "Starship (target)", val: "$100/kg", w: 2.5, color: C.gold },
    { label: "Psi-Bubble", val: "~$1/kg", w: 0.15, color: C.green },
  ];
  costBars.forEach((b, i) => {
    const y = 0.8 + i * 1.4;
    s.addText(b.label, { x: 0.5, y, w: 2.2, h: 0.35, fontSize: 13, fontFace: "Georgia", color: C.white, bold: true, align: "right", margin: 0 });
    s.addShape(pres.shapes.RECTANGLE, { x: 2.9, y: y + 0.4, w: b.w, h: 0.5, fill: { color: b.color, transparency: 25 } });
    s.addText(b.val, { x: 2.9, y: y + 0.4, w: Math.max(b.w, 1.5), h: 0.5, fontSize: 14, fontFace: "Georgia", color: C.white, align: "center", valign: "middle", bold: true, margin: 0 });
  });
  s.addText("2,720× cost reduction.  The floor is the cost of electricity.", { x: 0.5, y: 4.8, w: 9, h: 0.35, fontSize: 13, fontFace: "Georgia", color: C.gold, align: "center", bold: true });

  // ============================================================
  // SLIDE 24: PAYLOAD PIE CHARTS
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Payload Fraction Revolution", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  s.addText("Chemical Rocket", { x: 0.3, y: 0.6, w: 4.7, h: 0.4, fontSize: 15, fontFace: "Georgia", color: C.red, align: "center", bold: true, margin: 0 });
  s.addChart(pres.charts.PIE, [{ name: "Chemical", labels: ["Propellant 95%", "Structure 3%", "Payload 2%"], values: [95, 3, 2] }], {
    x: 0.6, y: 1.0, w: 4, h: 3.0, chartColors: [C.red, "555555", C.accent], showPercent: false, showLegend: true, legendPos: "b", legendColor: C.dim, legendFontSize: 9, dataLabelColor: C.white, dataLabelFontSize: 10,
  });
  s.addText("Psi-Bubble", { x: 5, y: 0.6, w: 4.7, h: 0.4, fontSize: 15, fontFace: "Georgia", color: C.green, align: "center", bold: true, margin: 0 });
  s.addChart(pres.charts.PIE, [{ name: "Psi-Bubble", labels: ["Shell + Power 25%", "PAYLOAD 75%"], values: [25, 75] }], {
    x: 5.3, y: 1.0, w: 4, h: 3.0, chartColors: [C.accent, C.gold], showPercent: false, showLegend: true, legendPos: "b", legendColor: C.dim, legendFontSize: 9, dataLabelColor: C.white, dataLabelFontSize: 10,
  });
  s.addText("From 2% useful payload to 75%.  A 37× improvement.", { x: 0.5, y: 4.3, w: 9, h: 0.35, fontSize: 13, fontFace: "Georgia", color: C.gold, align: "center", bold: true });

  // ============================================================
  // SLIDE 25: MARKET
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Total Addressable Market", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const mktRows = [
    [{ text: "Market", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 10 } }, { text: "10-Year", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 10 } }, { text: "20-Year", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 10 } }, { text: "50-Year", options: { fill: { color: C.accent }, color: "FFFFFF", bold: true, fontSize: 10 } }],
    ["Satellite Launch", "$10B", "$75B", "$500B"],
    ["Space Tourism", "$5B", "$50B", "$5T"],
    ["Asteroid Mining", "$50B", "$500B", "$50T"],
    ["Mars Colonization", "$10B", "$200B", "$10T"],
    ["P2P Transport", "$30B", "$150B", "$2T"],
    ["Military", "$20B", "$50B", "$200B"],
    [{ text: "TOTAL / year", options: { bold: true, color: C.gold } }, { text: "$125B", options: { bold: true, color: C.gold } }, { text: "~$1T", options: { bold: true, color: C.gold } }, { text: "~$70T", options: { bold: true, color: C.gold } }],
  ];
  s.addTable(mktRows, { x: 0.8, y: 0.7, w: 8.4, colW: [2.4, 1.8, 1.8, 2.4], border: { pt: 0.5, color: "1A2540" }, fill: { color: C.card }, color: C.white, fontSize: 11, fontFace: "Calibri Light", rowH: [0.38], align: "center", valign: "middle" });

  // ============================================================
  // SLIDE 26: IP
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Intellectual Property", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  s.addText("ALL PAIS / US NAVY PATENTS:  EXPIRED", { x: 0.5, y: 1.0, w: 9, h: 0.6, fontSize: 24, fontFace: "Georgia", color: C.green, align: "center", bold: true });
  s.addText("The only prior art portfolio for EM-gravitational propulsion is unenforceable.", { x: 1, y: 1.7, w: 8, h: 0.35, fontSize: 12, fontFace: "Calibri Light", color: C.dim, align: "center" });
  const ipItems = ["8 patentable innovation clusters identified", "Freedom to operate: FAVORABLE", "3-year patent program: $135 — 240K", "Provisional filing recommended within 30 days"];
  ipItems.forEach((item, i) => {
    s.addImage({ data: checkIcon, x: 2.5, y: 2.3 + i * 0.45, w: 0.25, h: 0.25 });
    s.addText(item, { x: 2.9, y: 2.25 + i * 0.45, w: 5, h: 0.35, fontSize: 13, fontFace: "Calibri Light", color: C.white, margin: 0 });
  });

  // ============================================================
  // SLIDE 27: DECISION + ROADMAP
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Decision", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 24, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  // Three option boxes
  s.addShape(pres.shapes.RECTANGLE, { x: 0.4, y: 0.7, w: 3, h: 1.3, fill: { color: C.red, transparency: 82 }, line: { color: C.red, width: 1 } });
  s.addText("Do Nothing", { x: 0.4, y: 0.75, w: 3, h: 0.4, fontSize: 14, fontFace: "Georgia", color: C.red, align: "center", bold: true, margin: 0 });
  s.addText("Risk being disrupted.\nSpaceX becomes Kodak.", { x: 0.4, y: 1.2, w: 3, h: 0.6, fontSize: 10, fontFace: "Calibri Light", color: C.dim, align: "center", margin: 0 });

  s.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 0.7, w: 3, h: 1.3, fill: { color: C.green, transparency: 82 }, line: { color: C.green, width: 1.5 } });
  s.addText("Fund Phase 0: $2-4M", { x: 3.6, y: 0.75, w: 3, h: 0.4, fontSize: 13, fontFace: "Georgia", color: C.green, align: "center", bold: true, margin: 0 });
  s.addText("Null → lose $4M.\nPositive → proceed.", { x: 3.6, y: 1.2, w: 3, h: 0.6, fontSize: 10, fontFace: "Calibri Light", color: C.dim, align: "center", margin: 0 });

  s.addShape(pres.shapes.RECTANGLE, { x: 6.8, y: 0.7, w: 2.8, h: 1.3, fill: { color: C.gold, transparency: 72 }, line: { color: C.gold, width: 2 } });
  s.addText("Expected Value", { x: 6.8, y: 0.75, w: 2.8, h: 0.35, fontSize: 11, fontFace: "Calibri Light", color: C.gold, align: "center", bold: true, margin: 0 });
  s.addText("$10B", { x: 6.8, y: 1.05, w: 2.8, h: 0.55, fontSize: 28, fontFace: "Georgia", color: C.white, align: "center", valign: "middle", bold: true });
  s.addText("at 0.1% probability", { x: 6.8, y: 1.65, w: 2.8, h: 0.25, fontSize: 8, fontFace: "Calibri Light", color: C.dim, align: "center", margin: 0 });

  // Roadmap
  s.addText("Development Roadmap", { x: 0.5, y: 2.3, w: 9, h: 0.35, fontSize: 14, fontFace: "Georgia", color: C.white, align: "center", bold: true, margin: 0 });
  const phases = [
    { label: "Phase 0\nSQMS", cost: "$2-4M", color: C.accent, w: 1.2 },
    { label: "Phase 1\nLab Demo", cost: "$10-50M", color: C.green, w: 1.8 },
    { label: "Phase 2\nSubscale", cost: "$100-500M", color: C.gold, w: 2.5 },
    { label: "Phase 3\nFull Vehicle", cost: "$1-5B", color: C.white, w: 3.2 },
  ];
  let phX = 0.4;
  phases.forEach(ph => {
    s.addShape(pres.shapes.RECTANGLE, { x: phX, y: 2.8, w: ph.w, h: 0.7, fill: { color: ph.color, transparency: 72 }, line: { color: ph.color, width: 1 } });
    s.addText(ph.label, { x: phX, y: 2.8, w: ph.w, h: 0.45, fontSize: 9, fontFace: "Calibri Light", color: C.white, align: "center", bold: true, margin: 0 });
    s.addText(ph.cost, { x: phX, y: 3.22, w: ph.w, h: 0.2, fontSize: 8, fontFace: "Calibri Light", color: C.dim, align: "center", margin: 0 });
    phX += ph.w + 0.08;
  });

  // ============================================================
  // SLIDE 28: THE ASK
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "space_stars.jpg", 75);
  s.addText("The Ask", { x: 0.5, y: 1.0, w: 9, h: 0.6, fontSize: 30, fontFace: "Georgia", color: C.white, align: "center", bold: true });
  goldLine(s, 1.75);
  s.addText("Fund the $200K MAGO parasitic experiment.", { x: 0.5, y: 2.1, w: 9, h: 0.5, fontSize: 20, fontFace: "Georgia", color: C.gold, align: "center", bold: true });
  s.addText("Or the $10M dedicated SQMS measurement.", { x: 0.5, y: 2.7, w: 9, h: 0.5, fontSize: 16, fontFace: "Georgia", color: C.accent, align: "center" });
  s.addText("Either one answers the question definitively.", { x: 0.5, y: 3.5, w: 9, h: 0.4, fontSize: 14, fontFace: "Georgia", color: C.white, align: "center" });

  // ============================================================
  // SLIDE 29: THE EVIDENCE — SECTION DIVIDER
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "dark_abstract.jpg", 85);
  s.addText("THE EVIDENCE", {
    x: 0.8, y: 1.5, w: 8.4, h: 1.2, fontSize: 56, fontFace: "Georgia",
    color: C.white, align: "center", bold: true,
  });
  goldLine(s, 2.85);
  s.addText("DFD's ab initio prediction of α matches experiment at sub-ppm", {
    x: 0.8, y: 3.1, w: 8.4, h: 0.5, fontSize: 16, fontFace: "Georgia",
    color: C.dim, align: "center", italic: true,
  });

  // ============================================================
  // SLIDE 30: THE FORMULA
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("α⁻¹ Derived from Topology — Zero Free Parameters", {
    x: 0.5, y: 0.2, w: 9, h: 0.55, fontSize: 20, fontFace: "Georgia",
    color: C.white, align: "center", bold: true, margin: 0,
  });
  // Equation box
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: 0.9, w: 9, h: 2.2,
    fill: { color: C.card }, line: { color: C.gold, width: 2 },
  });
  s.addText("α⁻¹ = (π³/² / 24) × Tr(Y²) × k_max × (k_max+3)/(k_max+4) × [1 + 7/(80×4095)]", {
    x: 0.7, y: 1.0, w: 8.6, h: 0.75, fontSize: 15, fontFace: "Georgia",
    color: C.white, align: "center", bold: true, margin: 0,
  });
  s.addText("= 137.035999854", {
    x: 0.7, y: 1.8, w: 8.6, h: 0.55, fontSize: 22, fontFace: "Georgia",
    color: C.gold, align: "center", bold: true, margin: 0,
  });
  s.addText("No parameter is fitted. Every input is fixed by the geometry of CP² × S³.", {
    x: 0.7, y: 2.4, w: 8.6, h: 0.45, fontSize: 12, fontFace: "Georgia",
    color: C.dim, align: "center", italic: true, margin: 0,
  });

  // ============================================================
  // SLIDE 31: ALL FOUR MEASUREMENTS SIT BELOW
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Bare Value Sits Above All Four Measurements", {
    x: 0.5, y: 0.15, w: 9, h: 0.5, fontSize: 20, fontFace: "Georgia",
    color: C.white, align: "center", bold: true, margin: 0,
  });
  const alphaRows = [
    [
      { text: "Measurement", options: { color: C.gold, bold: true, fontSize: 11 } },
      { text: "α⁻¹", options: { color: C.gold, bold: true, fontSize: 11 } },
      { text: "Residual (ppb)", options: { color: C.gold, bold: true, fontSize: 11 } },
    ],
    [
      { text: "Rb recoil (Parker 2018)", options: { color: C.white, fontSize: 11 } },
      { text: "137.035999206(11)", options: { color: C.white, fontSize: 11 } },
      { text: "+4.73", options: { color: C.gold, bold: true, fontSize: 11 } },
    ],
    [
      { text: "e⁻ g-2 (Fan 2023)", options: { color: C.white, fontSize: 11 } },
      { text: "137.035999166(15)", options: { color: C.white, fontSize: 11 } },
      { text: "+5.02", options: { color: C.gold, bold: true, fontSize: 11 } },
    ],
    [
      { text: "e⁻ g-2 (Hanneke 2008)", options: { color: C.white, fontSize: 11 } },
      { text: "137.035999084(51)", options: { color: C.white, fontSize: 11 } },
      { text: "+5.62", options: { color: C.gold, bold: true, fontSize: 11 } },
    ],
    [
      { text: "Cs recoil (Morel 2020)", options: { color: C.white, fontSize: 11 } },
      { text: "137.035999046(27)", options: { color: C.white, fontSize: 11 } },
      { text: "+5.90", options: { color: C.gold, bold: true, fontSize: 11 } },
    ],
  ];
  s.addTable(alphaRows, {
    x: 0.5, y: 0.8, w: 9, colW: [3.8, 3.2, 2.0],
    border: { pt: 0.5, color: "1A2540" }, fill: { color: C.card },
    fontFace: "Calibri Light", rowH: [0.38], valign: "middle",
  });
  s.addText("All residuals positive — expected in DFD for measurements at nonzero gravitational potential.", {
    x: 0.5, y: 3.6, w: 9, h: 0.45, fontSize: 12, fontFace: "Georgia",
    color: C.dim, align: "center", italic: true,
  });

  // ============================================================
  // SLIDE 32: SPECIES-DEPENDENT PREDICTION
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Rb-Cs Tension: A Species-Dependent Signal", {
    x: 0.5, y: 0.2, w: 9, h: 0.5, fontSize: 20, fontFace: "Georgia",
    color: C.white, align: "center", bold: true, margin: 0,
  });
  // Left box
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: 1.0, w: 4.1, h: 1.5,
    fill: { color: C.card }, line: { color: C.accent, width: 2 },
  });
  s.addText("δ(Cs)/δ(Rb) = 1.247", {
    x: 0.5, y: 1.1, w: 4.1, h: 0.65, fontSize: 20, fontFace: "Georgia",
    color: C.white, align: "center", bold: true, margin: 0,
  });
  s.addText("from measurement", {
    x: 0.5, y: 1.75, w: 4.1, h: 0.4, fontSize: 11, fontFace: "Calibri Light",
    color: C.dim, align: "center", margin: 0,
  });
  // Right box
  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.4, y: 1.0, w: 4.1, h: 1.5,
    fill: { color: C.card }, line: { color: C.gold, width: 2 },
  });
  s.addText("f_EM(Cs)/f_EM(Rb) = 1.266", {
    x: 5.4, y: 1.1, w: 4.1, h: 0.65, fontSize: 20, fontFace: "Georgia",
    color: C.white, align: "center", bold: true, margin: 0,
  });
  s.addText("from nuclear physics", {
    x: 5.4, y: 1.75, w: 4.1, h: 0.4, fontSize: 11, fontFace: "Calibri Light",
    color: C.dim, align: "center", margin: 0,
  });
  s.addText("Match: 1.5% — the shift scales with nuclear Coulomb energy fraction", {
    x: 0.5, y: 2.8, w: 9, h: 0.45, fontSize: 14, fontFace: "Georgia",
    color: C.gold, align: "center", bold: true,
  });
  s.addText("The 5.5σ Rb-Cs tension is not a systematic error — it's physics.", {
    x: 0.5, y: 3.35, w: 9, h: 0.4, fontSize: 13, fontFace: "Georgia",
    color: C.white, align: "center", italic: true,
  });

  // ============================================================
  // SLIDE 33: TESTABLE PREDICTIONS
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Four Testable Predictions for Future Experiments", {
    x: 0.5, y: 0.15, w: 9, h: 0.5, fontSize: 20, fontFace: "Georgia",
    color: C.white, align: "center", bold: true, margin: 0,
  });
  const predRows = [
    [
      { text: "Atom", options: { color: C.gold, bold: true, fontSize: 11 } },
      { text: "f_EM", options: { color: C.gold, bold: true, fontSize: 11 } },
      { text: "Predicted δ (ppb)", options: { color: C.gold, bold: true, fontSize: 11 } },
      { text: "Predicted α⁻¹", options: { color: C.gold, bold: true, fontSize: 11 } },
    ],
    [
      { text: "Li-7", options: { color: C.white, fontSize: 11 } },
      { text: "0.000341", options: { color: C.white, fontSize: 11 } },
      { text: "0.90", options: { color: C.white, fontSize: 11 } },
      { text: "137.035999731", options: { color: C.white, fontSize: 11 } },
    ],
    [
      { text: "K-39", options: { color: C.white, fontSize: 11 } },
      { text: "0.001976", options: { color: C.white, fontSize: 11 } },
      { text: "3.62", options: { color: C.white, fontSize: 11 } },
      { text: "137.035999357", options: { color: C.white, fontSize: 11 } },
    ],
    [
      { text: "Sr-87", options: { color: C.white, fontSize: 11 } },
      { text: "0.002787", options: { color: C.white, fontSize: 11 } },
      { text: "4.98", options: { color: C.white, fontSize: 11 } },
      { text: "137.035999172", options: { color: C.white, fontSize: 11 } },
    ],
    [
      { text: "Yb-174", options: { color: C.white, fontSize: 11 } },
      { text: "0.003797", options: { color: C.white, fontSize: 11 } },
      { text: "6.66", options: { color: C.white, fontSize: 11 } },
      { text: "137.035998942", options: { color: C.white, fontSize: 11 } },
    ],
  ];
  s.addTable(predRows, {
    x: 0.3, y: 0.8, w: 9.4, colW: [1.5, 1.8, 2.5, 3.6],
    border: { pt: 0.5, color: "1A2540" }, fill: { color: C.card },
    fontFace: "Calibri Light", rowH: [0.38], valign: "middle",
  });
  s.addText("Li-7 is the sharpest test: smallest f_EM predicts α⁻¹ closest to the bare value.", {
    x: 0.5, y: 3.65, w: 9, h: 0.45, fontSize: 12, fontFace: "Georgia",
    color: C.dim, align: "center", italic: true,
  });

  // ============================================================
  // SLIDE 34: THE BREAKTHROUGH — SECTION DIVIDER
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "space_stars.jpg", 75);
  s.addText("THE BREAKTHROUGH", {
    x: 0.5, y: 1.6, w: 9, h: 1.2, fontSize: 48, fontFace: "Georgia",
    color: C.white, align: "center", bold: true,
  });
  goldLine(s, 3.0);
  s.addText("DFD's founding postulate means gravity IS the optical metric.\nAbove threshold, EM fields produce mechanical forces — directly.", {
    x: 0.8, y: 3.3, w: 8.4, h: 1.0, fontSize: 16, fontFace: "Georgia",
    color: C.gold, align: "center", italic: true,
  });

  // ============================================================
  // SLIDE 35: ABOVE-THRESHOLD PROPULSION MECHANISM
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Above-Threshold Propulsion", {
    x: 0.5, y: 0.15, w: 9, h: 0.5, fontSize: 24, fontFace: "Georgia",
    color: C.white, bold: true, align: "center",
  });
  goldLine(s, 0.7);

  const mechItems = [
    { label: "Energy parameter", value: "η  =  U_EM / (ρ c²)" },
    { label: "Threshold", value: "η_c  =  α / 4  ≈  1.82 × 10⁻³" },
    { label: "Coupling", value: "κ  =  3 / (8α)  ≈  51.4   (not O(1)!)" },
    { label: "Matter acceleration", value: "a  =  (c² / 2) ∇ψ_eff   —   no G/c⁴ in the chain" },
    { label: "Self-force", value: "Cancels (Newton's 3rd law) → NOT reactionless" },
    { label: "Mechanism", value: "Reaction drive: gas expelled at up to 0.47c" },
  ];
  mechItems.forEach((item, i) => {
    const yPos = 1.0 + i * 0.65;
    s.addText(item.label, {
      x: 0.8, y: yPos, w: 3.2, h: 0.5, fontSize: 13, fontFace: "Calibri Light",
      color: C.gold, align: "right", valign: "middle",
    });
    s.addText(item.value, {
      x: 4.2, y: yPos, w: 5.3, h: 0.5, fontSize: 13, fontFace: "Calibri Light",
      color: C.white, align: "left", valign: "middle",
    });
  });
  caption(s, "DFD's founding postulate: matter follows geodesics of the optical metric g̃_μν");

  // ============================================================
  // SLIDE 36: PERFORMANCE — Isp 14 MILLION SECONDS
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Performance: Isp 14 Million Seconds", {
    x: 0.5, y: 0.15, w: 9, h: 0.5, fontSize: 22, fontFace: "Georgia",
    color: C.white, bold: true, align: "center",
  });
  goldLine(s, 0.7);

  // Comparison table
  const ispData = [
    [
      { text: "Technology", options: { bold: true, color: C.gold, fontSize: 12 } },
      { text: "Isp (seconds)", options: { bold: true, color: C.gold, fontSize: 12 } },
      { text: "Factor", options: { bold: true, color: C.gold, fontSize: 12 } },
    ],
    [
      { text: "Chemical (LOX/LH₂)", options: { color: C.dim, fontSize: 11 } },
      { text: "450", options: { color: C.white, fontSize: 11 } },
      { text: "1×", options: { color: C.dim, fontSize: 11 } },
    ],
    [
      { text: "Ion / Hall thruster", options: { color: C.dim, fontSize: 11 } },
      { text: "10,000", options: { color: C.white, fontSize: 11 } },
      { text: "22×", options: { color: C.dim, fontSize: 11 } },
    ],
    [
      { text: "Fusion (theoretical)", options: { color: C.dim, fontSize: 11 } },
      { text: "100,000", options: { color: C.white, fontSize: 11 } },
      { text: "222×", options: { color: C.dim, fontSize: 11 } },
    ],
    [
      { text: "DFD Threshold (1T)", options: { color: C.accent, bold: true, fontSize: 12 } },
      { text: "9,100,000", options: { color: C.accent, bold: true, fontSize: 12 } },
      { text: "20,000×", options: { color: C.accent, bold: true, fontSize: 12 } },
    ],
    [
      { text: "DFD Threshold (50T)", options: { color: C.gold, bold: true, fontSize: 12 } },
      { text: "14,400,000", options: { color: C.gold, bold: true, fontSize: 12 } },
      { text: "32,000×", options: { color: C.gold, bold: true, fontSize: 12 } },
    ],
  ];
  s.addTable(ispData, {
    x: 0.8, y: 0.95, w: 8.4, colW: [3.5, 2.5, 2.4],
    border: { pt: 0.5, color: "1A2540" }, fill: { color: C.card },
    fontFace: "Calibri Light", rowH: [0.42], valign: "middle",
  });

  // Visual bar chart representation
  const barData = [
    { label: "Chemical", w: 0.02, color: C.dim },
    { label: "Ion", w: 0.05, color: C.dim },
    { label: "Fusion", w: 0.1, color: C.dim },
    { label: "DFD (1T)", w: 4.5, color: C.accent },
    { label: "DFD (50T)", w: 7.0, color: C.gold },
  ];
  barData.forEach((b, i) => {
    const yPos = 3.7 + i * 0.35;
    s.addText(b.label, {
      x: 0.3, y: yPos, w: 1.5, h: 0.28, fontSize: 9, fontFace: "Calibri Light",
      color: C.dim, align: "right", valign: "middle",
    });
    s.addShape(pres.shapes.RECTANGLE, {
      x: 2.0, y: yPos + 0.04, w: Math.max(b.w, 0.03), h: 0.2,
      fill: { color: b.color }, rectRadius: 0.05,
    });
  });
  caption(s, "30,000× advantage over the best existing propulsion technology");

  // ============================================================
  // SLIDE 37: THE EXPERIMENTAL TEST
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("The Experimental Test", {
    x: 0.5, y: 0.15, w: 9, h: 0.5, fontSize: 24, fontFace: "Georgia",
    color: C.white, bold: true, align: "center",
  });
  goldLine(s, 0.7);

  const testItems = [
    { icon: "🧲", text: "1T magnet + UHV chamber  →  η/η_c ≈ 24  (well above threshold)" },
    { icon: "📈", text: "Predict: anomalous gas acceleration with sharp onset at  η = α/4" },
    { icon: "🔬", text: "The α-dependence is unmistakable — no conventional physics predicts this" },
    { icon: "💰", text: "Cost:  < $100K  with existing university equipment" },
  ];
  testItems.forEach((item, i) => {
    const yPos = 1.0 + i * 0.7;
    s.addText(item.icon, {
      x: 0.8, y: yPos, w: 0.6, h: 0.5, fontSize: 22, align: "center", valign: "middle",
    });
    s.addText(item.text, {
      x: 1.5, y: yPos, w: 7.8, h: 0.5, fontSize: 14, fontFace: "Calibri Light",
      color: C.white, align: "left", valign: "middle",
    });
  });

  // The smoking gun quote
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 1.0, y: 3.9, w: 8.0, h: 0.9,
    fill: { color: C.card }, line: { color: C.gold, width: 1.5 },
    rectRadius: 0.15,
  });
  s.addText("\"The threshold depends on the fine structure constant.\nIf you see it, DFD is confirmed.\"", {
    x: 1.2, y: 3.95, w: 7.6, h: 0.8, fontSize: 16, fontFace: "Georgia",
    color: C.gold, align: "center", valign: "middle", italic: true,
  });

  // ============================================================
  // SLIDE 38: KEY NUMBERS
  // ============================================================
  s = pres.addSlide();
  darkBg(s);
  s.addText("Key Numbers", { x: 0.5, y: 0.15, w: 9, h: 0.45, fontSize: 22, fontFace: "Georgia", color: C.white, bold: true, align: "center", margin: 0 });
  const keyNums = [
    ["Threshold η_c", "α/4 ≈ 1.82 × 10⁻³"], ["Coupling κ", "3/(8α) ≈ 51.4"],
    ["Isp (50T pulsed)", "14.4 million seconds"], ["Isp (1T standard)", "9.1 million seconds"],
    ["Exhaust velocity (50T)", "0.47c"], ["Advantage over chemical", "32,000×"],
    ["Lab test cost", "< $100K"], ["Equipment", "1T magnet + UHV (routine)"],
    ["Earth — Mars transit", "2.7 days"], ["Smoking gun", "Sharp onset at η = α/4"],
  ];
  const knTable = keyNums.map(([p, v]) => [
    { text: p, options: { color: C.dim, fontSize: 11 } },
    { text: v, options: { color: C.white, bold: true, fontSize: 11 } },
  ]);
  s.addTable(knTable, { x: 1.5, y: 0.7, w: 7, colW: [3.5, 3.5], border: { pt: 0.5, color: "1A2540" }, fill: { color: C.card }, fontFace: "Calibri Light", rowH: [0.38], valign: "middle" });

  // ============================================================
  // SLIDE 39: THE STAKES
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "space_stars.jpg", 80);
  s.addText("If this works, it is the most\nimportant technology\nin human history.", {
    x: 0.5, y: 0.8, w: 9, h: 2.0, fontSize: 28, fontFace: "Georgia",
    color: C.white, align: "center", valign: "middle", bold: true,
  });
  goldLine(s, 3.0);
  s.addText("If it doesn't, you lost less\nthan a fighter jet's landing gear.", {
    x: 0.5, y: 3.3, w: 9, h: 1.0, fontSize: 18, fontFace: "Georgia",
    color: C.gold, align: "center", valign: "middle", italic: true,
  });

  // ============================================================
  // SLIDE 40: FINAL
  // ============================================================
  s = pres.addSlide();
  photoBg(s, "galaxy.jpg", 82);
  s.addText("∇²ψ  =  (4πG / c²) · ρ_eff · μ(ψ)", {
    x: 0.5, y: 1.4, w: 9, h: 0.7, fontSize: 24, fontFace: "Georgia",
    color: C.white, align: "center", bold: true,
  });
  goldLine(s, 2.3);
  s.addText("The door is constrained but not locked.", {
    x: 0.5, y: 2.6, w: 9, h: 0.5, fontSize: 18, fontFace: "Georgia",
    color: C.gold, align: "center", italic: true,
  });
  s.addText("Gary Thomas Alcock", {
    x: 0.5, y: 3.5, w: 9, h: 0.35, fontSize: 14, fontFace: "Georgia",
    color: C.white, align: "center",
  });
  s.addText("Density Field Dynamics  |  densityfielddynamics.com", {
    x: 0.5, y: 3.85, w: 9, h: 0.3, fontSize: 11, fontFace: "Calibri Light",
    color: C.dim, align: "center",
  });
  s.addText("Technical appendix available: 15-page Physical Review paper · 12 engineering schematics · 7 simulation codes · Complete IP analysis", {
    x: 0.5, y: 4.6, w: 9, h: 0.3, fontSize: 9, fontFace: "Calibri Light",
    color: C.dim, align: "center",
  });

  // ===== SAVE =====
  const outPath = "/Users/garyalcock/claudecode/densityfielddynamics/DFD_Research_Output/presentation/DFD_Psi_Bubble_Propulsion_Deck.pptx";
  await pres.writeFile({ fileName: outPath });
  console.log("Deck saved: " + outPath);
}

main().catch(err => { console.error(err); process.exit(1); });
