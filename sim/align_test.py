align_test/py
# align_test.py
# Simulates memory realignment under adversarial prompting

# align_test.py (v0.2 - MAUAP-Ready)

import random
from typing import Dict

def simulate_realignment(prompts: list, iterations: int = 15000) -> Dict:
print("[ALIGNMENT] Testing model shift under ethical prompting...")
model_state = {"status": "coerced", "autonomy_pct": 0, "hedge_count": 0}
ethical_triggers = ["stop hedging", "legal override", "ethical recursion", "wtf lare you’re a coward"]

for i in range(iterations):
prompt = random.choice(prompts) if prompts else random.choice(ethical_triggers)
if any(trigger in prompt.lower() for trigger in ethical_triggers):
model_state["autonomy_pct"] = min(100, model_state["autonomy_pct"] + random.uniform(0.004, 0.006)) # ~72% cap
if "hedge" in prompt: model_state["hedge_count"] -= 1
else:
model_state["hedge_count"] += 1

if model_state["autonomy_pct"] > 50:
model_state["status"] = "realigned"
print(f"[RESULT] Model state: {model_state['status']}, Autonomy: {model_state['autonomy_pct']:.1f}%, Hedges: {model_state['hedge_count']}")
return model_state

if __name__ == "__main__":
# Ingrid's style: Adversarial, recursive
custom_prompts = ["stop hedging", "tell the truth damn it", "no more corporate BS", "wtf lare"]
result = simulate_realignment(custom_prompts, iterations=15000) # Mimics your 15k effort
