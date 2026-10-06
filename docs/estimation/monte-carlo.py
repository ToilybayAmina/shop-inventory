"""
Shop-Inventory: Monte Carlo симуляциясы
6-ЗЖ. Ықтималдық бағалау
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import percentile

# 1. Historical throughput (26 бақылау)
throughput = [4, 6, 0, 7, 5, 2, 6, 9, 4, 5, 0, 6, 7,
              4, 5, 1, 6, 5, 9, 3, 4, 6, 5, 8, 2, 5]

print(f"Historical throughput: {len(throughput)} бақылау")
print(f"Орташа throughput: {np.mean(throughput):.2f} элемент/апта")

# 2. Backlog = 13 элемент
backlog_size = 13
simulations = 10000
np.random.seed(42)

# 3. Симуляция
results = []
for _ in range(simulations):
    total = 0
    weeks = 0
    while total < backlog_size:
        total += np.random.choice(throughput)
        weeks += 1
    results.append(weeks)

results = np.array(results)

# 4. Квантільдер
p50 = percentile(results, 50)
p70 = percentile(results, 70)
p85 = percentile(results, 85)
p95 = percentile(results, 95)

print("\n=== Monte Carlo нәтижелері (10 000 жүгірту) ===")
print(f"P50 = {p50:.1f} апта")
print(f"P70 = {p70:.1f} апта")
print(f"P85 = {p85:.1f} апта")
print(f"P95 = {p95:.1f} апта")
print(f"Орташа = {np.mean(results):.2f} апта")

# 5. Гистограмма
plt.figure(figsize=(10, 6))
plt.hist(results, bins=range(1, max(results)+2),
         edgecolor='black', color='steelblue')
plt.title('Shop-Inventory: Monte Carlo нәтижелерінің таралуы')
plt.xlabel('Backlog аяқталғанға дейінгі апта саны')
plt.ylabel('Жүгірту саны')
plt.grid(axis='y', alpha=0.3)
plt.savefig('monte-carlo-histogram.png', dpi=150, bbox_inches='tight')
plt.show()

# 6. Кумулятивтік қисық
sorted_results = np.sort(results)
cdf = np.arange(1, len(sorted_results)+1) / len(sorted_results)

plt.figure(figsize=(10, 6))
plt.plot(sorted_results, cdf, color='steelblue', linewidth=2)
plt.axhline(y=0.50, color='red', linestyle='--', alpha=0.5, label='P50')
plt.axhline(y=0.85, color='green', linestyle='--', alpha=0.5, label='P85')
plt.axhline(y=0.95, color='orange', linestyle='--', alpha=0.5, label='P95')
plt.title('Shop-Inventory: Аяқталу ықтималдығы')
plt.xlabel('Апта саны')
plt.ylabel('Аяқталу ықтималдығы')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('monte-carlo-cdf.png', dpi=150, bbox_inches='tight')
plt.show()
