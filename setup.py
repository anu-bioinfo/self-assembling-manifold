from setuptools import setup

setup(

    name='sam-algorithm', 

    version='0.1.7',  

    description='The Self-Assembling-Manifold algorithm', 

    long_description="The Self-Assembling-Manifold algorithm for analyzing single-cell RNA sequencing data.",  

    long_description_content_type='text/markdown',  
    
    url='https://github.com/atarashansky/self-assembling-manifold',  

    author='Alexander J. Tarashansky',  

    author_email='tarashan@stanford.edu',  

    keywords='scrnaseq analysis manifold reconstruction',  

    py_modules=["SAM","utilities"],
    
    install_requires=['pandas>=0.23','numpy>=1.15','scikit-learn>=0.20','matplotlib>=2.2','scipy>=1.1','anndata>=0.6.6','scanpy>=1.2']
)
