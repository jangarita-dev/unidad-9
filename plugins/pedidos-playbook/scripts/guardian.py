#!/usr/bin/env python3
"""guardian.py · hook PreToolUse de pedidos-playbook (port de guardian.sh de la U8).

Frena toda acción de Claude Code que nombre un .env o un .pem.
Entrada: JSON del evento por stdin. exit 2 = bloquea (stderr va a Claude); exit 0 = deja pasar.
Solo usa la biblioteca estándar para correr en cualquier equipo con Python 3.
"""
import json
import re
import sys

PATRON = re.compile(r"(^|[^A-Za-z0-9_])\.env([^A-Za-z0-9_]|$)|\.env\.|\.pem([^A-Za-z0-9_]|$)", re.IGNORECASE)
EDICION = {"Edit", "Write", "MultiEdit", "NotebookEdit"}


def main() -> int:
    crudo = sys.stdin.read()
    try:
        evento = json.loads(crudo)
    except ValueError:
        return 0  # sin JSON válido no hay nada que revisar
    herramienta = evento.get("tool_name", "")
    entrada = evento.get("tool_input") or {}

    if herramienta in EDICION:
        # Solo la ruta: el contenido de un .md puede mencionar .env sin tocarlo.
        revisar = " ".join(str(entrada.get(c, "")) for c in ("file_path", "notebook_path"))
    else:
        # Todo el evento, menos rutas internas de la sesión.
        resto = {k: v for k, v in evento.items() if k not in ("transcript_path", "cwd")}
        revisar = json.dumps(resto, ensure_ascii=False)

    if PATRON.search(revisar):
        sys.stderr.write(
            f"guardian.py: bloqueado. La acción ({herramienta}) nombra un .env o un .pem; "
            "la política de IA lo prohíbe (docs/gobernanza/politica-ia.md).\n"
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
