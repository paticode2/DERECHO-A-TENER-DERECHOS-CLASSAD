import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------
# Configuración general
# --------------------------------------------------

st.set_page_config(
    page_title="Línea de Defensa",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Quita márgenes de Streamlit para que el prototipo ocupe la pantalla
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0;
            max-width: 480px;
        }
        header[data-testid="stHeader"] { display: none; }
        footer { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Prototipo: Línea de Defensa
# Toda la experiencia (pantallas, contenido, puntos,
# sonidos y navegación) vive en este HTML.
# Contenido demostrativo: casos inventados y
# teléfonos por verificar.
# --------------------------------------------------

PROTOTIPO_HTML = r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Línea de Defensa</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
*, *::before, *::after { box-sizing: border-box; }
:root {
  /* Modo oscuro con los colores de Espacios Abiertos: azul #003C69 y rosado #E6007E */
  --bg: #060D20;
  --surface: #0D1833;
  --surface-2: #152447;
  --surface-3: #1D3060;
  --ink: #F3F5FF;
  --muted: #A9B3D6;
  --line: #2A3C6B;
  --accent: #E6007E;
  --accent-dark: #93004F;
  --accent-ink: #FFFFFF;
  --link: #FF6FB8;
  --navy: #003C69;
  --signal: #FFC23D;
  --signal-dark: #B57F0E;
  --signal-ink: #2A2100;
  --bubble: #1D3366;
  --ok: #3DD68C;
  --ok-bg: #0F3A2A;
  --bad: #FF7A90;
  --bad-bg: #3A1426;
  --hero: linear-gradient(145deg, #003C69 0%, #1A2C78 55%, #B0087A 100%);
  --font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;
  --font-body: "Atkinson Hyperlegible", "Segoe UI", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  color-scheme: dark; /* siempre oscuro, aunque el dispositivo esté en modo claro */
}
html, body { min-height: 100%; }
body {
  margin: 0;
  background:
    radial-gradient(circle at 0% 0%, rgba(0, 60, 105, 0.55) 0, transparent 50%),
    radial-gradient(circle at 100% 35%, rgba(230, 0, 126, 0.18) 0, transparent 40%),
    var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  font-size: 17px;
  line-height: 1.5;
}
.app {
  max-width: 440px; margin: 0 auto; min-height: 100vh; background: var(--surface);
  display: flex; flex-direction: column; box-shadow: 0 0 0 1px var(--line), 0 10px 50px rgba(0, 0, 0, 0.5);
}
h1, h2, h3 { font-family: var(--font-display); text-wrap: balance; margin: 0; letter-spacing: -0.02em; }
h1 { font-size: 2.5rem; line-height: 1; font-weight: 800; }
h2 { font-size: 1.5rem; line-height: 1.12; font-weight: 800; }
h3 { font-size: 1.1rem; font-weight: 600; }
p { margin: 0; }
.muted { color: var(--muted); }
.small { font-size: 0.9rem; }
.eyebrow { font-family: var(--font-mono); font-size: 0.74rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }
:focus-visible { outline: 3px solid var(--signal); outline-offset: 2px; }

/* ---------- Íconos ---------- */
.ricon { width: 1em; height: 1em; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; display: block; }
.ava { display: block; border-radius: 50%; overflow: hidden; background: color-mix(in srgb, var(--c) 24%, #fff); flex: none; }
.ava svg { width: 100%; height: 100%; display: block; }

/* ---------- Barra superior tipo juego ---------- */
.topbar {
  position: sticky; top: 0; z-index: 5; background: rgba(13, 24, 51, 0.92); backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--line); padding: 6px 16px 0;
}
.hud { display: flex; align-items: center; gap: 8px; min-height: 46px; }
.brand {
  font-family: var(--font-display); font-weight: 800; font-size: 1rem; letter-spacing: -0.01em; margin-right: auto;
  display: flex; align-items: center; gap: 8px; color: var(--ink); background: none; border: 0; padding: 4px 0; cursor: pointer; min-height: 40px; text-align: left;
}
.shield { width: 24px; height: 28px; flex: none; }
.ea-logo { height: 28px; width: auto; display: block; }
.logo-menu { position: absolute; top: 52px; left: 12px; z-index: 20; display: grid; min-width: 210px; padding: 6px; border-radius: 16px;
  background: var(--surface-2); border: 1px solid var(--line); box-shadow: 0 14px 30px rgba(0, 0, 0, 0.5); animation: menu-in 0.18s ease-out both; }
.logo-menu button { font: inherit; font-weight: 700; text-align: left; color: var(--ink); background: none; border: 0; border-radius: 11px; padding: 10px 12px; min-height: 46px; cursor: pointer; }
.logo-menu button:hover { background: var(--surface-3); }
@keyframes menu-in { from { opacity: 0; transform: translateY(-6px); } }
.lvl { font-family: var(--font-mono); font-size: 0.74rem; background: var(--surface-3); color: var(--ink); border-radius: 8px; padding: 4px 8px; white-space: nowrap; }
.chip {
  font-family: var(--font-mono); font-size: 0.86rem; font-variant-numeric: tabular-nums; background: var(--signal); color: var(--signal-ink);
  border-radius: 999px; padding: 4px 11px; white-space: nowrap; box-shadow: 0 2px 0 var(--signal-dark);
}
.chip.bump { animation: bump 0.55s ease; }
@keyframes bump { 30% { transform: scale(1.28); } }
.icon-btn {
  width: 38px; height: 38px; border-radius: 50%; border: 1px solid var(--line); background: var(--surface-2); font-size: 1.05rem;
  cursor: pointer; display: grid; place-items: center; padding: 0; flex: none; color: var(--ink);
}
.badges-row { display: flex; align-items: center; gap: 6px; padding: 4px 0 8px; }
.rb {
  --c: #888; width: 36px; height: 36px; border-radius: 11px; border: 0; padding: 0; display: grid; place-items: center; cursor: pointer;
  background: var(--surface-2); color: #5C6B98; position: relative; font-size: 20px; transition: transform 0.15s;
}
.rb.on { background: var(--c); color: #fff; box-shadow: 0 3px 0 color-mix(in srgb, var(--c) 65%, #000); }
.rb.on::after {
  content: "✓"; position: absolute; right: -4px; bottom: -4px; width: 15px; height: 15px; border-radius: 50%; background: var(--ok);
  color: #06281A; font-size: 0.58rem; font-weight: 700; display: grid; place-items: center; border: 2px solid var(--surface);
}
.rb:active { transform: translateY(2px); }
.rb.pop { animation: unlock 0.9s cubic-bezier(0.2, 1.6, 0.4, 1); }
@keyframes unlock { 0% { transform: scale(0.2) rotate(-40deg); } 100% { transform: none; } }
.badges-row .count { margin-left: auto; font-family: var(--font-mono); font-size: 0.74rem; color: var(--muted); white-space: nowrap; }
.xp { height: 5px; margin: 0 -16px; background: var(--surface-2); }
.xp i { display: block; height: 100%; background: linear-gradient(90deg, var(--signal), #FF7A3D); transition: width 0.7s ease; }

/* ---------- Pantalla ---------- */
.screen { flex: 1; display: flex; flex-direction: column; gap: 16px; padding: 18px 16px 48px; }
.screen.enter { animation: enter 0.42s ease-out; }
@keyframes enter { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }

.btn {
  font: inherit; font-weight: 700; font-size: 1.05rem; width: 100%; min-height: 54px; border-radius: 16px; border: 2px solid var(--accent);
  background: var(--accent); color: var(--accent-ink); cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  text-decoration: none; padding: 0 18px; box-shadow: 0 4px 0 var(--accent-dark); transition: transform 0.08s, box-shadow 0.08s;
}
.btn:active:not(:disabled) { transform: translateY(3px); box-shadow: 0 1px 0 var(--accent-dark); }
.btn.ghost { background: transparent; color: var(--link); box-shadow: none; }
.btn.signal { background: var(--signal); border-color: var(--signal); color: var(--signal-ink); box-shadow: 0 4px 0 var(--signal-dark); }
.btn:disabled { opacity: 0.4; cursor: not-allowed; box-shadow: none; }
.btn-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }

/* ---------- Bienvenida ---------- */
.hero {
  background: var(--hero); color: #fff; border-radius: 26px; padding: 14px 18px 22px; display: grid; gap: 6px; justify-items: center;
  text-align: center; position: relative; overflow: hidden;
}
.hero::before {
  content: ""; position: absolute; inset: 0; opacity: 0.35;
  background-image: radial-gradient(rgba(255, 255, 255, 0.6) 1px, transparent 1.6px); background-size: 20px 20px;
}
.hero > * { position: relative; }
.hero .eyebrow { color: #fff; opacity: 0.8; }
.hero .tag { font-family: var(--font-display); font-weight: 600; font-size: 1.1rem; }
.orbit { width: 230px; height: 230px; position: relative; }
.orb {
  position: absolute; width: 58px; height: 58px; margin: -29px 0 0 -29px; border: 3px solid #fff; border-radius: 50%; box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
  animation: float 3.2s ease-in-out infinite; animation-delay: calc(var(--i) * -0.45s);
}
.orb .ava { width: 100%; height: 100%; }
@keyframes float { 50% { transform: translateY(-7px); } }
.hero-shield { position: absolute; left: 50%; top: 50%; width: 86px; height: 100px; transform: translate(-50%, -50%); filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.3)); }
.hero-shield svg { width: 100%; height: 100%; }
.facts { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }
.fact { border: 1px solid var(--line); border-radius: 999px; padding: 5px 12px; font-size: 0.88rem; color: var(--muted); background: var(--surface-2); }
.proto-tag { font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); text-align: center; }

/* ---------- Autoevaluación ---------- */
.q { display: grid; gap: 8px; border: 0; padding: 0; margin: 0; }
.q legend { font-weight: 700; padding: 0; margin-bottom: 8px; }
.scale { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; }
.scale label { position: relative; }
.scale input { position: absolute; opacity: 0; inset: 0; }
.scale span {
  display: grid; place-items: center; min-height: 48px; border: 2px solid var(--line); border-radius: 12px; font-family: var(--font-mono);
  font-size: 1.05rem; cursor: pointer; background: var(--surface-2); box-shadow: 0 3px 0 var(--line);
}
.scale input:checked + span { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 3px 0 var(--accent-dark); }
.scale input:focus-visible + span { outline: 3px solid var(--signal); outline-offset: 2px; }
.scale-ends { display: flex; justify-content: space-between; font-size: 0.8rem; color: var(--muted); }

/* ---------- Cómo funciona ---------- */
.steps { display: grid; gap: 10px; margin: 0; padding: 0; list-style: none; }
.steps li { display: grid; grid-template-columns: 48px 1fr; gap: 12px; align-items: center; background: var(--surface-2); border-radius: 16px; padding: 10px 12px; }
.step-ico { width: 48px; height: 48px; border-radius: 14px; display: grid; place-items: center; font-size: 1.5rem; background: var(--surface-3); box-shadow: 0 3px 0 var(--line); }
.ladder { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; }
.rung { background: var(--surface-2); border-radius: 14px; padding: 10px 4px; text-align: center; display: grid; gap: 2px; font-size: 0.78rem; line-height: 1.2; }
.rung b { font-size: 1.5rem; }
.rung .pts { font-family: var(--font-mono); color: var(--muted); font-size: 0.7rem; }
.note { background: var(--surface-2); border-radius: 14px; padding: 12px 14px; font-size: 0.9rem; color: var(--muted); }

/* ---------- Bandeja ---------- */
.resume {
  font: inherit; color: #fff; text-align: left; border: 0; cursor: pointer; background: var(--hero); border-radius: 20px; padding: 14px;
  display: grid; grid-template-columns: 56px 1fr auto; gap: 12px; align-items: center; box-shadow: 0 5px 0 rgba(0, 0, 0, 0.45);
}
.resume .ava { width: 56px; height: 56px; border: 3px solid #fff; }
.resume small { display: block; opacity: 0.8; font-size: 0.8rem; }
.resume strong { font-family: var(--font-display); font-size: 1.15rem; }
.resume .go { width: 42px; height: 42px; border-radius: 50%; background: var(--signal); color: var(--signal-ink); display: grid; place-items: center; font-size: 1rem; }
.status { display: flex; justify-content: space-between; align-items: baseline; gap: 10px; }
.status strong { font-family: var(--font-display); }
.inbox { display: grid; border: 1px solid var(--line); border-radius: 18px; overflow: hidden; }
.msg {
  font: inherit; color: inherit; text-align: left; background: var(--surface); border: 0; border-bottom: 1px solid var(--line);
  display: grid; grid-template-columns: 46px 1fr auto; gap: 12px; align-items: center; padding: 10px 14px; cursor: pointer; min-height: 68px;
}
.msg:last-child { border-bottom: 0; }
.msg:hover { background: var(--surface-2); }
.msg .ava { width: 46px; height: 46px; }
.msg-body { min-width: 0; }
.msg-name { font-weight: 700; display: block; }
.msg-prev { display: block; color: var(--muted); font-size: 0.9rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.pill { font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.06em; text-transform: uppercase; border-radius: 999px; padding: 3px 8px; white-space: nowrap; background: var(--bad-bg); color: var(--bad); }
.msg .rb { width: 32px; height: 32px; font-size: 17px; cursor: inherit; }
.nudge { background: var(--surface-2); border: 1px dashed var(--link); border-radius: 14px; padding: 10px 14px; display: grid; gap: 2px; font-size: 0.9rem; }
.nudge strong { color: var(--link); }

/* ---------- Caso ---------- */
.case-head { display: flex; align-items: center; gap: 10px; }
.back { width: 38px; height: 38px; border-radius: 50%; border: 1px solid var(--line); background: var(--surface-2); font: inherit; font-weight: 700; color: var(--link); cursor: pointer; padding: 0; flex: none; }
.case-head .ava { width: 46px; height: 46px; }
.ch-name { display: grid; line-height: 1.2; margin-right: auto; min-width: 0; }
.ch-name small { color: var(--muted); font-size: 0.8rem; }
.stepper { display: flex; gap: 4px; flex: none; }
.stepper i { width: 22px; height: 7px; border-radius: 99px; background: var(--line); display: block; }
.stepper i.on { background: var(--accent); }
.bubble { background: var(--bubble); border-radius: 4px 20px 20px 20px; padding: 12px 16px; position: relative; }
.bubble.mini { font-size: 0.92rem; padding: 9px 14px; color: #C9D1F0; }
.screen.enter .bubble { animation: pop 0.4s 0.1s both; }
@keyframes pop { from { opacity: 0; transform: scale(0.92); transform-origin: 0 0; } to { opacity: 1; transform: none; } }

.scene {
  position: relative; width: 100%; aspect-ratio: 16 / 11; border-radius: 20px; overflow: hidden; border: 3px solid #2E4478;
  box-shadow: 0 5px 0 #02060F, 0 0 30px rgba(0, 60, 105, 0.6); background: #E7EAF7;
}
.scene-art { position: absolute; inset: 0; width: 100%; height: 100%; }
.scene-tag {
  position: absolute; top: 10px; font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.04em; background: rgba(255, 255, 255, 0.94);
  color: #151936; border-radius: 999px; padding: 4px 10px; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
}
.scene-tag.l { left: 10px; } .scene-tag.r { right: 10px; }
.spot {
  position: absolute; transform: translate(-50%, -50%); width: 58px; height: 58px; border-radius: 50%; border: 3px solid #fff;
  background: var(--signal); font-size: 1.6rem; cursor: pointer; display: grid; place-items: center; box-shadow: 0 5px 14px rgba(10, 12, 40, 0.3); padding: 0;
}
.spot::after { content: ""; position: absolute; inset: -9px; border-radius: 50%; border: 3px solid var(--signal); animation: pulse 1.8s ease-out infinite; }
.spot.found { background: #fff; border-color: var(--ok); }
.spot.found::after { display: none; }
.spot.found::before {
  content: "✓"; position: absolute; right: -6px; top: -6px; width: 22px; height: 22px; border-radius: 50%; background: var(--ok);
  color: #fff; font-size: 0.8rem; font-weight: 700; display: grid; place-items: center;
}
.spot.just { animation: spot-pop 0.5s cubic-bezier(0.2, 1.8, 0.4, 1); }
@keyframes spot-pop { 0% { transform: translate(-50%, -50%) scale(0.6); } 100% { transform: translate(-50%, -50%) scale(1); } }
@keyframes pulse { from { transform: scale(0.85); opacity: 0.9; } to { transform: scale(1.35); opacity: 0; } }
/* Mini escena entre las dos partes */
.scene.playing .spot { visibility: hidden; }
.scene.spots-in .spot { animation: spot-pop 0.5s cubic-bezier(0.2, 1.8, 0.4, 1) both; }
.scene.spots-in .spot:nth-of-type(2) { animation-delay: 0.12s; }
.scene.spots-in .spot:nth-of-type(3) { animation-delay: 0.24s; }
.scene-tag.replay { border: 0; font: inherit; font-family: var(--font-mono); font-size: 0.72rem; cursor: pointer; }
.intro { position: absolute; inset: 0; z-index: 3; background: linear-gradient(180deg, rgba(6, 13, 32, 0.15), rgba(6, 13, 32, 0.45));
  animation: intro-out 0.5s ease-in calc(9.4s - var(--el)) forwards; }
@keyframes intro-out { to { opacity: 0; visibility: hidden; } }
.scene { container-type: inline-size; }
.scene.playing .scene-tag { visibility: hidden; }
.actor { position: absolute; bottom: -2%; width: 29%; aspect-ratio: 1; }
.actor .ava { width: 100%; height: 100%; background: transparent; border-radius: 0; overflow: visible; filter: drop-shadow(0 6px 8px rgba(0, 0, 0, 0.35)); }
.actor.l { left: 3%; animation: in-l 0.55s cubic-bezier(0.2, 1.3, 0.4, 1) calc(0s - var(--el)) both; }
.actor.r { right: 3%; animation: in-r 0.55s cubic-bezier(0.2, 1.3, 0.4, 1) calc(0.2s - var(--el)) both; }
@keyframes in-l { from { transform: translateX(-140%); } }
@keyframes in-r { from { transform: translateX(140%); } }
.actor.r .ava { animation: talk 0.2s ease-in-out calc(0.9s - var(--el)) 8 alternate; }
.actor.l .ava { animation: talk 0.2s ease-in-out calc(4.6s - var(--el)) 8 alternate; }
@keyframes talk { to { transform: translateY(-5%) rotate(-3deg); } }
.say {
  position: absolute; top: 4%; width: max-content; max-width: 46%; margin: 0; background: #fff; color: #151936; border-radius: 14px; padding: 7px 11px;
  font-size: clamp(0.66rem, 3.1cqw, 0.95rem); line-height: 1.3; font-weight: 700; box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
  animation: say-in 0.4s cubic-bezier(0.2, 1.6, 0.4, 1) both;
}
.say small { display: block; font-family: var(--font-mono); font-size: 0.6rem; letter-spacing: 0.06em; text-transform: uppercase; color: #6A6F8F; font-weight: 500; }
.say::after { content: ""; position: absolute; bottom: -8px; border: 8px solid transparent; border-bottom: 0; border-top-color: inherit; }
.say.r { right: 3%; border-bottom-right-radius: 3px; animation-delay: calc(0.8s - var(--el)); }
.say.r::after { right: 12%; border-top-color: #fff; }
.say.l { left: 3%; background: #FFE0F0; border-bottom-left-radius: 3px; animation-delay: calc(4.5s - var(--el)); }
.say.l::after { left: 12%; border-top-color: #FFE0F0; }
@keyframes say-in { from { opacity: 0; transform: scale(0.3) translateY(12px); } }
.skip {
  position: absolute; left: 50%; transform: translateX(-50%); bottom: 8px; z-index: 4; white-space: nowrap; font: inherit; font-size: 0.78rem; font-weight: 700; border: 0; border-radius: 999px;
  padding: 5px 11px; background: rgba(6, 13, 32, 0.75); color: #fff; cursor: pointer;
}
.tip { text-align: center; color: var(--muted); font-size: 0.92rem; }
.clues { display: grid; gap: 8px; margin: 0; padding: 0; list-style: none; }
.clues li { display: grid; grid-template-columns: 28px 1fr auto; gap: 10px; align-items: start; background: var(--surface-2); border-radius: 14px; padding: 9px 12px; font-size: 0.95rem; }
.clues li.just { animation: slide 0.4s ease-out; background: rgba(255, 194, 61, 0.14); }
@keyframes slide { from { opacity: 0; transform: translateX(-14px); } to { opacity: 1; transform: none; } }
.clues .plus { font-family: var(--font-mono); font-size: 0.8rem; color: var(--ok); }
.wait { display: grid; gap: 6px; }
.wait p { color: var(--ok); font-weight: 700; font-size: 0.95rem; }
@keyframes fill { to { width: 100%; } }

.q-title { font-size: 1.35rem; }
.options { display: grid; gap: 10px; }
.options.all7 { grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr)); gap: 8px; align-items: start; }
.options.all7 .opt { min-height: 52px; padding: 7px 10px; gap: 10px; grid-template-columns: 36px 1fr 22px; }
.options.all7 .opt-ico { width: 36px; height: 36px; font-size: 20px; }
.opt {
  font: inherit; color: inherit; text-align: left; background: var(--surface); border: 2px solid var(--line); border-radius: 16px; padding: 10px 12px;
  cursor: pointer; display: grid; grid-template-columns: 40px 1fr 24px; gap: 12px; align-items: center; min-height: 60px; box-shadow: 0 3px 0 var(--line);
}
.opt:hover:not(:disabled) { border-color: var(--link); }
.opt:disabled { cursor: default; }
.screen.enter .opt { animation: rise 0.36s both; animation-delay: calc(var(--n) * 70ms + 0.1s); }
@keyframes rise { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
.opt-ico {
  width: 40px; height: 40px; border-radius: 12px; display: grid; place-items: center; font-size: 22px;
  background: color-mix(in srgb, var(--c) 35%, var(--surface)); color: color-mix(in srgb, var(--c) 35%, #fff); font-family: var(--font-display); font-weight: 800;
}
.opt-txt { display: grid; gap: 4px; }
.why { font-size: 0.86rem; color: var(--bad); line-height: 1.35; }
.mark { width: 24px; height: 24px; border-radius: 50%; display: grid; place-items: center; font-weight: 700; font-size: 0.8rem; border: 2px solid var(--line); }
.opt.right { border-color: var(--ok); background: var(--ok-bg); box-shadow: 0 3px 0 var(--ok); animation: correct 0.5s ease; }
.opt.right .mark { background: var(--ok); border-color: var(--ok); color: #06281A; }
.opt.wrong { border-color: #6E2840; background: var(--bad-bg); box-shadow: none; }
.opt.wrong .mark { background: var(--bad); border-color: var(--bad); color: #2A0510; }
.opt.wrong .opt-txt > span:first-child { text-decoration: line-through; color: var(--muted); }
.opt.wrong .opt-ico { filter: grayscale(1); opacity: 0.5; }
.opt.shake { animation: shake 0.45s; }
@keyframes shake { 20% { transform: translateX(-8px); } 40% { transform: translateX(7px); } 60% { transform: translateX(-4px); } 80% { transform: translateX(2px); } }
@keyframes correct { 40% { transform: scale(1.04); } }
.hint { background: rgba(255, 194, 61, 0.12); border: 1px solid rgba(255, 194, 61, 0.35); border-radius: 14px; padding: 10px 14px; font-size: 0.92rem; }
.okbar { background: var(--ok-bg); border-left: 5px solid var(--ok); border-radius: 14px; padding: 10px 14px; display: grid; gap: 2px; font-size: 0.93rem; }
.okbar strong { font-family: var(--font-display); color: var(--ok); }

/* ---------- Caso resuelto ---------- */
.win {
  --c: var(--accent); position: relative; border-radius: 24px; padding: 18px 16px 16px; text-align: center; display: grid; gap: 6px;
  justify-items: center; color: #fff; overflow: hidden; background: radial-gradient(circle at 50% 0%, color-mix(in srgb, var(--c) 55%, #fff) 0, var(--c) 62%);
}
.win::before {
  content: ""; position: absolute; inset: -60%; animation: spin 22s linear infinite;
  background: repeating-conic-gradient(rgba(255, 255, 255, 0.14) 0 10deg, transparent 10deg 30deg);
}
@keyframes spin { to { transform: rotate(1turn); } }
.win > * { position: relative; }
.win .eyebrow { color: #fff; opacity: 0.85; }
.win h2 { color: #fff; }
.win-top { display: flex; align-items: flex-end; justify-content: center; }
.win-top .ava { width: 74px; height: 74px; border: 3px solid #fff; }
.win-badge {
  width: 56px; height: 56px; border-radius: 16px; background: #fff; color: var(--c); display: grid; place-items: center; font-size: 30px;
  margin-left: -14px; box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25); animation: unlock 0.9s 0.25s both cubic-bezier(0.2, 1.6, 0.4, 1);
}
.win-pts b { font-family: var(--font-display); font-size: 2.3rem; line-height: 1; }
.win-story { background: rgba(255, 255, 255, 0.16); border-radius: 14px; padding: 10px 12px; font-size: 0.95rem; text-align: left; width: 100%; }
.levelup { background: var(--signal); color: var(--signal-ink); border-radius: 14px; padding: 10px 14px; font-weight: 700; text-align: center; animation: bump 0.7s 0.4s both; }
.keyidea { background: var(--surface-2); border-radius: 16px; padding: 14px 16px; display: grid; gap: 4px; }
.learn-btn {
  font: inherit; color: inherit; text-align: left; cursor: pointer; width: 100%; border: 2px solid var(--line); background: var(--surface-2); border-radius: 16px;
  padding: 10px 14px; display: grid; grid-template-columns: 46px 1fr auto; gap: 12px; align-items: center; box-shadow: 0 3px 0 var(--line);
}
.learn-btn .play { width: 46px; height: 46px; border-radius: 14px; background: #E03E3E; display: grid; place-items: center; }
.learn-btn .play::before { content: ""; border-left: 14px solid #fff; border-top: 9px solid transparent; border-bottom: 9px solid transparent; margin-left: 4px; }
.learn-btn small { display: block; color: var(--muted); font-size: 0.84rem; }
.learn-btn .arrow { color: var(--link); font-weight: 700; }

/* Nuevo mensaje: entra con rebote, suena y brilla */
.notif {
  background: linear-gradient(150deg, #E6007E 0%, #8E1C9E 100%); color: #fff; border-radius: 24px; padding: 14px; display: grid; gap: 12px; position: relative;
  animation: notif-in 0.75s cubic-bezier(0.2, 1.5, 0.4, 1) calc(var(--notif-wait) - var(--el, 0ms)) both, glow 1.6s ease-out calc(var(--notif-wait) + 0.7s - var(--el, 0ms)) 3;
  box-shadow: 0 14px 30px rgba(0, 0, 0, 0.5);
}
@keyframes notif-in { from { opacity: 0; visibility: hidden; transform: translateY(46px) scale(0.9); } to { opacity: 1; transform: none; } }
@keyframes glow {
  0% { box-shadow: 0 14px 30px rgba(21, 25, 54, 0.35), 0 0 0 0 rgba(255, 194, 61, 0.8); }
  100% { box-shadow: 0 14px 30px rgba(21, 25, 54, 0.35), 0 0 0 18px rgba(255, 194, 61, 0); }
}
.notif-head { display: flex; align-items: center; gap: 8px; font-family: var(--font-mono); font-size: 0.76rem; letter-spacing: 0.06em; text-transform: uppercase; color: #fff; font-weight: 700; }
.ring { display: inline-block; font-size: 1.1rem; animation: ring 0.9s ease-in-out 1.6s 3; }
@keyframes ring { 0%, 100% { transform: rotate(0); } 20% { transform: rotate(-20deg); } 40% { transform: rotate(18deg); } 60% { transform: rotate(-12deg); } 80% { transform: rotate(8deg); } }
.notif-time { margin-left: auto; color: rgba(255, 255, 255, 0.6); text-transform: none; letter-spacing: 0; }
.notif-dot { position: absolute; top: -6px; right: -6px; min-width: 26px; height: 26px; border-radius: 99px; background: var(--signal); color: var(--signal-ink); font-weight: 700; font-size: 0.85rem; display: grid; place-items: center; border: 3px solid var(--bg); }
.notif-body { display: grid; grid-template-columns: 54px 1fr; gap: 12px; align-items: start; }
.notif-body .ava { width: 54px; height: 54px; border: 2px solid #fff; }
.notif-body p { color: rgba(255, 255, 255, 0.9); font-size: 0.95rem; margin-top: 2px; }
.final { background: var(--hero); color: #fff; border-radius: 24px; padding: 18px; display: grid; gap: 10px; text-align: center; }
.final b { font-size: 2.6rem; line-height: 1; }

/* ---------- Ficha del derecho (al tocar un ícono) ---------- */
.sheet-wrap { position: fixed; inset: 0; z-index: 30; background: rgba(8, 10, 30, 0.55); display: grid; place-items: center; padding: 14px; }
.sheet {
  --c: var(--accent); background: var(--surface); border: 1px solid var(--line); width: 100%; max-width: 420px; max-height: calc(100vh - 28px); overflow: auto; border-radius: 22px;
  display: grid; gap: 12px; padding: 16px; box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6); animation: pop 0.3s ease-out;
}
.sheet-head { display: flex; align-items: center; gap: 12px; }
.sheet-head .rb { width: 52px; height: 52px; font-size: 28px; border-radius: 15px; cursor: default; }
.sheet-head h3 { font-size: 1.25rem; }
.sheet-head > div { margin-right: auto; }
.locked { background: var(--surface-2); border-radius: 14px; padding: 14px; display: grid; gap: 6px; text-align: center; }
.locked b { font-size: 2rem; }
.video-embed { position: relative; width: 100%; aspect-ratio: 16 / 9; border-radius: 16px; overflow: hidden; background: #000; }
.video-embed iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
.video { display: grid; text-decoration: none; color: #fff; border-radius: 16px; overflow: hidden; background: #000; padding: 14px; }
.links { display: grid; gap: 8px; }
.link-row {
  display: grid; grid-template-columns: 40px 1fr auto; gap: 12px; align-items: center; padding: 10px 14px; border: 1px solid var(--line);
  border-radius: 14px; text-decoration: none; color: inherit; background: var(--surface-2); font: inherit; text-align: left; cursor: pointer; width: 100%;
}
.link-row .ico { width: 40px; height: 40px; border-radius: 10px; background: var(--bubble); display: grid; place-items: center; font-size: 1.2rem; }
.link-row .arrow { color: var(--link); font-weight: 700; }

/* ---------- Reporte ---------- */
.medal { background: var(--hero); color: #fff; border-radius: 24px; padding: 20px; display: grid; gap: 4px; text-align: center; justify-items: center; position: relative; overflow: hidden; }
.medal::before { content: ""; position: absolute; inset: -60%; background: repeating-conic-gradient(rgba(255, 255, 255, 0.1) 0 10deg, transparent 10deg 30deg); animation: spin 26s linear infinite; }
.medal > * { position: relative; }
.medal .eyebrow { color: #fff; opacity: 0.8; }
.medal .trophy { font-size: 3rem; line-height: 1; }
.medal .rank { font-family: var(--font-display); font-weight: 800; font-size: 1.9rem; line-height: 1.05; }
.medal .score { font-family: var(--font-mono); color: var(--signal); }
.badge-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px 6px; }
.bg-item { font: inherit; color: inherit; background: none; border: 0; padding: 0; cursor: pointer; display: grid; justify-items: center; gap: 4px; font-size: 0.72rem; line-height: 1.2; text-align: center; }
.bg-item .rb { width: 48px; height: 48px; font-size: 26px; border-radius: 14px; }
.compare { display: grid; gap: 12px; }
.cmp { display: grid; gap: 6px; }
.cmp-row { display: grid; grid-template-columns: 56px 1fr 22px; gap: 10px; align-items: center; font-size: 0.85rem; color: var(--muted); }
.bar { height: 12px; background: var(--surface-2); border-radius: 99px; overflow: hidden; border: 1px solid var(--line); }
.bar > div { height: 100%; border-radius: 99px; background: var(--muted); }
.bar.now > div { background: var(--accent); }
.cmp-row b { font-family: var(--font-mono); color: var(--ink); font-weight: 500; text-align: right; }

/* ---------- Compartir ---------- */
.tones { display: flex; gap: 8px; flex-wrap: wrap; }
.tone { font: inherit; font-size: 0.9rem; font-weight: 700; border: 2px solid var(--line); background: var(--surface-2); border-radius: 999px; padding: 6px 12px; cursor: pointer; color: var(--ink); }
.tone[aria-pressed="true"] { background: var(--accent); color: #fff; border-color: var(--accent); }
.share-card {
  width: 100%; min-height: 150px; border: 2px dashed var(--link); border-radius: 18px; padding: 14px; background: var(--bubble);
  font: inherit; font-size: 1rem; line-height: 1.45; color: var(--ink); resize: vertical;
}
.socials { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.socials button { font: inherit; min-height: 50px; border-radius: 14px; border: 1px solid rgba(255, 255, 255, 0.15); color: #fff; font-weight: 700; cursor: pointer; font-size: 0.95rem; }
.toast { font-size: 0.9rem; color: var(--ok); min-height: 1.4em; }

/* ---------- Recursos ---------- */
.res-group { display: grid; gap: 8px; }
.res { border: 1px solid var(--line); border-radius: 14px; padding: 12px 14px; display: grid; gap: 4px; background: var(--surface-2); }
.res .name { font-weight: 700; }
.res .what { font-size: 0.92rem; color: var(--muted); line-height: 1.4; }
.res .hours { font-size: 0.85rem; color: var(--muted); }
.res-group { gap: 10px; scroll-margin-top: 120px; }
.res-group h3 { display: flex; align-items: center; gap: 10px; margin: 6px 0 0; font-size: 1.05rem; line-height: 1.25; }
.res-group h3 small { display: block; font-weight: 500; font-size: 0.82rem; color: var(--muted); }
.res-ico { --c: var(--accent); flex: none; width: 36px; height: 36px; border-radius: 11px; display: grid; place-items: center; font-size: 20px;
  background: color-mix(in srgb, var(--c) 35%, var(--surface)); color: color-mix(in srgb, var(--c) 35%, #fff); }
.res-acts { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }
.res-acts a { display: inline-flex; align-items: center; gap: 6px; min-height: 44px; padding: 8px 14px; border-radius: 999px; font-weight: 700; font-size: 0.92rem;
  text-decoration: none; border: 1px solid var(--line); color: var(--ink); background: var(--surface); word-break: break-all; }
.res-acts a.call { background: var(--accent); border-color: var(--accent); color: #fff; font-family: var(--font-mono); letter-spacing: 0.02em; }
.res-group.urgent .res { border-color: #7A2A3C; background: color-mix(in srgb, var(--bad) 12%, var(--surface-2)); }
.res-jump { display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px; scrollbar-width: none; }
.res-jump button { flex: none; font: inherit; font-size: 0.82rem; font-weight: 700; min-height: 38px; padding: 6px 12px; border-radius: 999px;
  border: 1px solid var(--line); background: var(--surface-2); color: var(--ink); cursor: pointer; white-space: nowrap; }
.credits { font-size: 0.85rem; color: var(--muted); display: grid; gap: 6px; }
.back-row { display: flex; }
.back-txt { font: inherit; font-weight: 700; color: var(--link); background: none; border: 0; padding: 6px 0; cursor: pointer; min-height: 40px; }

/* ---------- De vuelta ---------- */
.wb { display: flex; align-items: center; gap: 8px; background: rgba(255, 194, 61, 0.12); border: 1px solid rgba(255, 194, 61, 0.4); border-radius: 14px; padding: 8px 10px 8px 14px; font-size: 0.92rem; animation: pop 0.4s; }
.wb span { margin-right: auto; }
.wb-link { font: inherit; font-size: 0.85rem; font-weight: 700; color: var(--link); background: none; border: 0; cursor: pointer; padding: 4px; }
.wb-x { font: inherit; background: none; border: 0; cursor: pointer; color: var(--muted); padding: 4px 6px; }

/* ---------- Confirmación ---------- */
.dlg-wrap { position: fixed; inset: 0; z-index: 40; background: rgba(8, 10, 30, 0.55); display: grid; place-items: center; padding: 16px; }
.dlg { background: var(--surface); border: 1px solid var(--line); border-radius: 20px; padding: 20px; width: 100%; max-width: 380px; display: grid; gap: 12px; box-shadow: 0 12px 40px rgba(10, 12, 40, 0.35); animation: pop 0.25s; }
.dlg .btn-row { grid-template-columns: 1fr; }

/* ---------- Efectos ---------- */
.confetti { position: fixed; inset: 0; width: 100%; height: 100%; pointer-events: none; z-index: 60; }
.floatpts {
  position: fixed; z-index: 55; transform: translate(-50%, -50%); pointer-events: none; font-family: var(--font-display); font-weight: 800;
  font-size: 1.4rem; color: var(--ok); text-shadow: 0 2px 0 #000, 0 0 10px rgba(0, 0, 0, 0.8); animation: float-up 1.1s ease-out forwards;
}
@keyframes float-up { from { opacity: 1; margin-top: 0; } to { opacity: 0; margin-top: -60px; } }

@media (max-width: 430px) { .ea-logo { height: 22px; } .hud { gap: 6px; } }
@media (max-width: 370px) { .ea-logo { height: 18px; } .lvl { display: none; } }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition: none !important; }
}
</style>
</head>
<body>
<div class="app" id="app"></div>

<script>
(function () {
  const SERIES_URL = "https://espaciosabiertos.org/derecho-a-tener-derechos-2/";

  // ---------- Enlaces reales (de espaciosabiertos.org/derecho-a-tener-derechos-2/) ----------
  // video: episodio en YouTube (se reproduce dentro de la app)
  // pdf:   material educativo · book: formato libro en blanco y negro
  // Si un campo queda vacío (""), el botón abre la página de la serie.
  const UPLOADS = "https://espaciosabiertos.org/wp-content/uploads/";
  const LINKS = {
    // Episodio 1 · Derecho a tener derechos
    tener: { video: "https://www.youtube.com/watch?v=rMizWVmnEZA", pdf: UPLOADS + "Derecho-FINAL.pdf", book: UPLOADS + "EA-DERECHOS-01-Derechos-BW.pdf" },
    // Episodio 2 · Educación
    educacion: { video: "https://www.youtube.com/watch?v=fMN7G4piQV0", pdf: UPLOADS + "Educacion-FINAL.pdf", book: UPLOADS + "EA-DERECHOS-02-Educacion-BW.pdf" },
    // Episodio 3 · Acceso a la información
    info: { video: "https://www.youtube.com/watch?v=1ZD-S44Y36E", pdf: UPLOADS + "Informacion-FINAL.pdf", book: UPLOADS + "EA-DERECHOS-03-Informacion-BW.pdf" },
    // Episodio 4 · Participación política
    participacion: { video: "https://www.youtube.com/watch?v=KL3BpPgW2FY", pdf: UPLOADS + "Opinion-Politica-FINAL.pdf", book: UPLOADS + "EA-DERECHOS-04-PartPolitica-BW.pdf" },
    // Episodio 5 · Acceso a la justicia
    justicia: { video: "https://www.youtube.com/watch?v=YurWptHGE5M", pdf: UPLOADS + "Acceso-Justicia-FINAL.pdf", book: UPLOADS + "EA-DERECHOS-05-Justicia-BW.pdf" },
    // Episodio 6 · Trabajo
    trabajo: { video: "https://www.youtube.com/watch?v=p4gJn6G36VM", pdf: UPLOADS + "Trabajo-FINAL.pdf", book: UPLOADS + "EA-DERECHOS-06-Trabajo-BW.pdf" },
    // Episodio 7 · Dignidad
    dignidad: { video: "https://www.youtube.com/watch?v=yTGCsf9OpmA", pdf: UPLOADS + "Dignidad-FINAL.pdf", book: UPLOADS + "EA-DERECHOS-07-Dignidad-BW.pdf" }
  };
  const orSeries = (u) => u || SERIES_URL;

  // Saca el código de un video de YouTube (youtube.com/watch?v=, youtu.be/, /embed/, /shorts/)
  function youtubeId(url) {
    const m = (url || "").match(/(?:youtube(?:-nocookie)?\.com\/(?:watch\?(?:.*&)?v=|embed\/|shorts\/|live\/)|youtu\.be\/)([\w-]{11})/);
    return m ? m[1] : null;
  }

  // ---------- Textos de la interfaz ----------
  const T = {
    brand: "Línea de Defensa", help: "Ayuda",
    presents: "Espacios Abiertos presenta", tagline: "Derechos. Son tuyos. Defiéndelos.",
    welcomeBody: "Hoy te toca atender la línea. Siete personas te escriben porque algo no anda bien. Tu misión: descubrir qué derecho está en juego y ayudarles a defenderlo.",
    fact1: "⏱ 5–10 minutos", fact2: "💬 7 casos", fact3: "🔒 Tu avance se guarda solo en este dispositivo",
    start: "Empezar mi turno",
    preEyebrow: "Antes de empezar", preTitle: "¿Cómo llegas hoy?", preIntro: "Contesta con honestidad. Al final verás cuánto cambió.",
    q1: "Conozco mis derechos", q2: "Reconozco cuando violan un derecho", q3: "Sé a dónde acudir por ayuda",
    low: "Nada", high: "Mucho", cont: "Continuar",
    howEyebrow: "Tu turno", howTitle: "Así funciona cada caso",
    steps: [
      ["🔍", "Busca pistas", "Toca los objetos que brillan en la escena."],
      ["⚖️", "Nombra el derecho", "Escoge qué derecho está en juego."],
      ["🧭", "Decide qué hacer", "Recomienda el mejor próximo paso."]
    ],
    ranksTitle: "Sube de nivel y gana insignias",
    tipWrong: "Si te equivocas, no pierdes: te explicamos por qué y lo intentas otra vez (con menos puntos).",
    seeCases: "Atender el primer caso", allFound: "¡Encontraste las 3 pistas!", goingQ: "Léelas con calma y, cuando quieras, sigue a la pregunta.", nextQ: "Siguiente",
    inboxEyebrow: "Bandeja de entrada", inboxTitle: "Te están escribiendo", solved: "resueltos", level: "Nivel",
    new: "Nuevo", finish: "Terminar turno", resources: "Dónde pedir ayuda",
    step: "Paso", of: "de",
    tapScene: "Toca la escena y busca pistas", found: "pistas",
    whichRight: "¿Qué derecho está en juego?", correct: "¡Correcto!",
    whatDo: "¿Qué le recomiendas?", good: "¡Buena jugada!",
    unlocked: "Insignia desbloqueada", points: "puntos", keyIdea: "💡 Idea clave", whatHappened: "Lo que pasó:",
    perfect: "⭐ ¡Perfecto, a la primera!",
    learnMore: "Aprende más sobre este derecho", learnSub: (n) => `Video del episodio ${n} y material educativo`,
    episode: "Episodio", watch: "Ver el episodio",
    material: "Material educativo (PDF)", bookBW: "Libro en blanco y negro (PDF)", allMaterials: "Material de los 7 episodios", whereHelp: "Dónde pedir ayuda",
    seeReport: "Ver mi reporte",
    reportEyebrow: "Reporte de turno", reached: "Llegaste a", casesOf: "casos de 7", myBadges: "Tus insignias",
    afterTitle: "¿Y ahora cómo te sientes?", afterIntro: "Contesta otra vez para comparar.",
    before: "Antes", now: "Ahora", shareRank: "Invitar a más gente", playAgain: "Jugar otra vez",
    shareEyebrow: "Comparte", shareTitle: "Invita a tu gente",
    shareIntro: "Escoge un mensaje, cámbialo a tu manera y envíalo.",
    tones: { warm: "💛 De corazón", dare: "😉 Un reto", learn: "✍️ Lo que aprendí" },
    copyText: "Copiar mensaje", copyLink: "Copiar enlace", copied: "¡Copiado! Ya lo puedes pegar donde quieras.", copyFail: "No se pudo copiar. Selecciona el texto y cópialo.",
    resTitle: "Dónde pedir ayuda", resNote: "Toca un número para llamar. Datos verificados en fuentes oficiales (noviembre 2026); si alguno no contesta, prueba el otro número o el sitio web.",
    aboutSeries: "Sobre la serie",
    credits: "“Derechos. Son tuyos. Defiéndelos.” es una serie de 7 videos de Espacios Abiertos y el Centro de Periodismo Investigativo, con el apoyo de Open Society Foundations y la Fundación Puertorriqueña de las Humanidades. Se presentó por WIPR y recibió un premio Emmy en 2016.",
    openSite: "Abrir la página de la serie",
    proto: "Prototipo · contenido demostrativo",
    waiting: (n) => n === 1 ? "Queda 1 persona esperando tu respuesta." : `Quedan ${n} personas esperando tu respuesta.`,
    toRank: (pts, r) => `Te faltan <strong>${pts} pts</strong> para llegar a «${r}».`,
    maxRank: "¡Llegaste al nivel más alto! Termina los casos para completar tu turno.",
    allDone: "¡Atendiste a todas las personas! Ya puedes ver tu reporte.",
    levelUp: (r) => `⬆ ¡Subiste de nivel: ${r}!`,
    keepGoing: "Seguir atendiendo",
    newMsg: "Nuevo mensaje", nowTxt: "ahora", replyTo: "Responderle a",
    skip: "Saltar", replay: "Ver la escena otra vez", replayShort: "Ver escena",
    resumeCase: "Caso en curso", resumeGo: (n) => `Seguir con ${n}`, nextMsg: "Te escribieron", nextGo: (n) => `Responderle a ${n}`,
    allSeven: "¡Atendiste a las 7 personas!", allSevenSub: "Gracias por defender sus derechos. Mira cómo te fue.",
    streak: (n) => `🔥 ${n} seguidas`,
    lockedTitle: "Todavía está bloqueada", lockedBody: "Resuelve el caso de este derecho y aquí verás su video y su material educativo.",
    lockedNow: "¡Lo estás resolviendo ahora mismo! Termina el caso para desbloquear esta ficha.",
    close: "Cerrar", sound: "Sonido",
    welcomeBack: "¡Qué bueno verte! Seguimos donde lo dejaste.", startOver: "Empezar de nuevo", toInbox: "Ir a mis casos",
    finishTitle: "¿Terminar el turno ya?",
    finishBody: (n) => `Todavía ${n === 1 ? "hay 1 persona" : `hay ${n} personas`} esperando ayuda. Cada caso te da hasta 120 puntos.`,
    finishAnyway: "Terminar de todos modos",
    restartTitle: "¿Empezar de nuevo?",
    restartBody: "Se borrarán tus puntos, tus insignias y tus respuestas.",
    restartYes: "Sí, empezar de nuevo", cancel: "Cancelar",
    ranks: ["En entrenamiento", "Voz de apoyo", "Línea firme", "Defensa total"],
    rankIcons: ["🎧", "📣", "🛡️", "🏆"]
  };

  // Mensajes para invitar a más gente (la persona los puede editar)
  const SHARE = {
    warm: (r, n) => n === 7
      ? "Hoy me tocó atender la Línea de Defensa 🛡️ y ayudé a 7 personas a defender sus derechos: una estudiante que no podía llegar a su salón, una señora que solo quería votar, un enfermero al que no querían contratar… Me quedé pensando en cuántas veces nos pasa algo así y no sabemos qué hacer. Terminé como «" + r + "». Son 10 minutitos y de verdad vale la pena 💛"
      : "Hoy me tocó atender la Línea de Defensa 🛡️ y ya ayudé a " + n + " de 7 personas a defender sus derechos. Me quedé pensando en cuántas veces nos pasa algo así y no sabemos qué hacer. Son 10 minutitos y de verdad vale la pena 💛",
    dare: (r, n, p) => "¿Sabrías qué hacer si te niegan un derecho? 🤔 Yo creía que sí… hasta que jugué Línea de Defensa. Llegué a «" + r + "» con " + p + " puntos. ¿Te atreves a ganarme? 😉",
    learn: () => "Algo que aprendí hoy: tener derechos no basta, también hay que saber defenderlos ✊ Y casi siempre el primer paso es el mismo: anotar lo que pasó y pedir ayuda. Lo aprendí jugando Línea de Defensa, de la serie “Derechos. Son tuyos. Defiéndelos.”"
  };

  // ---------- Íconos de los 7 derechos (líneas, 24×24) ----------
  const ICONS = {
    tener: '<circle cx="12" cy="7.5" r="3.2"/><path d="M5.5 20.5c.6-4.2 3.2-6.7 6.5-6.7s5.9 2.5 6.5 6.7"/><path d="M19.2 2.6l.8 1.6 1.7.3-1.2 1.2.3 1.7-1.6-.8-1.5.8.3-1.7-1.2-1.2 1.7-.3z" fill="currentColor" stroke-width="1"/>',
    educacion: '<path d="M2 9.5 12 5l10 4.5-10 4.5z"/><path d="M6 11.6V16c0 1.5 2.7 3 6 3s6-1.5 6-3v-4.4"/><path d="M22 9.5V15"/>',
    info: '<path d="M13 21H6V3h8l4 4v5"/><path d="M14 3v4h4"/><path d="M9 10h5M9 13.5h3"/><circle cx="16.5" cy="16.5" r="3"/><path d="m18.7 18.7 2.6 2.6"/>',
    participacion: '<path d="M3.5 12h17v8.5h-17z"/><path d="M8 12V4h8v8"/><path d="m10 8.2 1.6 1.6 2.8-3"/><path d="M8 16h8"/>',
    justicia: '<path d="M12 4v16M7.5 20h9M4.5 7h15"/><path d="M4.5 7 2 12.5a2.6 2.6 0 0 0 5 0z"/><path d="M19.5 7 17 12.5a2.6 2.6 0 0 0 5 0z"/>',
    trabajo: '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5.2c0-.7.5-1.2 1.2-1.2h3.6c.7 0 1.2.5 1.2 1.2V7"/><path d="M3 12.5h18"/><path d="M11 11.5h2v2.2h-2z"/>',
    dignidad: '<path d="M12 20.5s-8-4.8-8-10.6A4.3 4.3 0 0 1 12 7.3a4.3 4.3 0 0 1 8 2.6c0 5.8-8 10.6-8 10.6z"/>'
  };
  const rIcon = (id) => `<svg class="ricon" viewBox="0 0 24 24" aria-hidden="true">${ICONS[id]}</svg>`;

  // ---------- Contenido: los 7 derechos ----------
  const RIGHTS = {
    tener: { es: "Derecho a tener derechos", ep: 1, color: "#4B3CC9" },
    educacion: { es: "Educación", ep: 2, color: "#137A52" },
    info: { es: "Acceso a la información", ep: 3, color: "#1565B5" },
    participacion: { es: "Participación política", ep: 4, color: "#A65507" },
    justicia: { es: "Acceso a la justicia", ep: 5, color: "#6A3DB0" },
    trabajo: { es: "Trabajo", ep: 6, color: "#B3245A" },
    dignidad: { es: "Dignidad", ep: 7, color: "#C02E2E" }
  };

  // ---------- Contenido: los casos (demostrativos) ----------
  // look: cómo se dibuja el avatar · scene: qué escena se dibuja detrás de las pistas
  // why: por qué cada respuesta incorrecta no es el derecho en juego
  const CASES = [
    {
      id: "marco", right: "tener", name: "Marco", age: 31, color: "#B4462C", scene: "office",
      look: { skin: "#C68A5E", hair: "short", hairColor: "#2B1B12", shirt: "#B4462C", extra: ["stubble"] },
      other: { name: "Empleado", color: "#5A6378", look: { skin: "#E8C3A0", hair: "short", hairColor: "#6B4A2B", shirt: "#5A6378", extra: ["glasses"] },
        says: "Gente como tú no tiene derecho a quejarse.", reply: "¿Cómo que no? Tengo todos mis papeles en orden." },
      place: { es: "Oficina de gobierno" },
      msg: { es: "Fui a renovar un permiso y el empleado me dijo que “gente como yo” no tiene derecho a quejarse. ¿Eso es así?" },
      clues: [
        { icon: "🗣️", x: 22, y: 50, es: "“Gente como tú”: lo trataron como si valiera menos por ser de otro país." },
        { icon: "🪪", x: 52, y: 78, es: "Tenía todos sus documentos en orden." },
        { icon: "📜", x: 80, y: 34, es: "Afiche en la pared: “Todas las personas son iguales ante la ley”." }
      ],
      options: ["trabajo", "dignidad", "tener", "info", "educacion", "justicia", "participacion"],
      why: {
        trabajo: { es: "Marco no fue a buscar empleo: fue a renovar un permiso. Lo grave es que le dijeron que no tenía derecho a reclamar." },
        educacion: { es: "Aquí no hay escuela ni estudios de por medio. Le negaron algo más básico: que lo traten como una persona con derechos." },
        participacion: { es: "No se trata de votar ni de opinar sobre política. A Marco le dijeron que sus derechos no cuentan." },
        info: { es: "Marco no pidió ningún documento público. Lo grave es que le negaron, de entrada, que tuviera derechos." },
        justicia: { es: "Todavía no hay un caso ante un tribunal. Antes de eso, le dijeron que ni siquiera tenía derecho a reclamar." },
        dignidad: { es: "Lo trataron mal, sí, pero el golpe principal fue decirle que, por ser de otro país, sus derechos no cuentan." }
      },
      hint: { es: "Pista: a Marco le negaron algo más básico que un trámite. ¿Qué le dijeron que no tenía?" },
      rightFb: { es: "Toda persona tiene derecho a tener derechos, sin importar de dónde viene." },
      actions: [
        { es: "Irse y no volver más", ok: false, fb: { es: "Si se va sin decir nada, ese trato se repite con otras personas." } },
        { es: "Pedir un supervisor, anotar fecha, hora y nombre, y buscar orientación legal", ok: true, fb: { es: "Marco presentó una queja por escrito. La agencia lo atendió y le pidió disculpas." } },
        { es: "Gritarle al empleado", ok: false, fb: { es: "Es entendible, pero puede volverse en su contra. Documentar es más poderoso." } }
      ],
      key: { es: "La idea de que las personas tienen derecho a tener derechos se atribuye a Hannah Arendt, filósofa alemana y una de las principales intelectuales del siglo 20." }
    },
    {
      id: "valeria", right: "educacion", name: "Valeria", age: 19, color: "#2F7D6B", scene: "university",
      look: { skin: "#E0A880", hair: "long", hairColor: "#5A3420", shirt: "#2F7D6B", extra: [] },
      other: { name: "Oficina de matrícula", color: "#7A5C99", look: { skin: "#F0C9A8", hair: "bun", hairColor: "#3B2A1E", shirt: "#7A5C99", extra: [] },
        says: "El elevador sigue roto. Tome el curso el año que viene.", reply: "¿Y por qué tengo que esperar yo un año entero?" },
      place: { es: "Universidad" },
      msg: { es: "Me admitieron a la universidad, pero mi salón está en un tercer piso sin elevador. Uso silla de ruedas y me dicen que “lo tome el año que viene”." },
      clues: [
        { icon: "🛗", x: 20, y: 40, es: "El elevador lleva meses fuera de servicio." },
        { icon: "📩", x: 55, y: 70, es: "Correo de la universidad: “Espere al próximo año”." },
        { icon: "🦽", x: 82, y: 50, es: "Valeria necesita un acomodo razonable para llegar a clase." }
      ],
      options: ["dignidad", "info", "justicia", "participacion", "educacion", "tener", "trabajo"],
      why: {
        dignidad: { es: "El trato es injusto, sí, pero lo que se le está negando directamente es poder tomar sus clases." },
        info: { es: "Valeria no está pidiendo documentos: ya sabe lo que pasa. Lo que no puede es llegar a su salón." },
        justicia: { es: "Más adelante podría acudir a la justicia, pero el derecho que le están afectando ahora es el de estudiar." },
        tener: { es: "Nadie le dijo a Valeria que no tiene derechos: ya la admitieron. Lo que le impiden es llegar a sus clases." },
        participacion: { es: "No se trata de votar ni de elecciones. Se trata de poder llegar a su salón y estudiar este año." },
        trabajo: { es: "Valeria no está buscando empleo: es estudiante y quiere tomar su curso como los demás." }
      },
      hint: { es: "Pista: ¿qué es lo que Valeria no puede hacer por culpa del elevador?" },
      rightFb: { es: "La educación es un derecho, y eso incluye poder llegar al salón." },
      actions: [
        { es: "Solicitar por escrito un acomodo razonable y, si no responden, buscar asesoría legal", ok: true, fb: { es: "La universidad movió el curso a un salón accesible en el primer piso." } },
        { es: "Esperar al próximo año", ok: false, fb: { es: "Esperar no es su responsabilidad. La universidad tiene que buscar una solución." } },
        { es: "Dejar la universidad", ok: false, fb: { es: "Perdería algo a lo que tiene derecho. Hay caminos para exigir el acomodo." } }
      ],
      key: { es: "La Constitución de Puerto Rico establece que toda persona tiene derecho a una educación que fomente el pleno desarrollo de su personalidad." }
    },
    {
      id: "kiara", right: "info", name: "Kiara", age: 23, color: "#6A3FB5", scene: "townhall",
      look: { skin: "#8D5A3B", hair: "curly", hairColor: "#1E120C", shirt: "#6A3FB5", extra: ["earrings"] },
      other: { name: "Funcionario", color: "#4A5568", look: { skin: "#B07A55", hair: "buzz", hairColor: "#222222", shirt: "#4A5568", extra: ["stubble"] },
        says: "Eso está en trámite… vuelva otro día.", reply: "¡Ya van dos meses! Es información pública." },
      place: { es: "Municipio" },
      msg: { es: "Pedí al municipio el contrato del recogido de basura de mi barrio. Hace dos meses y nada. 😤" },
      clues: [
        { icon: "📄", x: 24, y: 72, es: "La carta de solicitud nunca tuvo respuesta." },
        { icon: "📅", x: 50, y: 32, es: "Ya pasaron dos meses desde que la entregó." },
        { icon: "💰", x: 80, y: 66, es: "El contrato se paga con dinero público." }
      ],
      options: ["educacion", "justicia", "trabajo", "dignidad", "info", "participacion", "tener"],
      why: {
        educacion: { es: "Kiara no está estudiando ni pidiendo clases: pidió un documento público." },
        trabajo: { es: "El contrato es de una empresa, pero Kiara no busca empleo: quiere saber cómo se usa el dinero de todos." },
        dignidad: { es: "Nadie la maltrató. El problema es que el municipio no le entrega información que es pública." },
        tener: { es: "A Kiara nadie le niega sus derechos en general. Le niegan algo concreto: un documento público." },
        participacion: { es: "Pedir cuentas ayuda a participar, pero lo que Kiara reclama ahora es ver el contrato: información pública." },
        justicia: { es: "Todavía no está en un tribunal. Primero está pidiendo información que el municipio tiene que entregar." }
      },
      hint: { es: "Pista: el contrato se paga con el dinero de todo el mundo. ¿Quién tiene derecho a verlo?" },
      rightFb: { es: "La información pública es tuya. El gobierno debe dártela." },
      actions: [
        { es: "Olvidarlo, no vale la pena", ok: false, fb: { es: "Si nadie pregunta, nadie rinde cuentas." } },
        { es: "Solo publicarlo en redes", ok: false, fb: { es: "Puede dar visibilidad, pero no obliga al municipio a contestar." } },
        { es: "Repetir la solicitud por escrito, guardar copia y buscar ayuda legal si no contestan", ok: true, fb: { es: "Kiara recibió el contrato dos semanas después. 🙌" } }
      ],
      key: { es: "La información es una herramienta vital para mantener nuestra democracia. Todas las personas tienen derecho a conocer la información pública que está en manos del Gobierno." }
    },
    {
      id: "ana", right: "participacion", name: "Doña Ana", age: 67, color: "#B07A12", scene: "home",
      look: { skin: "#E8B996", hair: "bun", hairColor: "#CFCFD6", shirt: "#B07A12", extra: ["glasses"] },
      other: { name: "Empleada", color: "#3D7EA6", look: { skin: "#D9A27A", hair: "long", hairColor: "#2A1A12", shirt: "#3D7EA6", extra: [] },
        says: "¿Votar desde aquí? Ay, eso es complicado.", reply: "Pero yo quiero votar, mija. Mi voz cuenta." },
      place: { es: "Égida" },
      msg: { es: "Quiero votar en las elecciones, pero no puedo caminar hasta el colegio. Me dijeron que “eso es complicado” y ya." },
      clues: [
        { icon: "🗳️", x: 24, y: 40, es: "Las elecciones son en tres semanas." },
        { icon: "🦯", x: 54, y: 74, es: "Doña Ana no puede caminar distancias largas." },
        { icon: "💬", x: 80, y: 44, es: "Nadie le explicó qué opciones tiene." }
      ],
      options: ["justicia", "tener", "dignidad", "participacion", "trabajo", "info", "educacion"],
      why: {
        justicia: { es: "Doña Ana no tiene un caso en el tribunal. Lo que quiere es votar." },
        tener: { es: "Nadie le dijo que no tiene derechos. Lo que le están poniendo difícil es votar, que es una forma de participar." },
        trabajo: { es: "Doña Ana no está buscando empleo. Quiere participar en las elecciones." },
        educacion: { es: "Doña Ana no quiere estudiar: quiere votar en las elecciones." },
        info: { es: "Ella ya sabe lo que quiere. Lo que le falta es una manera de votar sin tener que caminar al colegio." },
        dignidad: { es: "La respuesta fue desconsiderada, pero lo que está en juego es su voto: su participación política." }
      },
      hint: { es: "Pista: ¿qué quiere hacer Doña Ana en tres semanas?" },
      rightFb: { es: "Votar es participar. Este derecho es de todas las personas, también de quienes tienen dificultad para moverse." },
      actions: [
        { es: "No votar esta vez", ok: false, fb: { es: "Su voz cuenta. Hay opciones para quienes no pueden llegar al colegio." } },
        { es: "Pedirle a alguien que vote por ella", ok: false, fb: { es: "El voto es personal. Nadie puede votar en su lugar." } },
        { es: "Preguntar en la Comisión Estatal de Elecciones qué opciones hay para votar con acomodo", ok: true, fb: { es: "Doña Ana pudo votar con las opciones que le explicaron." } }
      ],
      key: { es: "Sin participación política no existe democracia. Este derecho debe reconocerse por igual a todas las personas, sin importar su posición social, sexo, raza u otras condiciones." }
    },
    {
      id: "jose", right: "justicia", name: "José", age: 35, color: "#1F5FA8", scene: "apartment",
      look: { skin: "#A86E48", hair: "short", hairColor: "#141414", shirt: "#1F5FA8", extra: ["beard"] },
      other: { name: "Dueño", color: "#7A3E2E", look: { skin: "#E2B48C", hair: "buzz", hairColor: "#9A9AA2", shirt: "#7A3E2E", extra: ["stubble"] },
        says: "Tienes dos días para irte. Si no, cambio la cerradura.", reply: "¿Dos días? ¿Y para dónde me voy?" },
      place: { es: "Apartamento" },
      msg: { es: "El dueño del apartamento me dejó una nota: tengo dos días para irme. No tengo dinero para un abogado. ¿Qué hago?" },
      clues: [
        { icon: "📝", x: 26, y: 46, es: "Nota en la puerta: “Tienes 2 días”. No hay orden de un tribunal." },
        { icon: "💵", x: 54, y: 74, es: "José no puede pagar un abogado." },
        { icon: "🔑", x: 80, y: 40, es: "El dueño amenazó con cambiar la cerradura." }
      ],
      options: ["info", "dignidad", "participacion", "educacion", "trabajo", "tener", "justicia"],
      why: {
        info: { es: "José ya sabe lo que le está pasando. Lo que necesita es usar la ley para defenderse, aunque no tenga dinero." },
        participacion: { es: "No se trata de votar ni de política: José necesita protección legal frente al desalojo." },
        educacion: { es: "No hay estudios de por medio. José necesita poder llegar a la ayuda legal." },
        tener: { es: "José tiene derechos como inquilino. Lo que necesita es poder defenderlos, aunque no tenga dinero." },
        trabajo: { es: "Esto no tiene que ver con su empleo, sino con su vivienda y con poder defenderse." },
        dignidad: { es: "La nota asusta, pero lo central es que nadie puede sacarlo sin un proceso legal, y él necesita ayuda para defenderse." }
      },
      hint: { es: "Pista: José necesita usar la ley para protegerse, aunque no tenga dinero." },
      rightFb: { es: "Tener derechos no basta: también tienes derecho a usar la ley para defenderlos." },
      actions: [
        { es: "Buscar servicios legales gratuitos: en general, para sacarte el dueño tiene que seguir un proceso legal", ok: true, fb: { es: "Con ayuda legal gratuita, José supo cuáles eran sus derechos y ganó tiempo para mudarse con dignidad." } },
        { es: "Irse ya, sin preguntar", ok: false, fb: { es: "Podría estar renunciando a protecciones que la ley le da." } },
        { es: "No hacer nada y esperar", ok: false, fb: { es: "Sin orientación, el problema puede crecer." } }
      ],
      key: { es: "El acceso a la justicia es el derecho que tienen todas las personas a utilizar las herramientas y mecanismos legales para que se reconozcan y protejan sus demás derechos." }
    },
    {
      id: "luis", right: "trabajo", name: "Luis", age: 27, color: "#A3326B", scene: "hospital",
      look: { skin: "#D69C72", hair: "buzz", hairColor: "#3A2414", shirt: "#3FA7A0", extra: [] },
      other: { name: "Entrevistadora", color: "#5B6B8C", look: { skin: "#C48B63", hair: "long", hairColor: "#4A2C1A", shirt: "#5B6B8C", extra: ["glasses"] },
        says: "Lo siento, este puesto es para mujeres.", reply: "Pero tengo licencia y experiencia…" },
      place: { es: "Hospital" },
      msg: { es: "Fui a una entrevista de enfermería y me dijeron que el puesto “es para mujeres”. Tengo licencia y experiencia." },
      clues: [
        { icon: "📋", x: 22, y: 44, es: "El anuncio pedía “personal de enfermería con licencia”." },
        { icon: "💬", x: 52, y: 72, es: "La entrevistadora dijo: “Es para mujeres”." },
        { icon: "🎓", x: 80, y: 40, es: "Luis cumple con todos los requisitos." }
      ],
      options: ["tener", "info", "trabajo", "justicia", "dignidad", "educacion", "participacion"],
      why: {
        dignidad: { es: "Lo trataron con prejuicio, sí, pero lo que le negaron fue un empleo por ser hombre." },
        tener: { es: "Nadie le dijo que no tiene derechos. Le cerraron la puerta a un trabajo para el que está preparado." },
        info: { es: "Luis no pidió documentos. Le negaron un puesto por su género." },
        educacion: { es: "Luis ya estudió y tiene su licencia. Lo que le niegan es el empleo." },
        participacion: { es: "No se trata de votar. Lo descartaron de un empleo por ser hombre." },
        justicia: { es: "Podría llegar a reclamar, pero el derecho que le violaron es el de trabajar sin discrimen." }
      },
      hint: { es: "Pista: lo que está en juego es el empleo de Luis." },
      rightFb: { es: "Tu género no define el trabajo que puedes hacer." },
      actions: [
        { es: "Aceptarlo porque “así son las cosas”", ok: false, fb: { es: "Así no tienen que ser. Es discriminación." } },
        { es: "Anotar lo que pasó y orientarse en una agencia u organización que atiende discriminación en el empleo", ok: true, fb: { es: "Luis presentó una querella. El hospital revisó su proceso de contratación." } },
        { es: "Cambiar de profesión", ok: false, fb: { es: "No debería renunciar a lo que estudió por un prejuicio." } }
      ],
      key: { es: "Todas las personas tienen derecho a seleccionar libremente su trabajo: las condiciones sociales o el género no deben definir el empleo que puede desempeñar." }
    },
    {
      id: "carmen", right: "dignidad", name: "Doña Carmen", age: 72, color: "#4E6B1F", scene: "clinic",
      look: { skin: "#7A4A2E", hair: "curly", hairColor: "#E4E4EA", shirt: "#4E6B1F", extra: ["glasses"] },
      other: { name: "Recepción", color: "#3FA7A0", look: { skin: "#F1CDB0", hair: "curly", hairColor: "#7A3B1E", shirt: "#3FA7A0", extra: [] },
        says: "¡SIÉNTESE Y ESPERE SU TURNO!", reply: "Llevo cinco horas… y no hay ni una silla." },
      place: { es: "Centro de salud" },
      msg: { es: "En el centro de salud me hablan gritando y me dejan horas esperando, sin silla ni agua. Como si yo no importara." },
      clues: [
        { icon: "🪑", x: 22, y: 70, es: "No hay sillas suficientes en la sala de espera." },
        { icon: "⏰", x: 52, y: 32, es: "Lleva cinco horas esperando." },
        { icon: "🗣️", x: 80, y: 62, es: "El personal le habla a gritos." }
      ],
      options: ["trabajo", "participacion", "info", "educacion", "justicia", "dignidad", "tener"],
      why: {
        trabajo: { es: "Doña Carmen no está buscando trabajo: es paciente y la están tratando sin respeto." },
        participacion: { es: "No se trata de votar ni de opinar sobre política. El problema es cómo la tratan." },
        educacion: { es: "No hay escuela de por medio. Lo que falta es respeto por ella como persona." },
        tener: { es: "Sí la atienden como paciente, pero sin respeto: gritos, horas de espera, sin silla ni agua." },
        info: { es: "No le están negando un documento. Le están negando un trato humano y respetuoso." },
        justicia: { es: "No hay un caso en tribunal. Lo que falla es el trato de todos los días: la tratan como si no importara." }
      },
      hint: { es: "Pista: Doña Carmen siente que la tratan como si no valiera. ¿Qué derecho protege ese valor?" },
      rightFb: { es: "Mereces respeto por el simple hecho de ser persona." },
      actions: [
        { es: "Quedarse callada", ok: false, fb: { es: "Su malestar es válido. Callar no cambia el trato." } },
        { es: "Irse sin que la atiendan", ok: false, fb: { es: "Su salud también es importante. Puede exigir respeto y seguir recibiendo atención." } },
        { es: "Pedir respeto con calma, anotar lo ocurrido y presentar una queja formal", ok: true, fb: { es: "La administración puso más sillas y habló con el personal sobre el trato." } }
      ],
      key: { es: "La dignidad humana es el valor que tienen las personas por el simple hecho de ser personas." }
    }
  ];

  // ---------- Recursos: dónde pedir ayuda ----------
  // Verificados en fuentes oficiales (sitios .pr.gov / .gov y directorio PR.gov) en noviembre de 2026.
  // Los números pueden cambiar: revisarlos de vez en cuando.
  // tel: número para marcar · email · web · hours: horario · note: para qué sirve
  const RESOURCES = [
    { tab: "Ayuda legal", icon: "⚖️", title: "Orientación legal gratis", sub: "Para cualquier duda sobre tus derechos", items: [
      { name: "Servicios Legales de Puerto Rico (Teleabogado)", note: "Orientación legal gratis por teléfono: vivienda, familia, empleo, consumidor y más. Para personas de bajos ingresos.",
        tel: ["1-800-981-5342", "787-728-5070"], hours: "Lunes a viernes, 8:00 a.m. a 5:30 p.m.", web: "https://www.servicioslegales.org" },
      { name: "Clínica de Asistencia Legal · Escuela de Derecho UPR", note: "Estudiantes de Derecho, supervisados por abogados, orientan y representan gratis.",
        tel: ["787-999-9545"], web: "https://derecho.uprrp.edu" },
      { name: "Pro Bono, Inc. (Colegio de Abogados)", note: "Abogados voluntarios que representan gratis a personas sin recursos.", web: "https://www.probonopr.org" } ] },
    { tab: "Gobierno", icon: "🏛️", right: "tener", title: "Si una agencia de gobierno te trata mal o te niega un servicio", items: [
      { name: "Oficina del Procurador del Ciudadano (Ombudsman)", note: "Recibe quejas contra agencias del gobierno: maltrato, trámites detenidos o servicios negados.",
        tel: ["787-724-7373"], email: "ombudsmanpr@opc.pr.gov", web: "https://ombudsman.pr.gov" },
      { name: "Comisión de Derechos Civiles", note: "Investiga violaciones de derechos civiles y educa sobre ellos.",
        tel: ["787-764-8686", "1-800-981-4144"], web: "https://cdc.pr.gov" } ] },
    { tab: "Información", icon: "📄", right: "info", title: "Si te niegan información pública", items: [
      { name: "Pide el documento por escrito", note: "La Ley 141-2019 (Ley de Transparencia) te da derecho a pedir documentos públicos. Escribe al Oficial de Información de la agencia y guarda copia. Si no te contestan, llama al Ombudsman (787-724-7373)." },
      { name: "Espacios Abiertos", note: "Organización que promueve la transparencia y el acceso a la información.", web: SERIES_URL } ] },
    { tab: "Votar", icon: "🗳️", right: "participacion", title: "Para votar", items: [
      { name: "Comisión Estatal de Elecciones (CEE)", note: "Inscripción, voto adelantado y voto en el hogar para personas que no pueden llegar al colegio.",
        tel: ["787-777-8682"], web: "https://www.ceepur.org" } ] },
    { tab: "Educación", icon: "🎓", right: "educacion", title: "En la escuela o la universidad", items: [
      { name: "Oficina de Protección y Defensa de las Personas con Impedimentos (OPDPI)", note: "Defiende los derechos de las personas con impedimentos, incluido el acceso a la educación.",
        tel: ["787-665-2120"], email: "info@opdpi.pr.gov", web: "https://www.opdpi.pr.gov" },
      { name: "Oficina de Derechos Civiles · Departamento de Educación federal", note: "Quejas por discrimen en escuelas y universidades que reciben fondos federales.",
        tel: ["1-800-421-3481"], email: "OCR@ed.gov" } ] },
    { tab: "Trabajo", icon: "💼", right: "trabajo", title: "En el trabajo", items: [
      { name: "Unidad Antidiscrimen · Departamento del Trabajo (DTRH)", note: "Querellas por discrimen en el empleo (sexo, edad, origen, impedimento y otros). Hay que presentarla dentro de un año.",
        tel: ["787-754-5806"], web: "https://www.trabajo.pr.gov/unidad_anti_discrimen.asp" },
      { name: "EEOC · Comisión federal de Igualdad de Oportunidades en el Empleo", note: "Oficina de San Juan, en Plaza Las Américas.",
        tel: ["1-800-669-4000"], web: "https://www.eeoc.gov/es" } ] },
    { tab: "Vivienda", icon: "🏠", right: "justicia", title: "Vivienda y desahucios", items: [
      { name: "Servicios Legales de Puerto Rico", note: "Nadie te puede sacar de tu casa sin una orden del tribunal. Pide orientación gratis antes de irte.",
        tel: ["1-800-981-5342"], web: "https://www.servicioslegales.org" },
      { name: "HUD · Línea de discrimen en la vivienda", note: "Si te niegan una vivienda por tu origen, sexo, impedimento u otra razón. Atienden en español.",
        tel: ["1-800-669-9777"], web: "https://www.hud.gov/espanol" } ] },
    { tab: "Salud", icon: "❤️", right: "dignidad", title: "Salud y personas mayores", items: [
      { name: "Oficina del Procurador del Paciente", note: "Quejas sobre servicios de salud, planes médicos y trato en hospitales o centros de salud.",
        tel: ["1-800-981-0031", "787-977-0909"], email: "info@opp.pr.gov", web: "https://www.opp.pr.gov" },
      { name: "Oficina del Procurador de las Personas de Edad Avanzada (OPPEA)", note: "Defiende los derechos de las personas de 60 años o más.",
        tel: ["787-721-6121"], web: "https://www.oppea.pr.gov" } ] },
    { tab: "Emergencias", icon: "🚨", title: "Emergencias", urgent: true, items: [
      { name: "Emergencias", note: "Si estás en peligro ahora mismo.", tel: ["911"] },
      { name: "Línea PAS (salud mental)", note: "Gratis, confidencial, 24 horas, todos los días. También por el 988.", tel: ["1-800-981-0023", "988"] } ] }
  ];

  const RANK_MIN = [0, 250, 500, 700];
  const INTRO_MS = 9900;       // mini escena entre las dos partes al abrir el caso
  const NOTIF_WAIT_MS = 4000;  // tiempo para leer el logro antes de que llegue el mensaje del caso nuevo
  const NEXT_WAIT_MS = 1000;   // pausa para ver la respuesta correcta en verde antes de seguir
  const MAX_POINTS = 120 * CASES.length;
  const STORE_KEY = "lineaDefensa.v2";
  const SOUND_KEY = "lineaDefensa.sound";

  // ---------- Dibujos: avatares ----------
  function avatar(c, mood) {
    const k = c.look, hc = k.hairColor, sk = k.skin, happy = mood === "happy";
    const back = k.hair === "long" ? `<path d="M15 30C14 11 50 11 49 30l1 22c-6 3-30 3-36 0z" fill="${hc}"/>` : "";
    const curls = [[20, 24, 5.5], [24, 17, 6], [32, 14, 6.5], [40, 17, 6], [44, 24, 5.5], [18, 31, 4.2], [46, 31, 4.2]];
    const top = {
      short: `<path d="M18.6 28C17.5 12 46.5 12 45.4 28c-2-6.5-7-9.5-13.4-9.5S20.6 21.5 18.6 28z" fill="${hc}"/>`,
      long: `<path d="M18 30C16.5 12 47.5 12 46 30c-3-7-9-11-15-10.5-5 .4-9.5 4-13 10.5z" fill="${hc}"/>`,
      curly: curls.map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${hc}"/>`).join(""),
      bun: `<circle cx="32" cy="11" r="6" fill="${hc}"/><path d="M19 27c0-12 26-12 26 0-3-5-8-7.5-13-7.5S22 22 19 27z" fill="${hc}"/>`,
      buzz: `<path d="M19.4 26c.6-11 24.6-11 25.2 0-3.5-4.5-7.5-5.6-12.6-5.6S22.9 21.5 19.4 26z" fill="${hc}"/>`
    }[k.hair];
    const stern = mood === "stern";
    const brows = happy ? "M23.5 25.4q2.5-2 5 0M35.5 25.4q2.5-2 5 0" : stern ? "M23.5 24.4l5 2M40.5 24.4l-5 2" : "M23.5 26.6l5-1.9M40.5 26.6l-5-1.9";
    const mouth = stern
      ? `<path d="M28.4 37.6h7.2" fill="none" stroke="#3A1F1A" stroke-width="1.7" stroke-linecap="round"/>`
      : happy
      ? `<path d="M26.8 36.2q5.2 5.6 10.4 0z" fill="#fff" stroke="#3A1F1A" stroke-width="1.5" stroke-linejoin="round"/>`
      : `<path d="M28.6 38.6q3.4-2.6 6.8 0" fill="none" stroke="#3A1F1A" stroke-width="1.6" stroke-linecap="round"/>`;
    const ex = k.extra || [];
    return `<span class="ava" style="--c:${c.color}"><svg viewBox="0 0 64 64" aria-hidden="true">
      ${back}
      <path d="M7 64c1-11 11-16.5 25-16.5S56 53 57 64z" fill="${k.shirt}"/>
      <path d="M27 47.5l5 6 5-6" fill="none" stroke="rgba(0,0,0,.22)" stroke-width="2"/>
      <path d="M27.5 40h9v8.5h-9z" fill="${sk}"/><path d="M27.5 40h9v4c-3 1.4-6 1.4-9 0z" fill="rgba(0,0,0,.12)"/>
      <circle cx="19.3" cy="31.5" r="3" fill="${sk}"/><circle cx="44.7" cy="31.5" r="3" fill="${sk}"/>
      <ellipse cx="32" cy="30" rx="13" ry="14.6" fill="${sk}"/>
      ${ex.includes("beard") ? `<path d="M19.5 32c1 9 6 13.5 12.5 13.5S43.5 41 44.5 32c-2 4-5 6-7 6.4-1.5-1.4-3.2-1.9-5.5-1.9s-4 .5-5.5 1.9c-2-.4-5-2.4-7-6.4z" fill="${hc}"/>` : ""}
      ${ex.includes("stubble") ? `<path d="M21 34c1.5 7 5.5 10 11 10s9.5-3 11-10c-2 3.5-6 5.5-11 5.5S23 37.5 21 34z" fill="${hc}" opacity=".22"/>` : ""}
      ${top}
      <path d="${brows}" fill="none" stroke="${hc === "#CFCFD6" || hc === "#E4E4EA" ? "#8A8A96" : hc}" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="27" cy="31" r="1.9" fill="#1D1B2B"/><circle cx="37" cy="31" r="1.9" fill="#1D1B2B"/>
      <circle cx="23.6" cy="36" r="2.6" fill="#FF7A8A" opacity="${happy ? ".45" : ".22"}"/><circle cx="40.4" cy="36" r="2.6" fill="#FF7A8A" opacity="${happy ? ".45" : ".22"}"/>
      ${ex.includes("glasses") ? `<g fill="none" stroke="#2A2A3A" stroke-width="1.4"><circle cx="27" cy="31" r="4.2"/><circle cx="37" cy="31" r="4.2"/><path d="M31.2 31h1.6"/></g>` : ""}
      ${ex.includes("earrings") ? `<circle cx="19" cy="36" r="1.7" fill="#FFC23D"/><circle cx="45" cy="36" r="1.7" fill="#FFC23D"/>` : ""}
      ${mouth}
    </svg></span>`;
  }

  // ---------- Dibujos: escenas (detrás de las pistas) ----------
  const windowArt = (x, y, w, h) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="2" fill="#fff"/><rect x="${x + 2}" y="${y + 2}" width="${w - 4}" height="${h - 4}" fill="#BFE3FF"/><circle cx="${x + w * 0.7}" cy="${y + h * 0.35}" r="${h * 0.12}" fill="#FFE08A"/><path d="M${x + 2} ${y + h - 6}q${w * 0.3} -7 ${w * 0.55} 0t${w * 0.45 - 4} 0V${y + h - 2}H${x + 2}z" fill="#9BD39B"/><path d="M${x + w / 2} ${y + 2}v${h - 4}" stroke="#fff" stroke-width="1.5"/>`;
  const chair = (x, col) => `<g fill="${col}"><rect x="${x}" y="58" width="14" height="4" rx="1"/><rect x="${x}" y="45" width="3" height="17" rx="1"/><rect x="${x + 1}" y="62" width="2" height="14"/><rect x="${x + 11}" y="62" width="2" height="14"/></g>`;
  const plant = (x) => `<rect x="${x}" y="64" width="11" height="12" rx="1" fill="#C8693C"/><circle cx="${x + 5.5}" cy="58" r="7" fill="#3E9B5A"/><circle cx="${x + 1}" cy="61" r="4" fill="#4FB06A"/><circle cx="${x + 10}" cy="61" r="4" fill="#4FB06A"/>`;
  const txt = (x, y, s, t, col) => `<text x="${x}" y="${y}" font-size="${s}" text-anchor="middle" fill="${col || "#fff"}" font-family="Arial, sans-serif" font-weight="700">${t}</text>`;
  const SCENES = {
    office: { wall: "#E7EAF7", floor: "#CDB99C", art: windowArt(8, 14, 34, 28) +
      `<rect x="60" y="11" width="42" height="12" rx="2" fill="#2B37D1"/>${txt(81, 19.4, 6, "TURNOS")}` +
      `<rect x="62" y="36" width="18" height="13" rx="1" fill="#2D3142"/><rect x="69" y="49" width="4" height="3" fill="#2D3142"/>` +
      `<rect x="50" y="54" width="68" height="22" fill="#8C6A4A"/><rect x="47" y="51" width="74" height="5" rx="1" fill="#A88563"/>` +
      `<rect x="124" y="16" width="26" height="34" rx="1" fill="#fff" stroke="#C9CDE3"/><path d="M128 23h18M128 28h18M128 33h13M128 38h16" stroke="#9AA0C3" stroke-width="1.6"/>` + plant(138) },
    university: { wall: "#E8F3EE", floor: "#B9C2CF", art:
      `<rect x="6" y="24" width="30" height="52" fill="#A9B4C2"/><path d="M21 24v52" stroke="#8592A3"/><rect x="9" y="15" width="24" height="8" rx="1" fill="#E03E3E"/>${txt(21, 21, 4.6, "AVERIADO")}` +
      `<rect x="48" y="14" width="58" height="34" rx="2" fill="#8C6A4A"/><rect x="51" y="17" width="52" height="28" fill="#2F5D4A"/><path d="M56 24h24M56 30h32M56 36h18" stroke="#E8F3EC" stroke-width="1.4" opacity=".8"/>` +
      `<path d="M116 76V70h7v-6h7v-6h7v-6h7v-6h7v-6h9v36z" fill="#D5DBE5" stroke="#9AA4B5" stroke-width=".8"/>${txt(150, 36, 7, "3", "#2B37D1")}` },
    townhall: { wall: "#D7E8FF", floor: "#D2C8B5", art:
      `<g fill="#fff" opacity=".9"><ellipse cx="18" cy="16" rx="11" ry="4"/><ellipse cx="146" cy="9" rx="9" ry="3"/></g>` +
      `<path d="M34 34 80 13l46 21z" fill="#E6DAC0"/><rect x="38" y="34" width="84" height="42" fill="#F3ECDD"/>${txt(80, 30, 5.5, "MUNICIPIO", "#7A6A4A")}` +
      `<g fill="#DCCFB4">${[42, 54, 92, 104, 116].map((x) => `<rect x="${x}" y="38" width="5" height="38"/>`).join("")}</g>` +
      `<rect x="70" y="50" width="18" height="26" rx="1" fill="#8C6A4A"/><path d="M79 50v26" stroke="#6E4E32"/>` +
      `<path d="M140 76V18" stroke="#777" stroke-width="1.5"/><path d="M140 19h17l-3.5 5.5 3.5 5.5h-17z" fill="#2B37D1"/>` },
    home: { wall: "#FCEBDD", floor: "#C8A27C", art: windowArt(58, 12, 40, 28) +
      `<path d="M54 10h8v34c-3-6-5-6-8-8zM102 10h-8v34c3-6 5-6 8-8z" fill="#D9485F" opacity=".85"/>` +
      `<rect x="12" y="46" width="42" height="12" rx="4" fill="#6E8AF0"/><rect x="10" y="56" width="46" height="18" rx="4" fill="#5C7AEA"/><rect x="6" y="52" width="10" height="22" rx="4" fill="#4A66D6"/><rect x="50" y="52" width="10" height="22" rx="4" fill="#4A66D6"/>` +
      `<rect x="114" y="16" width="24" height="26" rx="2" fill="#fff" stroke="#D6D9EC"/><rect x="114" y="16" width="24" height="7" fill="#E03E3E"/><g fill="#9AA0C3">${[0, 1, 2, 3].map((i) => [0, 1, 2].map((j) => `<rect x="${117 + i * 5}" y="${26 + j * 5}" width="3" height="3"/>`).join("")).join("")}</g>` + plant(132) },
    apartment: { wall: "#F4F0E6", floor: "#A57B55", art:
      `<path d="M18 76V42" stroke="#555" stroke-width="1.6"/><path d="M9 42h18l-4.5-11h-9z" fill="#FFC23D"/><rect x="13" y="74" width="10" height="2" fill="#555"/>` +
      `<rect x="56" y="20" width="36" height="56" rx="1" fill="#8C5A3C"/><rect x="60" y="25" width="28" height="21" fill="none" stroke="#6E4630" stroke-width="1.5"/><rect x="60" y="50" width="28" height="22" fill="none" stroke="#6E4630" stroke-width="1.5"/><circle cx="87" cy="50" r="2.2" fill="#FFC23D"/>` +
      `<rect x="64" y="29" width="13" height="11" fill="#FFF3A3" transform="rotate(-6 70 34)"/>` +
      `<rect x="112" y="16" width="30" height="22" rx="1" fill="#fff" stroke="#C9B48F" stroke-width="2"/><path d="M115 34l8-9 6 6 4-4 6 7z" fill="#7FB3D5"/>` +
      `<rect x="108" y="54" width="46" height="20" rx="4" fill="#A3326B" opacity=".85"/><rect x="104" y="50" width="10" height="24" rx="4" fill="#8A2A5A"/><rect x="148" y="50" width="10" height="24" rx="4" fill="#8A2A5A"/>` },
    hospital: { wall: "#E3F4F4", floor: "#BFD0D6", art:
      `<rect x="10" y="12" width="24" height="24" rx="5" fill="#fff"/><path d="M19.5 16h5v6.5H31v5h-6.5V34h-5v-6.5H13v-5h6.5z" fill="#E03E3E"/>` +
      `<rect x="44" y="14" width="44" height="30" rx="2" fill="#C89B6A"/><rect x="48" y="18" width="18" height="22" fill="#fff"/><path d="M51 23h12M51 27h12M51 31h8" stroke="#9AA0C3" stroke-width="1.3"/><rect x="70" y="18" width="14" height="13" fill="#FFF3A3"/>` +
      `<rect x="96" y="54" width="58" height="22" fill="#7FA7B5"/><rect x="94" y="51" width="62" height="5" rx="1" fill="#9CC0CC"/>` +
      `<rect x="112" y="38" width="18" height="13" rx="1" fill="#2D3142"/>` + chair(54, "#3FA7A0") + chair(74, "#3FA7A0") },
    clinic: { wall: "#F1EFFA", floor: "#C9C3B4", art:
      `<circle cx="80" cy="24" r="13" fill="#fff" stroke="#2D3142" stroke-width="2"/><path d="M80 24v-8M80 24l6 3.5" stroke="#2D3142" stroke-width="1.9" stroke-linecap="round"/>` +
      chair(8, "#E8890C") + chair(26, "#E8890C") +
      `<g opacity=".35">${chair(44, "#9AA0C3")}</g>` +
      `<rect x="92" y="56" width="11" height="20" fill="#D6D9EC"/><rect x="93" y="43" width="9" height="13" rx="3" fill="#F1F7FF" stroke="#B5C6DA"/>` +
      `<rect x="112" y="18" width="42" height="30" fill="#BFE3FF" stroke="#fff" stroke-width="3"/><rect x="108" y="48" width="50" height="28" fill="#9AA0C3"/>${txt(133, 63, 5.5, "RECEPCIÓN")}` }
  };
  function sceneArt(c) {
    const s = SCENES[c.scene];
    return `<svg class="scene-art" viewBox="0 0 160 110" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
      <rect width="160" height="110" fill="${s.wall}"/><rect y="76" width="160" height="34" fill="${s.floor}"/><rect y="74" width="160" height="3" fill="rgba(0,0,0,.12)"/>
      <g stroke="rgba(0,0,0,.07)" stroke-width=".7"><path d="M0 89H160M0 101H160M40 76 28 110M80 76v34M120 76l12 34"/></g>
      ${s.art}
    </svg>`;
  }

  // Logo de Espacios Abiertos (versión para fondo oscuro: "ea" en blanco, ¡ ! en rosado)
  const EA_LOGO = "data:image/png;base64,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";

  const shieldSvg = (w, h) => `<svg class="shield" viewBox="0 0 22 26" ${w ? `style="width:${w};height:${h}"` : ""} aria-hidden="true"><path d="M11 1 2 4.5v7.2C2 18 6 23 11 25c5-2 9-7 9-13.3V4.5Z" fill="var(--accent)" stroke="#fff" stroke-width="${w ? 1.2 : 0}"/><path d="m6.5 13 3.2 3.2L15.8 10" fill="none" stroke="var(--signal)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>`;

  // ---------- Sonidos (se generan en el navegador, sin archivos) ----------
  let SOUND = true;
  try { SOUND = localStorage.getItem(SOUND_KEY) !== "off"; } catch (_) {}
  let actx = null;
  function tone(f, at, dur, type, vol, f2) {
    if (!SOUND) return;
    try {
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      if (actx.state === "suspended") actx.resume();
      const t0 = actx.currentTime + at, o = actx.createOscillator(), g = actx.createGain();
      o.type = type || "sine";
      o.frequency.setValueAtTime(f, t0);
      if (f2) o.frequency.exponentialRampToValueAtTime(f2, t0 + dur);
      g.gain.setValueAtTime(0.0001, t0);
      g.gain.exponentialRampToValueAtTime(vol || 0.15, t0 + 0.015);
      g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
      o.connect(g); g.connect(actx.destination);
      o.start(t0); o.stop(t0 + dur + 0.05);
    } catch (_) {}
  }
  const SFX = {
    tap: () => tone(560, 0, 0.06, "sine", 0.06),
    talk: (hi) => [0, 0.09, 0.18, 0.3].forEach((d, i) => tone((hi ? 420 : 250) + ((i * 53) % 90), d, 0.07, "square", 0.035)),
    clue: () => { tone(784, 0, 0.09, "triangle", 0.14); tone(1175, 0.07, 0.15, "triangle", 0.12); },
    right: () => { tone(659, 0, 0.12, "triangle", 0.17); tone(988, 0.1, 0.25, "triangle", 0.17); },
    wrong: () => { tone(220, 0, 0.16, "square", 0.06, 165); tone(165, 0.14, 0.26, "square", 0.06, 110); },
    win: () => [523, 659, 784, 1047, 1319].forEach((f, i) => tone(f, i * 0.09, 0.32, "triangle", 0.13)),
    msg: () => { tone(1047, 0, 0.1, "sine", 0.13); tone(1397, 0.13, 0.2, "sine", 0.13); },
    level: () => [392, 523, 659, 784, 1047].forEach((f, i) => tone(f, 0.5 + i * 0.07, 0.22, "sawtooth", 0.05))
  };
  const vibrate = (ms) => { try { if (navigator.vibrate) navigator.vibrate(ms); } catch (_) {} };
  const calm = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Confeti y puntos que flotan ----------
  function confetti(big) {
    if (calm()) return;
    const cv = document.createElement("canvas");
    cv.className = "confetti";
    document.body.appendChild(cv);
    const dpr = Math.min(window.devicePixelRatio || 1, 2), W = window.innerWidth, H = window.innerHeight;
    cv.width = W * dpr; cv.height = H * dpr;
    const x = cv.getContext("2d"); x.scale(dpr, dpr);
    const cols = ["#FFC23D", "#2B37D1", "#E03E3E", "#1E9E6A", "#D6336C", "#1C7ED6", "#E8890C", "#9A2A9E"];
    const N = big ? 240 : 130, D = big ? 3800 : 2700;
    const ps = Array.from({ length: N }, (_, i) => {
      const left = i % 2 === 0;
      return { x: left ? -10 : W + 10, y: H * (0.5 + Math.random() * 0.35), vx: (left ? 1 : -1) * (3 + Math.random() * 8),
        vy: -(7 + Math.random() * 10), w: 6 + Math.random() * 6, h: 8 + Math.random() * 8, r: Math.random() * 6, vr: (Math.random() - 0.5) * 0.4, c: cols[i % cols.length] };
    });
    const t0 = performance.now();
    (function frame(now) {
      const el = now - t0;
      x.clearRect(0, 0, W, H);
      ps.forEach((p) => {
        p.vy += 0.3; p.vx *= 0.99; p.x += p.vx; p.y += p.vy; p.r += p.vr;
        x.save(); x.globalAlpha = Math.max(0, 1 - el / D); x.translate(p.x, p.y); x.rotate(p.r);
        x.fillStyle = p.c; x.fillRect(-p.w / 2, -p.h / 2, p.w, p.h * Math.abs(Math.cos(p.r * 1.5)) + 2); x.restore();
      });
      if (el < D) requestAnimationFrame(frame); else cv.remove();
    })(t0);
  }
  function floatPts(el, text) {
    if (!el || calm()) return;
    const r = el.getBoundingClientRect(), s = document.createElement("span");
    s.className = "floatpts"; s.textContent = text;
    s.style.left = r.left + r.width / 2 + "px"; s.style.top = r.top + "px";
    document.body.appendChild(s);
    setTimeout(() => s.remove(), 1200);
  }

  // ---------- Estado ----------
  const fresh = () => ({
    screen: "welcome", prevScreen: null, pre: [0, 0, 0], post: [0, 0, 0], points: 0, streak: 0,
    progress: {}, current: null, banner: null, shareTone: "warm", shareDraft: null,
    sheet: null, toast: "", confirm: null, welcomeBack: false
  });
  let S = fresh();
  const P = (id) => (S.progress[id] ||= { clues: [], dTries: 0, aTries: 0, dWrong: [], aWrong: [], dOk: false, aOk: false, earned: 0, done: false, startRank: null, introSeen: false });
  const firstOpen = () => CASES.find((c) => !P(c.id).done);
  const nextOpen = () => CASES.find((c) => c.id !== S.current && !P(c.id).done);
  const hasProgress = () => S.screen !== "welcome" || S.pre.some(Boolean) || S.points > 0;

  const t = (k) => T[k];
  const L = (o) => o.es;
  const rankIndex = (p) => RANK_MIN.reduce((acc, min, i) => (p >= min ? i : acc), 0);
  const solvedCount = () => CASES.filter((c) => P(c.id).done).length;
  const curCase = () => CASES.find((c) => c.id === S.current);
  const caseOfRight = (r) => CASES.find((c) => c.right === r);

  // ---------- Guardar el avance en este dispositivo ----------
  // Si la persona sale o recarga, vuelve a la misma pantalla.
  let canSave = false;
  function save() {
    try {
      const keep = ["screen", "prevScreen", "pre", "post", "points", "streak", "progress", "current", "banner", "shareTone", "shareDraft"];
      const data = {}; keep.forEach((k) => (data[k] = S[k]));
      localStorage.setItem(STORE_KEY, JSON.stringify(data));
      canSave = true;
    } catch (_) { canSave = false; }
  }
  function restore() {
    try {
      const d = JSON.parse(localStorage.getItem(STORE_KEY) || "null");
      if (!d || !d.screen || d.screen === "welcome") return;
      S = Object.assign(fresh(), d);
      if (!screens[S.screen]) S.screen = "inbox";
      if (["clues", "right", "action", "solved"].includes(S.screen) && !curCase()) S.screen = "inbox";
      if (S.screen === "clues" && P(S.current).clues.length === 3) S.screen = "right";
      S.welcomeBack = true;
    } catch (_) { S = fresh(); }
  }

  // La app vive dentro de un recuadro (iframe) de Streamlit. Si el recuadro es más alto o más
  // bajo que la pantalla, hay DOS barras de desplazamiento (la de la página y la del recuadro)
  // y el dedo mueve una u otra: eso causaba el "sube y baja". Solución: el recuadro ocupa
  // exactamente la pantalla y la página de afuera no se mueve; solo se desplaza la app.
  function fitFrame() {
    try {
      const fe = window.frameElement, pw = window.parent;
      if (!fe || !pw || pw === window) return;
      const h = Math.round((pw.visualViewport && pw.visualViewport.height) || pw.innerHeight);
      Object.assign(fe.style, { position: "fixed", top: "0", left: "0", width: "100%", height: h + "px",
        maxWidth: "none", border: "0", margin: "0", zIndex: "999990", background: "#060D20" });
      const pd = pw.document;
      pd.documentElement.style.overflow = "hidden"; pd.body.style.overflow = "hidden";
      pd.querySelectorAll('[data-testid="stMain"], [data-testid="stAppViewContainer"], section.main').forEach((e) => { e.style.overflow = "hidden"; });
      pd.documentElement.style.background = pd.body.style.background = "#060D20";
      if (!pw.__lineaDefensaFit) {
        pw.__lineaDefensaFit = true;
        pw.addEventListener("resize", () => { try { pw.__lineaDefensaFitFn && pw.__lineaDefensaFitFn(); } catch (_) {} });
        if (pw.visualViewport) pw.visualViewport.addEventListener("resize", () => { try { pw.__lineaDefensaFitFn && pw.__lineaDefensaFitFn(); } catch (_) {} });
      }
      pw.__lineaDefensaFitFn = fitFrame; // siempre la versión de este recuadro
      pw.scrollTo(0, 0);
    } catch (_) { /* página contenedora de otro origen: queda como recuadro normal */ }
  }

  // Desplaza solo dentro de la app (scrollIntoView movería también la página de afuera)
  function innerScroll(el, block) {
    const r = el.getBoundingClientRect(), vh = window.innerHeight, pad = 12;
    let dy = 0;
    if (block === "end" || r.bottom > vh - pad) dy = r.bottom - vh + pad;
    if (r.top + (dy) < pad) dy = r.top - pad;
    if (Math.abs(dy) > 1) window.scrollBy({ top: dy, behavior: calm() ? "auto" : "smooth" });
  }

  // Sube al inicio de la pantalla (dentro de la app; la página de afuera ya no se mueve).
  function toTop() {
    window.scrollTo(0, 0);
    try {
      const fe = window.frameElement;
      if (fe && fe.style.position !== "fixed" && fe.getBoundingClientRect().top < 0) fe.scrollIntoView({ block: "start" });
    } catch (_) { /* página contenedora de otro origen */ }
  }

  function go(screen, extra) {
    Object.assign(S, { screen, toast: "", banner: null, sheet: null, logoMenu: false }, extra || {});
    S.enter = true;
    render();
    S.enter = false;
    toTop();
  }

  // ---------- Piezas ----------
  function badgeBtn(c, extraCls) {
    const done = P(c.id).done, r = RIGHTS[c.right];
    return `<button class="rb ${done ? "on" : ""} ${S.justUnlocked === c.right ? "pop" : ""} ${extraCls || ""}" style="--c:${r.color}" data-act="info" data-v="${c.right}"
      aria-label="${L(r)}${done ? "" : " (bloqueada)"}" title="${L(r)}">${rIcon(c.right)}</button>`;
  }

  function topbar() {
    const game = !["welcome", "pre"].includes(S.screen);
    const ri = rankIndex(S.points), nextMin = RANK_MIN[ri + 1];
    const xp = nextMin ? ((S.points - RANK_MIN[ri]) / (nextMin - RANK_MIN[ri])) * 100 : 100;
    const n = solvedCount();
    return `<header class="topbar">
      <div class="hud">
        <button class="brand" data-act="${S.screen === "welcome" ? "noop" : "logoMenu"}" aria-haspopup="menu" aria-expanded="${!!S.logoMenu}" aria-label="Espacios Abiertos · ${t("brand")}${S.screen === "welcome" ? "" : ": menú"}"><img class="ea-logo" src="${EA_LOGO}" alt=""></button>
        ${game ? `<span class="lvl" title="${t("level")}: ${t("ranks")[ri]}">${t("rankIcons")[ri]} Nv ${ri + 1}</span>
          <span class="chip${S.bump ? " bump" : ""}" aria-label="${S.points} ${t("points")}">★ ${S.points}</span>` : ""}
        <button class="icon-btn" data-act="sound" aria-pressed="${SOUND}" aria-label="${t("sound")}">${SOUND ? "🔊" : "🔇"}</button>
        ${S.screen !== "resources" ? `<button class="icon-btn" data-act="go" data-v="resources" aria-label="${t("help")}" title="${t("help")}">❓</button>` : ""}
      </div>
      ${game ? `<div class="badges-row" aria-label="${t("myBadges")}: ${n} ${t("of")} 7">${CASES.map((c) => badgeBtn(c)).join("")}<span class="count">${n}/7</span></div>
        <div class="xp" role="progressbar" aria-label="${t("level")}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.round(xp)}"><i style="width:${xp}%"></i></div>` : ""}
      ${S.logoMenu ? `<div class="logo-menu" role="menu">
        ${game && S.screen !== "inbox" ? `<button role="menuitem" data-act="go" data-v="inbox">📬 ${t("toInbox")}</button>` : ""}
        <button role="menuitem" data-act="restart">↺ ${t("startOver")}</button>
      </div>` : ""}
    </header>`;
  }

  function scaleQ(name, idx, arr) {
    const v = arr[idx];
    return `<fieldset class="q">
      <legend>${t("q" + (idx + 1))}</legend>
      <div class="scale">${[1, 2, 3, 4, 5].map((n) => `<label><input type="radio" id="${name}${idx}-${n}" name="${name}${idx}" value="${n}" data-act="rate" data-set="${name}" data-i="${idx}" ${v === n ? "checked" : ""}><span>${n}</span></label>`).join("")}</div>
      <div class="scale-ends"><span>${t("low")}</span><span>${t("high")}</span></div>
    </fieldset>`;
  }

  function caseHead(n, c) {
    return `<div class="case-head">
      <button class="back" data-act="go" data-v="inbox" aria-label="Volver a la bandeja">←</button>
      ${avatar(c)}
      <span class="ch-name"><strong>${c.name}, ${c.age}</strong><small>📍 ${L(c.place)}</small></span>
      <span class="stepper" aria-label="${t("step")} ${n} ${t("of")} 3">${[1, 2, 3].map((i) => `<i class="${i <= n ? "on" : ""}"></i>`).join("")}</span>
    </div>`;
  }

  function streakTxt() { return S.streak >= 2 ? ` · ${t("streak")(S.streak)}` : ""; }

  // Mini escena: la persona del caso (izquierda) y la otra parte (derecha) hablan
  function intro(c) {
    const el = introStart ? Date.now() - introStart : 0; // si se redibuja, sigue donde iba
    const o = c.other;
    return `<div class="intro" style="--el:${el}ms" aria-live="polite">
      <span class="actor l">${avatar(c)}</span>
      <span class="actor r">${avatar(o, "stern")}</span>
      <p class="say r"><small>${o.name}</small>${o.says}</p>
      <p class="say l"><small>${c.name}</small>${o.reply}</p>
      <button class="skip" data-act="skipIntro">${t("skip")} ⏭</button>
    </div>`;
  }

  // ---------- Pantallas ----------
  const screens = {
    welcome() {
      const orbs = CASES.map((c, i) => {
        const a = (i / CASES.length) * Math.PI * 2 - Math.PI / 2;
        return `<span class="orb" style="--i:${i};left:${50 + 39 * Math.cos(a)}%;top:${50 + 39 * Math.sin(a)}%">${avatar(c, "happy")}</span>`;
      }).join("");
      return `<div class="hero">
          <div class="orbit">${orbs}<span class="hero-shield">${shieldSvg("100%", "100%")}</span></div>
          <span class="eyebrow">${t("presents")}</span>
          <h1>${t("brand")}</h1>
          <p class="tag">${t("tagline")}</p>
        </div>
        <p>${t("welcomeBody")}</p>
        <div class="facts"><span class="fact">${t("fact1")}</span><span class="fact">${t("fact2")}</span><span class="fact">${t("fact3")}</span></div>
        <button class="btn" data-act="go" data-v="pre">${t("start")} →</button>
        <p class="proto-tag">${t("proto")}</p>`;
    },
    pre() {
      const ready = S.pre.every(Boolean);
      return `<span class="eyebrow">${t("preEyebrow")}</span>
        <h2>${t("preTitle")}</h2>
        <p class="muted">${t("preIntro")}</p>
        ${[0, 1, 2].map((i) => scaleQ("pre", i, S.pre)).join("")}
        <button class="btn" data-act="go" data-v="how" ${ready ? "" : "disabled"}>${t("cont")} →</button>`;
    },
    how() {
      return `<span class="eyebrow">${t("howEyebrow")}</span>
        <h2>${t("howTitle")}</h2>
        <ol class="steps">
          ${t("steps").map(([ico, ti, d]) => `<li><span class="step-ico">${ico}</span><div><h3>${ti}</h3><p class="muted small">${d}</p></div></li>`).join("")}
        </ol>
        <h3>${t("ranksTitle")}</h3>
        <div class="ladder">${t("ranks").map((r, i) => `<div class="rung"><b>${t("rankIcons")[i]}</b><span>${r}</span><span class="pts">${RANK_MIN[i]}+ pts</span></div>`).join("")}</div>
        <p class="note">${t("tipWrong")}</p>
        <button class="btn" data-act="open" data-v="${firstOpen().id}">${t("seeCases")} →</button>`;
    },
    inbox() {
      const n = solvedCount();
      const cur = S.current && !P(S.current).done ? curCase() : null, nx = cur || firstOpen();
      return `${nx ? `<button class="resume" data-act="open" data-v="${nx.id}">
            ${avatar(nx)}
            <span><small>${cur ? t("resumeCase") : t("nextMsg")}</small><strong>${cur ? t("resumeGo")(nx.name) : t("nextGo")(nx.name)}</strong></span>
            <span class="go">▶</span>
          </button>` : ""}
        <div class="status"><span><strong>${n}</strong> ${t("of")} 7 ${t("solved")}</span><span class="muted small">${t("level")}: <strong>${t("ranks")[rankIndex(S.points)]}</strong></span></div>
        ${nudge(n)}
        <div class="inbox">
          ${CASES.map((c) => {
            const done = P(c.id).done;
            return `<button class="msg" data-act="open" data-v="${c.id}">
              ${avatar(c, done ? "happy" : "")}
              <span class="msg-body"><span class="msg-name">${c.name}</span><span class="msg-prev">${L(c.msg)}</span></span>
              ${done ? `<span class="rb on" style="--c:${RIGHTS[c.right].color}" aria-label="${L(RIGHTS[c.right])}">${rIcon(c.right)}</span>` : `<span class="pill">${t("new")}</span>`}
            </button>`;
          }).join("")}
        </div>
        <div class="btn-row">
          <button class="btn ghost" data-act="go" data-v="resources">${t("resources")}</button>
          <button class="btn ${n === 7 ? "" : "ghost"}" data-act="finish">${n === 7 ? t("seeReport") : t("finish")}</button>
        </div>`;
    },
    clues() {
      const c = curCase(), p = P(c.id), all = p.clues.length === 3;
      return `${caseHead(1, c)}
        <div class="bubble">${L(c.msg)}</div>
        <div class="scene ${p.introSeen ? (S.spotsIn ? "spots-in" : "") : "playing"}" role="group" aria-label="${L(c.place)}">
          ${sceneArt(c)}
          <span class="scene-tag l">🔍 ${p.clues.length}/3 ${t("found")}</span>
          ${p.introSeen ? `<button class="scene-tag r replay" data-act="replay" aria-label="${t("replay")}">▶ ${t("replayShort")}</button>` : intro(c)}
          ${c.clues.map((cl, i) => `<button class="spot ${p.clues.includes(i) ? "found" : ""} ${S.justClue === i ? "just" : ""}" style="left:${cl.x}%;top:${cl.y}%" data-act="clue" data-v="${i}" aria-label="${p.clues.includes(i) ? L(cl) : t("tapScene")}">${cl.icon}</button>`).join("")}
        </div>
        ${p.clues.length ? "" : `<p class="tip">👆 ${t("tapScene")}</p>`}
        <ul class="clues" aria-live="polite">
          ${p.clues.map((i) => `<li class="${S.justClue === i ? "just" : ""}"><span>${c.clues[i].icon}</span><span>${L(c.clues[i])}</span><span class="plus">+10</span></li>`).join("")}
        </ul>
        ${all ? `<div class="wait" role="status">
            <p>✓ ${t("allFound")} <span class="muted">${t("goingQ")}</span></p>
            <button class="btn" data-act="go" data-v="right">${t("nextQ")} →</button>
          </div>` : ""}`;
    },
    right() {
      const c = curCase(), p = P(c.id);
      return `${caseHead(2, c)}
        <div class="bubble mini">${L(c.msg)}</div>
        <h2 class="q-title">${t("whichRight")}</h2>
        <div class="options all7">
          ${c.options.map((r, n) => {
            const wrong = p.dWrong.includes(r), ok = p.dOk && r === c.right;
            const cls = ok ? "right" : wrong ? "wrong" : "";
            return `<button class="opt ${cls} ${S.shake === r ? "shake" : ""}" style="--n:${n}" data-act="answerRight" data-v="${r}" ${p.dOk || wrong ? "disabled" : ""}>
              <span class="opt-ico" style="--c:${RIGHTS[r].color}">${rIcon(r)}</span>
              <span class="opt-txt"><span>${L(RIGHTS[r])}</span>${wrong ? `<small class="why">${L(c.why[r])}</small>` : ""}</span>
              <span class="mark">${ok ? "✓" : wrong ? "✕" : ""}</span></button>`;
          }).join("")}
        </div>
        ${p.dWrong.length && !p.dOk ? `<p class="hint">💡 ${L(c.hint)}</p>` : ""}`;
    },
    action() {
      const c = curCase(), p = P(c.id), b = S.banner;
      return `${caseHead(3, c)}
        ${b ? `<div class="okbar" role="status"><strong>✓ ${b.title}</strong><span>${b.text}</span></div>` : ""}
        <div class="bubble mini">${L(c.msg)}</div>
        <h2 class="q-title">${t("whatDo")}</h2>
        <div class="options">
          ${c.actions.map((a, i) => {
            const wrong = p.aWrong.includes(i), ok = p.aOk && a.ok;
            const cls = ok ? "right" : wrong ? "wrong" : "";
            return `<button class="opt ${cls} ${S.shake === i ? "shake" : ""}" style="--n:${i}" data-act="answerAction" data-v="${i}" ${p.aOk || wrong ? "disabled" : ""}>
              <span class="opt-ico" style="--c:var(--accent)">${"ABC"[i]}</span>
              <span class="opt-txt"><span>${L(a)}</span>${wrong ? `<small class="why">${L(a.fb)}</small>` : ""}</span>
              <span class="mark">${ok ? "✓" : wrong ? "✕" : ""}</span></button>`;
          }).join("")}
        </div>`;
    },
    solved() {
      const c = curCase(), p = P(c.id), r = RIGHTS[c.right], b = S.banner;
      const all = solvedCount() === 7, nx = nextOpen(), ri = rankIndex(S.points);
      const up = p.startRank !== null && ri > p.startRank;
      const perfect = p.dTries === 0 && p.aTries === 0;
      return `<section class="win" style="--c:${r.color}">
          <div class="win-top">${avatar(c, "happy")}<span class="win-badge">${rIcon(c.right)}</span></div>
          <span class="eyebrow">🏅 ${t("unlocked")}</span>
          <h2>${L(r)}</h2>
          <div class="win-pts"><b>+${p.earned}</b> ${t("points")}</div>
          ${perfect ? `<div>${t("perfect")}</div>` : ""}
          ${b ? `<p class="win-story"><strong>${t("whatHappened")}</strong> ${b.text}</p>` : ""}
        </section>
        ${up ? `<div class="levelup" role="status">${t("levelUp")(t("rankIcons")[ri] + " " + t("ranks")[ri])}</div>` : ""}
        <div class="keyidea"><span class="eyebrow">${t("keyIdea")}</span><p>${L(c.key)}</p></div>
        <button class="learn-btn" data-act="info" data-v="${c.right}">
          <span class="play" aria-hidden="true"></span>
          <span><strong>${t("learnMore")}</strong><small>${t("learnSub")(r.ep)}</small></span>
          <span class="arrow">→</span>
        </button>
        ${all ? `<div class="final"><b>🏆</b><h2>${t("allSeven")}</h2><p>${t("allSevenSub")}</p>
              <button class="btn signal" data-act="go" data-v="report">${t("seeReport")} →</button></div>`
          : `<div class="notif" role="status" style="--notif-wait:${NOTIF_WAIT_MS}ms;--el:${S.solvedAt ? Date.now() - S.solvedAt : 99999}ms">
              <span class="notif-dot" aria-hidden="true">${7 - solvedCount()}</span>
              <div class="notif-head"><span class="ring" aria-hidden="true">📱</span><span>💬 ${t("newMsg")}</span><span class="notif-time">${t("nowTxt")}</span></div>
              <div class="notif-body">${avatar(nx)}<div><strong>${nx.name}, ${nx.age}</strong><p>${L(nx.msg)}</p></div></div>
              <button class="btn signal" data-act="open" data-v="${nx.id}">${t("replyTo")} ${nx.name} →</button>
            </div>`}`;
    },
    report() {
      const ri = rankIndex(S.points), n = solvedCount();
      const ready = S.post.every(Boolean);
      return `<div class="medal">
          <span class="eyebrow">${t("reportEyebrow")} · ${t("reached")}</span>
          <span class="trophy" aria-hidden="true">${t("rankIcons")[ri]}</span>
          <span class="rank">${t("ranks")[ri]}</span>
          <span class="score">★ ${S.points} / ${MAX_POINTS} · ${n} ${t("casesOf")}</span>
        </div>
        <h3>${t("myBadges")}</h3>
        <div class="badge-grid">${CASES.map((c) => `<span class="bg-item">${badgeBtn(c)}<span>${L(RIGHTS[c.right])}</span></span>`).join("")}</div>
        ${n < 7 ? `<button class="btn ghost" data-act="go" data-v="inbox">← ${t("keepGoing")} (${7 - n})</button>` : ""}
        <h2>${t("afterTitle")}</h2>
        <p class="muted">${t("afterIntro")}</p>
        ${[0, 1, 2].map((i) => scaleQ("post", i, S.post)).join("")}
        ${ready ? `<div class="compare">${[0, 1, 2].map((i) => `<div class="cmp"><strong>${t("q" + (i + 1))}</strong>
            <div class="cmp-row"><span>${t("before")}</span><div class="bar"><div style="width:${(S.pre[i] || 0) * 20}%"></div></div><b>${S.pre[i] || "–"}</b></div>
            <div class="cmp-row"><span>${t("now")}</span><div class="bar now"><div style="width:${S.post[i] * 20}%"></div></div><b>${S.post[i]}</b></div>
          </div>`).join("")}</div>` : ""}
        <button class="btn" data-act="go" data-v="share" ${ready ? "" : "disabled"}>💌 ${t("shareRank")} →</button>`;
    },
    share() {
      const txt = S.shareDraft ?? SHARE[S.shareTone](t("ranks")[rankIndex(S.points)], solvedCount(), S.points);
      return `<span class="eyebrow">${t("shareEyebrow")}</span>
        <h2>${t("shareTitle")}</h2>
        <p class="muted">${t("shareIntro")}</p>
        <div class="tones">${Object.entries(t("tones")).map(([k, v]) => `<button class="tone" data-act="tone" data-v="${k}" aria-pressed="${S.shareTone === k}">${v}</button>`).join("")}</div>
        <textarea class="share-card" id="share-text" aria-label="Mensaje para compartir">${txt}</textarea>
        <div class="btn-row">
          <button class="btn" data-act="copy" data-v="text">${t("copyText")}</button>
          <button class="btn ghost" data-act="copy" data-v="link">${t("copyLink")}</button>
        </div>
        <p class="toast" aria-live="polite">${S.toast}</p>
        <div class="socials">
          <button data-act="social" data-v="wa" style="background:#1E9E57">WhatsApp</button>
          <button data-act="social" data-v="fb" style="background:#1877F2">Facebook</button>
          <button data-act="social" data-v="x" style="background:#000">X</button>
        </div>
        <button class="btn ghost" data-act="restart">↺ ${t("playAgain")}</button>`;
    },
    resources() {
      return `<div class="back-row"><button class="back-txt" data-act="go" data-v="${S.prevScreen && S.prevScreen !== "resources" ? S.prevScreen : "inbox"}">← Volver</button></div>
        <h2>📞 ${t("resTitle")}</h2>
        <p class="note">${t("resNote")}</p>
        <nav class="res-jump" aria-label="Temas">${RESOURCES.map((g, n) => `<button data-act="resJump" data-v="${n}">${g.icon} ${g.tab}</button>`).join("")}</nav>
        ${RESOURCES.map((g, n) => `<section class="res-group${g.urgent ? " urgent" : ""}" id="res-${n}">
          <h3><span class="res-ico" ${g.right ? `style="--c:${RIGHTS[g.right].color}"` : ""}>${g.right ? rIcon(g.right) : g.icon}</span><span>${g.title}${g.sub ? `<small>${g.sub}</small>` : ""}</span></h3>
          ${g.items.map((it) => `<div class="res">
            <span class="name">${it.name}</span>
            <span class="what">${it.note}</span>
            ${it.hours ? `<span class="hours">🕘 ${it.hours}</span>` : ""}
            <div class="res-acts">
              ${(it.tel || []).map((n) => `<a class="call" href="tel:${n.replace(/[^0-9]/g, "")}" target="_blank" rel="noopener" aria-label="Llamar al ${n}">📞 ${n}</a>`).join("")}
              ${it.email ? `<a class="mail" href="mailto:${it.email}" target="_blank" rel="noopener">✉️ ${it.email}</a>` : ""}
              ${it.web ? `<a class="web" href="${it.web}" target="_blank" rel="noopener">🌐 Sitio web ↗</a>` : ""}
            </div>
          </div>`).join("")}
        </section>`).join("")}
        <div class="credits"><h3>${t("aboutSeries")}</h3><p>${t("credits")}</p></div>
        <a class="btn ghost" href="${SERIES_URL}" target="_blank" rel="noopener">${t("openSite")} ↗</a>`;
    }
  };

  function nudge(n) {
    if (n === 7) return `<div class="nudge">${t("allDone")}</div>`;
    const ri = rankIndex(S.points);
    const rankLine = ri < RANK_MIN.length - 1 ? t("toRank")(RANK_MIN[ri + 1] - S.points, t("ranks")[ri + 1]) : t("maxRank");
    return `<div class="nudge"><span>${t("waiting")(7 - n)}</span><span>${rankLine}</span></div>`;
  }

  // Ventana de confirmación dentro de la app
  function dialog() {
    const d = S.confirm;
    if (!d) return "";
    return `<div class="dlg-wrap" data-act="cancelConfirm">
      <div class="dlg" role="alertdialog" aria-modal="true" aria-labelledby="dlg-t">
        <h3 id="dlg-t">${d.title}</h3>
        <p class="muted">${d.body}</p>
        <div class="btn-row">
          <button class="btn" data-act="cancelConfirm">${d.stay}</button>
          <button class="btn ghost" data-act="${d.act}">${d.leave}</button>
        </div>
      </div>
    </div>`;
  }

  // Ficha de un derecho: se abre al tocar su ícono (arriba, en el reporte o en "Aprende más")
  function rightSheet() {
    const id = S.sheet;
    if (!id) return "";
    const r = RIGHTS[id], c = caseOfRight(id), p = P(c.id);
    const solvingNow = c.id === S.current && ["clues", "right", "action"].includes(S.screen);
    const body = p.done
      ? `<div class="keyidea"><span class="eyebrow">${t("keyIdea")}</span><p>${L(c.key)}</p></div>
        ${videoBlock(id)}
        ${learnLinks(id)}`
      : `<div class="locked"><b>🔒</b><strong>${t("lockedTitle")}</strong><p class="muted small">${solvingNow ? t("lockedNow") : t("lockedBody")}</p></div>`;
    return `<div class="sheet-wrap" data-act="closeSheet">
      <div class="sheet" role="dialog" aria-modal="true" aria-labelledby="sheet-t" style="--c:${r.color}">
        <div class="sheet-head">
          <span class="rb ${p.done ? "on" : ""}" style="--c:${r.color}">${rIcon(id)}</span>
          <div><span class="eyebrow">${t("episode")} ${r.ep}</span><h3 id="sheet-t">${L(r)}</h3></div>
          <button class="icon-btn" data-act="closeSheet" aria-label="${t("close")}">✕</button>
        </div>
        ${body}
      </div>
    </div>`;
  }

  // Video del episodio: dentro de la app si es YouTube; si no, enlace
  function videoBlock(id) {
    const r = RIGHTS[id], url = LINKS[id].video, yt = youtubeId(url);
    const label = `${t("episode")} ${r.ep} · ${L(r)}`;
    if (yt) {
      return `<div class="video-embed"><iframe src="https://www.youtube-nocookie.com/embed/${yt}?rel=0" title="${label}" loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>`;
    }
    return `<a class="video" href="${orSeries(url)}" target="_blank" rel="noopener"><strong>▶ ${t("watch")}</strong></a>`;
  }

  // Material del episodio y "Dónde pedir ayuda"
  function learnLinks(id) {
    return `<div class="links">
      <a class="link-row" href="${orSeries(LINKS[id].pdf)}" target="_blank" rel="noopener"><span class="ico">📄</span><span>${t("material")}</span><span class="arrow">↗</span></a>
      <a class="link-row" href="${orSeries(LINKS[id].book)}" target="_blank" rel="noopener"><span class="ico">📖</span><span>${t("bookBW")}</span><span class="arrow">↗</span></a>
      <button class="link-row" data-act="go" data-v="resources"><span class="ico">📞</span><span>${t("whereHelp")}</span><span class="arrow">→</span></button>
    </div>`;
  }

  function welcomeBackBar() {
    return S.welcomeBack ? `<div class="wb" role="status"><span>👋 ${t("welcomeBack")}</span>
      <button class="wb-link" data-act="restart">${t("startOver")}</button>
      <button class="wb-x" data-act="dismissWb" aria-label="${t("close")}">✕</button></div>` : "";
  }

  // Controla la mini escena: sonidos, y al terminar deja buscar las pistas
  let introTimers = [], introFor = null, introStart = 0;
  function stopIntro() { introTimers.forEach(clearTimeout); introTimers = []; introFor = null; introStart = 0; }
  function maybeIntro() {
    const c = curCase();
    if (S.screen !== "clues" || !c || P(c.id).introSeen) { if (introFor) stopIntro(); return; }
    if (introFor === c.id) return;
    stopIntro();
    introFor = c.id; introStart = Date.now();
    introTimers.push(setTimeout(() => SFX.talk(false), 900));
    introTimers.push(setTimeout(() => SFX.talk(true), 4600));
    introTimers.push(setTimeout(() => {
      stopIntro();
      P(c.id).introSeen = true;
      if (S.screen === "clues" && S.current === c.id) { S.spotsIn = true; render(); }
    }, INTRO_MS));
  }

  // ---------- Render ----------
  const app = document.getElementById("app");
  let lastPts = null;
  function render() {
    S.bump = lastPts !== null && S.points !== lastPts;
    lastPts = S.points;
    app.innerHTML = topbar() + `<main class="screen${S.enter ? " enter" : ""}">${welcomeBackBar()}${screens[S.screen]()}</main>` + rightSheet() + dialog();
    if (S.confirm) { const b = app.querySelector(".dlg .btn"); if (b) b.focus(); }
    S.justUnlocked = null; S.justClue = null; S.shake = null; S.spotsIn = false;
    maybeIntro();
    save();
  }

  // Dirección para invitar: la de esta app si se puede leer; si no, la de la serie
  function appUrl() {
    for (const w of [window.top, window.parent]) {
      try { const u = w.location.href; if (/^https?:/.test(u)) return u.split("#")[0]; } catch (_) {}
    }
    return SERIES_URL;
  }

  // ---------- Interacciones ----------
  app.addEventListener("click", (e) => {
    const el = e.target.closest("[data-act]");
    // El menú del logo se cierra con cualquier toque fuera de él
    if (S.logoMenu && (!el || el.dataset.act !== "logoMenu")) { S.logoMenu = false; if (!el) { render(); return; } }
    if (!el) return;
    const act = el.dataset.act, v = el.dataset.v;
    if (act === "rate" || act === "noop") return; // "rate" lo maneja "change"
    // Clic en el fondo oscuro cierra; clic dentro de la ventana no
    if ((el.classList.contains("sheet-wrap") || el.classList.contains("dlg-wrap")) && e.target !== el) return;
    const c = curCase();

    switch (act) {
      case "go":
        if (v === "resources") S.prevScreen = S.screen;
        SFX.tap();
        go(v);
        break;
      case "open": {
        const p = P(v);
        if (p.startRank === null) p.startRank = rankIndex(S.points);
        const step = p.done ? "solved" : p.dOk ? "action" : p.clues.length === 3 ? "right" : "clues";
        SFX.tap();
        go(step, { current: v, welcomeBack: false });
        break;
      }
      case "info": SFX.tap(); S.sheet = v; render(); break;
      case "resJump": { const sec = app.querySelector("#res-" + v); if (sec) { const top = app.querySelector(".topbar"); window.scrollBy({ top: sec.getBoundingClientRect().top - (top ? top.offsetHeight : 0) - 10, behavior: calm() ? "auto" : "smooth" }); } break; }
      case "skipIntro": stopIntro(); P(c.id).introSeen = true; S.spotsIn = true; render(); break;
      case "replay": stopIntro(); P(c.id).introSeen = false; render(); break;
      case "logoMenu": SFX.tap(); S.logoMenu = !S.logoMenu; render(); break;
      case "closeSheet": S.sheet = null; render(); break;
      case "sound":
        SOUND = !SOUND;
        try { localStorage.setItem(SOUND_KEY, SOUND ? "on" : "off"); } catch (_) {}
        render();
        SFX.tap();
        break;
      case "dismissWb": S.welcomeBack = false; render(); break;
      case "finish": {
        const left = 7 - solvedCount();
        if (left === 0) { go("report"); break; }
        S.confirm = { title: t("finishTitle"), body: t("finishBody")(left), stay: t("keepGoing"), leave: t("finishAnyway"), act: "finishYes" };
        render();
        break;
      }
      case "finishYes": S.confirm = null; go("report"); break;
      case "cancelConfirm": S.confirm = null; render(); break;
      case "clue": {
        const p = P(c.id), i = +v;
        if (p.clues.includes(i)) break;
        p.clues.push(i); p.earned += 10; S.points += 10;
        S.justClue = i;
        SFX.clue();
        render();
        floatPts(app.querySelector(`.spot[data-v="${i}"]`), "+10");
        // Con las 3 pistas aparece el botón "Siguiente" (no pasa sola)
        if (p.clues.length === 3) {
          const w = app.querySelector(".wait");
          if (w) innerScroll(w, "end");
        }
        break;
      }
      case "answerRight": {
        const p = P(c.id);
        if (p.dOk) break;
        if (v === c.right) {
          const pts = [50, 20][p.dTries] ?? 10;
          p.dOk = true; p.earned += pts; S.points += pts;
          S.streak = p.dTries === 0 ? S.streak + 1 : 0;
          SFX.right();
          render();
          floatPts(app.querySelector(".opt.right"), `+${pts}`);
          const banner = { title: `${t("correct")} +${pts}${streakTxt()}`, text: L(c.rightFb) };
          setTimeout(() => { if (S.screen === "right" && S.current === c.id) go("action", { banner }); }, NEXT_WAIT_MS);
        } else {
          p.dTries++; p.dWrong.push(v); S.streak = 0; S.shake = v;
          SFX.wrong(); vibrate(90);
          render();
        }
        break;
      }
      case "answerAction": {
        const p = P(c.id), a = c.actions[+v];
        if (p.aOk) break;
        if (a.ok) {
          const pts = [40, 15][p.aTries] ?? 5;
          p.aOk = true; p.done = true; p.earned += pts; S.points += pts;
          S.streak = p.aTries === 0 ? S.streak + 1 : 0;
          SFX.right();
          render();
          floatPts(app.querySelector(".opt.right"), `+${pts}`);
          const banner = { title: `${t("good")} +${pts}`, text: L(a.fb) };
          setTimeout(() => {
            if (S.screen !== "action" || S.current !== c.id) return;
            const leveled = p.startRank !== null && rankIndex(S.points) > p.startRank;
            S.justUnlocked = c.right;
            go("solved", { banner, solvedAt: Date.now() });
            const all = solvedCount() === 7;
            confetti(all); SFX.win(); if (leveled) SFX.level();
            if (!all) {
              // El nuevo mensaje entra con rebote: suena y se asoma en pantalla
              setTimeout(() => {
                if (S.screen !== "solved" || S.current !== c.id) return;
                SFX.msg(); vibrate([40, 60, 40]);
                const n = app.querySelector(".notif");
                if (n) innerScroll(n, "nearest");
              }, NOTIF_WAIT_MS + 300);
            }
          }, NEXT_WAIT_MS);
        } else {
          p.aTries++; p.aWrong.push(+v); S.streak = 0; S.shake = +v;
          SFX.wrong(); vibrate(90);
          render();
        }
        break;
      }
      case "tone": S.shareTone = v; S.shareDraft = null; S.toast = ""; render(); break;
      case "copy": {
        const box = document.getElementById("share-text");
        const text = v === "link" ? appUrl() : `${box.value.trim()}\n${appUrl()}`;
        const done = (ok) => { S.toast = ok ? t("copied") : t("copyFail"); render(); };
        try { navigator.clipboard.writeText(text).then(() => done(true), () => done(false)); } catch (_) { done(false); }
        break;
      }
      case "social": {
        const msg = document.getElementById("share-text").value.trim(), url = appUrl();
        const enc = encodeURIComponent(msg), u = encodeURIComponent(url);
        const href = v === "wa" ? `https://wa.me/?text=${enc}%20${u}`
          : v === "fb" ? `https://www.facebook.com/sharer/sharer.php?u=${u}&quote=${enc}`
          : `https://twitter.com/intent/tweet?text=${enc}&url=${u}`;
        window.open(href, "_blank", "noopener");
        break;
      }
      case "restart":
        S.confirm = { title: t("restartTitle"), body: t("restartBody"), stay: t("cancel"), leave: t("restartYes"), act: "restartYes" };
        render();
        break;
      case "restartYes": {
        try { localStorage.removeItem(STORE_KEY); } catch (_) {}
        S = fresh(); render(); toTop();
        break;
      }
    }
  });

  app.addEventListener("change", (e) => {
    const el = e.target;
    if (el.dataset.act !== "rate") return;
    S[el.dataset.set][+el.dataset.i] = +el.value;
    SFX.tap();
    const y = window.scrollY;
    render();
    window.scrollTo(0, y);
    const again = document.getElementById(el.id);
    if (again) again.focus({ preventScroll: true });
  });

  // Lo que la persona escribe en el mensaje para compartir se guarda
  app.addEventListener("input", (e) => {
    if (e.target.id === "share-text") { S.shareDraft = e.target.value; save(); }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    if (S.confirm) { S.confirm = null; render(); }
    else if (S.sheet) { S.sheet = null; render(); }
  });

  // ---------- Avisar antes de salir (solo si el avance NO se puede guardar) ----------
  function warnBeforeLeave(e) {
    if (canSave || !hasProgress()) return;
    e.preventDefault();
    e.returnValue = "";
    return "";
  }
  window.addEventListener("beforeunload", warnBeforeLeave);
  // Streamlit muestra esto dentro de un iframe: también escuchamos en la página que lo contiene.
  try {
    const top = window.parent;
    if (top && top !== window) {
      if (top.__lineaDefensaLeave) top.removeEventListener("beforeunload", top.__lineaDefensaLeave);
      top.__lineaDefensaLeave = warnBeforeLeave;
      top.addEventListener("beforeunload", warnBeforeLeave);
    }
  } catch (_) { /* página contenedora de otro origen: basta con el aviso del iframe */ }

  try { history.scrollRestoration = "manual"; } catch (_) {}
  fitFrame();
  restore();
  render();
  window.scrollTo(0, 0);
  if (S.welcomeBack) setTimeout(() => { if (S.welcomeBack) { S.welcomeBack = false; const w = app.querySelector(".wb"); if (w) w.remove(); save(); } }, 8000);
})();
</script>
</body>
</html>
'''

# --------------------------------------------------
# Mostrar el prototipo
# --------------------------------------------------

components.html(PROTOTIPO_HTML, height=900, scrolling=True)
