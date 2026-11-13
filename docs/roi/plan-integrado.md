# Plan integrado de adopción de IA · Pedidos Web

**Para:** Gerencia general · **Autor:** jangarita-dev · **Fecha:** 13-nov-2026

**Recomendación:** extender la forma de trabajar de Pedidos Web a un equipo más (Bodega) durante 3 meses y medir cada semana las horas ahorradas. Decisión antes del 20-nov-2026.

*Preparado con apoyo de IA; cifras verificadas por jangarita-dev.*

## Página 1 · Informe ejecutivo

### 1. Problema
Terminó el piloto de 12 semanas en Pedidos Web y hay que decidir si esta forma de trabajar con IA se extiende a otros equipos. Hay que decidir ahora porque los demás equipos ya usan la herramienta, cada uno a su manera y sin reglas comunes.

### 2. Qué se hizo
Un equipo de 6 desarrolladores trabajó 6 semanas como siempre y 6 semanas con Claude Code, con reglas, revisiones y controles comunes. Comparamos lo que entregaron en los dos períodos.

### 3. Resultados
- **Más rápido:** un cambio tarda 4,4 días en llegar a producción, antes tardaba 6,6. Se despliega 3,5 veces por semana, antes 2.
- **Más estable:** fallan el 21 % de los despliegues (antes el 42 %) y escapa 1 defecto por semana (antes 2).
- **Costo de aprender:** las 2 primeras semanas con IA fueron peores que antes. Lo contamos como costo.
- **ROI a 6 meses: entre 81 % y 148 %** (costo USD 3.300 por 6 devs). Lo que más lo mueve son las horas ahorradas, que reporta el propio equipo: si son la mitad, el ROI baja a 14 %.

### 4. Recomendación
Extender la forma de trabajar de Pedidos Web a un equipo más (Bodega) durante 3 meses, con un costo de referencia de USD 3.300 por cada 6 devs en 6 meses, y decidir el resto de la BU con esos datos.

### 5. Próximo paso
El champion de Bodega y el senior de Pedidos Web instalan `pedidos-playbook` en Bodega la semana del 23-nov-2026. A las 4 semanas presentan a la gerencia las horas ahorradas y la tasa de fallas.

*Preparado con apoyo de IA; cifras verificadas por jangarita-dev.*

<div style="page-break-before: always"></div>

## Anexo

No repite los entregables: los cita.

### Roadmap
- **3 meses:** el playbook está instalado en Bodega (mes 1), Facturacion (mes 2) y Reportes (mes 3), cada equipo con su champion.
- **6 meses:** los cuatro equipos llegan al nivel 3 (equipo con reglas).
- **12 meses:** la BU decide con indicadores (nivel 5).

Respaldo: `docs/adopcion/plan-evolucion.md` (U9), sección 5.

### Indicadores
| Indicador | Hoy con IA (semanas 9-12) | Meta para los equipos nuevos |
|---|---|---|
| Lead time | 4,38 días | Bajar respecto de su propia línea base |
| Change fail rate | 21 % | No superar su línea base después de la curva de adopción |
| Defectos escapados | 1,0 por semana | Bajar respecto de su línea base |
| Horas ahorradas (equipo) | 11 h por semana | Medirlas cada semana: es el supuesto que más pesa |

Respaldo: `docs/roi/modelo-roi.md` (sección 1). En este repo, `docs/calidad/registro-u6.md` (U6) y `docs/checklist-revision.md` (U7) siguen siendo plantillas: FALTA.

### Gobernanza
Los controles que se llevan a los otros equipos dentro de `pedidos-playbook`:

- El guardián bloquea toda acción que nombre un `.env` o un `.pem`.
- El subagente revisor revisa los cambios antes de cada PR, con las reglas de `REVIEW.md`.
- Las plantillas de `AGENTS.md` y `REVIEW.md` se copian a cada repositorio.

Respaldo: `plugins/pedidos-playbook/` (U9). `docs/gobernanza/politica-ia.md` (U8) sigue siendo plantilla: FALTA.

### ROI
- **Supuestos clave:** asiento USD 25 por dev al mes (oficial); horas ahorradas y defectos evitados (medidos en el piloto); valor hora USD 20, capacitación y curva de 10 h por dev cada una, y USD 120 por defecto (estimados).
- **Escenarios:** costo de USD 3.300 frente a un beneficio de USD 5.980 (conservador) o USD 8.180 (optimista). El ROI queda entre 81 % y 148 %.
- **Sensibilidad:** si el ahorro es la mitad, el ROI es 14 %; si también los defectos evitados son la mitad, el ROI es −9 %.
- **Punto de equilibrio:** pendiente. Es el reto de la sección 6 del modelo.

Respaldo: `docs/roi/modelo-roi.md`. En este repo, `docs/migracion/defectos-corregidos.md` (U5) sigue siendo plantilla: FALTA.

### Evolución
| Equipo | Hoy | Meta a 6 meses |
|---|---|---|
| Pedidos Web | Nivel 4 · proceso AI-native | Nivel 4, y piloto de referencia |
| Bodega | Nivel 2 · uso individual | Nivel 3 |
| Reportes | Nivel 2 · uso individual | Nivel 3 |
| Facturacion | Nivel 1 · uso a escondidas | Nivel 3 |

Respaldo: `docs/adopcion/plan-evolucion.md` (U9), secciones 2 y 5.
