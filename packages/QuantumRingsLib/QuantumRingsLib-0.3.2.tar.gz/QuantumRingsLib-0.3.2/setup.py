import os
from setuptools import setup, Distribution
from prebuilt_binaries import prebuilt_binary, PrebuiltExtension

ext_module = PrebuiltExtension('QuantumRingsLib.pyd')

setup(
    name='QuantumRingsLib',
    version='0.3.2',
    description='A Quantum Development Library',
    include_package_data=True,
    packages=['QuantumRingsLib'],
    package_data={
        "QuantumRingsLib": ["*.pyd"],
    },
    cmdclass={
        'build_ext': prebuilt_binary,
    },
    ext_modules=[ext_module],
    python_requires="==3.9.*",
    
)

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Topic :: Software Development :: Build Tools",
    "Programming Language :: Python :: 3.9",
    "Operating System :: Microsoft :: Windows :: Windows 11",
]


