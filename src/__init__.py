"""
AI Failure Periodic Table Classifier

Classifies any AI failure or behavior against the 343-class
AI Failure Periodic Table across 7 structural dimensions.
"""

from importlib.metadata import PackageNotFoundError, version as _pkg_version

try:
    __version__ = _pkg_version("ai-failure-periodic-table")
except PackageNotFoundError:
    __version__ = "0.0.0+local"
