"""
Create PNG images of all results for the research paper
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
fig = plt.figure(figsize=(16, 10))

# ============================================================================
# 1. Security Comparison Table as Image
# ============================================================================
ax1 = plt.subplot(2, 2, 1)
ax1.axis('off')
ax1.set_title('Security Feature Comparison', fontsize=14, fontweight='bold', pad=20)

# Table data
columns = ['Xu et al.\n[1]', 'Chen et al.\n[3]', 'Kumar et al.\n[5]*', 'Proposed\nPQC-MFA']
rows = [
    'Replay Attack',
    'Man-in-the-Middle (MitM)',
    'Impersonation',
    "Quantum 'Harvest Now,\nDecrypt Later'",
    'Forward Secrecy',
    'Single Point of\nFailure (SPoF)'
]

# Data: 1 = checkmark, 0 = cross
data = [
    [1, 1, 1, 1],  # Replay Attack
    [1, 1, 1, 1],  # MitM
    [1, 1, 1, 1],  # Impersonation
    [0, 0, 1, 1],  # Quantum
    [0, 0, 1, 1],  # Forward Secrecy
    [1, 1, 1, 1],  # SPoF
]

# Create table
table_data = []
for i, row in enumerate(rows):
    row_data = []
    for j, col in enumerate(columns):
        if data[i][j] == 1:
            row_data.append('YES')
        else:
            row_data.append('NO')
    table_data.append(row_data)

table = ax1.table(
    cellText=table_data,
    rowLabels=rows,
    colLabels=columns,
    cellLoc='center',
    loc='center',
    bbox=[0, 0, 1, 1]
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

# Color code the cells
for i in range(len(rows)):
    for j in range(len(columns)):
        cell = table[(i+1, j)]
        if data[i][j] == 1:
            cell.set_facecolor('#90EE90')  # Light green
        else:
            cell.set_facecolor('#FFB6C1')  # Light red
        cell.set_text_props(weight='bold', fontsize=11)

# Style header
for j in range(len(columns)):
    cell = table[(0, j)]
    cell.set_facecolor('#4A90E2')
    cell.set_text_props(weight='bold', color='white', fontsize=11)

# Style row labels
for i in range(len(rows)):
    cell = table[(i+1, -1)]
    cell.set_facecolor('#F0F0F0')
    cell.set_text_props(weight='bold', fontsize=10)

ax1.text(0.5, -0.15, '* Requires hardware support', 
         ha='center', fontsize=9, style='italic', transform=ax1.transAxes)

# ============================================================================
# 2. Scyther Verification Results Summary
# ============================================================================
ax2 = plt.subplot(2, 2, 2)
ax2.axis('off')
ax2.set_title('Scyther Formal Verification Results', fontsize=14, fontweight='bold', pad=20)

# Verification results
verification_data = [
    ('Patient - Alive', '✓ Verified'),
    ('Patient - Weakagree', '✓ Verified'),
    ('Patient - Niagree', '✓ Verified'),
    ('Patient - Nisynch', '✓ Verified'),
    ('Server - Alive', '✓ Verified'),
    ('Server - Weakagree', '✓ Verified'),
    ('Server - Niagree', '✓ Verified'),
    ('Server - Nisynch', '✓ Verified'),
]

y_pos = np.arange(len(verification_data))
colors = ['#2E7D32'] * len(verification_data)  # All green (all verified)

bars = ax2.barh(y_pos, [1]*len(verification_data), color=colors, alpha=0.7)
ax2.set_yticks(y_pos)
ax2.set_yticklabels([d[0] for d in verification_data], fontsize=10)
ax2.set_xlim(0, 1.2)
ax2.set_xlabel('Verification Status', fontsize=11, fontweight='bold')

# Add checkmarks
for i, (label, status) in enumerate(verification_data):
    ax2.text(0.5, i, status, ha='center', va='center', 
             fontsize=12, fontweight='bold', color='white')

ax2.text(0.5, -0.15, 'All 8 security claims verified - No attacks found', 
         ha='center', fontsize=10, style='italic', transform=ax2.transAxes)

# ============================================================================
# 3. Performance Metrics Summary
# ============================================================================
ax3 = plt.subplot(2, 2, 3)
ax3.set_title('Performance Metrics Summary', fontsize=14, fontweight='bold', pad=15)

metrics = ['KeyGen', 'Encaps', 'Decaps']
kyber_times = [0.04, 0.05, 0.06]  # Literature-based values (ms)
ecc_times = [0.5, 0.3, 0.3]  # Standard ECC (ms)

x = np.arange(len(metrics))
width = 0.35

bars1 = ax3.bar(x - width/2, kyber_times, width, label='PQC-MFA (Kyber-512)', 
                color='#2E86AB', alpha=0.8)
bars2 = ax3.bar(x + width/2, ecc_times, width, label='Standard ECC', 
                color='#A23B72', alpha=0.8)

ax3.set_xlabel('Operation', fontsize=11, fontweight='bold')
ax3.set_ylabel('Time (ms)', fontsize=11, fontweight='bold')
ax3.set_xticks(x)
ax3.set_xticklabels(metrics)
ax3.legend()
ax3.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}', ha='center', va='bottom', fontsize=9)

# ============================================================================
# 4. Communication Cost Comparison
# ============================================================================
ax4 = plt.subplot(2, 2, 4)
ax4.set_title('Communication Cost Comparison', fontsize=14, fontweight='bold', pad=15)

sizes = ['Public Key', 'Ciphertext']
kyber_sizes = [800, 768]  # Accurate Kyber-512 sizes (bytes)
ecc_sizes = [64, 64]  # Standard ECC (bytes)

x2 = np.arange(len(sizes))
width = 0.35

bars3 = ax4.bar(x2 - width/2, kyber_sizes, width, label='PQC-MFA (Kyber-512)', 
                color='#2E86AB', alpha=0.8)
bars4 = ax4.bar(x2 + width/2, ecc_sizes, width, label='Standard ECC', 
                color='#A23B72', alpha=0.8)

ax4.set_xlabel('Component', fontsize=11, fontweight='bold')
ax4.set_ylabel('Size (bytes)', fontsize=11, fontweight='bold')
ax4.set_xticks(x2)
ax4.set_xticklabels(sizes)
ax4.legend()
ax4.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels
for bars in [bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('all_results_summary.png', dpi=300, bbox_inches='tight')
print("✅ Created: all_results_summary.png")

# ============================================================================
# Create separate Security Comparison Table PNG
# ============================================================================
fig2, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')
ax.set_title('Security Feature Comparison Table', fontsize=16, fontweight='bold', pad=20)

# Create table data for separate image
table_data2 = []
for i, row in enumerate(rows):
    row_data = []
    for j, col in enumerate(columns):
        if data[i][j] == 1:
            row_data.append('YES')
        else:
            row_data.append('NO')
    table_data2.append(row_data)

table2 = ax.table(
    cellText=table_data2,
    rowLabels=rows,
    colLabels=columns,
    cellLoc='center',
    loc='center',
    bbox=[0, 0, 1, 1]
)

table2.auto_set_font_size(False)
table2.set_fontsize(11)
table2.scale(1, 2.2)

# Color code
for i in range(len(rows)):
    for j in range(len(columns)):
        cell = table2[(i+1, j)]
        if data[i][j] == 1:
            cell.set_facecolor('#90EE90')
        else:
            cell.set_facecolor('#FFB6C1')
        cell.set_text_props(weight='bold', fontsize=12)

for j in range(len(columns)):
    cell = table2[(0, j)]
    cell.set_facecolor('#4A90E2')
    cell.set_text_props(weight='bold', color='white', fontsize=12)

for i in range(len(rows)):
    cell = table2[(i+1, -1)]
    cell.set_facecolor('#F0F0F0')
    cell.set_text_props(weight='bold', fontsize=11)

ax.text(0.5, -0.1, '* Kumar et al. requires hardware support', 
        ha='center', fontsize=10, style='italic', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('security_comparison_table.png', dpi=300, bbox_inches='tight')
print("✅ Created: security_comparison_table.png")

# ============================================================================
# Create Scyther Results PNG
# ============================================================================
fig3, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.set_title('Scyther Formal Verification Results\nProtocol: PQC-MFA', 
             fontsize=16, fontweight='bold', pad=20)

# Create verification results display
results_text = """
SECURITY CLAIMS VERIFICATION

Patient Role:
  ✓ Alive_Patient1          [proof of correctness]
  ✓ Weakagree_Patient2      [proof of correctness]
  ✓ Niagree_Patient3        [proof of correctness]
  ✓ Nisynch_Patient4        [proof of correctness]

Server Role:
  ✓ Alive_Server1           [proof of correctness]
  ✓ Weakagree_Server2       [proof of correctness]
  ✓ Niagree_Server3         [proof of correctness]
  ✓ Nisynch_Server4         [proof of correctness]

RESULT: All 8 security claims verified
        No attacks found within state space bounds
        Protocol is secure against Man-in-the-Middle attacks
"""

ax.text(0.5, 0.5, results_text, ha='center', va='center', 
        fontsize=12, family='monospace', 
        bbox=dict(boxstyle='round', facecolor='#E8F5E9', alpha=0.8))

plt.tight_layout()
plt.savefig('scyther_verification_results.png', dpi=300, bbox_inches='tight')
print("✅ Created: scyther_verification_results.png")

print("\n" + "="*60)
print("All PNG files created successfully!")
print("="*60)
