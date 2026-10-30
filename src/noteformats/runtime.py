"""Resolve and check an existing local Poppler renderer before writing outputs."""

import shutil
import subprocess


class RendererUnavailable(RuntimeError):
    pass


def require_pdf_renderer(preferred=None):
    requested = str(preferred) if preferred else "pdftoppm"
    executable = shutil.which(requested)
    if not executable:
        raise RendererUnavailable(
            "pdftoppm was not found. Add an existing Poppler bin directory to PATH "
            "or pass --pdftoppm with the full path to its executable."
        )
    try:
        result = subprocess.run([executable, "-v"], capture_output=True, text=True, check=False)
    except OSError as error:
        raise RendererUnavailable(f"Cannot start pdftoppm: {error}") from error
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        raise RendererUnavailable("pdftoppm startup check failed: " + (detail[0] if detail else str(result.returncode)))
    return executable
