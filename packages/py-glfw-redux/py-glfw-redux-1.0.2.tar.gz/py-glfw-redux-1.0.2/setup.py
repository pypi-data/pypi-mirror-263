from setuptools_pybind11 import setup, PyBindModule

import os

SRC_DIR = os.path.split(__file__)[0]
BUILD_DIR = os.path.join(SRC_DIR, "build")
if not os.path.exists(BUILD_DIR):
    os.mkdir(BUILD_DIR)

setup(
    [
        PyBindModule(
            module_name="glfw",
            source_dir=".",
            dep_bin_prefixes=["third-party/glfw/src"],
            inc_dirs=[("third-party/glfw/include", "")],
        )
    ]
)
