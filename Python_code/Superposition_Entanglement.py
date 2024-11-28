import pennylane as qml
from pennylane import numpy as np

dev = qml.device(name="default.qubit", wires=2)

@qml.qnode(dev)
def qfun():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    qml.RX(np.pi / 4, wires=1)
    qml.RY(np.pi / 3, wires=0)
    return qml.probs(wires=[0, 1])

print(qml.draw(qfun)())

result = qfun()
print("Resultados del circuito:", result)