from setuptools import setup, Extension
from Cython.Build import cythonize

# nome gerado da função -> arquivo 
ext_modules = [
    Extension("funcaoDecifrar", sources=["decifrar.pyx"], include_dirs=["C:/Users/felip/AppData/Local/Programs/Python/Python310/include/python.h"], library_dirs=["C:/Users/felip/AppData/Local/Programs/Python/Python310/libs"])
]


setup(
    ext_modules = cythonize(ext_modules)
)