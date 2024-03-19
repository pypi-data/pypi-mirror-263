from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = [line.split('==')[0]
                         for line in f.read().splitlines() if line.strip()]

setup(
    name='dillagent',  # Name of your package
    version='1.0.2',  # Version number
    author='buzzoo123',  # Author name
    author_email='buzzoo123@gmail.com',  # Author email
    description='Agentic LLM library',  # Package description
    # Type of long description (if applicable)
    long_description_content_type='text/markdown',
    url='https://github.com/buzzoo123/dillagent',  # URL of your project repository
    # Find all packages in the project (alternatively, you can list them manually)
    packages=find_packages(),
    install_requires=required_packages,
    python_requires='>=3.8',  # Python version required by your package
    classifiers=[  # Classifiers for your package (e.g., Python versions, license, etc.)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
