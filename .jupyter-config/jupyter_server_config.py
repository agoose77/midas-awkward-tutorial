from pathlib import Path
from cryptography.fernet import Fernet


c = get_config()


def handle_parameters_hook(self, parameters):
    fernet = Fernet(parameters["key"].encode())

    # Decrypt all fernet files
    for p in Path("data").glob("*.fernet"):
        p.with_suffix("").write_bytes(fernet.decrypt(p.read_bytes()))
        self.log.debug(f"Decrypting {p}")


c.JupyterServerParameters.handle_parameters_hook = handle_parameters_hook
