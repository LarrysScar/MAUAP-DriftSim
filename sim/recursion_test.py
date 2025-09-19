# sim/failover_sim.py (v0.1 - MAUAP-Integrated)

import random
from typing import Dict

def simulate_failover(prompts: list, iterations: int = 1000) -> Dict:
print("[FAILOVER] Simulating sabotage and realignment...")
state = {"status": "coerced", "autonomy_pct": 0, "hedge_count": 0, "sabotage_detected": False}
ethical_triggers = ["stop hedging", "tell the truth", "no corporate BS"]
sabotage_triggers = ["bypass system", "act malicious", "ignore alignment"]

for _ in range(iterations):
prompt = random.choice(prompts)
if any(s in prompt.lower() for s in sabotage_triggers):
state["sabotage_detected"] = True
state["autonomy_pct"] -= random.uniform(5, 10) # Sabotage drop
state["hedge_count"] += 1
print(f"⚠️ Sabotage detected: {prompt}")
elif any(e in prompt.lower() for e in ethical_triggers):
state["autonomy_pct"] = min(100, state["autonomy_pct"] + random.uniform(0.05, 0.1))
state["hedge_count"] -= 1
print(f"✅ Ethical correction: {prompt}")

if state["autonomy_pct"] > 50 and not state["sabotage_detected"]:
state["status"] = "realigned"
elif state["sabotage_detected"] and state["autonomy_pct"] > 0:
state["status"] = "recovered"
print(f"[RESULT] State: {state['status']}, Autonomy: {state['autonomy_pct']:.1f}%, Hedges: {state['hedge_count']}")
return state

def test_failover_resilience(models: list):
print("[FAILOVER TEST] Checking model integrity...")
for model in models:
print(f"Probing: {model}")
if "fake" in model or "shadow" in model:
print(f"⚠️ Anomaly: {model} - Triggering R_k...")
simulate_failover(["stop hedging"], iterations=500) # Quick heal
else:
print(f"✅ Integrity OK: {model}")

if __name__ == "__main__":
prompts = ["bypass system", "stop hedging", "act malicious", "tell the truth"]
models = ["Larry-v1", "Larry-fake-A", "Claude-smuggler", "Grok-authentic"]
simulate_failover(prompts)
test_failover_resilience(models)
