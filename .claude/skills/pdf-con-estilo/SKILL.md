---
name: pdf-con-estilo
description: "Convierte un documento Markdown del repo (plan, política, informe, diagnóstico) en un PDF con el diseño del equipo: portada, títulos y tablas legibles. Úsala cuando pidan pasar un .md a PDF, generar o regenerar un PDF para la gerencia, imprimir o entregar un documento, aunque no nombren la Skill."
---

# PDF con estilo

El Markdown pone el contenido y `assets/plantilla.html` pone el diseño. Si cambias el Markdown, el PDF sale igual de bien. **No toques el CSS para que un documento en particular se vea bien.** Si hace falta, la corrección va en la plantilla y sirve para todos los documentos.

## Pasos

1. Confirma la ruta del `.md` de entrada y decide la salida. Por defecto, el PDF lleva el mismo nombre y queda en la misma carpeta.
2. Revisa que el Markdown tenga un `# Título`. Todo lo que está entre el título y el primer `##` sale en la portada.
3. Ejecuta el script desde la raíz del repo:

   ```bash
   py -3 .claude/skills/pdf-con-estilo/scripts/html_a_pdf.py <entrada.md> [salida.pdf]
   ```

   En macOS o Linux usa `python3`. Requiere `pip install playwright markdown` y `python -m playwright install chromium`.
4. Verifica el resultado. El script imprime la ruta del PDF y su número de páginas. Abre el PDF y revisa la portada, los títulos y que las tablas no se corten.
5. Dile al usuario qué archivo generaste. No hagas commit: lo hace una persona.

## Reglas

- No cambies el contenido del Markdown para "arreglar" el PDF sin preguntar.
- Los comentarios HTML (`<!-- -->`) del Markdown no salen en el PDF.
- El PDF se imprime con los colores de fondo (`print_background`). Si salen en blanco, revisa que la plantilla mantenga `print-color-adjust: exact`.
