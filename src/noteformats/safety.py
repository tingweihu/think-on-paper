"""Portable checkout and output-path guards for local generators.

These application guards do not provide operating-system isolation.
"""

from __future__ import annotations

import os
import stat
from pathlib import Path, PureWindowsPath

MARKERS = ("catalog-144.csv", "profiles/a5-draft.json", "src/noteformats/geometry.py")
REPARSE = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)


def _linked(path: Path) -> bool:
    if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
        return True
    try:
        return bool(getattr(path.stat(follow_symlinks=False), "st_file_attributes", 0) & REPARSE)
    except FileNotFoundError:
        return False


def assert_safe_workspace(root: Path) -> Path:
    """Require execution from an unlinked checkout with its own source markers."""
    root = Path(root).absolute()
    if _linked(root):
        raise RuntimeError("Project root is a link or junction")
    actual = root.resolve(strict=True)
    if Path.cwd().resolve(strict=True) != actual:
        raise RuntimeError(f"Run from the project root: {actual}")
    if not all((actual / name).is_file() for name in MARKERS):
        raise RuntimeError("Project markers are missing")
    stack = [actual]
    while stack:
        folder = stack.pop()
        with os.scandir(folder) as entries:
            for entry in entries:
                child = Path(entry.path)
                if _linked(child):
                    raise RuntimeError(f"Project contains a link or reparse point: {child}")
                if entry.is_dir(follow_symlinks=False):
                    stack.append(child)
    return actual


def safe_project_path(root: Path, relative: str | Path) -> Path:
    """Reject traversal, absolute paths and existing linked path components."""
    if _linked(Path(root)):
        raise ValueError("Linked output root")
    base = Path(root).resolve(strict=True)
    rel = Path(relative)
    windows = PureWindowsPath(str(relative))
    if (windows.anchor or windows.drive or ".." in windows.parts
            or rel.anchor or rel.drive or rel.is_absolute() or not rel.parts
            or any(part in ("..", "") for part in rel.parts)):
        raise ValueError(f"Unsafe relative output path: {relative}")
    target = base / rel
    current = base
    for part in rel.parts:
        current = current / part
        if _linked(current):
            raise ValueError(f"Linked output path: {current}")
    resolved = target.resolve(strict=False)
    if resolved != base and base not in resolved.parents:
        raise ValueError(f"Output escapes checkout: {relative}")
    return target
