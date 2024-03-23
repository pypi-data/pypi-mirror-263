import ctypes
from dataclasses import dataclass
import platform
import pkg_resources

# Determine the shared library file based on the platform
if platform.system().lower() == "linux":
    lib_file = "library_linux.so"
else:
    lib_file = "library.so"  # Fallback or default to non-Linux

# Try to load the library from the package resources
so_path = pkg_resources.resource_filename("last_layer", f"lib/{lib_file}")
try:
    library = ctypes.cdll.LoadLibrary(so_path)
except OSError:
    # Fallback to trying to load directly in case of failure
    library = ctypes.cdll.LoadLibrary(f"lib/{lib_file}")


@dataclass
class RiskModel:
    query: str
    markers: dict
    score: float
    passed: bool


def scan_prompt(prompt: str) -> RiskModel:
    heuristic = library.heuristicP
    heuristic.restype = ctypes.c_void_p
    heuristic.argtypes = [ctypes.c_char_p]
    # this is a pointer to our string
    farewell_output = heuristic(prompt.encode("utf-8"))
    # we dereference the pointer to a byte array
    farewell_bytes = ctypes.string_at(farewell_output)
    return RiskModel(
        query=prompt, score=0.95, markers={"Threat": "Illegal Activity"}, passed=True
    )


scan_llm = scan_prompt


def version():
    return "0.1.0"
