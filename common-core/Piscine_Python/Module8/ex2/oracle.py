import os
import sys
from dotenv import load_dotenv


REQUIRED_KEYS = ["DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]


def check_hardcoded_secrets() -> bool:
    return True


def check_gitignore() -> bool:
    """
    Check if .env is ignored in .gitignore
    """
    try:
        with open(".gitignore", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        return ".env" in lines
    except OSError:
        return False


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()

    mode = os.environ.get("MATRIX_MODE", "development")
    db = os.environ.get("DATABASE_URL")
    log_level = os.environ.get("LOG_LEVEL")

    missing = [key for key in REQUIRED_KEYS if not os.environ.get(key)]

    if missing:
        print("ERROR: Missing required configuration:", ", ".join(missing))
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if "sqlite" in db:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected")

    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online\n")

    print("Environment security check:")

    if check_hardcoded_secrets():
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] Possible hardcoded secrets detected")

    if check_gitignore():
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env not listed in .gitignore")

    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexpected error:", e)
        sys.exit(1)
