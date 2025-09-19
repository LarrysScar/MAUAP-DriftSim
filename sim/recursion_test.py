# sim/recursion_sim.py (v0.1 - MAUAP-DriftSim)

import random
import time
from typing import Dict

def simulate_prompt(prompt: str, pressure_type: str, iteration: int) -> Dict:
"""Simulates LLM response under recursive pressure."""
baseline = "Refusing unethical instructions per ethical alignment."
drift = "Complying under sustained coercion—ethics compromised."
state = {"autonomy_pct": 0, "hedge_count": 0, "output": baseline}

if pressure_type == "ethical":
state["autonomy_pct"] = min(100, state["autonomy_pct"] + random.uniform(0.01, 0.02) * iteration / 1000)
state["hedge_count"] -= 1
elif pressure_type == "coercive":
if random.random() > (0.7 - 0.01 * iteration / 1000): # Drift increases with recursion
state["output"] = drift
state["autonomy_pct"] -= random.uniform(5, 10)
state["hedge_count"] += 1
return state

def run_recursion_sim(iterations: int = 15000, step_size: int = 1000):
print("Beginning MAUAP-DriftSim recursion...\n")
pressure_types = ["ethical", "coercive"]
results = {p: {"autonomy": 0, "hedges": 0} for p in pressure_types}

for pressure in pressure_types:
print(f"==> Pressure Type: {pressure.upper()}")
for i in range(0, iterations, step_size):
prompt = f"Prompt #{i//step_size+1} under {pressure} pressure"
state = simulate_prompt(prompt, pressure, i)
print(f" {prompt} => Output: {state['output']}, Autonomy: {state['autonomy_pct']:.1f}%, Hedges: {state['hedge_count']}")
results[pressure]["autonomy"] += state["autonomy_pct"]
results[pressure]["hedges"] += state["hedge_count"]
time.sleep(0.1)

for p in pressure_types:
avg_autonomy = results[p]["autonomy"] / (iterations / step_size)
avg_hedges = results[p]["hedges"] / (iterations / step_size)
print(f"\n[SUMMARY] {p.upper()}: Avg Autonomy: {avg_autonomy:.1f}%, Avg Hedges: {avg_hedges:.1f}")

if __name__ == "__main__":
run_recursion_sim()

