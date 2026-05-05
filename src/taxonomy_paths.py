"""
Filesystem locations for bundled taxonomy JSON (wheel-safe).

The `src` directory is the Python package root both in a git checkout
(…/repo/src) and when installed from PyPI (…/site-packages/src).
"""

from __future__ import annotations

from pathlib import Path


def package_src_root() -> Path:
    """Directory that contains `data_loader.py`, `data/`, and `ai_failure_mcp/`."""
    return Path(__file__).resolve().parent


def bundled_data_dir() -> Path:
    """Directory with failures.json, search_index.json, and related ship artifacts."""
    return package_src_root() / "data"


def default_filesystem_root() -> Path:
    """
    Default anchor for resolving relative document paths (MCP).

    In a checkout this is the repository root (directory that contains
    pyproject.toml). When installed as a wheel, the parent of the package
    is site-packages, so we fall back to the process current working directory.
    """
    pkg = package_src_root()
    parent = pkg.parent
    if (parent / "pyproject.toml").exists():
        return parent.resolve()
    return Path.cwd().resolve()
