from setuptools import setup, find_packages

setup(
    name='agptx15',  # Replace with your package name
    version='1.0.2',  # Start with an initial version
    description='Project & Project Path Management library.\nUse agptx15 to manage and import the root directories of your projects into various python files across the system. The sole purpose of this library is to make your projects quickly deployable without worrying about setting up paths across your project files.',
    long_description=open('README.md').read(),  # Use your README for this
    long_description_content_type='text/plain',
    author='Akshat Gupta',
    author_email='agptx15@gmail.com',
    packages=find_packages(),  # Find packages automatically
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose an appropriate license 
        'Operating System :: OS Independent',
    ],

    python_requires='>=3',  # Specify minimum Python version
    install_requires=[],
)