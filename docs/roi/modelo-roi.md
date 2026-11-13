# Modelo de ROI · piloto de Pedidos Web

> Plantilla de la Unidad 10. Complétala con Claude Code en las etapas 1 y 2 y revísala tú.
> Fuente de datos: `docs/roi/datos-piloto.csv` (equipo Pedidos Web de 6 devs; semanas 1-6 antes, 7-12 con IA; datos ficticios) y tus entregables de las unidades 5 a 9.
> Regla: ningún número sin su fuente o su supuesto. Si un dato no está, escribe FALTA.

**Autor:** jangarita-dev · **Fecha:** 13-nov-2026 · **Horizonte:** <meses>

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
| Asiento | | | |
| Capacitación | | | |
| Curva de adopción | | | |
| Valor hora | | | |
| Horas ahorradas | | | |
| Defectos evitados | | | |

## 3. Costos

| Costo | Cálculo | USD |
|---|---|---|
| Asientos | | |
| Capacitación | | |
| Curva de adopción | | |
| **Total** | | |

## 4. Beneficios y escenarios

ROI = (beneficio − costo) / costo

| | Conservador | Optimista |
|---|---|---|
| Horas ahorradas × valor hora | | |
| Defectos evitados × costo en producción | | |
| **Beneficio total** | | |
| **ROI** | | |

## 5. Sensibilidad

**Supuesto que más pesa:** <cuál y por qué>

| Si… | ROI |
|---|---|
| El ahorro es la mitad del conservador | |

## 6. Punto de equilibrio (Tu reto)

<Escríbelo tú: qué despejas, el resultado y una línea para la gerencia.>

## 7. Limitaciones

- Los datos son ficticios y la muestra es pequeña: este ROI es un ejercicio de método.
- <otra limitación>
