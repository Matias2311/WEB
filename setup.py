from setuptools import setup, find_packages

setup(
    name="mi_paquete",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gestion-usuarios = gestion_usuarios:menu',
        ],
    },
)
