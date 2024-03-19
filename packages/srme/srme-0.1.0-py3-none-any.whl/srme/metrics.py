import subprocess as sp
import psutil


def is_nvidia_smi_available() -> bool:
    """Check if nvidia-smi command available.
    Used to get gpu info.
    """
    try:
        sp.check_output(["nvidia-smi"])
        return True
    except (sp.CalledProcessError, FileNotFoundError):
        return False


def get_gpu_memory():
    raise NotImplementedError("need to test on gpu")


def get_cpu_percent() -> float:
    return psutil.cpu_percent()


def get_vm_percent() -> float:
    return psutil.virtual_memory().percent


def get_disk_usage_percent() -> float:
    return psutil.disk_usage("/").percent
