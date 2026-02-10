def handle_archive_access(filename: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            content = file.read()
        print(f"SUCCESS: Archive recovered - \"{content.strip()}\"")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unknown system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_archive_access("lost_archive.txt")
    handle_archive_access("classified_vault.txt")
    handle_archive_access("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
