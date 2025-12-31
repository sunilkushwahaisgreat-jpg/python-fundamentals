📌 Linear Regression From Scratch — Feature Scaling Experiments

This project implements Linear Regression using Gradient Descent in NumPy, without using ML libraries.

The goal is to understand learning behavior, not just get accuracy — similar to how ML engineers study models through experiments.

The model is tested under three conditions:

1️⃣ No Feature Scaling (Baseline)
2️⃣ Min–Max Normalization
3️⃣ Z-Score Standardization

Then we compare:

Loss (MSE)

Convergence behavior

Weight stability

Bias accuracy

🎯 Learning Objectives

Through this project, I learned:

✔ How multivariate regression works mathematically
✔ How gradient descent optimizes weights & bias
✔ Why feature scaling affects convergence
✔ That scaling is not always beneficial
✔ How to run controlled ML experiments

This project focuses on intuition over libraries.

🧠 Dataset (Synthetic)

Data is generated to simulate student performance:

Feature	Meaning
Study hours	academic effort
Sleep hours	rest / focus level
Practice problems solved	skill reinforcement

Target output:

Noise simulates real-world randomness.

🧮 Model Implementation

The model is implemented in matrix form:

Training uses batch gradient descent.

No ML frameworks are used.

🧪 Experiments Performed
1️⃣ Baseline – No Feature Scaling

Features kept in natural units

Training was stable

Loss was lowest

But bias drifted away from true value

This showed that:

features were already reasonably scaled
scaling was not necessary

2️⃣ Min–Max Normalization (0–1 range)

Result:

Loss increased drastically

Weights became very large

Bias inflated

Reason:

compression removed useful scale signals
gradients overcompensated

Key takeaway:

❌ Min–Max scaling can hurt regression models
when features are already balanced

3️⃣ Z-Score Standardization

Result:

Loss still worse than baseline

Bias became extremely large

Reason:

standardization removed meaning of real-world units

Important learning:

⚠️ Scaling must respect data semantics
not just numerical ranges

📝 Key Insights From This Project

✔ Scaling is not universally good
✔ Good ML requires experimentation
✔ Natural feature meaning matters
✔ Bias behaves differently under scaling
✔ Noise influences parameter stability
✔ Gradient descent behavior must be observed — not assumed

This project helped me move from:

❌ “apply preprocessing blindly”
to
✔ “think like an ML engineer”