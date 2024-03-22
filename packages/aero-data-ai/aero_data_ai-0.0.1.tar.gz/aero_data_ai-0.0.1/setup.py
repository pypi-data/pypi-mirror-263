from setuptools import setup, find_packages

setup(
    name='aero_data_ai',  # Replace with your package name
    version='0.0.1',  # Start with an initial version
    description='The official project path management library published by team Aero Data AI @InvoLead.',
    long_description=open('README.md').read(),  # Use your README for this
    long_description_content_type='text/markdown',
    author='Team Aero Data AI',
    author_email='akshat.gupta@involead.com',
    packages=find_packages(),  # Find packages automatically
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose an appropriate license 
        'Operating System :: OS Independent',
    ],

    python_requires='>=3',  # Specify minimum Python version
    # install_requires=[],
    package_data={'': ['*.json']}
)