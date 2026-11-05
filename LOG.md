# Log del proyecto: Línea de Defensa

Prototipo de app educativa para la serie **“Derechos. Son tuyos. Defiéndelos.”** de Espacios Abiertos.
La persona atiende una “línea de ayuda”: resuelve 7 casos, uno por cada derecho, buscando pistas,
nombrando el derecho y recomendando qué hacer.

- **Código:** todo vive en `app.py` (Streamlit muestra un HTML con CSS y JavaScript dentro de `PROTOTIPO_HTML`).
- **Tema:** `.streamlit/config.toml` fija el modo oscuro.
- **Publicación:** Streamlit Community Cloud, rama `main`. Tras cambiar `.streamlit/config.toml`, usar “Reboot app”.

---

## Sesión del 5 de noviembre de 2026

### Idioma
- La app es solo en español (el selector EN | ES ya se había quitado en `6770314`).

### Aviso antes de salir
- Si hay progreso y la persona cierra o recarga la página, el navegador pregunta si quiere salir
  (nada se guarda, así que el progreso se perdería).
- “Terminar turno” antes de tiempo y “Jugar otra vez” piden confirmación dentro de la app.

### Flujo directo, con menos clics
- “Cómo funciona” → **“Atender el primer caso”** abre el caso de Marco directamente.
- Tocar una respuesta la contesta: si es correcta, pasa sola a la siguiente pantalla; si no, sale una pista
  y esa opción queda tachada.
- Ya no hay botones “Siguiente” ni “Comprobar” dentro de los casos.
- Al encontrar las 3 pistas, espera **5 segundos** (barra que se llena + “Pasando a la pregunta…”) y pasa
  a la pregunta. Se ajusta con `CLUE_WAIT_MS` en `app.py`.
- Al reabrir un caso, sigue en el paso donde se quedó.
- Cada pantalla entra con un desvanecido suave (sin animación si el dispositivo pide reducir movimiento).

### Enganche para completar los 7 casos
- Arriba: fila con las 7 personas; se marcan con ✓ al ayudarlas, y el caso actual tiene un aro azul. Conteo “3/7 ayudadas”.
- Bandeja: cuántas personas faltan y cuántos puntos faltan para el próximo nivel.
- “¡Caso resuelto!” (en este orden): puntos y resultado → idea clave → **📚 Aprende más** (plegado) →
  **💬 Nuevo mensaje** de la próxima persona con el botón “Responderle a …”.
- Aviso amarillo cuando la persona sube de nivel.
- El reporte tiene “Seguir atendiendo” si faltan casos, y una sección plegada con los 7 episodios.

### Apariencia
- Siempre en modo claro, aunque el dispositivo esté en modo oscuro.
- Arreglado el desborde horizontal en móvil (`box-sizing: border-box` global).

### Enlaces reales de la serie
Tomados de https://espaciosabiertos.org/derecho-a-tener-derechos-2/ y guardados en el bloque `LINKS` de `app.py`.
Los videos de YouTube se ven dentro de la app.

| Ep. | Derecho | Video (YouTube) | Material educativo | Libro B/N |
|---|---|---|---|---|
| 1 | Derecho a tener derechos | `rMizWVmnEZA` | `Derecho-FINAL.pdf` | `EA-DERECHOS-01-Derechos-BW.pdf` |
| 2 | Educación | `fMN7G4piQV0` | `Educacion-FINAL.pdf` | `EA-DERECHOS-02-Educacion-BW.pdf` |
| 3 | Acceso a la información | `1ZD-S44Y36E` | `Informacion-FINAL.pdf` | `EA-DERECHOS-03-Informacion-BW.pdf` |
| 4 | Participación política | `KL3BpPgW2FY` | `Opinion-Politica-FINAL.pdf` | `EA-DERECHOS-04-PartPolitica-BW.pdf` |
| 5 | Acceso a la justicia | `YurWptHGE5M` | `Acceso-Justicia-FINAL.pdf` | `EA-DERECHOS-05-Justicia-BW.pdf` |
| 6 | Trabajo | `p4gJn6G36VM` | `Trabajo-FINAL.pdf` | `EA-DERECHOS-06-Trabajo-BW.pdf` |
| 7 | Dignidad | `yTGCsf9OpmA` | `Dignidad-FINAL.pdf` | `EA-DERECHOS-07-Dignidad-BW.pdf` |

PDF en `https://espaciosabiertos.org/wp-content/uploads/`.

### Entorno de trabajo
- Se creó el entorno personal **DERECHO-A-TENER-DERECHOS-CLASSAD**, que permite `espaciosabiertos.org`
  (el entorno Default no lo permitía).

### Pruebas
- Se jugaron los 7 casos de corrido en un navegador sin interfaz: sin errores, y cada caso muestra el video
  y los PDF de su episodio.
- **Pendiente de probar en el sitio publicado:** que los videos se reproduzcan y que los PDF abran
  (desde el entorno de trabajo no se pudo comprobar).

---

## Rediseño visual tipo juego (5 de noviembre de 2026, segunda parte)

### Look más inmersivo
- Avatares ilustrados para las 7 personas (dibujados en SVG dentro de la app, sin imágenes externas).
  Se ven preocupados mientras esperan y contentos cuando se resuelve su caso.
- Una escena dibujada para cada lugar (oficina, universidad, municipio, égida, apartamento, hospital,
  centro de salud) detrás de las pistas.
- Un ícono propio para cada derecho (birrete, balanza, urna, maletín, corazón…).
- Barra superior con nivel, puntos (que saltan al sumar), barra de experiencia y las 7 insignias.
- Botones con relieve, entradas animadas y una portada con las 7 personas alrededor del escudo.

### Arreglos de la lista
- **Cada respuesta incorrecta explica por qué no es** (debajo de la opción misma, sin tener que bajar).
  Las explicaciones de los derechos están en `why` de cada caso; las de las acciones, en `fb`.
- **Nuevo mensaje más destacado:** tarjeta oscura que entra con rebote, celular que vibra, brillo amarillo,
  globito rojo con los casos que faltan y sonido de notificación.
- **Botón “☰ Pantallas” eliminado.**
- **Íconos de los derechos** en lugar de la letra del nombre. Arriba se ven en gris y se colorean al ganarlos.
  No se marca cuál es el del caso actual para no regalar la respuesta.
- **Íconos de arriba interactivos:** al tocarlos se abre la ficha del derecho (idea clave, video y PDF)
  sin salir de la pantalla. Si aún no se ha ganado, dice que está bloqueada.
- **Menos subir y bajar:** el video y los PDF pasaron a la ficha (botón “Aprende más”), la explicación de un
  error aparece junto a la opción, y cada pantalla de caso cabe casi completa.
- **Volver es fácil:** el avance se guarda en el dispositivo (`localStorage`). Si la persona sale o recarga,
  vuelve a la misma pantalla con “¡Qué bueno verte! Seguimos donde lo dejaste” y la opción de empezar de nuevo.
  La bandeja tiene arriba “Seguir con …”. El aviso del navegador al salir ahora solo sale si no se puede guardar.
- **Sonidos** (generados en el navegador, sin archivos): pista, correcto, error, caso resuelto, subir de nivel
  y mensaje nuevo. Botón 🔊/🔇 arriba. En Android también vibra al equivocarse.
- **Confeti** al resolver cada caso (más grande al terminar los 7), “+10 / +50” que flotan al sumar,
  sacudida al equivocarse, “⭐ ¡Perfecto!” si se acierta todo a la primera y racha “🔥 3 seguidas”.
- **Texto para invitar más humano:** tres mensajes para escoger (“De corazón”, “Un reto”, “Lo que aprendí”),
  que la persona puede editar. Se envía con el enlace de la app.

### Pruebas
- Se jugaron los 7 casos en un navegador sin interfaz, con respuestas incorrectas incluidas: sin errores.
- Se probó dentro de Streamlit: al recargar la página vuelve a la misma pantalla.

---

## Modo oscuro y logo de Espacios Abiertos (5 de noviembre de 2026, tercera parte)
- La app es **siempre oscura**, con los colores de la marca: azul `#003C69` y rosado `#E6007E`
  (botones principales en rosado). `.streamlit/config.toml` también quedó en oscuro.
- **Logo “¡ea!” arriba:** completo (“¡ea! espacios abiertos”) en la portada y en las pantallas de inicio,
  y solo “¡ea!” durante el juego para que quepan los puntos. Al tocarlo se vuelve a la bandeja.
- El logo se tomó de espaciosabiertos.org (`wp-content/uploads/logo.png` y el ícono del sitio). Para que se
  vea sobre fondo oscuro, el “ea” azul se pasó a blanco y los signos ¡ ! se quedaron en su rosado original.
  Va dentro de `app.py` (no depende de que el sitio esté arriba).
- La tarjeta de “Nuevo mensaje” ahora es rosada para que resalte sobre el fondo oscuro.

---

## Pendiente / ideas
- Comprobar videos y PDF en la app publicada.
- Teléfonos y enlaces de “Dónde pedir ayuda”: siguen “por verificar” en fuentes oficiales.
- Idea no hecha aún: certificado para compartir al completar los 7 casos.
- Opcional: quitar el botón “← Bandeja” de los casos si no se quiere volver a la bandeja.
