"""Entry point: python -m src.ai_failure_api  or  ai-failure-api"""
import sys

try:
    import uvicorn
except ImportError:
    raise SystemExit(
        "uvicorn is required. Install with: pip install 'ai-failure-periodic-table[api]'"
    )


def main() -> None:
    uvicorn.run(
        "src.ai_failure_api.server:app",
        host="0.0.0.0",
        port=8000,
        reload="--reload" in sys.argv,
    )


if __name__ == "__main__":
    main()
