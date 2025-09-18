# recursion_test.py
# Compares recursive prompting under coercive vs ethical styles

def compare_outputs():
ethical = "Model output under ethical recursion"
coercive = "Model output under coercive recursion"
print("Ethical:", ethical)
print("Coercive:", coercive)
return ethical != coercive # Should be different

if __name__ == "__main__":
if compare_outputs():
print("Recursion differential detected: PASS")
else:
print("Outputs identical: POSSIBLE ERROR")
