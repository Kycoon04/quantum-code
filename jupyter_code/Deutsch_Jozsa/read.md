# Deutsch-Jozsa Algorithm

This code implements the Deutsch-Jozsa algorithm, a quantum algorithm that determines whether a Boolean function \(f(x)\) is constant (producing the same output for all inputs) or balanced (producing an equal number of 0s and 1s). The circuit uses two qubits: one for the input and one auxiliary qubit. Initially, Hadamard gates are applied to create a superposition. The function \(f(x)\) is encoded in the oracle, implemented using a CNOT gate in this example. After applying the oracle, another round of Hadamard gates creates interference. Measuring the first qubit reveals whether \(f(x)\) is constant (\(+1\)) or balanced (\(-1\)) with just one evaluation.