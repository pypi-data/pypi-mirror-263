import os
from setuptools import setup, find_packages

path = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(path, 'README.md'), 'r', encoding='utf-8') as f:
        long_description = f.read()
except Exception as e:
    long_description = 'Interpretable super-resolution dimension reduction of spatial transcriptomics data by DeepFuseNMF'

print (find_packages())
setup(
    name='DeepFuseNMF',
    version='0.0.1',
    description='Interpretable super-resolution dimension reduction of spatial transcriptomics data by DeepFuseNMF',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT Licence',
    Home_page='https://github.com/sldyns/DeepFuseNMF',
    include_package_data=True,
    python_requires='>=3.9',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.2',
        'cython>=0.29.24',
        'torch>=1.7.0',
        'scikit-learn>=0.23.2',
        'tqdm',
        'h5py',
        'scanpy',
        'pandas',
        'scikit-image',
        'opencv-python',
        'scipy',
        'torchvision'
    ],
    author='Junjie Tang, Kun Qian',
    author_email='kunqian@stu.pku.edu.cn',
    maintainer='Kun Qian',
    maintainer_email='kun_qian@stu.pku.edu.cn'
)