from qiskit.transpiler.preset_passmanagers.plugin import PassManagerStagePlugin
from qiskit.transpiler import PassManager
from dynacir.dynacir_passes import CollectResets

class DynacirPlugin(PassManagerStagePlugin):
    def pass_manager(self, pass_manager_config, optimization_level):
        pm = PassManager(
            [
                CollectResets()
            ]
        )
        return pm