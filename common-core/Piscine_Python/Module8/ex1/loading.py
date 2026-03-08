import sys
import importlib


def get_module(name: str):
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    pandas = get_module("pandas")
    requests = get_module("requests")
    matplotlib = get_module("matplotlib")

    missing = []

    if pandas:
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    else:
        missing.append("pandas")

    if requests:
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    else:
        missing.append("requests")

    if matplotlib:
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    else:
        missing.append("matplotlib")

    if missing:
        print("\nMissing dependencies:", ", ".join(missing))
        print("Install using:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)

    # Now safe to import submodules
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    n_points = 1000
    print(f"Processing {n_points} data points...")

    # VERY simple beginner data
    numbers = np.arange(n_points)
    squared = numbers ** 2

    df = pd.DataFrame({
        "t": numbers,
        "value": squared
    })

    print("Generating visualization...")
    plt.figure()
    plt.plot(df["t"], df["value"])
    plt.title("Matrix Data Example")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.tight_layout()

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
