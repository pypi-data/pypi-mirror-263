"""Replace resets after measure with a conditional XGate."""

from qiskit.transpiler.basepasses import TransformationPass
from qiskit.dagcircuit import DAGCircuit
from qiskit.circuit.reset import Reset


class CollectResets(TransformationPass):
    def run(self, dag: DAGCircuit) -> DAGCircuit:
        # This method will be called on the DAG of the quantum circuit
        # to perform the transformation.
        
        # Iterate over all qubits in the circuit
        for qubit in dag.qubits:
            # Keep track of previous reset nodes for each qubit
            prev_reset_node = None
            
            # Get the nodes in topological order for processing
            for node in dag.topological_op_nodes():
                # Check if the node is a reset operation on the current qubit
                if isinstance(node.op, Reset) and node.qargs[0] == qubit:
                    if prev_reset_node:
                        # Merge this reset with the previous by removing the current node
                        dag.remove_op_node(node)
                    else:
                        # Update the previous reset node
                        prev_reset_node = node
                else:
                    # Reset prev_reset_node if the operation is not a reset
                    # or it's applied to a different qubit
                    prev_reset_node = None
        
        return dag