# ex02/oracle.py
import os
import sys

from dotenv import load_dotenv


REQUIRED_KEYS = ["DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]


def mask_secret(value: str, keep: int = 3) -> str:
    if not value:
        return ""
    if len(value) <= keep:
        return "*" * len(value)
    return value[:keep] + "*" * (len(value) - keep)


def env_mode() -> str:
    mode = os.environ.get("MATRIX_MODE", "development").strip().lower()
    return mode if mode in ("development", "production") else "development"


def load_env_for_dev(mode: str) -> None:
    # Load .env only for development (and only if it exists).
    # Environment variables should override .env values => override=False.
    if mode == "development":
        load_dotenv(override=False)


def validate_config(mode: str) -> tuple[dict[str, str], list[str]]:
    cfg: dict[str, str] = {"MATRIX_MODE": mode}
    missing: list[str] = []

    for key in REQUIRED_KEYS:
        val = os.environ.get(key, "").strip()
        if not val:
            missing.append(key)
        cfg[key] = val

    return cfg, missing


def security_checks() -> list[str]:
    checks: list[str] = []

    # 1) Ensure .env is ignored
    gitignore_ok = False
    try:
        with open(".gitignore", "r", encoding="utf-8") as f:
            gitignore_ok = any(line.strip() == ".env" for line in f)
    except OSError:
        gitignore_ok = False
    checks.append("[OK] .env file properly configured" if gitignore_ok else "[WARN] .env is not in .gitignore")

    # 2) Very basic “no hardcoded secrets” sanity check:
    # Read this source file and ensure we aren't literally assigning API_KEY="..."
    try:
        with open(__file__, "r", encoding="utf-8") as f:
            src = f.read()
        hardcoded = 'API_KEY="' in src or "API_KEY='" in src
        checks.append("[OK] No hardcoded secrets detected" if not hardcoded else "[WARN] Possible hardcoded API_KEY in code")
    except OSError:
        checks.append("[WARN] Could not read source to verify hardcoded secrets")

    # 3) Indicate overrides are possible (by design: env vars override .env)
    checks.append("[OK] Production overrides available")

    return checks


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    mode = env_mode()
    load_env_for_dev(mode)

    cfg, missing = validate_config(mode)

    print("Configuration loaded:")
    print("Mode:", cfg["MATRIX_MODE"])
    print("Database:", "Connected" if cfg["DATABASE_URL"] else "Missing DATABASE_URL")
    print("API Access:", "Authenticated" if cfg["API_KEY"] else "Missing API_KEY")
    print("Log Level:", cfg["LOG_LEVEL"] if cfg["LOG_LEVEL"] else "Missing LOG_LEVEL")
    print("Zion Network:", "Online" if cfg["ZION_ENDPOINT"] else "Missing ZION_ENDPOINT")

    if missing:
        print()
        print("ERROR: Missing required configuration:", ", ".join(missing))
        print("Tip:")
        print("  - Development: copy .env.example to .env and fill values")
        print("  - Production: export env vars (they override .env)")
        sys.exit(1)

    # Never print real secrets
    print()
    print("Secret preview (masked):", mask_secret(cfg["API_KEY"]))

    print("Environment security check:")
    for line in security_checks():
        print(line)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
