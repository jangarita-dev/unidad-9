# Modelo de ROI · piloto de Pedidos Web

> Plantilla de la Unidad 10. Complétala con Claude Code en las etapas 1 y 2 y revísala tú.
> Fuente de datos: `docs/roi/datos-piloto.csv` (equipo Pedidos Web de 6 devs; semanas 1-6 antes, 7-12 con IA; datos ficticios) y tus entregables de las unidades 5 a 9.
> Regla: ningún número sin su fuente o su supuesto. Si un dato no está, escribe FALTA.

**Autor:** jangarita-dev · **Fecha:** 13-nov-2026 · **Horizonte:** 6 meses (26 semanas) · **Equipo:** 6 devs

## 1. Datos (etapa 1)

"Antes" = promedio de las semanas 1-6. "Con IA" = promedio de las semanas 9-12, sin contar las semanas 7-8, que fueron de adaptación (ver abajo). Entre paréntesis va el promedio de las semanas 7-12 completas.

| Dato | Antes | Con IA | Fuente (archivo y semanas) |
|---|---|---|---|
| Despliegues por semana | 2,0 | 3,5 (7-12: 3,0) | `datos-piloto.csv`, `despliegues`, semanas 1-6 frente a 9-12 |
| Lead time (días) | 6,58 | 4,38 (7-12: 5,17) | `datos-piloto.csv`, `lead_time_dias`, semanas 1-6 frente a 9-12 |
| Change fail rate | 42 % (5 fallas / 12 despliegues) | 21 % (3 / 14) (7-12: 33 %, 6 / 18) | `datos-piloto.csv`, `cambios_con_falla` ÷ `despliegues`, semanas 1-6 frente a 9-12 |
| Tiempo de recuperación (horas por falla) | 6,0 (30 h / 5 fallas) | 3,3 (10 h / 3 fallas) (7-12: 4,0) | `datos-piloto.csv`, `horas_recuperacion` ÷ `cambios_con_falla`, semanas 1-6 frente a 9-12 |
| Defectos escapados por semana | 2,0 | 1,0 (7-12: 1,5) | `datos-piloto.csv`, `defectos_escapados`, semanas 1-6 frente a 9-12 |
| Horas de retrabajo por semana | 12,0 | 8,75 (7-12: 10,67) | `datos-piloto.csv`, `horas_retrabajo`, semanas 1-6 frente a 9-12 |
| Horas ahorradas por semana (equipo) | 0 | 11,0 (7-12: 8,5) | `datos-piloto.csv`, `horas_ahorradas_equipo`, semanas 9-12 (semanas 1-6 = 0) |

> Muestra pequeña: un solo equipo de 6 devs, con 4 semanas estables con IA. Los datos son ficticios y esto es un ejercicio de método, no una prueba de productividad.

**Evidencia propia** (una línea por archivo: qué dato aporta):

- `docs/migracion/defectos-corregidos.md` (U5): **FALTA en este repo** (sigue siendo la plantilla). La versión completa está fuera del repo, en `D:/Vela/CAP/taller-u5/pedidos-web/docs/migracion/defectos-corregidos.md`. Aporta 1 defecto del legado corregido (D1 · R05, redondeo al peso): cambia 13 casos del golden master en ±1 o ±2 pesos, y la suma total pasa de 58.202.135 a 58.202.144 (+9). También registra 1 hallazgo no corregido (H1, umbrales del descuento por volumen) que afecta a 13 pedidos.
- `docs/calidad/registro-u6.md` (U6): **FALTA en este repo** (sigue siendo la plantilla). La versión completa está fuera del repo, en `D:/Vela/CAP/taller-u6/pedidos-web/docs/calidad/registro-u6.md`. Aporta 5 tests de borde para `CalculoTotales`; cada uno falló ante al menos una rotura hecha a mano, y se pasó de 74 a 79 tests en verde, con el CI en verde. La etapa 3 (la falla y su corrección) tampoco está completa ahí: FALTA.
- `docs/checklist-revision.md` (U7): FALTA (es la plantilla, sin completar en ninguna carpeta del curso).
- `docs/gobernanza/politica-ia.md` (U8): FALTA (es la plantilla, sin completar en ninguna carpeta del curso).
- `docs/adopcion/plan-evolucion.md` (U9): Pedidos Web está en nivel 4. Su tasa de aceptación va de 0,74 a 0,78 y 86 de 107 PR (80 %) se hicieron con Claude Code, según `docs/adopcion/analytics-ficticio.csv`, semanas 1-8. Ojo: es otra fuente ficticia, con otras semanas, y no se mezcla con `datos-piloto.csv`.

**Lo que veo en las semanas 7 y 8:** al llegar la IA el equipo empeoró antes de mejorar. Comparado con las semanas 1-6, subieron el change fail rate (75 %, 3 fallas en 4 despliegues), el retrabajo (14,5 h/semana) y los defectos escapados (2,5/semana), y solo se ahorraron 3,5 h/semana; el lead time casi no cambió (6,75 días). Es la curva de aprendizaje. Por eso se compara 1-6 con 9-12 y estas dos semanas se cuentan como costo de aprender (fuente: `datos-piloto.csv`, semanas 7-8).

## 2. Supuestos (etapa 2)

Tipos: **oficial** (publicado, con fecha) · **medido** (dato del piloto) · **estimado** (juicio del equipo, el más débil).

| Supuesto | Valor | Tipo | Fuente |
|---|---|---|---|
| Asiento | USD 25 por dev al mes (Team Standard, facturación mensual; incluye Claude Code) | oficial | claude.com/pricing, consultado el 13-nov-2026 |
| Capacitación | 10 h por dev (una sola vez) | estimado | Juicio del equipo: una jornada y media de práctica guiada |
| Curva de adopción | 10 h por dev (una sola vez) | estimado | Juicio del equipo, contrastado con lo medido: en las semanas 7-8 hubo 9 h extra de retrabajo y recuperación para todo el equipo (`datos-piloto.csv`). Se usa la cifra mayor por prudencia |
| Valor hora | USD 20 | estimado | Costo interno promedio por hora de dev; no hay un dato del piloto |
| Horas ahorradas (equipo), conservador | 8,5 h/semana | medido | `datos-piloto.csv`, promedio de las semanas 7-12 (incluye la curva) |
| Horas ahorradas (equipo), optimista | 3,5 h/semana las 2 primeras semanas y 11 h/semana las 24 siguientes | medido | `datos-piloto.csv`, semanas 7-8 y 9-12: el piloto se replica tal cual |
| Defectos evitados, conservador | 0,5 por semana (2,0 → 1,5) | medido | `datos-piloto.csv`, `defectos_escapados`, semanas 1-6 frente a 7-12 |
| Defectos evitados, optimista | 1,0 por semana (2,0 → 1,0); −0,5 las 2 primeras semanas | medido | `datos-piloto.csv`, semanas 1-6 frente a 9-12 y 7-8 |
| Costo de un defecto en producción | USD 120 (6 h × USD 20) | estimado | 6 h = recuperación por falla antes de la IA (`datos-piloto.csv`, semanas 1-6). Se toma como aproximación: no incluye el impacto en el cliente |

## 3. Costos

| Costo | Cálculo | USD |
|---|---|---|
| Asientos | 6 devs × USD 25 × 6 meses | 900 |
| Capacitación | 6 devs × 10 h × USD 20 | 1.200 |
| Curva de adopción | 6 devs × 10 h × USD 20 | 1.200 |
| **Total** | 900 + 1.200 + 1.200 | **3.300** |

Aprender cuesta más que los asientos: la capacitación y la curva suman el 73 % del costo.

## 4. Beneficios y escenarios

ROI = (beneficio − costo) / costo

| | Conservador | Optimista |
|---|---|---|
| Horas ahorradas × valor hora | 8,5 h × 26 sem = 221 h × USD 20 = **4.420** | (3,5 × 2 + 11 × 24) = 271 h × USD 20 = **5.420** |
| Defectos evitados × costo en producción | 0,5 × 26 = 13 defectos × USD 120 = **1.560** | (−0,5 × 2 + 1 × 24) = 23 defectos × USD 120 = **2.760** |
| **Beneficio total** | **5.980** | **8.180** |
| **ROI** | (5.980 − 3.300) / 3.300 = **81 %** | (8.180 − 3.300) / 3.300 = **148 %** |

**ROI entre 81 % y 148 % en 6 meses.** El retrabajo (de 12 a 8,75 h/semana) no se suma como beneficio aparte: es probable que ya esté dentro de las horas ahorradas que reporta el equipo, y sumarlo lo contaría dos veces.

## 5. Sensibilidad

**Supuesto que más pesa:** las horas ahorradas. Son el 74 % del beneficio conservador (4.420 de 5.980) y salen de lo que reporta el propio equipo, en solo 6 semanas.

| Si… | Cálculo | ROI |
|---|---|---|
| El ahorro es la mitad del conservador | 2.210 + 1.560 = 3.770 → (3.770 − 3.300) / 3.300 | **14 %** |
| El ahorro y los defectos evitados son la mitad del conservador | 2.210 + 780 = 2.990 → (2.990 − 3.300) / 3.300 | **−9 %** |

Si el ahorro real es la mitad de lo medido, el ROI apenas queda positivo. Hay que seguir midiendo las horas ahorradas antes de escalar.

## 6. Punto de equilibrio (Tu reto)

<Escríbelo tú: qué despejas, el resultado y una línea para la gerencia.>

## 7. Limitaciones

- Los datos son ficticios y la muestra es pequeña: este ROI es un ejercicio de método.
- Un solo equipo (6 devs) y 6 semanas con IA, de las cuales solo 4 son estables: no hay estacionalidad ni equipos de control.
- El valor hora, la capacitación y el costo de un defecto son estimados: no hay un dato oficial ni medido para ellos.
- Las horas ahorradas las reporta el mismo equipo y no hay una medición independiente.
- No incluye costos de uso por encima del asiento, ni el tiempo del champion y del senior multiplicador.
