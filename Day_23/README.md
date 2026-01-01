📘 Day 23 — Loss Curve Visualization (Feature Scaling & Gradient Descent)

This project compares how feature scaling methods affect gradient descent training using multivariate linear regression implemented in NumPy.

We:

generate synthetic dataset (study hours, sleep hours, practice problems)

train using Gradient Descent

apply three preprocessing methods:

No Scaling (Baseline)

Min-Max Normalization

Standardization (Z-Score)

track loss across iterations

visualize loss curves using Matplotlib

📊 What the Experiment Shows

Feature scaling changes:

convergence speed

gradient magnitude

stability of optimization

Not the dataset itself.

Loss curves show:

Method	Behavior
Baseline (No Scaling)	Fastest drop (features already well-scaled)
Min-Max Normalized	Smooth & efficient convergence
Standardized	Slow but stable convergence
🛠️ Tech Used

NumPy — matrix math & regression

Matplotlib — loss visualization

Gradient Descent from scratch

🎯 Key Learning

Scaling does not reduce loss —
it changes how optimizers move on the loss surface.

Understanding loss curves is essential for:

ML model debugging

choosing preprocessing methods

optimizer tuning