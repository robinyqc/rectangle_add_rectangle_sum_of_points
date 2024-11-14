### Problem Description

You are given an initial set of $N$ weighted points, $P = (P_0, P_1, \dots, P_{N - 1})$, on a two-dimensional plane. Each point $P_i$ ($0 \leq i < N$) is located at $(x_i, y_i)$ and has an associated weight $w_i$. Process $Q$ queries of the following types. For the $i$-th ($0\leq i < Q$) query:

- **`0 $x$ $y$ $w$`**: Append a new point $P_{i + |P|}$ with weight $w$ at coordinates $(x, y)$. If a point already exists at these coordinates, add the new point as a separate instance.

- **`1 $x$ $w$`**: Update the weight of point $P_x$ to $w$. (i.e., $w_x \gets w$)

- **`2 $l$ $d$ $r$ $u$`**: Calculate the sum of weights modulo $998244353$ for all points where $l \leq x_i < r$ and $d \leq y_i < u$.

- **`3 $l$ $d$ $r$ $u$ $a$ $b$`**: For each $i$ such that $l \leq x_i < r$ and $d \leq y_i < u$, apply the transformation $w_i \gets a \cdot w_i + b$.

---

### Constraints

- $1 \leq N \leq 10^5$
- $1 \leq Q \leq 2 \times 10^5$
- $0 \leq x_i, y_i \leq 10^9$
- $0 \leq w_i < 998244353$

For each query type:
- **Type `0` (Add a Point):** $0 \leq x, y \leq 10^9$, $0 \leq w < 998244353$
- **Type `1` (Update Weight):** $0\leq x < (\text{Number of existing points})$
- **Type `2` (Sum of Weights):** $0 \leq l < r \leq 10^9$, $0 \leq d < u \leq 10^9$
- **Type `3` (Weighted Transformation):** $0 \leq l < r \leq 10^9$, $0 \leq d < u \leq 10^9$, $0 \leq a, b < 998244353$
