import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Para mi princesa 🐻❤️",
    page_icon="🧸",
    layout="centered"
)

# Fondo nocturno romántico y limpieza de márgenes de Streamlit para móvil
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #120D31 0%, #26184D 55%, #3E2158 100%);
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    .block-container {
        padding-top: 0.6rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 460px;
    }
    </style>
""", unsafe_allow_html=True)

html_osito = r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
<style>
  * {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
  }
  html, body {
    margin: 0;
    padding: 0;
    background: transparent;
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: 'Quicksand', -apple-system, BlinkMacSystemFont, sans-serif;
    user-select: none;
    touch-action: manipulation;
  }
  .titulo-pao {
    font-family: 'Dancing Script', cursive;
    color: #FFD1E6;
    font-size: 2.2rem;
    margin: 4px 0 12px 0;
    text-align: center;
    text-shadow: 0 0 14px rgba(255, 105, 180, 0.55);
  }
  canvas {
    cursor: pointer;
    width: 100%;
    max-width: 400px;
    aspect-ratio: 400 / 340;
    height: auto;
    border-radius: 24px;
    border: 1.5px solid rgba(255, 209, 230, 0.25);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45), 0 0 22px rgba(255, 64, 129, 0.2);
  }
  .tarjeta-mensaje {
    width: 100%;
    max-width: 400px;
    min-height: 76px;
    margin: 14px 0 16px 0;
    padding: 12px 18px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.09);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 209, 230, 0.22);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  #mensaje {
    color: #FFF5F8;
    font-size: 16.5px;
    font-weight: 500;
    line-height: 1.4;
    text-align: center;
    transition: opacity 0.25s ease, transform 0.25s ease;
  }
  #mensaje.oculto {
    opacity: 0;
    transform: translateY(4px);
  }
  button {
    background: linear-gradient(135deg, #FF4081 0%, #EC407A 50%, #D81B60 100%);
    color: #FFFFFF;
    border: none;
    border-radius: 30px;
    padding: 13px 32px;
    font-family: 'Quicksand', sans-serif;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(255, 64, 129, 0.45);
    transition: transform 0.15s ease, box-shadow 0.2s ease;
  }
  button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(255, 64, 129, 0.6);
  }
  button:active {
    transform: scale(0.95);
  }
</style>
</head>
<body>

<div class="titulo-pao">Un detalle para mi princesa 💌</div>
<canvas id="lienzo"></canvas>

<div class="tarjeta-mensaje">
  <div id="mensaje">¡Toca al osito o presiona el botón! 🐾</div>
</div>

<button onclick="accionCarino(200, 235)">Toca para ver ❤️</button>

<script>
const canvas = document.getElementById("lienzo");
const ctx = canvas.getContext("2d");
const lblMensaje = document.getElementById("mensaje");

// Resolución HiDPI / Retina para que se vea súper nítido en celular
const W = 400;
const H = 340;
const dpr = Math.min(window.devicePixelRatio || 1, 3);
canvas.width = W * dpr;
canvas.height = H * dpr;
ctx.scale(dpr, dpr);

const mensajes = [
  "¡Hola mi amor! Solo pasaba a recordarte lo increíble que eres ✨",
  "Te mando un abrazo enorme y muchos besitos 🐻🤗",
  "A tu lado cada día es mi favorito ❤️",
  "¿Ya te dije hoy lo mucho que te amo? 😊",
  "Eres mi persona favorita en el mundo entero 🌟",
  "Un recordatorio rápido: me haces muy feliz 💕",
  "Gracias por dejarme estar en tu vida, te amo ❤️🌠",
  "Te amo mucho mi amor 🧸💖",
  "Soy la persona más feliz desde que te conocí 💕💕",
  "Recordatorio del día: eres lo más bonito que me ha pasado 💕✨",
  "Tu sonrisa tiene superpoderes, me arregla cualquier día al instante 😊💖",
  "¿Ya te dijeron hoy que tienes la sonrisa más linda del mundo? Porque sí 😍❤️",
  "Contigo hasta los días normales se sienten mágicos ✨❤️",
  "Te pienso más veces al día de las que me atrevo a admitir 💭💕",
  "Un besito virtual en lo que te puedo dar mil en persona 😘🧸",
  "No sé qué hice para tener tanta suerte de coincidir contigo 🍀💖",
  "Eres mi lugar seguro y mi pensamiento favorito de todo el día 🧸✨",
  "Ojalá pudieras verte con mis ojos para que supieras lo perfecta que eres 💖🌟",
  "Me encantas hoy, mañana y todos los días que nos faltan juntos ❤️♾️",
  "De todas las cosas bonitas que me han pasado, tú siempre eres mi favorita 🌟💞",
  "Gracias por hacer mi mundo mucho más bonito desde que llegaste 💐❤️"
];

// Cola barajada para que no se repitan mensajes hasta verlos todos
let colaMensajes = [];
let timerMensaje = null;

function siguienteMensaje() {
  if (colaMensajes.length === 0) {
    colaMensajes = [...mensajes];
    for (let i = colaMensajes.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [colaMensajes[i], colaMensajes[j]] = [colaMensajes[j], colaMensajes[i]];
    }
    if (colaMensajes[colaMensajes.length - 1] === lblMensaje.innerText) {
      colaMensajes.unshift(colaMensajes.pop());
    }
  }
  return colaMensajes.pop();
}

let corazones = [];
let destellos = [];
let estrellasFugaces = [];
let ojosCerrados = false;
let felizTimer = 0;
let rebote = 0;
let latido = 0;

// Estrellas fijas
const estrellasFijas = Array.from({ length: 50 }, () => ({
  x: Math.random() * W,
  y: Math.random() * 245,
  radio: 0.6 + Math.random() * 1.4,
  desfase: Math.random() * Math.PI * 2,
  velocidad: 0.03 + Math.random() * 0.05
}));

// Luciérnagas flotando cerca de los lirios y el pasto
const luciernagas = Array.from({ length: 14 }, () => ({
  x: Math.random() * W,
  y: 195 + Math.random() * 125,
  radio: 1.5 + Math.random() * 1.6,
  desfase: Math.random() * Math.PI * 2,
  vx: -0.25 + Math.random() * 0.5,
  vy: -0.15 + Math.random() * 0.3
}));

// Briznas de pasto
const briznasPasto = Array.from({ length: 75 }, () => ({
  x: Math.random() * W,
  y: 278 + Math.random() * 62,
  altura: 10 + Math.random() * 14,
  inclinacion: -4 + Math.random() * 8,
  color: Math.random() > 0.5 ? "#388E3C" : "#66BB6A"
}));

// Lirios
const lirios = [
  { x: 38, y: 245, escala: 0.85, rot: -0.2, color: "#FFF9FB", centro: "#F06292" },
  { x: 78, y: 262, escala: 0.95, rot: 0.12, color: "#FCE4EC", centro: "#EC407A" },
  { x: 22, y: 282, escala: 0.7, rot: -0.3, color: "#F8BBD0", centro: "#D81B60" },
  { x: 362, y: 242, escala: 0.88, rot: 0.2, color: "#FFF9FB", centro: "#F06292" },
  { x: 320, y: 260, escala: 0.95, rot: -0.15, color: "#FCE4EC", centro: "#EC407A" },
  { x: 378, y: 284, escala: 0.72, rot: 0.28, color: "#F8BBD0", centro: "#D81B60" }
];

function crearEstrellaFugaz() {
  estrellasFugaces.push({
    x: 80 + Math.random() * 310,
    y: 10 + Math.random() * 100,
    vx: -4.5 - Math.random() * 3,
    vy: 2.0 + Math.random() * 2,
    longitud: 45 + Math.random() * 35,
    vida: 1.0
  });
}

function dibujarLuna() {
  ctx.save();
  ctx.translate(64, 58);
  ctx.rotate(-0.35);

  // Halo suave alrededor de la luna
  const halo = ctx.createRadialGradient(-4, 0, 6, -4, 0, 52);
  halo.addColorStop(0, "rgba(255, 245, 200, 0.28)");
  halo.addColorStop(1, "rgba(255, 245, 200, 0)");
  ctx.fillStyle = halo;
  ctx.beginPath();
  ctx.arc(-4, 0, 52, 0, Math.PI * 2);
  ctx.fill();

  // Luna creciente
  const r = 21;
  const ang = 0.32 * Math.PI;
  const xEnd = r * Math.cos(ang);
  const yEnd = r * Math.sin(ang);

  ctx.shadowColor = "rgba(255, 243, 196, 0.85)";
  ctx.shadowBlur = 14;
  ctx.fillStyle = "#FFF8DC";
  ctx.beginPath();
  ctx.arc(0, 0, r, ang, 2 * Math.PI - ang, false);
  ctx.quadraticCurveTo(-7, 0, xEnd, yEnd);
  ctx.closePath();
  ctx.fill();
  ctx.restore();
}

function dibujarCielo() {
  const gradCielo = ctx.createLinearGradient(0, 0, 0, 285);
  gradCielo.addColorStop(0, "#0F0A29");
  gradCielo.addColorStop(0.55, "#231955");
  gradCielo.addColorStop(1, "#4C2E78");
  ctx.fillStyle = gradCielo;
  ctx.fillRect(0, 0, W, H);

  // Estrellas fijas titilando
  estrellasFijas.forEach(e => {
    const alpha = 0.3 + 0.7 * Math.abs(Math.sin(latido * e.velocidad * 7 + e.desfase));
    ctx.beginPath();
    ctx.arc(e.x, e.y, e.radio, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255, 250, 225, ${alpha})`;
    ctx.fill();
  });

  dibujarLuna();

  // Estrellas fugaces
  for (let i = estrellasFugaces.length - 1; i >= 0; i--) {
    let ef = estrellasFugaces[i];
    ef.x += ef.vx;
    ef.y += ef.vy;
    ef.vida -= 0.022;

    if (ef.vida > 0) {
      ctx.save();
      const angulo = Math.atan2(ef.vy, ef.vx);
      const colaX = ef.x - Math.cos(angulo) * ef.longitud;
      const colaY = ef.y - Math.sin(angulo) * ef.longitud;

      const gradEstrella = ctx.createLinearGradient(ef.x, ef.y, colaX, colaY);
      gradEstrella.addColorStop(0, `rgba(255, 255, 255, ${ef.vida})`);
      gradEstrella.addColorStop(0.4, `rgba(255, 200, 235, ${ef.vida * 0.65})`);
      gradEstrella.addColorStop(1, "rgba(255, 255, 255, 0)");

      ctx.strokeStyle = gradEstrella;
      ctx.lineWidth = 2.4;
      ctx.lineCap = "round";
      ctx.beginPath();
      ctx.moveTo(ef.x, ef.y);
      ctx.lineTo(colaX, colaY);
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(ef.x, ef.y, 2.2, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 255, 255, ${ef.vida})`;
      ctx.fill();
      ctx.restore();
    } else {
      estrellasFugaces.splice(i, 1);
    }
  }
}

function dibujarPastoFondo() {
  ctx.fillStyle = "#164A1B";
  ctx.beginPath();
  ctx.moveTo(0, 280);
  ctx.quadraticCurveTo(110, 252, 240, 275);
  ctx.quadraticCurveTo(330, 290, W, 265);
  ctx.lineTo(W, H);
  ctx.lineTo(0, H);
  ctx.closePath();
  ctx.fill();

  const gradPasto = ctx.createLinearGradient(0, 265, 0, H);
  gradPasto.addColorStop(0, "#266D2B");
  gradPasto.addColorStop(1, "#144218");
  ctx.fillStyle = gradPasto;
  ctx.beginPath();
  ctx.moveTo(0, 278);
  ctx.quadraticCurveTo(200, 260, W, 282);
  ctx.lineTo(W, H);
  ctx.lineTo(0, H);
  ctx.closePath();
  ctx.fill();

  const brisa = Math.sin(latido * 0.35) * 2.5;
  briznasPasto.forEach(b => {
    ctx.strokeStyle = b.color;
    ctx.lineWidth = 1.7;
    ctx.lineCap = "round";
    ctx.beginPath();
    ctx.moveTo(b.x, b.y);
    ctx.quadraticCurveTo(
      b.x + b.inclinacion * 0.5,
      b.y - b.altura * 0.5,
      b.x + b.inclinacion + brisa,
      b.y - b.altura
    );
    ctx.stroke();
  });
}

function dibujarLirio(l) {
  const brisa = Math.sin(latido * 0.4 + l.x) * 0.06;
  ctx.save();

  const baseX = l.x - l.rot * 25;
  const baseY = l.y + 52 * l.escala;
  ctx.strokeStyle = "#388E3C";
  ctx.lineWidth = 3 * l.escala;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(baseX, baseY);
  ctx.quadraticCurveTo(l.x - 5, l.y + 25 * l.escala, l.x + brisa * 20, l.y);
  ctx.stroke();

  ctx.fillStyle = "#43A047";
  [-1, 1].forEach(dir => {
    ctx.beginPath();
    ctx.moveTo(baseX + dir * 2, baseY - 12 * l.escala);
    ctx.quadraticCurveTo(
      l.x + dir * 22 * l.escala,
      l.y + 18 * l.escala,
      l.x + dir * 16 * l.escala,
      l.y + 36 * l.escala
    );
    ctx.closePath();
    ctx.fill();
  });

  ctx.translate(l.x + brisa * 20, l.y);
  ctx.rotate(l.rot + brisa);
  ctx.scale(l.escala, l.escala);

  for (let i = 0; i < 6; i++) {
    ctx.save();
    ctx.rotate((i * Math.PI) / 3);

    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.quadraticCurveTo(8, -11, 0, -25);
    ctx.quadraticCurveTo(-8, -11, 0, 0);
    ctx.fillStyle = l.color;
    ctx.fill();
    ctx.strokeStyle = "#F48FB1";
    ctx.lineWidth = 0.7;
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(0, -2);
    ctx.lineTo(0, -16);
    ctx.strokeStyle = l.centro;
    ctx.lineWidth = 1.4;
    ctx.stroke();

    ctx.fillStyle = l.centro;
    ctx.beginPath();
    ctx.arc(-2, -9, 0.8, 0, Math.PI * 2);
    ctx.arc(2, -11, 0.8, 0, Math.PI * 2);
    ctx.arc(0, -6, 0.8, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();
  }

  for (let i = -2; i <= 2; i++) {
    const ang = i * 0.25 - Math.PI / 2;
    const ex = Math.cos(ang) * 11;
    const ey = Math.sin(ang) * 11;
    ctx.strokeStyle = "#F8BBD0";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(ex, ey);
    ctx.stroke();

    ctx.fillStyle = "#FFB300";
    ctx.beginPath();
    ctx.arc(ex, ey, 1.8, 0, Math.PI * 2);
    ctx.fill();
  }

  ctx.fillStyle = "#C5E1A5";
  ctx.beginPath();
  ctx.arc(0, 0, 2.5, 0, Math.PI * 2);
  ctx.fill();

  ctx.restore();
}

function dibujarLuciernagas() {
  luciernagas.forEach(lu => {
    lu.x += lu.vx + Math.sin(latido * 0.4 + lu.desfase) * 0.25;
    lu.y += lu.vy + Math.cos(latido * 0.35 + lu.desfase) * 0.2;

    if (lu.x < 10) lu.x = W - 10;
    if (lu.x > W - 10) lu.x = 10;
    if (lu.y < 185) lu.vy = Math.abs(lu.vy);
    if (lu.y > 325) lu.vy = -Math.abs(lu.vy);

    const brillo = 0.25 + 0.75 * Math.abs(Math.sin(latido * 0.6 + lu.desfase));
    ctx.save();
    ctx.shadowColor = "rgba(255, 238, 128, 0.9)";
    ctx.shadowBlur = 10;
    ctx.fillStyle = `rgba(255, 245, 165, ${brillo})`;
    ctx.beginPath();
    ctx.arc(lu.x, lu.y, lu.radio, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  });
}

function dibujarCorazon(cx, cy, escala, color, alpha = 1, brillo = false) {
  ctx.save();
  ctx.globalAlpha = alpha;
  if (brillo) {
    ctx.shadowColor = "rgba(255, 45, 110, 0.75)";
    ctx.shadowBlur = 16;
  }
  ctx.beginPath();
  for (let t = 0; t <= 360; t += 6) {
    let rad = (t * Math.PI) / 180;
    let x = 16 * Math.pow(Math.sin(rad), 3);
    let y = -(13 * Math.cos(rad) - 5 * Math.cos(2 * rad) - 2 * Math.cos(3 * rad) - Math.cos(4 * rad));
    if (t === 0) ctx.moveTo(cx + x * escala, cy + y * escala);
    else ctx.lineTo(cx + x * escala, cy + y * escala);
  }
  ctx.closePath();
  ctx.fillStyle = color;
  ctx.fill();
  ctx.restore();
}

function dibujarOvalo(x1, y1, x2, y2, fill, stroke = null, lineWidth = 2) {
  const cx = (x1 + x2) / 2;
  const cy = (y1 + y2) / 2;
  const rx = (x2 - x1) / 2;
  const ry = (y2 - y1) / 2;
  ctx.beginPath();
  ctx.ellipse(cx, cy, rx, ry, 0, 0, 2 * Math.PI);
  if (fill) {
    ctx.fillStyle = fill;
    ctx.fill();
  }
  if (stroke) {
    ctx.strokeStyle = stroke;
    ctx.lineWidth = lineWidth;
    ctx.stroke();
  }
}

function dibujarOsito() {
  const cafeCuerpo = "#A66A33";
  const cafeOscuro = "#7B4B20";
  const crema = "#EAD0B3";
  const rubor = felizTimer > 0 ? "#FF5C8D" : "#FF8A80";

  // Sombra suave bajo el osito
  ctx.save();
  ctx.fillStyle = "rgba(10, 25, 12, 0.35)";
  ctx.beginPath();
  ctx.ellipse(200, 318, 86, 14, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();

  // Respiración suave + saltito tierno al tocarlo
  const respiracion = Math.sin(latido * 0.5) * 1.8;
  const saltoY = -Math.sin(rebote * Math.PI) * 10;

  ctx.save();
  ctx.translate(0, respiracion + saltoY);

  // Orejas
  dibujarOvalo(115, 45, 165, 95, cafeCuerpo, cafeOscuro);
  dibujarOvalo(125, 55, 155, 85, crema);
  dibujarOvalo(235, 45, 285, 95, cafeCuerpo, cafeOscuro);
  dibujarOvalo(245, 55, 275, 85, crema);

  // Cuerpo y pancita
  dibujarOvalo(125, 175, 275, 315, cafeCuerpo, cafeOscuro);
  dibujarOvalo(155, 200, 245, 300, crema);

  // Patitas inferiores
  dibujarOvalo(115, 275, 170, 325, cafeCuerpo, cafeOscuro);
  dibujarOvalo(127, 287, 158, 313, crema);
  dibujarOvalo(230, 275, 285, 325, cafeCuerpo, cafeOscuro);
  dibujarOvalo(242, 287, 273, 313, crema);

  // Cabeza
  dibujarOvalo(110, 65, 290, 210, cafeCuerpo, cafeOscuro);

  // Hocico y nariz
  dibujarOvalo(165, 135, 235, 185, crema);
  dibujarOvalo(188, 142, 212, 158, "#3E2723");

  // Sonrisa
  ctx.strokeStyle = "#3E2723";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(190, 162, 10, 0, Math.PI, false);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(210, 162, 10, 0, Math.PI, false);
  ctx.stroke();

  // Mejillas sonrojadas
  dibujarOvalo(128, 137, 156, 153, rubor);
  dibujarOvalo(244, 137, 272, 153, rubor);

  // Ojos (felices al tocarlo o parpadeando)
  if (!ojosCerrados && felizTimer <= 0) {
    dibujarOvalo(150, 110, 168, 128, "#212121");
    dibujarOvalo(154, 113, 160, 119, "white");
    dibujarOvalo(232, 110, 250, 128, "#212121");
    dibujarOvalo(236, 113, 242, 119, "white");
  } else {
    ctx.strokeStyle = "#212121";
    ctx.lineWidth = 2.6;
    ctx.lineCap = "round";
    ctx.beginPath();
    ctx.arc(159, 122, 10, Math.PI, 0, false);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(241, 122, 10, Math.PI, 0, false);
    ctx.stroke();
  }

  // Corazón central con brillo y latido
  const extraLatido = felizTimer > 0 ? 0.25 : 0;
  const escalaCorazon = 2.2 + extraLatido + 0.16 * Math.sin(latido * 1.1);
  dibujarCorazon(200, 235, escalaCorazon, "#FF1744", 1, true);

  // Bracitos abrazando
  dibujarOvalo(125, 205, 175, 245, cafeCuerpo, cafeOscuro);
  dibujarOvalo(225, 205, 275, 245, cafeCuerpo, cafeOscuro);

  ctx.restore();
}

function accionCarino(origenX = 200, origenY = 235) {
  // Transición suave del mensaje
  clearTimeout(timerMensaje);
  lblMensaje.classList.add("oculto");
  timerMensaje = setTimeout(() => {
    lblMensaje.innerText = siguienteMensaje();
    lblMensaje.classList.remove("oculto");
  }, 190);

  // Reacción feliz del osito
  felizTimer = 42;
  rebote = 1.0;

  // Corazones flotantes con desvanecimiento suave
  const colores = ["#FF1744", "#FF4081", "#FF80AB", "#F48FB1", "#FFD1DC"];
  for (let i = 0; i < 10; i++) {
    corazones.push({
      x: origenX + (-45 + Math.random() * 90),
      y: origenY + (-20 + Math.random() * 35),
      escala: 0.45 + Math.random() * 0.45,
      color: colores[Math.floor(Math.random() * colores.length)],
      vx: -1.1 + Math.random() * 2.2,
      vy: 1.4 + Math.random() * 2.1,
      vida: 70,
      vidaMax: 70
    });
  }

  // Destellitos mágicos en el punto donde tocó
  for (let i = 0; i < 8; i++) {
    const ang = (Math.PI * 2 * i) / 8 + Math.random() * 0.4;
    const vel = 1.2 + Math.random() * 1.8;
    destellos.push({
      x: origenX,
      y: origenY,
      vx: Math.cos(ang) * vel,
      vy: Math.sin(ang) * vel,
      radio: 1.8 + Math.random() * 1.8,
      vida: 30,
      vidaMax: 30
    });
  }

  crearEstrellaFugaz();
  setTimeout(crearEstrellaFugaz, 240);
}

canvas.addEventListener("click", (e) => {
  const rect = canvas.getBoundingClientRect();
  const x = (e.clientX - rect.left) * (W / rect.width);
  const y = (e.clientY - rect.top) * (H / rect.height);
  accionCarino(x, y);
});

function cicloParpadeo() {
  ojosCerrados = true;
  setTimeout(() => {
    ojosCerrados = false;
    setTimeout(cicloParpadeo, 2500 + Math.random() * 2000);
  }, 180);
}
setTimeout(cicloParpadeo, 2000);

function cicloEstrellasFugaces() {
  crearEstrellaFugaz();
  setTimeout(cicloEstrellasFugaces, 2000 + Math.random() * 2400);
}
setTimeout(cicloEstrellasFugaces, 1000);

function animar() {
  ctx.clearRect(0, 0, W, H);
  latido += 0.11;

  if (felizTimer > 0) felizTimer--;
  if (rebote > 0.01) rebote *= 0.86;
  else rebote = 0;

  dibujarCielo();
  dibujarPastoFondo();
  lirios.forEach(dibujarLirio);
  dibujarOsito();
  dibujarLuciernagas();

  // Corazones con fade-out suave
  for (let i = corazones.length - 1; i >= 0; i--) {
    let c = corazones[i];
    c.x += c.vx + Math.sin(latido * 0.4 + i) * 0.25;
    c.y -= c.vy;
    c.vida -= 1;
    if (c.vida > 0) {
      const alpha = Math.min(1, (c.vida / c.vidaMax) * 1.4);
      dibujarCorazon(c.x, c.y, c.escala, c.color, alpha, false);
    } else {
      corazones.splice(i, 1);
    }
  }

  // Destellitos mágicos al tocar
  for (let i = destellos.length - 1; i >= 0; i--) {
    let d = destellos[i];
    d.x += d.vx;
    d.y += d.vy;
    d.vida -= 1;
    if (d.vida > 0) {
      ctx.save();
      ctx.fillStyle = `rgba(255, 240, 200, ${d.vida / d.vidaMax})`;
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.radio, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    } else {
      destellos.splice(i, 1);
    }
  }

  requestAnimationFrame(animar);
}

animar();
</script>
</body>
</html>
"""

components.html(html_osito, height=585, scrolling=False)
