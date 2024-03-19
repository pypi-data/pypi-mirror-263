from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = [line.split('==')[0]
                         for line in f.read().splitlines() if line.strip()]

setup(
    name='dillagent',
    version='1.0.1',
    author='buzzoo123',
    author_email='buzzoo123@gmail.com',
    description='Agentic LLM library',
    long_description='DillAgent is an AI agent library based on the principles of ReAct: Synergizing Reasoning and Acting in Language Models. While there are existing libraries such as Langchain, Langroid, and Llamaindex, DillAgent takes a different approach by prioritizing modularity and abstraction to provide developers with more control over their LLM-powered applications.',
    url='https://github.com/buzzoo123/dillagent',
    packages=find_packages(),
    install_requires=required_packages,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
