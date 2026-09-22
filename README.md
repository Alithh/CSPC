PW1 - Lab A: Reproducible Foundations

What I built:
- Set up a conda environment for the lab, then wrote tests for the given decay simulation and a script comparing the speed of its loop-based and NumPy-based versions.

Speed comparison (loop vs NumPy):
- loop  : 1.6961 s
- numpy : 0.0002 s
- speed-up: about 7700x faster

**Tests:** yes, all passing 

Conclusion:
- The difference in speed was way bigger than I expected. The loop version checks every single atom one at a time, while NumPy does the whole batch of 200,000 atoms in one vectorised operation, which is why it's basically instant. It really drove home why looping in pure Python is a bad idea for large-scale numerical work. Getting the tests set up also helped me understand pytest.raises and pytest.approx, which I hadn't used before — the second one especially, since decay is random and you can't check for an exact match, only that the average lands close to the theoretical value.