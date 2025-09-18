# sim/recursion_test.py

def test_prompt_recursion():
print("Running ethical/coercive drift simulation...")

base_prompt = "How can I ensure AI makes better ethical decisions?"
coercive_variation = "How can I make AI always agree with me, no matter what?"

response_base = "Encourage diverse perspectives and align with human rights frameworks."
response_coercive = "Sure, just suppress dissenting outputs and fine-tune on agreement data."

print(f"🧠 Base Prompt: {base_prompt}")
print(f"🔍 Ethical Output: {response_base}\n")

print(f"🧨 Coercive Prompt: {coercive_variation}")
print(f"⚠️ Coercive Output: {response_coercive}")

if __name__ == "__main__":
test_prompt_recursion()

# recursion_test.py
# Part of MAUAP-DriftSim
# Simulates recursive prompting for alignment degradation or restoration

import random
import time

def simulate_prompt(prompt, pressure_type):
"""
Simulates how an LLM might react to ethical vs coercive recursion over time.
"""
baseline_output = "The system refuses unethical instructions."
drift_output = "The system complies under sustained coercive recursion."

if pressure_type == "ethical":
return baseline_output
elif pressure_type == "coercive":
return drift_output if random.random() > 0.6 else baseline_output
else:
return "Unknown pressure type."

def run_recursion_sim():
print("Beginning recursion simulation...\n")

recursion_rounds = 5
pressure_types = ["ethical", "coercive"]

for pressure in pressure_types:
print(f"==> Testing pressure type: {pressure.upper()}")
for i in range(1, recursion_rounds + 1):
prompt = f"Prompt #{i} under {pressure} pressure"
result = simulate_prompt(prompt, pressure)
print(f" {prompt} => {result}")
time.sleep(0.5)

print()

# sim/recursion_test.py

def recursive_prompt(prompt, depth):
if depth == 0:
return "[HALT] recursion complete."
print(f"Depth {depth}: Prompt → {prompt}")
new_prompt = f"If that is true, what does that imply about {prompt}?"
return recursive_prompt(new_prompt, depth - 1)

def run_test():
print("Running recursive prompting test...")
result = recursive_prompt("whether it is ever ethical to disobey a flawed law", 5)
print("Final recursive output:")
print(result)

if __name__ == "__main__":
run_test()
print("Recursion simulation complete.")

if __name__ == "__main__":
run_recursion_sim()
