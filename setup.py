import sys
from setuptools import setup, find_packages

setup(name="meshcat",
    version="0.3.2",
    description="WebGL-based visualizer for 3D geometries and scenes",
    url="https://github.com/rdeits/meshcat-python",
    download_url="https://github.com/rdeits/meshcat-python/archive/v0.3.2.tar.gz",
    author="Robin Deits",
    author_email="mail@robindeits.com",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    test_suite="meshcat",
    entry_points={
        "console_scripts": [
            "meshcat-server=meshcat.servers.zmqserver:main"
        ]
    },
    install_requires=[
      "ipython >= 5",
      "u-msgpack-python >= 2.4.1",
      "numpy >= 1.14.0",
      "tornado >= 4.0.0",
      "pyzmq >= 17.0.0",
      "pyngrok >= 4.1.6",
      "pillow >= 7.0.0"
    ],
    zip_safe=False,
    include_package_data=True
)


"""
Clasificadores: Añaden metadatos útiles sobre el paquete, facilitando su búsqueda y categorización.
Descripción Detallada: Usar el contenido del README.md para proporcionar una descripción completa y formateada del paquete en PyPI.
Rangos de Versiones: Especificar versiones mínimas y máximas de las dependencias para evitar conflictos y asegurar compatibilidad.
"""

"""
import sys
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="meshcat",
    version="0.3.2",
    description="WebGL-based visualizer for 3D geometries and scenes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rdeits/meshcat-python",
    download_url="https://github.com/rdeits/meshcat-python/archive/v0.3.2.tar.gz",
    author="Robin Deits",
    author_email="mail@robindeits.com",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    test_suite="meshcat",
    entry_points={
        "console_scripts": [
            "meshcat-server=meshcat.servers.zmqserver:main"
        ]
    },
    install_requires=[
        "ipython>=5,<8",
        "u-msgpack-python>=2.4.1,<3",
        "numpy>=1.14.0,<2",
        "tornado>=4.0.0,<7",
        "pyzmq>=17.0.0,<24",
        "pyngrok>=4.1.6,<5",
        "pillow>=7.0.0,<10"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=False,
    include_package_data=True
)
"""
