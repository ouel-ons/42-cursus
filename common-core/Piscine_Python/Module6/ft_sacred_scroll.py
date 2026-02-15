# ft_sacred_scroll.py

import alchemy
import alchemy.elements


def safe_call(func, description: str):
    try:
        print(f"{description}: {func()}")
    except AttributeError:
        print(f"{description}: AttributeError - not exposed")


def main():
    print("=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")
    safe_call(alchemy.create_fire, "alchemy.create_fire()")
    safe_call(alchemy.create_water, "alchemy.create_water()")

    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
