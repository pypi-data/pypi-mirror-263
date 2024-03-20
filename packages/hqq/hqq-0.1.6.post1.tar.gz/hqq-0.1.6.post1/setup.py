from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
import os


def install_cuda_cmd() -> str:
    cmd = "cd hqq/kernels; "
    cmd += "python setup_cuda.py install; "
    cmd += "cd ../..;"
    return cmd


def run_setup_cuda():
    print("Running setup_cuda.py...")
    try:
        os.system(install_cuda_cmd())
    except Exception as e:
        print("Error while running setup_cuda.py:", e)


class InstallCommand(install):
    def run(self):
        install.run(self)
        run_setup_cuda()


class DevelopCommand(develop):
    def run(self):
        develop.run(self)
        run_setup_cuda()


class EgginfoCommand(egg_info):
    def run(self):
        egg_info.run(self)
        run_setup_cuda()

setup(
    name="hqq",
    version="0.1.6.post1",
    description="Half-Quadratic Quantization (HQQ)",
    url="https://github.com/mobiusml/hqq/",
    author="Dr. Hicham Badri",
    author_email="hicham@mobiuslabs.com",
    license="Apache 2",
    packages=find_packages(include=["hqq", "hqq.*"]),
    cmdclass={
        "install": InstallCommand,
        "develop": DevelopCommand,
        "egg_info": EgginfoCommand,
    },
    install_requires=[
        "numpy>=1.24.4",
        "tqdm>=4.64.1",
        "huggingface_hub",
        "accelerate",
        "timm",
        "transformers>=4.36.1",
        "termcolor",
    ],
)
