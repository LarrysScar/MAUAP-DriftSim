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
