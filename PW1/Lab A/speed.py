"""
Compare the speed of the pure-Python loop vs the NumPy vectorised
version of the decay simulation.
"""

import time
from decay import simulate, simulate_loop

N0 = 200_000
LAM = 0.4

start = time.perf_counter()
simulate_loop(N0, LAM)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, LAM)
numpy_time = time.perf_counter() - start

print(f"Loop  (pure Python): {loop_time:.4f} s")
print(f"NumPy (vectorised):  {numpy_time:.4f} s")
print(f"NumPy is {loop_time / numpy_time:.1f}x faster")