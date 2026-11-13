#!/usr/bin/env python3
"""html_a_pdf.py · Skill pdf-con-estilo.

Convierte un Markdown en PDF con assets/plantilla.html y Playwright (Chromium).
Uso: python html_a_pdf.py <entrada.md> [salida.pdf] [--marca "Texto de la portada"]
Requiere: pip install playwright markdown  y  python -m playwright install chromium
"""
import argparse
import html
import re
import sys
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

PLANTILLA = Path(__file__).resolve().parent.parent / "assets" / "plantilla.html"
EXTENSIONES = ["tables", "fenced_code", "sane_lists"]
PIE = ('<div style="font-size:8pt;color:#52606d;width:100%;text-align:center;">'
       '<span class="pageNumber"></span> / <span class="totalPages"></span></div>')


def separar(texto: str):
    """Devuelve (titulo, portada_md, cuerpo_md). La portada es lo que va entre el # y el primer ##."""
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.DOTALL)
    lineas = texto.splitlines()
    titulo = "Documento"
    inicio = 0
    for n, linea in enumerate(lineas):
        if linea.startswith("# "):
            titulo, inicio = linea[2:].strip(), n + 1
            break
    resto = lineas[inicio:]
    corte = next((n for n, linea in enumerate(resto) if linea.startswith("## ")), len(resto))
    return titulo, "\n".join(resto[:corte]).strip(), "\n".join(resto[corte:]).strip()


ETIQUETAS_HTML = {"a", "b", "br", "code", "details", "div", "em", "i", "img", "kbd", "p", "span",
                  "strong", "sub", "summary", "sup", "u"}


def proteger_marcadores(texto_md: str) -> str:
    """Muestra como texto los marcadores tipo <tu nombre>, que Markdown tomaría como HTML.

    No toca los bloques de código ni el código en línea: ahí Markdown ya los escapa.
    """
    def escapar(segmento: str) -> str:
        def cambiar(m):
            nombre = re.match(r"/?([A-Za-z][A-Za-z0-9]*)", m.group(1))
            if nombre and nombre.group(1).lower() in ETIQUETAS_HTML:
                return m.group(0)
            return "&lt;" + m.group(1) + "&gt;"
        return re.sub(r"<([^<>\n]+)>", cambiar, segmento)

    salida, en_bloque = [], False
    for linea in texto_md.splitlines():
        if linea.lstrip().startswith("```"):
            en_bloque = not en_bloque
        elif not en_bloque:
            partes = linea.split("`")
            linea = "`".join(escapar(p) if i % 2 == 0 else p for i, p in enumerate(partes))
        salida.append(linea)
    return "\n".join(salida)


def a_html(texto_md: str) -> str:
    return markdown.markdown(proteger_marcadores(texto_md), extensions=EXTENSIONES)


def construir_html(texto_md: str, marca: str) -> str:
    titulo, portada_md, cuerpo_md = separar(texto_md)
    return (PLANTILLA.read_text(encoding="utf-8")
            .replace("{{marca}}", html.escape(marca))
            .replace("{{titulo}}", html.escape(titulo))
            .replace("{{portada}}", a_html(portada_md))
            .replace("{{contenido}}", a_html(cuerpo_md)))


def main() -> int:
    parser = argparse.ArgumentParser(description="Convierte un Markdown en PDF con estilo.")
    parser.add_argument("entrada", type=Path)
    parser.add_argument("salida", type=Path, nargs="?")
    parser.add_argument("--marca", default="Desarrollo · Pedidos Web")
    args = parser.parse_args()
    if not args.entrada.is_file():
        print(f"No existe {args.entrada}", file=sys.stderr)
        return 1
    salida = args.salida or args.entrada.with_suffix(".pdf")
    documento = construir_html(args.entrada.read_text(encoding="utf-8"), args.marca)

    with sync_playwright() as pw:
        navegador = pw.chromium.launch()
        pagina = navegador.new_page()
        pagina.set_content(documento, wait_until="load")
        pagina.pdf(path=str(salida), format="A4", print_background=True, prefer_css_page_size=True,
                   display_header_footer=True, header_template="<span></span>", footer_template=PIE)
        navegador.close()

    paginas = len(re.findall(rb"/Type\s*/Page[^s]", salida.read_bytes()))
    print(f"PDF generado: {salida} ({paginas} páginas)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
