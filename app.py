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
# Toda la experiencia (pantallas, contenido, puntos
# y navegación) vive en este HTML.
# Contenido demostrativo: casos inventados, enlaces de
# videos y PDF pendientes, teléfonos por verificar.
# --------------------------------------------------

PROTOTIPO_HTML = r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Línea de Defensa</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
*, *::before, *::after { box-sizing: border-box; }
/* Layout: una columna tipo celular centrada; barra superior fija; cada pantalla es una tarjeta que llena la columna. */
:root {
  --bg: #EEF0F8;
  --surface: #FFFFFF;
  --surface-2: #F6F7FC;
  --ink: #151936;
  --muted: #565B7C;
  --line: #D6D9EC;
  --accent: #2B37D1;
  --accent-ink: #FFFFFF;
  --signal: #FFC23D;
  --signal-ink: #2A2100;
  --bubble: #E4E7FF;
  --ok: #17734A;
  --ok-bg: #E2F4EA;
  --bad: #A8202F;
  --bad-bg: #FBE6E8;
  --scene-a: #DCE1FF;
  --scene-b: #F3E9D7;
  --font-display: "Bricolage Grotesque", "Arial Black", system-ui, sans-serif;
  --font-body: "Atkinson Hyperlegible", "Segoe UI", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  color-scheme: light; /* siempre claro, aunque el teléfono esté en modo oscuro */
}
html, body { min-height: 100%; }
body {
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  font-size: 17px;
  line-height: 1.5;
}
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--surface); }

.app {
  max-width: 440px;
  margin: 0 auto;
  min-height: 100vh;
  background: var(--surface);
  display: flex;
  flex-direction: column;
  box-shadow: 0 0 0 1px var(--line);
}
.topbar {
  position: sticky;
  top: env(safe-area-inset-top, 0px);
  z-index: 5;
  background: var(--surface);
  border-bottom: 1px solid var(--line);
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  padding-block: 10px;
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px));
}
.brand { font-family: var(--font-display); font-weight: 800; font-size: 1rem; letter-spacing: -0.01em; margin-right: auto; display: flex; align-items: center; gap: 8px;
  color: var(--ink); background: none; border: 0; padding: 4px 0; cursor: pointer; min-height: 40px; text-align: left; }
.shield { width: 22px; height: 26px; flex: none; }
.chip {
  font-family: var(--font-mono); font-size: 0.85rem; font-variant-numeric: tabular-nums;
  background: var(--signal); color: var(--signal-ink); border-radius: 999px; padding: 3px 10px; font-weight: 500; white-space: nowrap;
}
.tbtn {
  font: inherit; font-size: 0.85rem; font-weight: 700; color: var(--ink); background: var(--surface-2);
  border: 1px solid var(--line); border-radius: 999px; padding: 5px 11px; cursor: pointer; min-height: 34px;
}
.tbtn[aria-pressed="true"] { background: var(--ink); color: var(--surface); border-color: var(--ink); }

.screen {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding-block: 22px 96px;
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px));
}
.eyebrow { font-family: var(--font-mono); font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }
h1, h2, h3 { font-family: var(--font-display); text-wrap: balance; margin: 0; letter-spacing: -0.02em; }
h1 { font-size: 2.6rem; line-height: 1; font-weight: 800; }
h2 { font-size: 1.6rem; line-height: 1.1; font-weight: 800; }
h3 { font-size: 1.1rem; font-weight: 600; }
p { margin: 0; }
.muted { color: var(--muted); }
.small { font-size: 0.9rem; }

.btn {
  font: inherit; font-weight: 700; font-size: 1.05rem; width: 100%; min-height: 54px; border-radius: 14px;
  border: 2px solid var(--accent); background: var(--accent); color: var(--accent-ink); cursor: pointer;
  display: inline-flex; align-items: center; justify-content: center; gap: 8px; text-decoration: none; padding: 0 18px;
}
.btn.ghost { background: transparent; color: var(--accent); }
.btn:disabled { opacity: 0.4; cursor: not-allowed; }
.btn-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
:focus-visible { outline: 3px solid var(--signal); outline-offset: 2px; }

/* Bienvenida */
.hero-band {
  background: var(--accent); color: var(--accent-ink); border-radius: 22px; padding: 26px 22px; display: grid; gap: 14px;
  position: relative; overflow: hidden;
}
.hero-band .eyebrow { color: inherit; opacity: 0.8; }
.hero-band .tag { font-family: var(--font-display); font-weight: 600; font-size: 1.15rem; }
.hero-band::after {
  content: "7"; position: absolute; right: -10px; bottom: -40px; font-family: var(--font-display); font-weight: 800;
  font-size: 11rem; line-height: 1; opacity: 0.14;
}
.facts { display: flex; flex-wrap: wrap; gap: 8px; }
.fact { border: 1px solid var(--line); border-radius: 999px; padding: 4px 12px; font-size: 0.88rem; color: var(--muted); }

/* Autoevaluación */
.q { display: grid; gap: 10px; border: 0; padding: 0; margin: 0; }
.q legend { font-weight: 700; padding: 0; margin-bottom: 10px; }
.scale { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; }
.scale label { position: relative; }
.scale input { position: absolute; opacity: 0; inset: 0; }
.scale span {
  display: grid; place-items: center; min-height: 48px; border: 2px solid var(--line); border-radius: 12px;
  font-family: var(--font-mono); font-size: 1.05rem; cursor: pointer; background: var(--surface-2);
}
.scale input:checked + span { background: var(--accent); color: var(--accent-ink); border-color: var(--accent); }
.scale input:focus-visible + span { outline: 3px solid var(--signal); outline-offset: 2px; }
.scale-ends { display: flex; justify-content: space-between; font-size: 0.8rem; color: var(--muted); }

/* Cómo funciona */
.steps { display: grid; gap: 12px; margin: 0; padding: 0; list-style: none; }
.steps li { display: grid; grid-template-columns: 40px 1fr; gap: 12px; align-items: start; }
.num {
  width: 40px; height: 40px; border-radius: 12px; background: var(--bubble); display: grid; place-items: center;
  font-family: var(--font-display); font-weight: 800; color: var(--accent);
}
.ranks { display: grid; gap: 6px; }
.rank-row { display: flex; justify-content: space-between; gap: 10px; padding: 10px 14px; border-radius: 12px; background: var(--surface-2); }
.rank-row .pts { font-family: var(--font-mono); font-size: 0.85rem; color: var(--muted); font-variant-numeric: tabular-nums; }

/* Bandeja */
.progress { height: 10px; background: var(--surface-2); border: 1px solid var(--line); border-radius: 999px; overflow: hidden; }
.progress > div { height: 100%; background: var(--accent); border-radius: 999px; transition: width .4s ease; }
.status { display: flex; justify-content: space-between; align-items: baseline; gap: 10px; }
.status strong { font-family: var(--font-display); }
.inbox { display: grid; border: 1px solid var(--line); border-radius: 16px; overflow: hidden; }
.msg {
  font: inherit; color: inherit; text-align: left; background: var(--surface); border: 0; border-bottom: 1px solid var(--line);
  display: grid; grid-template-columns: 46px 1fr auto; gap: 12px; align-items: center; padding: 12px 14px; cursor: pointer; min-height: 72px;
}
.msg:last-child { border-bottom: 0; }
.msg:hover { background: var(--surface-2); }
.avatar {
  width: 46px; height: 46px; border-radius: 50%; display: grid; place-items: center; font-family: var(--font-display);
  font-weight: 800; color: #fff; font-size: 1.05rem;
}
.msg-body { min-width: 0; }
.msg-name { font-weight: 700; display: block; }
.msg-prev { display: block; color: var(--muted); font-size: 0.92rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.pill { font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.06em; text-transform: uppercase; border-radius: 999px; padding: 3px 8px; white-space: nowrap; }
.pill.new { background: var(--bad-bg); color: var(--bad); }
.pill.done { background: var(--ok-bg); color: var(--ok); }
.msg.is-done .msg-prev { text-decoration: line-through; }

/* Caso */
.case-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
.back { font: inherit; font-weight: 700; color: var(--accent); background: none; border: 0; padding: 6px 0; cursor: pointer; min-height: 40px; }
.stepper { display: flex; gap: 6px; }
.stepper i { width: 28px; height: 6px; border-radius: 99px; background: var(--line); display: block; }
.stepper i.on { background: var(--accent); }
.chat { display: grid; gap: 6px; }
.bubble { background: var(--bubble); border-radius: 18px 18px 18px 4px; padding: 12px 16px; max-width: 92%; }
.who { font-size: 0.85rem; color: var(--muted); display: flex; align-items: center; gap: 8px; }
.who .avatar { width: 26px; height: 26px; font-size: 0.75rem; }

.scene {
  position: relative; width: 100%; max-width: 100%; aspect-ratio: 16 / 11; border-radius: 18px; overflow: hidden;
  background:
    linear-gradient(180deg, transparent 68%, color-mix(in srgb, var(--scene-b) 100%, transparent) 68%),
    linear-gradient(160deg, var(--scene-a), color-mix(in srgb, var(--scene-a) 70%, var(--surface)));
  border: 1px solid var(--line);
}
.scene-label {
  position: absolute; left: 12px; top: 12px; font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.06em;
  text-transform: uppercase; background: var(--surface); color: var(--ink); border-radius: 999px; padding: 4px 10px;
}
.scene-deco { position: absolute; font-size: 2.2rem; opacity: 0.35; pointer-events: none; }
.spot {
  position: absolute; transform: translate(-50%, -50%); width: 62px; height: 62px; border-radius: 50%;
  border: 3px solid var(--surface); background: var(--signal); font-size: 1.7rem; cursor: pointer;
  display: grid; place-items: center; box-shadow: 0 4px 14px rgba(10, 12, 40, 0.25);
}
.spot::after {
  content: ""; position: absolute; inset: -9px; border-radius: 50%; border: 3px solid var(--signal); animation: pulse 1.8s ease-out infinite;
}
.spot.found { background: var(--surface); border-color: var(--ok); }
.spot.found::after { display: none; }
.spot.found::before {
  content: "✓"; position: absolute; right: -6px; top: -6px; width: 24px; height: 24px; border-radius: 50%; background: var(--ok);
  color: var(--surface); font-size: 0.85rem; font-weight: 700; display: grid; place-items: center;
}
@keyframes pulse { from { transform: scale(0.85); opacity: 0.9; } to { transform: scale(1.35); opacity: 0; } }
@media (prefers-reduced-motion: reduce) { .spot::after { animation: none; opacity: 0.6; } .progress > div { transition: none; } }
.clues { display: grid; gap: 8px; margin: 0; padding: 0; list-style: none; }
.clues li { display: grid; grid-template-columns: 30px 1fr auto; gap: 10px; align-items: start; background: var(--surface-2); border-radius: 12px; padding: 10px 12px; }
.clues .plus { font-family: var(--font-mono); font-size: 0.8rem; color: var(--ok); }
.clues .empty { color: var(--muted); font-style: italic; grid-template-columns: 1fr; }

.options { display: grid; gap: 10px; }
.opt {
  font: inherit; color: inherit; text-align: left; background: var(--surface); border: 2px solid var(--line); border-radius: 14px;
  padding: 14px 16px; cursor: pointer; display: grid; grid-template-columns: 26px 1fr; gap: 12px; align-items: center; min-height: 56px;
}
.opt .dot { width: 22px; height: 22px; border-radius: 50%; border: 2px solid var(--muted); display: grid; place-items: center; font-size: 0.8rem; font-weight: 700; }
.opt[aria-checked="true"] { border-color: var(--accent); background: var(--bubble); }
.opt[aria-checked="true"] .dot { background: var(--accent); border-color: var(--accent); }
.opt.right { border-color: var(--ok); background: var(--ok-bg); }
.opt.right .dot { background: var(--ok); border-color: var(--ok); color: var(--surface); }
.opt.wrong { border-color: var(--bad); background: var(--bad-bg); opacity: 0.85; }
.opt.wrong .dot { background: var(--bad); border-color: var(--bad); color: var(--surface); }
.opt:disabled { cursor: default; }

.feedback { border-radius: 14px; padding: 14px 16px; display: grid; gap: 6px; }
.feedback.ok { background: var(--ok-bg); color: var(--ink); border-left: 5px solid var(--ok); }
.feedback.no { background: var(--bad-bg); color: var(--ink); border-left: 5px solid var(--bad); }
.feedback strong { font-family: var(--font-display); }

/* Caso resuelto */
.celebrate { text-align: center; display: grid; gap: 6px; justify-items: center; }
.big-pts { font-family: var(--font-display); font-weight: 800; font-size: 3.4rem; line-height: 1; color: var(--accent); }
.keyidea { background: var(--surface-2); border-radius: 16px; padding: 16px; display: grid; gap: 6px; }
.video {
  display: grid; text-decoration: none; color: var(--accent-ink); border-radius: 16px; overflow: hidden; background: var(--ink);
}
.video .thumb {
  aspect-ratio: 16 / 9; max-width: 100%; display: grid; place-items: center; position: relative;
  background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 40%, var(--ink)));
}
.video .play { width: 64px; height: 64px; border-radius: 50%; background: var(--signal); display: grid; place-items: center; }
.video .play::before { content: ""; border-left: 20px solid var(--signal-ink); border-top: 12px solid transparent; border-bottom: 12px solid transparent; margin-left: 5px; }
.video .ep { position: absolute; left: 12px; bottom: 10px; font-family: var(--font-mono); font-size: 0.75rem; color: #fff; letter-spacing: 0.05em; }
.video .cap { padding: 12px 14px; background: var(--surface-2); color: var(--ink); display: grid; gap: 2px; }
.links { display: grid; gap: 8px; }
.link-row {
  display: grid; grid-template-columns: 40px 1fr auto; gap: 12px; align-items: center; padding: 12px 14px; border: 1px solid var(--line);
  border-radius: 14px; text-decoration: none; color: inherit; background: var(--surface); font: inherit; text-align: left; cursor: pointer; width: 100%;
}
.link-row .ico { width: 40px; height: 40px; border-radius: 10px; background: var(--bubble); display: grid; place-items: center; font-size: 1.2rem; }
.link-row .arrow { color: var(--accent); font-weight: 700; }

/* Reporte */
.medal {
  background: var(--ink); color: var(--surface); border-radius: 22px; padding: 22px; display: grid; gap: 4px; text-align: center; justify-items: center;
}
.medal .eyebrow { color: inherit; opacity: 0.7; }
.medal .rank { font-family: var(--font-display); font-weight: 800; font-size: 2rem; line-height: 1.05; }
.medal .score { font-family: var(--font-mono); color: var(--signal); }
.compare { display: grid; gap: 14px; }
.cmp { display: grid; gap: 6px; }
.cmp-row { display: grid; grid-template-columns: 64px 1fr 22px; gap: 10px; align-items: center; font-size: 0.85rem; color: var(--muted); }
.bar { height: 12px; background: var(--surface-2); border-radius: 99px; overflow: hidden; border: 1px solid var(--line); }
.bar > div { height: 100%; border-radius: 99px; background: var(--muted); }
.bar.now > div { background: var(--accent); }
.cmp-row b { font-family: var(--font-mono); color: var(--ink); font-weight: 500; text-align: right; }

/* Compartir */
.share-card {
  border: 2px dashed var(--accent); border-radius: 18px; padding: 18px; background: var(--bubble); font-size: 1.05rem;
}
.socials { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.socials a {
  display: grid; place-items: center; min-height: 50px; border-radius: 12px; border: 1px solid var(--line); text-decoration: none;
  color: var(--ink); font-weight: 700; background: var(--surface-2); font-size: 0.95rem;
}
.toast { font-size: 0.9rem; color: var(--ok); min-height: 1.4em; }

/* Recursos */
.res-group { display: grid; gap: 8px; }
.res {
  border: 1px solid var(--line); border-radius: 14px; padding: 12px 14px; display: grid; gap: 4px; background: var(--surface);
}
.res .name { font-weight: 700; }
.res .tbd { font-family: var(--font-mono); font-size: 0.75rem; color: var(--bad); }
.note { background: var(--surface-2); border-radius: 14px; padding: 14px; font-size: 0.9rem; color: var(--muted); }
.credits { font-size: 0.85rem; color: var(--muted); display: grid; gap: 6px; }

/* Selector de pantallas (solo prototipo) */
.jump {
  position: fixed; z-index: 20; right: max(16px, env(safe-area-inset-right, 0px)); bottom: calc(16px + env(safe-area-inset-bottom, 0px));
  font: inherit; font-weight: 700; font-size: 0.85rem; background: var(--ink); color: var(--surface); border: 0; border-radius: 999px;
  padding: 10px 16px; cursor: pointer; box-shadow: 0 6px 20px rgba(10, 12, 40, 0.3);
}
.sheet-wrap { position: fixed; inset: 0; z-index: 30; background: rgba(8, 10, 30, 0.5); display: flex; align-items: flex-end; justify-content: center; }
.sheet {
  background: var(--surface); width: 100%; max-width: 440px; border-radius: 20px 20px 0 0; display: grid; gap: 10px; max-height: 80vh; overflow: auto;
  padding-block: 18px calc(18px + env(safe-area-inset-bottom, 0px));
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
}
.sheet-list { display: grid; gap: 6px; }
.sheet-list button {
  font: inherit; color: inherit; text-align: left; border: 1px solid var(--line); background: var(--surface-2); border-radius: 12px;
  padding: 10px 12px; cursor: pointer; display: grid; grid-template-columns: 34px 1fr; gap: 8px; align-items: center;
}
.sheet-list .n { font-family: var(--font-mono); color: var(--accent); font-weight: 500; }
/* Empuje para completar */
.nudge { background: var(--surface-2); border: 1px dashed var(--accent); border-radius: 14px; padding: 12px 14px; display: grid; gap: 4px; font-size: 0.92rem; }
.nudge strong { color: var(--accent); }
.levelup { background: var(--signal); color: var(--signal-ink); border-radius: 14px; padding: 12px 14px; font-weight: 700; text-align: center; }
.next-case { display: grid; gap: 2px; text-align: left; }
.next-case small { font-weight: 500; opacity: 0.85; }
/* Las 7 personas: progreso siempre a la vista */
.crew { flex-basis: 100%; display: flex; align-items: center; gap: 6px; list-style: none; margin: 0; padding: 2px 0 0; }
.crew li { position: relative; }
.crew .avatar { width: 30px; height: 30px; font-size: 0.8rem; opacity: 0.35; filter: grayscale(0.6); transition: opacity .3s, filter .3s; }
.crew .done .avatar { opacity: 1; filter: none; }
.crew .now .avatar { opacity: 1; filter: none; box-shadow: 0 0 0 2px var(--surface), 0 0 0 4px var(--accent); }
.crew .done::after {
  content: "✓"; position: absolute; right: -3px; bottom: -3px; width: 15px; height: 15px; border-radius: 50%;
  background: var(--ok); color: #fff; font-size: 0.6rem; font-weight: 700; display: grid; place-items: center; border: 2px solid var(--surface);
}
.crew .count { margin-left: auto; font-family: var(--font-mono); font-size: 0.75rem; color: var(--muted); white-space: nowrap; }
@media (prefers-reduced-motion: reduce) { .crew .avatar { transition: none; } }
/* Gancho al próximo caso */
.teaser { border: 2px solid var(--accent); border-radius: 18px; padding: 14px; display: grid; gap: 10px; background: var(--surface); }
.teaser .eyebrow { color: var(--accent); }
/* Aprende más (plegado) */
.more { border: 1px solid var(--line); border-radius: 14px; background: var(--surface-2); }
.more > summary { cursor: pointer; padding: 14px 16px; font-weight: 700; list-style: none; display: flex; justify-content: space-between; gap: 10px; }
.more > summary::-webkit-details-marker { display: none; }
.more > summary::after { content: "+"; color: var(--accent); font-size: 1.2rem; line-height: 1; }
.more[open] > summary::after { content: "–"; }
.more-body { display: grid; gap: 12px; padding: 0 12px 12px; }
/* Confirmación */
.dlg-wrap { position: fixed; inset: 0; z-index: 40; background: rgba(8, 10, 30, 0.55); display: grid; place-items: center; padding: 16px; }
.dlg { background: var(--surface); border-radius: 20px; padding: 20px; width: 100%; max-width: 380px; display: grid; gap: 12px; box-shadow: 0 12px 40px rgba(10, 12, 40, 0.35); }
.dlg h3 { margin: 0; }
.dlg p { margin: 0; }
.dlg .btn-row { grid-template-columns: 1fr; }
.proto-tag { font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); text-align: center; }
</style>

</head>
<body style="margin:0">
<div class="app" id="app"></div>

<script>
(function () {
  const SERIES_URL = "https://espaciosabiertos.org/derecho-a-tener-derechos-2/";

  // ---------- Textos de la interfaz ----------
  const T = {
      brand: "Línea de Defensa", help: "Ayuda", jump: "Pantallas",
      presents: "Espacios Abiertos presenta", tagline: "Derechos. Son tuyos. Defiéndelos.",
      welcomeBody: "Hoy te toca atender la línea. Siete personas te escriben porque algo no anda bien. Tu misión: descubrir qué derecho está en juego y ayudarles a defenderlo.",
      fact1: "5–10 minutos", fact2: "7 casos", fact3: "No pedimos ni guardamos datos",
      start: "Empezar mi turno",
      preEyebrow: "Antes de empezar", preTitle: "¿Cómo llegas hoy?", preIntro: "Contesta con honestidad. Al final verás cuánto cambió. Nada de esto se guarda.",
      q1: "Conozco mis derechos", q2: "Reconozco cuando violan un derecho", q3: "Sé a dónde acudir por ayuda",
      low: "Nada", high: "Mucho", cont: "Continuar",
      howEyebrow: "Tu turno", howTitle: "Así funciona cada caso",
      s1t: "Lee y busca pistas", s1d: "Toca los objetos de la escena para descubrir qué pasó.",
      s2t: "Nombra el derecho", s2d: "Escoge qué derecho está en juego.",
      s3t: "Decide qué hacer", s3d: "Recomienda el mejor próximo paso y mira qué pasa.",
      ranksTitle: "Sube de nivel", tipWrong: "Si te equivocas, no pierdes: recibes una pista y lo intentas otra vez, pero ganas menos puntos.",
      seeCases: "Atender el primer caso", allFound: "¡Encontraste todas las pistas!",
      inboxEyebrow: "Bandeja de entrada", inboxTitle: "Te están escribiendo", solved: "resueltos", level: "Nivel",
      new: "Nuevo", done: "Resuelto", finish: "Terminar turno", resources: "Recursos",
      back: "← Bandeja", step: "Paso", of: "de",
      tapScene: "Toca la escena y busca pistas", found: "encontradas", noClues: "Todavía no has encontrado pistas.",
      next: "Siguiente",
      whichRight: "¿Qué derecho está en juego?", check: "Comprobar", correct: "¡Correcto!", notQuite: "Casi…",
      whatDo: "¿Qué le recomiendas?", decide: "Decidir", good: "Buena jugada", rethink: "Piénsalo otra vez",
      caseSolved: "¡Caso resuelto!", points: "puntos", keyIdea: "Idea clave",
      episode: "Episodio", watch: "Ver el episodio", pendingLink: "Enlace al video pendiente: por ahora abre la página de la serie",
      material: "Material educativo (PDF)", bookBW: "Libro en blanco y negro (PDF)", whereHelp: "Dónde pedir ayuda",
      backInbox: "Volver a la bandeja", seeReport: "Ver mi reporte",
      reportEyebrow: "Reporte de turno", reached: "Llegaste a", casesOf: "casos de 7",
      afterTitle: "¿Y ahora cómo te sientes?", afterIntro: "Contesta otra vez para comparar.",
      before: "Antes", now: "Ahora", shareRank: "Compartir mi nivel", playAgain: "Jugar otra vez",
      shareEyebrow: "Comparte", shareTitle: "Reta a tu gente",
      shareText: (r, n, p) => `Llegué a "${r}" en Línea de Defensa: resolví ${n} de 7 casos y sumé ${p} puntos. ¿Te atreves? #DerechosSonTuyos`,
      copyText: "Copiar texto", copyLink: "Copiar enlace", copied: "Copiado.", copyFail: "No se pudo copiar. Selecciona el texto y cópialo.",
      resTitle: "Dónde pedir ayuda", resNote: "Prototipo: los teléfonos y enlaces se añadirán después de verificarlos en las fuentes oficiales de cada organización.",
      tbd: "Teléfono por verificar", aboutSeries: "Sobre la serie",
      credits: "“Derechos. Son tuyos. Defiéndelos.” es una serie de 7 videos de Espacios Abiertos y el Centro de Periodismo Investigativo, con el apoyo de Open Society Foundations y la Fundación Puertorriqueña de las Humanidades. Se presentó por WIPR y recibió un premio Emmy en 2016.",
      openSite: "Abrir la página de la serie",
      jumpTitle: "Ir a una pantalla", jumpNote: "Solo para el prototipo en papel. Las pantallas de caso usan el caso de Kiara.",
      proto: "Prototipo · contenido demostrativo",
      waiting: (n) => n === 1 ? "Queda 1 persona esperando tu respuesta." : `Quedan ${n} personas esperando tu respuesta.`,
      toRank: (pts, r) => `Te faltan <strong>${pts} pts</strong> para llegar a «${r}».`,
      maxRank: "¡Llegaste al nivel más alto! Termina los casos para completar tu turno.",
      allDone: "¡Atendiste a todas las personas! Ya puedes ver tu reporte.",
      levelUp: (r) => `⬆ ¡Subiste de nivel: ${r}!`,
      nextCase: "Siguiente caso", nextWaiting: "te está esperando",
      leftCases: (n) => `Te faltan ${n} de 7. ¡Tú puedes!`,
      keepGoing: "Seguir atendiendo",
      newMsg: "Nuevo mensaje", replyTo: "Responderle a", learnMore: "Aprende más sobre este derecho",
      learnAll: "Aprende más: los 7 episodios", helped: "ayudadas", crewLabel: "Personas que has ayudado",
      finishTitle: "¿Terminar el turno ya?",
      finishBody: (n) => `Todavía ${n === 1 ? "hay 1 persona" : `hay ${n} personas`} esperando ayuda. Cada caso te da hasta 120 puntos.`,
      finishAnyway: "Terminar de todos modos",
      restartTitle: "¿Empezar de nuevo?",
      restartBody: "Se borrarán tus puntos, tus casos resueltos y tus respuestas.",
      restartYes: "Sí, empezar de nuevo", cancel: "Cancelar",
      ranks: ["En entrenamiento", "Voz de apoyo", "Línea firme", "Defensa total"],
      screens: ["Bienvenida", "Autoevaluación (antes)", "Cómo funciona", "Bandeja de casos", "Caso · Pistas (hotspot)", "Caso · ¿Qué derecho?", "Caso · ¿Qué haces?", "Caso resuelto", "Reporte + autoevaluación (después)", "Compartir", "Recursos"]
  };

  // ---------- Contenido: los 7 derechos ----------
  const RIGHTS = {
    tener: { es: "Derecho a tener derechos", ep: 1 },
    educacion: { es: "Educación", ep: 2 },
    info: { es: "Acceso a la información", ep: 3 },
    participacion: { es: "Participación política", ep: 4 },
    justicia: { es: "Acceso a la justicia", ep: 5 },
    trabajo: { es: "Trabajo", ep: 6 },
    dignidad: { es: "Dignidad", ep: 7 }
  };

  // ---------- Contenido: los casos (demostrativos) ----------
  const CASES = [
    {
      id: "marco", right: "tener", name: "Marco", age: 31, color: "#B4462C",
      place: { es: "Oficina de gobierno" }, deco: ["🏢", "🪑"],
      msg: { es: "Fui a renovar un permiso y el empleado me dijo que “gente como yo” no tiene derecho a quejarse. ¿Eso es así?" },
      clues: [
        { icon: "🗣️", x: 22, y: 50, es: "“Gente como tú”: lo trataron como si valiera menos por ser de otro país." },
        { icon: "🪪", x: 52, y: 78, es: "Tenía todos sus documentos en orden." },
        { icon: "📜", x: 80, y: 34, es: "Afiche en la pared: “Todas las personas son iguales ante la ley”." }
      ],
      options: ["trabajo", "tener", "educacion", "participacion"],
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
      id: "valeria", right: "educacion", name: "Valeria", age: 19, color: "#2F7D6B",
      place: { es: "Universidad" }, deco: ["🏫", "📚"],
      msg: { es: "Me admitieron a la universidad, pero mi salón está en un tercer piso sin elevador. Uso silla de ruedas y me dicen que “lo tome el año que viene”." },
      clues: [
        { icon: "🛗", x: 20, y: 40, es: "El elevador lleva meses fuera de servicio." },
        { icon: "📩", x: 55, y: 70, es: "Correo de la universidad: “Espere al próximo año”." },
        { icon: "🦽", x: 82, y: 50, es: "Valeria necesita un acomodo razonable para llegar a clase." }
      ],
      options: ["dignidad", "info", "educacion", "justicia"],
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
      id: "kiara", right: "info", name: "Kiara", age: 23, color: "#6A3FB5",
      place: { es: "Municipio" }, deco: ["🏛️", "🗂️"],
      msg: { es: "Pedí al municipio el contrato del recogido de basura de mi barrio. Hace dos meses y nada. 😤" },
      clues: [
        { icon: "📄", x: 24, y: 72, es: "La carta de solicitud nunca tuvo respuesta." },
        { icon: "📅", x: 50, y: 32, es: "Ya pasaron dos meses desde que la entregó." },
        { icon: "💰", x: 80, y: 66, es: "El contrato se paga con dinero público." }
      ],
      options: ["educacion", "info", "trabajo", "dignidad"],
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
      id: "ana", right: "participacion", name: "Doña Ana", age: 67, color: "#B07A12",
      place: { es: "Égida" }, deco: ["🏠", "🪴"],
      msg: { es: "Quiero votar en las elecciones, pero no puedo caminar hasta el colegio. Me dijeron que “eso es complicado” y ya." },
      clues: [
        { icon: "🗳️", x: 24, y: 40, es: "Las elecciones son en tres semanas." },
        { icon: "🦯", x: 54, y: 74, es: "Doña Ana no puede caminar distancias largas." },
        { icon: "💬", x: 80, y: 44, es: "Nadie le explicó qué opciones tiene." }
      ],
      options: ["participacion", "justicia", "tener", "trabajo"],
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
      id: "jose", right: "justicia", name: "José", age: 35, color: "#1F5FA8",
      place: { es: "Apartamento" }, deco: ["🚪", "🛋️"],
      msg: { es: "El dueño del apartamento me dejó una nota: tengo dos días para irme. No tengo dinero para un abogado. ¿Qué hago?" },
      clues: [
        { icon: "📝", x: 26, y: 46, es: "Nota en la puerta: “Tienes 2 días”. No hay orden de un tribunal." },
        { icon: "💵", x: 54, y: 74, es: "José no puede pagar un abogado." },
        { icon: "🔑", x: 80, y: 40, es: "El dueño amenazó con cambiar la cerradura." }
      ],
      options: ["info", "participacion", "justicia", "educacion"],
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
      id: "luis", right: "trabajo", name: "Luis", age: 27, color: "#A3326B",
      place: { es: "Hospital" }, deco: ["🏥", "🩺"],
      msg: { es: "Fui a una entrevista de enfermería y me dijeron que el puesto “es para mujeres”. Tengo licencia y experiencia." },
      clues: [
        { icon: "📋", x: 22, y: 44, es: "El anuncio pedía “personal de enfermería con licencia”." },
        { icon: "💬", x: 52, y: 72, es: "La entrevistadora dijo: “Es para mujeres”." },
        { icon: "🎓", x: 80, y: 40, es: "Luis cumple con todos los requisitos." }
      ],
      options: ["dignidad", "tener", "info", "trabajo"],
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
      id: "carmen", right: "dignidad", name: "Doña Carmen", age: 72, color: "#4E6B1F",
      place: { es: "Centro de salud" }, deco: ["🏥", "🕐"],
      msg: { es: "En el centro de salud me hablan gritando y me dejan horas esperando, sin silla ni agua. Como si yo no importara." },
      clues: [
        { icon: "🪑", x: 22, y: 70, es: "No hay sillas suficientes en la sala de espera." },
        { icon: "⏰", x: 52, y: 32, es: "Lleva cinco horas esperando." },
        { icon: "🗣️", x: 80, y: 62, es: "El personal le habla a gritos." }
      ],
      options: ["trabajo", "dignidad", "participacion", "educacion"],
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

  // ---------- Recursos (por verificar) ----------
  const RESOURCES = [
    { title: { es: "Ayuda legal gratuita" }, items: [
      { es: "Organización de servicios legales gratuitos" },
      { es: "Clínica de asistencia legal universitaria" } ] },
    { title: { es: "Discriminación en el empleo" }, items: [
      { es: "Agencia que atiende querellas de discriminación laboral" } ] },
    { title: { es: "Personas de edad avanzada" }, items: [
      { es: "Oficina que defiende a personas de edad avanzada" } ] },
    { title: { es: "Elecciones" }, items: [
      { es: "Comisión Estatal de Elecciones (CEE)" } ] },
    { title: { es: "Información pública" }, items: [
      { es: "Espacios Abiertos", url: SERIES_URL } ] }
  ];

  const RANK_MIN = [0, 250, 500, 700];
  const MAX_POINTS = 120 * CASES.length;

  // ---------- Estado ----------
  const fresh = () => ({
    screen: "welcome", pre: [0, 0, 0], post: [0, 0, 0], points: 0,
    progress: {}, current: null, sel: null, fb: null, sheet: false, toast: "", confirm: null, banner: null
  });
  let S = fresh();
  const P = (id) => (S.progress[id] ||= { clues: [], dTries: 0, aTries: 0, dOk: false, aOk: false, earned: 0, done: false, startRank: null });
  const firstOpen = () => CASES.find((c) => !P(c.id).done);
  const nextOpen = () => CASES.find((c) => c.id !== S.current && !P(c.id).done);
  // Hay datos que se perderían si la persona sale de la página
  const hasProgress = () => S.screen !== "welcome" || S.pre.some(Boolean) || S.points > 0;

  const t = (k) => T[k];
  const L = (o) => o.es;
  const rankIndex = (p) => RANK_MIN.reduce((acc, min, i) => (p >= min ? i : acc), 0);
  const solvedCount = () => CASES.filter((c) => P(c.id).done).length;
  const curCase = () => CASES.find((c) => c.id === S.current);
  const initials = (n) => n.replace("Doña ", "").slice(0, 1);

  function go(screen, extra) {
    Object.assign(S, { screen, sel: null, fb: null, toast: "", banner: null }, extra || {});
    render();
    window.scrollTo(0, 0);
  }

  // ---------- Piezas ----------
  const shield = `<svg class="shield" viewBox="0 0 22 26" aria-hidden="true"><path d="M11 1 2 4.5v7.2C2 18 6 23 11 25c5-2 9-7 9-13.3V4.5Z" fill="var(--accent)"/><path d="m6.5 13 3.2 3.2L15.8 10" fill="none" stroke="var(--signal)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>`;

  function topbar() {
    const showPts = !["welcome", "pre"].includes(S.screen);
    return `<header class="topbar">
      <button class="brand" data-act="go" data-v="inbox" aria-label="${t("brand")}: ir a la bandeja">${shield}<span>${t("brand")}</span></button>
      ${showPts ? `<span class="chip" aria-label="${S.points} ${t("points")}">★ ${S.points}</span>` : ""}
      ${S.screen !== "resources" ? `<button class="tbtn" data-act="go" data-v="resources">${t("help")}</button>` : ""}
      ${["inbox", "clues", "right", "action", "solved"].includes(S.screen) ? crew() : ""}
    </header>`;
  }

  function crew() {
    const n = solvedCount();
    return `<ul class="crew" aria-label="${t("crewLabel")}: ${n} ${t("of")} 7">
      ${CASES.map((c) => {
        const cls = P(c.id).done ? "done" : (c.id === S.current && S.screen !== "inbox" ? "now" : "");
        return `<li class="${cls}" title="${c.name}"><span class="avatar" style="background:${c.color}" aria-hidden="true">${initials(c.name)}</span></li>`;
      }).join("")}
      <li class="count" aria-hidden="true">${n}/7 ${t("helped")}</li>
    </ul>`;
  }

  function scaleQ(name, idx, arr) {
    const v = arr[idx];
    return `<fieldset class="q">
      <legend>${t("q" + (idx + 1))}</legend>
      <div class="scale">${[1, 2, 3, 4, 5].map((n) => `<label><input type="radio" id="${name}${idx}-${n}" name="${name}${idx}" value="${n}" data-act="rate" data-set="${name}" data-i="${idx}" ${v === n ? "checked" : ""}><span>${n}</span></label>`).join("")}</div>
      <div class="scale-ends"><span>${t("low")}</span><span>${t("high")}</span></div>
    </fieldset>`;
  }

  function stepper(n) {
    return `<div class="stepper" aria-label="${t("step")} ${n} ${t("of")} 3">${[1, 2, 3].map((i) => `<i class="${i <= n ? "on" : ""}"></i>`).join("")}</div>`;
  }

  function caseHead(n) {
    return `<div class="case-head"><button class="back" data-act="go" data-v="inbox">${t("back")}</button>${stepper(n)}</div>`;
  }

  function chat(c) {
    return `<div class="chat">
      <div class="bubble">${L(c.msg)}</div>
      <div class="who"><span class="avatar" style="background:${c.color}">${initials(c.name)}</span>${c.name}, ${c.age}</div>
    </div>`;
  }

  // ---------- Pantallas ----------
  const screens = {
    welcome() {
      return `<div class="hero-band">
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
          ${[1, 2, 3].map((i) => `<li><span class="num">${i}</span><div><h3>${t("s" + i + "t")}</h3><p class="muted">${t("s" + i + "d")}</p></div></li>`).join("")}
        </ol>
        <h3>${t("ranksTitle")}</h3>
        <div class="ranks">${t("ranks").map((r, i) => `<div class="rank-row"><span>${i + 1}. ${r}</span><span class="pts">${RANK_MIN[i]}+ pts</span></div>`).join("")}</div>
        <p class="note">${t("tipWrong")}</p>
        <button class="btn" data-act="open" data-v="${firstOpen().id}">${t("seeCases")} →</button>`;
    },
    inbox() {
      const n = solvedCount();
      return `<span class="eyebrow">${t("inboxEyebrow")}</span>
        <h2>${t("inboxTitle")}</h2>
        <div class="status"><span><strong>${n}</strong> ${t("of")} 7 ${t("solved")}</span><span class="muted small">${t("level")}: <strong>${t("ranks")[rankIndex(S.points)]}</strong></span></div>
        <div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="7" aria-valuenow="${n}"><div style="width:${(n / 7) * 100}%"></div></div>
        ${nudge(n)}
        <div class="inbox">
          ${CASES.map((c) => {
            const done = P(c.id).done;
            return `<button class="msg ${done ? "is-done" : ""}" data-act="open" data-v="${c.id}">
              <span class="avatar" style="background:${c.color}">${initials(c.name)}</span>
              <span class="msg-body"><span class="msg-name">${c.name}</span><span class="msg-prev">${L(c.msg)}</span></span>
              <span class="pill ${done ? "done" : "new"}">${done ? t("done") : t("new")}</span>
            </button>`;
          }).join("")}
        </div>
        <div class="btn-row">
          <button class="btn ghost" data-act="go" data-v="resources">${t("resources")}</button>
          <button class="btn ${n === 7 ? "" : "ghost"}" data-act="finish">${n === 7 ? t("seeReport") : t("finish")}</button>
        </div>`;
    },
    clues() {
      const c = curCase(), p = P(c.id);
      return `${caseHead(1)}
        ${chat(c)}
        <h3>🔍 ${t("tapScene")} <span class="muted small">(${p.clues.length} ${t("of")} 3 ${t("found")})</span></h3>
        <div class="scene" role="group" aria-label="${L(c.place)}">
          <span class="scene-label">${L(c.place)}</span>
          <span class="scene-deco" style="left:8%;top:22%">${c.deco[0]}</span>
          <span class="scene-deco" style="right:10%;top:12%">${c.deco[1]}</span>
          ${c.clues.map((cl, i) => `<button class="spot ${p.clues.includes(i) ? "found" : ""}" style="left:${cl.x}%;top:${cl.y}%" data-act="clue" data-v="${i}" aria-label="${p.clues.includes(i) ? L(cl) : t("tapScene")}">${cl.icon}</button>`).join("")}
        </div>
        <ul class="clues" aria-live="polite">
          ${p.clues.length ? p.clues.map((i) => `<li><span>${c.clues[i].icon}</span><span>${L(c.clues[i])}</span><span class="plus">+10</span></li>`).join("") : `<li class="empty">${t("noClues")}</li>`}
        </ul>
        ${p.clues.length === 3 ? `<p class="toast" role="status">${t("allFound")}</p>` : ""}`;
    },
    right() {
      const c = curCase(), p = P(c.id);
      return `${caseHead(2)}
        <h2>${t("whichRight")}</h2>
        <div class="options">
          ${c.options.map((r) => {
            let cls = "";
            if (p.dOk && r === c.right) cls = "right";
            else if (S.fb && S.fb.wrong && S.fb.wrong.includes(r)) cls = "wrong";
            return `<button class="opt ${cls}" data-act="answerRight" data-v="${r}" ${p.dOk || cls === "wrong" ? "disabled" : ""}><span class="dot">${cls === "right" ? "✓" : cls === "wrong" ? "✕" : ""}</span><span>${L(RIGHTS[r])}</span></button>`;
          }).join("")}
        </div>
        ${feedbackBox()}
`;
    },
    action() {
      const c = curCase(), p = P(c.id);
      return `${caseHead(3)}
        ${bannerBox()}
        ${chat(c)}
        <h2>${t("whatDo")}</h2>
        <div class="options">
          ${c.actions.map((a, i) => {
            let cls = "";
            if (p.aOk && a.ok) cls = "right";
            else if (S.fb && S.fb.wrong && S.fb.wrong.includes(i)) cls = "wrong";
            return `<button class="opt ${cls}" data-act="answerAction" data-v="${i}" ${p.aOk || cls === "wrong" ? "disabled" : ""}><span class="dot">${cls === "right" ? "✓" : cls === "wrong" ? "✕" : ""}</span><span>${L(a)}</span></button>`;
          }).join("")}
        </div>
        ${feedbackBox()}
`;
    },
    solved() {
      const c = curCase(), p = P(c.id), r = RIGHTS[c.right];
      const all = solvedCount() === 7, nx = nextOpen(), ri = rankIndex(S.points);
      const up = p.startRank !== null && ri > p.startRank;
      return `${up ? `<div class="levelup" role="status">${t("levelUp")(t("ranks")[ri])}</div>` : ""}
        <div class="celebrate">
          <span class="eyebrow">${L(r)}</span>
          <h2>${t("caseSolved")} 🎉</h2>
          <span class="big-pts">+${p.earned}</span>
          <span class="muted">${t("points")}</span>
          ${all ? "" : `<span class="muted small">${t("leftCases")(7 - solvedCount())}</span>`}
        </div>
        ${bannerBox()}
        <div class="keyidea"><span class="eyebrow">${t("keyIdea")}</span><p>${L(c.key)}</p></div>
        ${all ? `<button class="btn" data-act="go" data-v="report">${t("seeReport")} →</button>`
          : `<div class="teaser">
              <span class="eyebrow">💬 ${t("newMsg")}</span>
              ${chat(nx)}
              <button class="btn" data-act="open" data-v="${nx.id}">${t("replyTo")} ${nx.name} →</button>
            </div>`}
        <details class="more">
          <summary>📚 ${t("learnMore")}</summary>
          <div class="more-body">
            <a class="video" href="${SERIES_URL}" target="_blank" rel="noopener">
              <span class="thumb"><span class="play"></span><span class="ep">${t("episode").toUpperCase()} ${r.ep} · ${L(r).toUpperCase()}</span></span>
              <span class="cap"><strong>▶ ${t("watch")}</strong><span class="muted small">${t("pendingLink")}</span></span>
            </a>
            ${learnLinks()}
          </div>
        </details>`;
    },
    report() {
      const ri = rankIndex(S.points), n = solvedCount();
      const ready = S.post.every(Boolean);
      return `<span class="eyebrow">${t("reportEyebrow")}</span>
        <div class="medal">
          <span class="eyebrow">${t("reached")}</span>
          <span style="font-size:2.4rem" aria-hidden="true">🏅</span>
          <span class="rank">${t("ranks")[ri]}</span>
          <span class="score">★ ${S.points} / ${MAX_POINTS} · ${n} ${t("casesOf")}</span>
        </div>
        <h2>${t("afterTitle")}</h2>
        <p class="muted">${t("afterIntro")}</p>
        ${[0, 1, 2].map((i) => scaleQ("post", i, S.post)).join("")}
        ${ready ? `<div class="compare">${[0, 1, 2].map((i) => `<div class="cmp"><strong>${t("q" + (i + 1))}</strong>
            <div class="cmp-row"><span>${t("before")}</span><div class="bar"><div style="width:${(S.pre[i] || 0) * 20}%"></div></div><b>${S.pre[i] || "–"}</b></div>
            <div class="cmp-row"><span>${t("now")}</span><div class="bar now"><div style="width:${S.post[i] * 20}%"></div></div><b>${S.post[i]}</b></div>
          </div>`).join("")}</div>` : ""}
        <button class="btn" data-act="go" data-v="share" ${ready ? "" : "disabled"}>${t("shareRank")} →</button>
        ${n < 7 ? `<button class="btn ghost" data-act="go" data-v="inbox">← ${t("keepGoing")} (${7 - n})</button>` : ""}
        <details class="more">
          <summary>📚 ${t("learnAll")}</summary>
          <div class="more-body">
            <div class="links">${Object.values(RIGHTS).map((r) => `<a class="link-row" href="${SERIES_URL}" target="_blank" rel="noopener"><span class="ico">▶</span><span>${t("episode")} ${r.ep} · ${L(r)}</span><span class="arrow">↗</span></a>`).join("")}</div>
            ${learnLinks()}
          </div>
        </details>`;
    },
    share() {
      const txt = t("shareText")(t("ranks")[rankIndex(S.points)], solvedCount(), S.points);
      const enc = encodeURIComponent(txt), url = encodeURIComponent(SERIES_URL);
      return `<span class="eyebrow">${t("shareEyebrow")}</span>
        <h2>${t("shareTitle")}</h2>
        <div class="share-card" id="share-text">${txt}</div>
        <div class="btn-row">
          <button class="btn" data-act="copy" data-v="text">${t("copyText")}</button>
          <button class="btn ghost" data-act="copy" data-v="link">${t("copyLink")}</button>
        </div>
        <p class="toast" aria-live="polite">${S.toast}</p>
        <div class="socials">
          <a href="https://wa.me/?text=${enc}%20${url}" target="_blank" rel="noopener">WhatsApp</a>
          <a href="https://twitter.com/intent/tweet?text=${enc}&url=${url}" target="_blank" rel="noopener">X</a>
          <a href="https://www.facebook.com/sharer/sharer.php?u=${url}" target="_blank" rel="noopener">Facebook</a>
        </div>
        <button class="btn ghost" data-act="restart">↺ ${t("playAgain")}</button>`;
    },
    resources() {
      return `<button class="back" data-act="go" data-v="${S.prevScreen && S.prevScreen !== "resources" ? S.prevScreen : "inbox"}">← Volver</button>
        <h2>📞 ${t("resTitle")}</h2>
        <p class="note">${t("resNote")}</p>
        ${RESOURCES.map((g) => `<div class="res-group"><h3>${L(g.title)}</h3>
          ${g.items.map((it) => it.url
            ? `<a class="link-row" href="${it.url}" target="_blank" rel="noopener"><span class="ico">🔗</span><span>${L(it)}</span><span class="arrow">↗</span></a>`
            : `<div class="res"><span class="name">${L(it)}</span><span class="tbd">${t("tbd")}</span></div>`).join("")}
        </div>`).join("")}
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
          <button class="btn" data-act="cancelConfirm" autofocus>${d.stay}</button>
          <button class="btn ghost" data-act="${d.act}">${d.leave}</button>
        </div>
      </div>
    </div>`;
  }

  function learnLinks() {
    return `<div class="links">
      <a class="link-row" href="${SERIES_URL}" target="_blank" rel="noopener"><span class="ico">📄</span><span>${t("material")}</span><span class="arrow">↗</span></a>
      <a class="link-row" href="${SERIES_URL}" target="_blank" rel="noopener"><span class="ico">📖</span><span>${t("bookBW")}</span><span class="arrow">↗</span></a>
      <button class="link-row" data-act="go" data-v="resources"><span class="ico">📞</span><span>${t("whereHelp")}</span><span class="arrow">→</span></button>
    </div>`;
  }

  function bannerBox() {
    const b = S.banner;
    return b ? `<div class="feedback ok" role="status"><strong>${b.title}</strong><p>${b.text}</p></div>` : "";
  }

  function feedbackBox() {
    if (!S.fb) return "";
    return `<div class="feedback ${S.fb.ok ? "ok" : "no"}" role="status"><strong>${S.fb.title}</strong><p>${S.fb.text}</p></div>`;
  }

  function sheet() {
    if (!S.sheet) return "";
    const ids = ["welcome", "pre", "how", "inbox", "clues", "right", "action", "solved", "report", "share", "resources"];
    return `<div class="sheet-wrap" data-act="closeSheet">
      <div class="sheet" role="dialog" aria-modal="true" aria-label="${t("jumpTitle")}">
        <h3>${t("jumpTitle")}</h3>
        <p class="muted small">${t("jumpNote")}</p>
        <div class="sheet-list">${ids.map((id, i) => `<button data-act="jumpTo" data-v="${id}"><span class="n">${String(i + 1).padStart(2, "0")}</span><span>${t("screens")[i]}</span></button>`).join("")}</div>
      </div>
    </div>`;
  }

  // ---------- Render ----------
  const app = document.getElementById("app");
  function render() {
    document.documentElement.lang = "es";
    app.innerHTML = topbar() + `<main class="screen">${screens[S.screen]()}</main>` +
      `<button class="jump" data-act="openSheet">☰ ${t("jump")}</button>` + sheet() + dialog();
    if (S.confirm) { const b = app.querySelector(".dlg .btn"); if (b) b.focus(); }
  }

  // ---------- Interacciones ----------
  app.addEventListener("click", (e) => {
    const el = e.target.closest("[data-act]");
    if (!el) return;
    const act = el.dataset.act, v = el.dataset.v;
    if (act === "rate") return; // lo maneja "change"
    // Clic en el fondo oscuro cierra; clic dentro de la ventana no
    if ((el.classList.contains("sheet-wrap") || el.classList.contains("dlg-wrap")) && e.target !== el) return;
    const c = curCase();

    switch (act) {
      case "go":
        if (v === "resources") S.prevScreen = S.screen;
        go(v);
        break;
      case "open": {
        const p = P(v);
        if (p.startRank === null) p.startRank = rankIndex(S.points);
        const step = p.done ? "solved" : p.dOk ? "action" : p.clues.length === 3 ? "right" : "clues";
        go(step, { current: v });
        break;
      }
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
        if (!p.clues.includes(i)) { p.clues.push(i); p.earned += 10; S.points += 10; }
        render();
        // Con las 3 pistas, pasa sola a la pregunta
        if (p.clues.length === 3) setTimeout(() => { if (S.screen === "clues" && S.current === c.id) go("right"); }, 1100);
        break;
      }
      case "answerRight": {
        const p = P(c.id);
        if (p.dOk) break;
        if (v === c.right) {
          const pts = [50, 20][p.dTries] ?? 10;
          p.dOk = true; p.earned += pts; S.points += pts;
          go("action", { banner: { title: `${t("correct")} +${pts}`, text: L(c.rightFb) } });
        } else {
          p.dTries++;
          S.fb = { ok: false, title: t("notQuite"), text: L(c.hint), wrong: [...(S.fb?.wrong || []), v] };
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
          go("solved", { banner: { title: `${t("good")} +${pts}`, text: L(a.fb) } });
        } else {
          p.aTries++;
          S.fb = { ok: false, title: t("rethink"), text: L(a.fb), wrong: [...(S.fb?.wrong || []), +v] };
          render();
        }
        break;
      }
      case "copy": {
        const text = v === "link" ? SERIES_URL : document.getElementById("share-text").textContent;
        const done = (ok) => { S.toast = ok ? t("copied") : t("copyFail"); render(); };
        try { navigator.clipboard.writeText(text).then(() => done(true), () => done(false)); } catch (_) { done(false); }
        break;
      }
      case "restart":
        S.confirm = { title: t("restartTitle"), body: t("restartBody"), stay: t("cancel"), leave: t("restartYes"), act: "restartYes" };
        render();
        break;
      case "restartYes": { S = fresh(); render(); window.scrollTo(0, 0); break; }
      case "openSheet": S.sheet = true; render(); break;
      case "closeSheet": S.sheet = false; render(); break;
      case "jumpTo": demoJump(v); break;
    }
  });

  app.addEventListener("change", (e) => {
    const el = e.target;
    if (el.dataset.act !== "rate") return;
    S[el.dataset.set][+el.dataset.i] = +el.value;
    const y = window.scrollY;
    render();
    window.scrollTo(0, y);
    const again = document.getElementById(el.id);
    if (again) again.focus({ preventScroll: true });
  });

  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    if (S.confirm) { S.confirm = null; render(); }
    else if (S.sheet) { S.sheet = false; render(); }
  });

  // ---------- Avisar antes de salir de la página ----------
  // Nada se guarda: si la persona cierra o recarga, pierde su progreso.
  // El navegador muestra su propio mensaje ("¿Salir del sitio? Es posible que no se guarden los cambios").
  function warnBeforeLeave(e) {
    if (!hasProgress()) return;
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

  // Salta a cualquier pantalla con datos de ejemplo (caso de Kiara)
  function demoJump(id) {
    S.sheet = false;
    if (["clues", "right", "action", "solved"].includes(id)) {
      S.current = "kiara";
      const p = P("kiara");
      if (id !== "clues" && p.clues.length === 0) { p.clues = [0, 1, 2]; p.earned += 30; S.points += 30; }
      if (["action", "solved"].includes(id) && !p.dOk) { p.dOk = true; p.earned += 50; S.points += 50; }
      if (id === "solved" && !p.aOk) { p.aOk = true; p.done = true; p.earned += 40; S.points += 40; }
    }
    if (["report", "share"].includes(id) && S.pre.every((x) => !x)) S.pre = [2, 3, 1];
    if (id === "share" && !S.post.every(Boolean)) S.post = [4, 5, 4];
    go(id);
  }

  render();
})();
</script>
</body>
</html>
'''

# --------------------------------------------------
# Mostrar el prototipo
# --------------------------------------------------

components.html(PROTOTIPO_HTML, height=900, scrolling=True)
