# Post-Quantum Mutual Authentication Performance Simulation

This Python script simulates and evaluates the performance of a Post-Quantum Mutual Authentication (PQC-MFA) scheme using Kyber-512 (Lattice-based Cryptography) for IoMT (Internet of Medical Things) security.

## Features

- **Key Generation**: Simulates generating public/private keys for Patient and Server using Kyber-512
- **Authentication Handshake**: Simulates the complete mutual authentication data exchange (Encapsulation/Decapsulation)
- **Performance Metrics**: Measures computation time (ms) and communication cost (bytes)
- **Visualization**: Generates bar charts comparing PQC-MFA (Kyber) vs Standard ECC

## Installation

### Option 1: Using liboqs-python (Recommended for Real Measurements)

```bash
pip install -r requirements.txt
```

**Note**: The `oqs` package requires the Open Quantum Safe library to be installed. For detailed installation instructions, visit: https://github.com/open-quantum-safe/liboqs-python

### Option 2: Simulation Mode (No External Dependencies)

If `liboqs-python` is not available, the script will automatically use a simulation mode with realistic Kyber-512 values based on specifications.

**Minimum requirements for simulation mode:**
```bash
pip install matplotlib numpy
```

## Usage

Simply run the script:

```bash
python main.py
```

The script will:
1. Run 100 iterations of the authentication handshake
2. Calculate average performance metrics
3. Generate comparison bar charts
4. Save the chart as `pqc_mfa_performance_comparison.png`

## Output

The script provides:

1. **Console Output**:
   - Average computation times (KeyGen, Encaps, Decaps) in milliseconds
   - Communication costs (Public Key and Ciphertext sizes) in bytes
   - Standard deviations for statistical accuracy

2. **Visualization**:
   - Bar chart comparing computation times (PQC-MFA vs ECC)
   - Bar chart comparing communication costs (PQC-MFA vs ECC)
   - Saved as high-resolution PNG (300 DPI) for publication

## Metrics Explained

- **KeyGen Time**: Time to generate public/private key pair
- **Encaps Time**: Time for encapsulation (creating ciphertext and shared secret)
- **Decaps Time**: Time for decapsulation (recovering shared secret)
- **Public Key Size**: Size of the public key in bytes
- **Ciphertext Size**: Size of the ciphertext in bytes

## For Research Publication

For accurate real-world measurements in your research paper:
1. Install `liboqs-python` following the official documentation
2. Run the script with `liboqs` available
3. The script will use actual Kyber-512 implementations for precise measurements

## References

- Kyber: A CCA-secure module-lattice-based KEM (https://pq-crystals.org/kyber/)
- Open Quantum Safe: https://openquantumsafe.org/
