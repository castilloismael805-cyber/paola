import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. PERSONALIZA TU CARTA AQUÍ
# ==========================================
TITULO_INICIAL = "Para Paola la mujer mas hermosa del mundo ✨"
SUBTITULO_INICIAL = "Dale color a tu flor para descubrir un mensaje..."

TEXTO_CARTA = """
Hola, Princesa.

Quería hacerte un detalle diferente. 

Dicen que los lirios representan algo único y especial, pero siendo sincero, cualquier flor se queda corta comparada contigo.

Desde que empezamos a hablar, me encanta cada momento que compartimos, tu forma de ser y lo increíblemente hermosa que eres.

Quería crear este pequeño rincón bajo las estrellas solo para recordarte lo mucho que me gustas y lo especial que te has vuelto para mí.


"""

FIRMA = "Con mucho cariño, Ismael ❤️"
# =========================================

st.set_page_config(
    page_title="Para Paola 🤍", page_icon="🌷", layout="wide"
)

# Estilos en la ventana principal (pantalla completa + animación global de estrellas)
st.markdown(
    """
<style>
.stApp {
    background: linear-gradient(180deg, #0b0e1e 0%, #151934 55%, #221c38 100%);
}
header, footer {visibility: hidden;}
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}
iframe {
    width: 100% !important;
    border: none !important;
}
.contenedor-estrellas-global {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 999999;
    overflow: hidden;
}
.estrella-caida {
    position: absolute;
    top: -10%;
    color: #ffd97d;
    text-shadow: 0 0 12px rgba(255, 217, 125, 0.95);
    opacity: 0;
    animation: caerBrillarGlobal ease-in-out forwards;
}
@keyframes caerBrillarGlobal {
    0% { transform: translateY(0vh) rotate(0deg) scale(0.5); opacity: 0; }
    20% { opacity: 1; transform: translateY(22vh) rotate(45deg) scale(1.15); }
    50% { opacity: 0.9; transform: translateY(55vh) rotate(90deg) scale(0.95); }
    80% { opacity: 1; transform: translateY(85vh) rotate(135deg) scale(1.1); }
    100% { transform: translateY(110vh) rotate(180deg) scale(0.6); opacity: 0; }
}
</style>
""",
    unsafe_allow_html=True,
)

parrafos_html = "".join(
    [f"<p>{p}</p>" for p in TEXTO_CARTA.strip().split("\n\n")]
)

html_interactivo = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap');

* {{
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    user-select: none;
}}

body {{
    margin: 0;
    padding: 10px 14px 45px 14px;
    background: transparent;
    font-family: 'Montserrat', sans-serif;
    color: #fdfbf7;
    overflow-x: hidden;
}}

.contenedor-central {{
    max-width: 480px;
    margin: 0 auto;
}}

.titulo {{
    font-family: 'Cormorant Garamond', serif;
    color: #fdfbf7;
    text-align: center;
    font-size: 2.2rem;
    font-weight: 600;
    margin-bottom: 6px;
    line-height: 1.2;
    text-shadow: 0 2px 12px rgba(255, 215, 140, 0.25);
}}

.subtitulo {{
    color: #c5c1d4;
    text-align: center;
    font-size: 0.9rem;
    margin-bottom: 18px;
}}

/* Lienzo del cielo y el lirio */
.sketch-container {{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto 14px auto;
    padding: 10px;
    background: #0d1226;
    border-radius: 20px;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.55), 0 0 20px rgba(212, 175, 55, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.14);
}}

/* Piezas coloreables del lirio */
.coloreable {{
    fill: rgba(255, 255, 255, 0.03);
    stroke: #e2dce8;
    stroke-width: 1.7;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 1000;
    stroke-dashoffset: 1000;
    cursor: pointer;
    pointer-events: all;
    transition: fill 0.4s ease, filter 0.3s ease, stroke 0.3s ease;
    animation: dibujar 3s ease-in-out forwards;
}}

.coloreable:hover, .coloreable:active {{
    filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.45));
    stroke: #ffffff;
}}

.trazo-boceto {{
    fill: none;
    stroke: rgba(255, 240, 245, 0.45);
    stroke-width: 0.9;
    stroke-linecap: round;
    pointer-events: none;
    stroke-dasharray: 800;
    stroke-dashoffset: 800;
    animation: dibujar 3s ease-in-out 0.6s forwards;
}}

.trazo-nervadura {{
    fill: none;
    stroke: rgba(255, 255, 255, 0.35);
    stroke-width: 1;
    stroke-linecap: round;
    pointer-events: none;
    stroke-dasharray: 500;
    stroke-dashoffset: 500;
    animation: dibujar 2.5s ease-out 1.2s forwards;
}}

.trazo-estambre {{
    fill: none;
    stroke: #ffe5ec;
    stroke-width: 1.3;
    stroke-linecap: round;
    pointer-events: none;
    stroke-dasharray: 400;
    stroke-dashoffset: 400;
    animation: dibujar 2s ease-out 1.8s forwards;
}}

.puntos-pecas {{
    fill: rgba(255, 255, 255, 0.45);
    pointer-events: none;
    opacity: 0;
    animation: aparecerPecas 1.5s ease-in 2.2s forwards;
}}

/* Estrellas del cielo */
.estrella-cielo {{
    fill: #ffffff;
    animation: parpadeo 3s infinite ease-in-out alternate;
}}
.estrella-dorada {{
    fill: #ffe699;
    animation: parpadeo 2.2s infinite ease-in-out alternate;
}}
.estrella-fugaz {{
    stroke: url(#gradFugaz);
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-dasharray: 120;
    stroke-dashoffset: 120;
    animation: fugaz 5s ease-in-out 1.5s infinite;
}}

@keyframes dibujar {{ to {{ stroke-dashoffset: 0; }} }}
@keyframes aparecerPecas {{ to {{ opacity: 0.7; }} }}
@keyframes parpadeo {{
    0% {{ opacity: 0.25; transform: scale(0.8); }}
    100% {{ opacity: 1; transform: scale(1.2); }}
}}
@keyframes fugaz {{
    0% {{ stroke-dashoffset: 120; opacity: 0; }}
    10% {{ opacity: 1; }}
    25% {{ stroke-dashoffset: -120; opacity: 0; }}
    100% {{ stroke-dashoffset: -120; opacity: 0; }}
}}

/* Panel de paleta de colores */
.panel-colores {{
    background: rgba(18, 23, 52, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 16px;
    padding: 14px 12px;
    text-align: center;
    margin-bottom: 14px;
    backdrop-filter: blur(8px);
}}

.instruccion-paleta {{
    font-size: 0.82rem;
    color: #e0dcf0;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 6px;
}}

.contador {{
    color: #ffd97d;
    font-weight: 600;
}}

.paleta {{
    display: flex;
    justify-content: center;
    gap: 11px;
    flex-wrap: wrap;
    margin-bottom: 12px;
}}

.color-btn {{
    width: 38px;
    height: 38px;
    border-radius: 50%;
    border: 2px solid rgba(255, 255, 255, 0.35);
    cursor: pointer;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}}

.color-btn.activo {{
    transform: scale(1.22);
    border: 2.5px solid #ffffff;
    box-shadow: 0 0 14px rgba(255, 255, 255, 0.75);
}}

.acciones-extra {{
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 6px;
}}

.btn-secundario {{
    background: rgba(255, 255, 255, 0.08);
    color: #d8d4e8;
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 0.75rem;
    font-family: 'Montserrat', sans-serif;
    cursor: pointer;
    transition: 0.2s;
}}

.btn-secundario:hover {{
    background: rgba(255, 255, 255, 0.18);
    color: #ffffff;
}}

/* Botón Principal Dorado */
.btn-principal {{
    width: 100%;
    background: linear-gradient(135deg, #d4af37 0%, #f3e5ab 50%, #aa8010 100%);
    color: #151934;
    font-weight: 600;
    border-radius: 30px;
    padding: 14px 24px;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.95rem;
    border: none;
    box-shadow: 0 4px 18px rgba(212, 175, 55, 0.4);
    cursor: pointer;
    transition: 0.3s;
    margin-top: 6px;
}}

.btn-principal:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(212, 175, 55, 0.65);
}}

/* Carta */
.carta-papel {{
    display: none;
    background: #fffdf9;
    padding: 26px 22px;
    border-radius: 14px;
    border: 1px solid #e6dec8;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
    font-family: 'Cormorant Garamond', serif;
    color: #2c2623;
    font-size: 1.25rem;
    line-height: 1.7;
    margin-top: 18px;
    animation: subirCarta 1s ease-out forwards;
}}

.carta-papel p {{
    margin: 0 0 14px 0;
}}

.firma {{
    text-align: right;
    font-style: italic;
    font-weight: 600;
    margin-top: 18px;
    font-size: 1.3rem;
    color: #9e2a4c;
}}

@keyframes subirCarta {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

/* Respaldo de estrellas a pantalla completa dentro del frame */
.contenedor-estrellas-local {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 99999;
    overflow: hidden;
}}

.estrella-caida {{
    position: absolute;
    top: -10%;
    color: #ffd97d;
    text-shadow: 0 0 12px rgba(255, 217, 125, 0.95);
    opacity: 0;
    animation: caerBrillarLocal ease-in-out forwards;
}}

@keyframes caerBrillarLocal {{
    0% {{ transform: translateY(0vh) rotate(0deg) scale(0.5); opacity: 0; }}
    20% {{ opacity: 1; transform: translateY(22vh) rotate(45deg) scale(1.15); }}
    50% {{ opacity: 0.9; transform: translateY(55vh) rotate(90deg) scale(0.95); }}
    80% {{ opacity: 1; transform: translateY(85vh) rotate(135deg) scale(1.1); }}
    100% {{ transform: translateY(110vh) rotate(180deg) scale(0.6); opacity: 0; }}
}}
</style>
</head>
<body>

<div class="contenedor-central">
    <div class="titulo">{TITULO_INICIAL}</div>
    <div class="subtitulo" id="subtitulo-texto">{SUBTITULO_INICIAL}</div>

    <!-- LIENZO DEL LIRIO BAJO LAS ESTRELLAS -->
    <div class="sketch-container">
    <svg viewBox="0 0 400 470" width="100%" height="370">
    <defs>
        <linearGradient id="cieloNocturno" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#060919" />
            <stop offset="50%" stop-color="#121738" />
            <stop offset="100%" stop-color="#241b3d" />
        </linearGradient>
        <radialGradient id="haloLuna" cx="50%" cy="42%" r="48%">
            <stop offset="0%" stop-color="rgba(255, 210, 230, 0.22)" />
            <stop offset="55%" stop-color="rgba(160, 140, 220, 0.08)" />
            <stop offset="100%" stop-color="rgba(10, 14, 36, 0)" />
        </radialGradient>
        <linearGradient id="gradFugaz" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255,255,255,0)" />
            <stop offset="100%" stop-color="#ffffff" />
        </linearGradient>

        <!-- 7 Acuarelas / Degradados -->
        <linearGradient id="rosaLirio" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" />
            <stop offset="30%" stop-color="#ffdbe6" />
            <stop offset="75%" stop-color="#ff7597" />
            <stop offset="100%" stop-color="#c9184a" />
        </linearGradient>
        <linearGradient id="lavandaEstelar" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#f8f0fc" />
            <stop offset="40%" stop-color="#e599f7" />
            <stop offset="100%" stop-color="#862e9c" />
        </linearGradient>
        <linearGradient id="azulCeleste" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#e7f5ff" />
            <stop offset="45%" stop-color="#74c0fc" />
            <stop offset="100%" stop-color="#1864ab" />
        </linearGradient>
        <linearGradient id="coralAtardecer" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#fff4e6" />
            <stop offset="40%" stop-color="#ffa8a8" />
            <stop offset="100%" stop-color="#e03131" />
        </linearGradient>
        <linearGradient id="blancoPerla" x1="50%" y1="0%" x2="50%" y2="100%">
            <stop offset="0%" stop-color="#ffffff" />
            <stop offset="65%" stop-color="#f8f9fa" />
            <stop offset="100%" stop-color="#ced4da" />
        </linearGradient>
        <linearGradient id="doradoSol" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fff9db" />
            <stop offset="50%" stop-color="#ffd43b" />
            <stop offset="100%" stop-color="#f08c00" />
        </linearGradient>
        <linearGradient id="verdeEsmeralda" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#95d5b2" />
            <stop offset="55%" stop-color="#40916c" />
            <stop offset="100%" stop-color="#1b4332" />
        </linearGradient>
    </defs>

    <!-- Fondo de cielo estrellado -->
    <rect width="400" height="470" rx="14" fill="url(#cieloNocturno)" />
    <circle cx="200" cy="210" r="175" fill="url(#haloLuna)" />
    <path d="M 330 48 A 22 22 0 1 1 305 80 A 17 17 0 1 0 330 48 Z" fill="#fff3cc" opacity="0.9" />
    <circle cx="320" cy="64" r="32" fill="rgba(255, 243, 204, 0.12)" />
    <line class="estrella-fugaz" x1="45" y1="65" x2="135" y2="25" />

    <!-- Estrellas titilando -->
    <circle class="estrella-cielo" cx="35" cy="45" r="1.3" style="animation-delay: 0.1s;" />
    <circle class="estrella-dorada" cx="75" cy="85" r="1.8" style="animation-delay: 0.7s;" />
    <circle class="estrella-cielo" cx="120" cy="40" r="1.1" style="animation-delay: 1.4s;" />
    <circle class="estrella-cielo" cx="165" cy="65" r="1.4" style="animation-delay: 0.4s;" />
    <circle class="estrella-dorada" cx="245" cy="42" r="1.7" style="animation-delay: 1.1s;" />
    <circle class="estrella-cielo" cx="275" cy="95" r="1.2" style="animation-delay: 1.9s;" />
    <circle class="estrella-cielo" cx="360" cy="115" r="1.5" style="animation-delay: 0.3s;" />
    <circle class="estrella-dorada" cx="42" cy="160" r="1.6" style="animation-delay: 1.6s;" />
    <circle class="estrella-cielo" cx="85" cy="200" r="1.1" style="animation-delay: 0.8s;" />
    <circle class="estrella-cielo" cx="348" cy="195" r="1.3" style="animation-delay: 1.2s;" />
    <circle class="estrella-dorada" cx="365" cy="285" r="1.7" style="animation-delay: 0.5s;" />
    <circle class="estrella-cielo" cx="32" cy="295" r="1.4" style="animation-delay: 2.1s;" />
    <circle class="estrella-cielo" cx="65" cy="390" r="1.2" style="animation-delay: 0.9s;" />
    <circle class="estrella-dorada" cx="335" cy="410" r="1.5" style="animation-delay: 1.5s;" />
    <path class="estrella-dorada" d="M 60 115 L 62 121 L 68 123 L 62 125 L 60 131 L 58 125 L 52 123 L 58 121 Z" style="animation-delay: 0.6s;" />
    <path class="estrella-dorada" d="M 340 145 L 341.5 150 L 346.5 151.5 L 341.5 153 L 340 158 L 338.5 153 L 333.5 151.5 L 338.5 150 Z" style="animation-delay: 1.3s;" />

    <!-- Tallo y Hojas -->
    <path id="pieza-tallo" class="coloreable" onclick="pintar(this)" d="M 196 260 Q 191 355 178 450 L 190 450 Q 203 355 205 260 Z" />
    <path id="pieza-hoja-izq" class="coloreable" onclick="pintar(this)" d="M 192 380 Q 130 340 90 288 Q 145 315 195 355 Z" />
    <path class="trazo-boceto" d="M 188 366 Q 145 335 106 300" />
    <path id="pieza-hoja-der" class="coloreable" onclick="pintar(this)" d="M 189 410 Q 255 372 306 314 Q 245 340 191 385 Z" />
    <path class="trazo-boceto" d="M 192 396 Q 245 362 288 326" />

    <!-- 6 Pétalos del Lirio -->
    <path id="petalo-1" class="coloreable" onclick="pintar(this)" d="M 195 245 C 130 200, 95 150, 82 105 C 135 115, 175 155, 198 238 Z" />
    <path class="trazo-nervadura" d="M 192 240 Q 140 175 92 114" />

    <path id="petalo-2" class="coloreable" onclick="pintar(this)" d="M 205 245 C 270 200, 305 150, 318 105 C 265 115, 225 155, 202 238 Z" />
    <path class="trazo-nervadura" d="M 208 240 Q 260 175 308 114" />

    <path id="petalo-3" class="coloreable" onclick="pintar(this)" d="M 200 252 C 152 180, 158 108, 200 55 C 242 108, 248 180, 200 252 Z" />
    <path class="trazo-nervadura" d="M 200 245 Q 200 150 200 68" />
    <path class="trazo-boceto" d="M 195 220 Q 178 160 185 110" />
    <path class="trazo-boceto" d="M 205 220 Q 222 160 215 110" />

    <path id="petalo-4" class="coloreable" onclick="pintar(this)" d="M 198 255 C 135 212, 82 212, 52 240 C 95 282, 150 282, 198 260 Z" />
    <path class="trazo-nervadura" d="M 195 257 Q 125 240 65 240" />

    <path id="petalo-5" class="coloreable" onclick="pintar(this)" d="M 202 255 C 265 212, 318 212, 348 240 C 305 282, 250 282, 202 260 Z" />
    <path class="trazo-nervadura" d="M 205 257 Q 275 240 335 240" />

    <path id="petalo-6" class="coloreable" onclick="pintar(this)" d="M 198 256 C 152 280, 158 328, 200 358 C 242 328, 248 280, 202 256 Z" />
    <path class="trazo-nervadura" d="M 200 260 Q 200 310 200 348" />

    <!-- Pecas botánicas y estambres -->
    <circle class="puntos-pecas" cx="195" cy="195" r="1.6" />
    <circle class="puntos-pecas" cx="205" cy="185" r="1.8" />
    <circle class="puntos-pecas" cx="165" cy="215" r="1.6" />
    <circle class="puntos-pecas" cx="235" cy="212" r="1.6" />
    <circle class="puntos-pecas" cx="155" cy="245" r="1.7" />
    <circle class="puntos-pecas" cx="245" cy="248" r="1.7" />
    <circle class="puntos-pecas" cx="196" cy="290" r="1.6" />

    <path class="trazo-estambre" d="M 200 248 Q 182 185 162 145" />
    <path class="trazo-estambre" d="M 200 248 Q 190 175 182 130" />
    <path class="trazo-estambre" d="M 200 248 Q 200 170 202 122" />
    <path class="trazo-estambre" d="M 200 248 Q 212 175 220 132" />
    <path class="trazo-estambre" d="M 200 248 Q 220 185 238 148" />

    <!-- Centro dorado del lirio -->
    <g id="pieza-centro">
        <ellipse cx="160" cy="143" rx="6.5" ry="2.8" fill="#ffb703" transform="rotate(-30 160 143)" />
        <ellipse cx="181" cy="128" rx="6.5" ry="2.8" fill="#ffb703" transform="rotate(-15 181 128)" />
        <ellipse cx="202" cy="119" rx="7.5" ry="3.2" fill="#ffb703" transform="rotate(5 202 119)" />
        <ellipse cx="221" cy="130" rx="6.5" ry="2.8" fill="#ffb703" transform="rotate(20 221 130)" />
        <ellipse cx="240" cy="146" rx="6.5" ry="2.8" fill="#ffb703" transform="rotate(35 240 146)" />
    </g>
    </svg>
    </div>

    <!-- PALETA DE ACUARELAS INTERACTIVA -->
    <div class="panel-colores">
        <div class="instruccion-paleta">
            <span>🎨 Elige un color y toca cada pétalo:</span>
            <span class="contador" id="progreso-texto">0 / 9 ✨</span>
        </div>
        <div class="paleta">
            <div class="color-btn activo" style="background: linear-gradient(135deg, #ffdbe6, #c9184a);" onclick="seleccionarColor('url(#rosaLirio)', this)" title="Rosa Lirio"></div>
            <div class="color-btn" style="background: linear-gradient(135deg, #f8f0fc, #862e9c);" onclick="seleccionarColor('url(#lavandaEstelar)', this)" title="Lavanda"></div>
            <div class="color-btn" style="background: linear-gradient(135deg, #fff4e6, #e03131);" onclick="seleccionarColor('url(#coralAtardecer)', this)" title="Coral"></div>
            <div class="color-btn" style="background: linear-gradient(135deg, #e7f5ff, #1864ab);" onclick="seleccionarColor('url(#azulCeleste)', this)" title="Celeste"></div>
            <div class="color-btn" style="background: linear-gradient(135deg, #ffffff, #adb5bd);" onclick="seleccionarColor('url(#blancoPerla)', this)" title="Blanco Perla"></div>
            <div class="color-btn" style="background: linear-gradient(135deg, #fff9db, #f08c00);" onclick="seleccionarColor('url(#doradoSol)', this)" title="Dorado"></div>
            <div class="color-btn" style="background: linear-gradient(135deg, #95d5b2, #1b4332);" onclick="seleccionarColor('url(#verdeEsmeralda)', this)" title="Verde Hoja"></div>
        </div>
        <div class="acciones-extra">
            <button class="btn-secundario" onclick="colorearMagico()">✨ Color mágico automático</button>
            <button class="btn-secundario" onclick="reiniciarLienzo()">🔄 Borrar colores</button>
        </div>
    </div>

    <!-- BOTÓN PARA ABRIR LA CARTA -->
    <button class="btn-principal" id="btn-carta" onclick="mostrarCarta()">
        💌 Desbloquear y leer la carta
    </button>

    <!-- CARTA DESPLEGABLE -->
    <div class="carta-papel" id="contenedor-carta">
        {parrafos_html}
        <div class="firma">{FIRMA}</div>
    </div>
</div>

<div class="contenedor-estrellas-local" id="lluvia-estrellas"></div>

<script>
let colorActual = 'url(#rosaLirio)';
let piezasPintadas = new Set();
const totalPiezas = 9;

function ajustarAltura() {{
    setTimeout(() => {{
        if (window.frameElement) {{
            window.frameElement.style.height = (document.body.scrollHeight + 45) + 'px';
        }}
    }}, 60);
}}

window.addEventListener('load', ajustarAltura);

function seleccionarColor(gradiente, elemento) {{
    colorActual = gradiente;
    document.querySelectorAll('.color-btn').forEach(btn => btn.classList.remove('activo'));
    elemento.classList.add('activo');
}}

function pintar(elemento) {{
    elemento.style.fill = colorActual;
    elemento.style.fillOpacity = "0.94";
    const piId = elemento.getAttribute('id');
    piezasPintadas.add(piId);
    actualizarContador();
}}

function actualizarContador() {{
    const cuenta = piezasPintadas.size;
    const texto = document.getElementById('progreso-texto');
    texto.innerText = cuenta + ' / ' + totalPiezas + ' ✨';
    if (cuenta === totalPiezas) {{
        texto.innerText = '¡Lirio completado! 🌟';
    }}
}}

function colorearMagico() {{
    const asignacion = {{
        'petalo-1': 'url(#rosaLirio)',
        'petalo-2': 'url(#rosaLirio)',
        'petalo-3': 'url(#rosaLirio)',
        'petalo-4': 'url(#rosaLirio)',
        'petalo-5': 'url(#rosaLirio)',
        'petalo-6': 'url(#rosaLirio)',
        'pieza-tallo': 'url(#verdeEsmeralda)',
        'pieza-hoja-izq': 'url(#verdeEsmeralda)',
        'pieza-hoja-der': 'url(#verdeEsmeralda)'
    }};
    Object.keys(asignacion).forEach((id, index) => {{
        setTimeout(() => {{
            const el = document.getElementById(id);
            el.style.fill = asignacion[id];
            el.style.fillOpacity = "0.94";
            piezasPintadas.add(id);
            actualizarContador();
        }}, index * 120);
    }});
}}

function reiniciarLienzo() {{
    document.querySelectorAll('.coloreable').forEach(el => {{
        el.style.fill = 'rgba(255, 255, 255, 0.03)';
    }});
    piezasPintadas.clear();
    actualizarContador();
}}

function mostrarCarta() {{
    const carta = document.getElementById('contenedor-carta');
    carta.style.display = 'block';
    lanzarEstrellasPantallaCompleta();
    ajustarAltura();
    setTimeout(() => {{
        carta.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    }}, 150);
}}

function lanzarEstrellasPantallaCompleta() {{
    const simbolos = ['✦', '✧', '✨', '⋆', '★'];
    let contenedorGlobal = null;

    // Intentamos inyectar las estrellas directamente en toda la pantalla del navegador
    try {{
        if (window.parent && window.parent.document && window.parent.document.body) {{
            const docPadre = window.parent.document;
            contenedorGlobal = docPadre.getElementById('lluvia-estrellas-global');
            if (!contenedorGlobal) {{
                contenedorGlobal = docPadre.createElement('div');
                contenedorGlobal.id = 'lluvia-estrellas-global';
                contenedorGlobal.className = 'contenedor-estrellas-global';
                docPadre.body.appendChild(contenedorGlobal);
            }}
        }}
    }} catch (e) {{
        contenedorGlobal = null;
    }}

    // Si por políticas del navegador no permite salir al padre, usa el contenedor local de ancho 100vw
    const contenedor = contenedorGlobal || document.getElementById('lluvia-estrellas');
    contenedor.innerHTML = '';

    for (let i = 0; i < 65; i++) {{
        const div = document.createElement('div');
        div.className = 'estrella-caida';
        div.innerText = simbolos[Math.floor(Math.random() * simbolos.length)];
        div.style.left = (Math.random() * 98 + 1) + 'vw';
        div.style.fontSize = (Math.random() * 1.3 + 1.0) + 'rem';
        div.style.animationDuration = (Math.random() * 3.5 + 3.2) + 's';
        div.style.animationDelay = (Math.random() * 2.5) + 's';
        contenedor.appendChild(div);
    }}
}}
</script>
</body>
</html>
"""

components.html(html_interactivo, height=950, scrolling=False)
