# ex01/loading.py
import importlib
import sys


def try_import(name: str):
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def print_install_help(missing: list[str]) -> None:
    print("Missing dependencies:", ", ".join(missing))
    print()
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Or install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def package_version(mod) -> str:
    return getattr(mod, "__version__", "unknown")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    pandas = try_import("pandas")
    numpy = try_import("numpy")
    matplotlib = try_import("matplotlib")
    requests = try_import("requests")  # optional

    missing = []
    if pandas is None:
        missing.append("pandas")
    if numpy is None:
        missing.append("numpy")
    if matplotlib is None:
        missing.append("matplotlib")

    if missing:
        for name in missing:
            print(f"[MISSING] {name}")
        print()
        print_install_help(missing)
        sys.exit(1)

    # Safe: these exist now
    plt = try_import("matplotlib.pyplot")
    if plt is None:
        print("[MISSING] matplotlib.pyplot (broken matplotlib install?)")
        print_install_help(["matplotlib"])
        sys.exit(1)

    print(f"[OK] pandas ({package_version(pandas)}) - Data manipulation ready")
    print(f"[OK] numpy ({package_version(numpy)}) - Numerical computations ready")
    print(f"[OK] matplotlib ({package_version(matplotlib)}) - Visualization ready")
    if requests is not None:
        print(f"[OK] requests ({package_version(requests)}) - Network access ready")
    else:
        print("[INFO] requests not installed (optional)")

    # Show environment clue to highlight pip vs Poetry: where python runs from
    print("Python executable:", sys.executable)
    print()

    print("Analyzing Matrix data...")
    n_points = 1000
    print(f"Processing {n_points} data points...")

    # Simulated data
    rng = numpy.random.default_rng(42)
    time_idx = numpy.arange(n_points)
    signal = numpy.sin(time_idx / 50.0) + rng.normal(0, 0.25, size=n_points)
    anomaly = signal + (rng.random(n_points) < 0.02) * rng.normal(3.0, 0.5, size=n_points)

    df = pandas.DataFrame(
        {"t": time_idx, "signal": signal, "anomaly_signal": anomaly}
    )
    df["rolling_mean"] = df["anomaly_signal"].rolling(window=25, min_periods=1).mean()

    print("Generating visualization...")
    plt.figure()
    plt.plot(df["t"], df["anomaly_signal"])
    plt.plot(df["t"], df["rolling_mean"])
    plt.title("Matrix Signal (with rolling mean)")
    plt.xlabel("t")
    plt.ylabel("value")
    plt.tight_layout()

    out_path = "matrix_analysis.png"
    plt.savefig(out_path)
    print("Analysis complete!")
    print(f"Results saved to: {out_path}")


if __name__ == "__main__":
    main()
