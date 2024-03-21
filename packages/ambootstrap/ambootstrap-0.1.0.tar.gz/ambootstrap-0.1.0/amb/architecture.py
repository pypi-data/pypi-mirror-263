import platform
from dataclasses import dataclass


@dataclass
class Architecture:
    alpine: str
    platform: str
    linux: str
    qemu: str


_arch_map = [
    Architecture(alpine="x86_64", platform="x86_64", linux="amd64", qemu="x86_64"),
    Architecture(alpine="x86", platform="i686", linux="x86", qemu="i386"),
    Architecture(alpine="aarch64", platform="aarch64", linux="arm64", qemu="aarch64"),
    Architecture(alpine="armhf", platform="armv6l", linux="arm", qemu="arm"),
    Architecture(alpine="armv7", platform="armv7l", linux="arm", qemu="arm"),
    Architecture(alpine="riscv64", platform="riscv64", linux="riscv", qemu="riscv64"),
]


def get_arch(alpine=None, platform=None, linux=None, qemu=None):
    if alpine is not None:
        key = "alpine"
        val = alpine
    elif platform is not None:
        key = "platform"
        val = platform
    elif linux is not None:
        key = "linux"
        val = linux
    elif qemu is not None:
        key = "qemu"
        val = qemu
    else:
        raise ValueError("Set at least one arch attribute")

    for arch in _arch_map:
        if getattr(arch, key) == val:
            return arch
    raise ValueError(f"The {key} architecture '{val}' is not known.")


def host_arch():
    return get_arch(platform=platform.machine())
