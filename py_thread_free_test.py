import threading
import time
import sys


def count_even():
    # CPU-bound workload
    for _ in range(100_000_000):
        pass


def count_odd():
    # CPU-bound workload
    for _ in range(100_000_000):
        pass


def main():
    print(f"Python version: {sys.version}")

    # Check for free-threading (PEP 703)
    # sys._is_gil_enabled() is available in 3.13+ builds with GIL support
    gil_status = "Unknown"
    if hasattr(sys, "_is_gil_enabled"):
        gil_status = "Enabled" if sys._is_gil_enabled() else "Disabled (Thread-Free)"
    print(f"GIL Status: {gil_status}")
    print("-" * 40)

    start_time = time.perf_counter()

    t1 = threading.Thread(target=count_even)
    t2 = threading.Thread(target=count_odd)  # Fix: Pass function reference

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"Total execution time: {duration:.4f} seconds")


if __name__ == "__main__":
    main()

# Python version: 3.14.2 (main, Jan 14 2026, 23:37:46) [Clang 21.1.4 ]
# GIL Status: Enabled
# ----------------------------------------
# Total execution time: 0.9342 seconds
# ###########################################################################
# Python version: 3.14.2 free-threading build (main, Jan 14 2026, 23:26:37) [Clang 21.1.4 ]
# GIL Status: Disabled (Thread-Free)
# ----------------------------------------
#  Total execution time: 0.5269 seconds
