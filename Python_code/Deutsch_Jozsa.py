import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=2)

def oracle():
    qml.CNOT(wires=[0, 1])

@qml.qnode(dev)
def deutsch_jozsa():
    qml.Hadamard(wires=0)
    qml.PauliX(wires=1)
    qml.Hadamard(wires=1)
    oracle()
    qml.Hadamard(wires=0)
    return qml.expval(qml.PauliZ(0))

result = deutsch_jozsa()

if np.isclose(result, 1.0):
    print("La función es constante.")
else:
    print("La función es equilibrada.")