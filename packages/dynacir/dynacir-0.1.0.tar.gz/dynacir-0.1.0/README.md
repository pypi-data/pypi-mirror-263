# `dynacir`

## Description
Dynacir is a transpilation plugin for Qiskit that optimizes dynamic quantum circuits. 

## Features
- Feature 1 (current): Merges sequential resets on a given qubit into a single reset.
- Feature 2 (upcoming): Merge sequences of `reset`-`first single-qubit gate`-...-`reset`-`final single-qubit gate` into just `reset`-`final single-qubit gate`
- Feature 3 (upcoming): Compile inefficient classical logic to minimize memory load

## Installation

To install `dynacir`, run the following command in your terminal:

```bash
pip install git+https://github.com/derek-wang-ibm/dynacir.git
```

### Usage

First, create a `QuantumCircuit`.`
```python
from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(2)
qc.reset(0)
qc.x(0)
qc.cx(0, 1)
qc.reset(0)
qc.reset(0)
qc.h(0)
qc.draw(output='mpl', style='iqp')

```

Then, apply a `PassManager` generated using the `dynacir` plugin.
```python
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService

pm = generate_preset_pass_manager(optimization_level=3, optimization_method="dynacir"

qc_dynacir = pm.run(qc)
qc_dynacir.draw(output='mpl', style='iqc')
)
```