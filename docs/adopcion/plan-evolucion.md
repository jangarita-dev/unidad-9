# Plan de evolución de la IA para una Business Unit

> Fuente de datos: `docs/adopcion/analytics-ficticio.csv` (4 equipos × 8 semanas, datos ficticios). Todas las cifras de este plan salen de ese archivo.

**BU:** Desarrollo de la distribuidora · **Autor:** jangarita-dev · **Fecha:** 13-nov-2026

## 1. Resumen para la gerencia

La BU tiene cuatro equipos en tres niveles distintos de madurez. Pedidos Web trabaja en nivel 4 (proceso AI-native): el 80 % de sus PR se hacen con Claude Code y acepta el 76 % de lo que propone. Bodega y Reportes están en nivel 2 por razones opuestas: Bodega usa mucho la herramienta pero acepta muy poco, y Reportes la usa a ratos. Facturacion está en nivel 1, casi sin uso. Proponemos instalar en los tres equipos `pedidos-playbook`, el plugin que empaqueta la forma de trabajar de Pedidos Web. Se haría con un piloto por equipo, un champion por equipo y una revisión mensual de indicadores.

## 2. Diagnóstico por equipo

Modelo de madurez del curso: 1 Uso a escondidas · 2 Uso individual · 3 Equipo con reglas · 4 Proceso AI-native · 5 Organización que mide y mejora.

| Equipo | Nivel | Evidencia 1 (indicador del CSV) | Evidencia 2 (indicador del CSV) |
|---|---|---|---|
| Pedidos Web | 4 · Proceso AI-native | Tasa de aceptación estable entre 0,74 y 0,78 las 8 semanas (promedio 0,76) | 86 de 107 PR con Claude Code (80 %), con 5 a 6 usuarios activos todas las semanas |
| Facturacion | 1 · Uso a escondidas | 0 a 1 usuario activo y 0 a 4 sesiones por semana (15 sesiones en total; las semanas 2 y 5 sin sesiones) | 1 PR con Claude Code de 71 PR totales (1 %) |
| Bodega | 2 · Uso individual | Es el equipo que más lo usa: 7 usuarios activos y entre 105 y 124 sesiones por semana (921 en total) | Su tasa de aceptación es la más baja, entre 0,11 y 0,17 (promedio 0,14), y solo 30 de 109 PR son con Claude Code (28 %) |
| Reportes | 2 · Uso individual | El uso es intermitente: 3 o 4 usuarios en las semanas 1, 3, 5 y 7, y 0 o 1 en las semanas 2, 4, 6 y 8 (la semana 4 sin sesiones) | Tasa de aceptación media, entre 0,50 y 0,58, y 18 de 49 PR con Claude Code (37 %) |

> Ningún indicador por sí solo decide el nivel. Bodega tiene el mayor uso de la BU, pero el más bajo nivel de aceptación: es una señal de alerta, no un éxito.

## 3. Objetivo por equipo para el próximo trimestre

| Equipo | Objetivo medible | Indicador que lo muestra |
|---|---|---|
| Pedidos Web | Mantener el nivel 4 y servir de piloto y referencia para el playbook | Tasa de aceptación ≥ 0,74 y ≥ 75 % de PR con Claude Code |
| Facturacion | Pasar a nivel 2: uso semanal sostenido con el playbook instalado | Usuarios activos ≥ 3 todas las semanas y 0 semanas sin sesiones |
| Bodega | Pasar a nivel 3: aceptar más de lo que genera, usando el revisor y las reglas compartidas | Tasa de aceptación de 0,14 a ≥ 0,40 sin bajar sesiones |
| Reportes | Pasar a nivel 3: uso constante, no solo en semanas alternas | Usuarios activos ≥ 3 en las 8 semanas y PR con Claude Code ≥ 50 % |

## 4. El playbook

`pedidos-playbook` es un plugin de Claude Code publicado en el marketplace `pedidos-jangarita-dev` (repositorio `jangarita-dev/unidad-9`). Trae:

| Pieza | Tipo | Para qué sirve |
|---|---|---|
| `revisor` | Subagente (U7) | Revisa los cambios con la lista de verificación del equipo antes del PR |
| `documentar-modulo` | Skill (U3) | Documenta un módulo con el formato común del equipo |
| `planificador-proyectos-web` | Skill | Planifica y documenta épicas, specs y decisiones |
| Guardián (`guardian.py`) | Hook PreToolUse (U8) | Bloquea cualquier acción que nombre un `.env` o un `.pem` |
| `claude-academy` | Servidor MCP de solo lectura | Busca cursos y guías de Claude Academy sin salir de Claude Code |
| `plantillas/AGENTS.md` y `plantillas/REVIEW.md` | Plantillas | Se copian a cada repositorio y se adaptan (no se instalan) |

Instalación en otro equipo, desde Claude Code:

```
/plugin marketplace add jangarita-dev/unidad-9
/plugin install pedidos-playbook@pedidos-jangarita-dev
```

Los equipos reciben las actualizaciones cuando cambia el campo `version`, con `/plugin marketplace update pedidos-jangarita-dev`. Los secretos no viajan en el plugin.

## 5. Hoja de ruta a 6 y 12 meses

| Hito | Mes | Equipo | Champion | Cómo sabemos que se cumplió |
|---|---|---|---|---|
| Playbook 1.x instalado y validado como piloto | 1 | Bodega | Champion de Bodega, acompañado por el senior de Pedidos Web | Tasa de aceptación ≥ 0,25 en 4 semanas seguidas |
| Playbook instalado y pareo semanal con Pedidos Web | 2 | Facturacion | Champion de Facturacion | Usuarios activos ≥ 3 y 0 semanas sin sesiones durante 1 mes |
| Playbook instalado y AGENTS.md propio | 3 | Reportes | Champion de Reportes | Usuarios activos ≥ 3 todas las semanas durante 1 mes |
| Los cuatro equipos en nivel 3 | 6 | BU completa | Senior multiplicador | Los 4 equipos cumplen el objetivo trimestral de la sección 3 |
| Bodega y Reportes en nivel 4 (spec, plan, CI y revisión) | 9 | Bodega y Reportes | Champions de cada equipo | ≥ 60 % de PR con Claude Code y aceptación ≥ 0,60 |
| La BU decide con indicadores (nivel 5) | 12 | BU completa | Gerencia y senior multiplicador | Revisión mensual de indicadores con decisiones registradas |

El ciclo se repite para cada equipo: **estandarizar → medir → ajustar → escalar**.

## 6. Indicadores que vamos a seguir

| Indicador | Frecuencia | Quién lo revisa |
|---|---|---|
| Usuarios activos y sesiones | Semanal | Champion de cada equipo |
| Tasa de aceptación | Semanal | Champion de cada equipo y senior multiplicador |
| PR con Claude Code / PR totales | Mensual | Senior multiplicador |
| Líneas aceptadas (solo junto a la tasa de aceptación, nunca sola) | Mensual | Gerencia de la BU |

El panel Analytics de Claude Code (Team y Enterprise) lo revisan el Admin y el Owner una vez al mes con los champions.

## 7. Riesgos y próximos pasos

- Premiar el volumen (sesiones o líneas) en lugar del resultado → miramos siempre la tasa de aceptación y los PR junto con el uso.
- Imponer el playbook a todos al mismo tiempo → un equipo piloto por vez, empezando por Bodega.
- Licencias sin práctica en Facturacion → sesiones guiadas con el champion y pareo con Pedidos Web.
- Que el plugin quede desactualizado en los equipos → cada cambio se publica subiendo `version` y se anuncia a los champions.
- Filtración de secretos → el guardián bloquea `.env` y `.pem`, y los secretos nunca van dentro del plugin.

**Próximo paso:** instalar `pedidos-playbook` en Bodega esta semana y revisar su tasa de aceptación en 4 semanas.
