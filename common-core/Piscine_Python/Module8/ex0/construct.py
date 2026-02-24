# ex0/construct.py
import os
import site
import sys


def in_virtual_env() -> bool:
    """
    Detect venv without extra imports.
    Works for venv/virtualenv.
    """
    # virtualenv sets sys.real_prefix; venv uses base_prefix != prefix
    if hasattr(sys, "real_prefix"):
        return True
    if getattr(sys, "base_prefix", sys.prefix) != sys.prefix:
        return True
    # Common env var used by activation scripts
    if os.environ.get("VIRTUAL_ENV"):
        return True
    return False


def safe_get_site_packages() -> list[str]:
    try:
        paths = site.getsitepackages()  # may fail in some restricted builds
        return [str(p) for p in paths]
    except Exception:
        return []


def main() -> None:
    is_venv = in_virtual_env()
    print("MATRIX STATUS:", "Welcome to the construct" if is_venv else "You're still plugged in")
    print("Current Python:", sys.executable)

    venv_name = None
    venv_path = None
    if is_venv:
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        venv_name = os.path.basename(venv_path.rstrip(os.sep))

    print("Virtual Environment:", venv_name if is_venv else "None detected")

    if not is_venv:
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")
        print("Then run this program again.")
        print()
    else:
        print("Environment Path:", venv_path)
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()

    # Show package locations (difference between global vs venv will be visible)
    site_pkgs = safe_get_site_packages()
    user_site = None
    try:
        user_site = site.getusersitepackages()
    except Exception:
        user_site = None

    print("Package locations:")
    if site_pkgs:
        for p in site_pkgs:
            print("-", p)
    else:
        print("- (site.getsitepackages() unavailable on this system)")

    if user_site:
        print("User site-packages:", user_site)


if __name__ == "__main__":
    main()