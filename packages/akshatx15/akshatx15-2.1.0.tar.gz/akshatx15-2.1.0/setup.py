from setuptools import setup, find_packages

setup(
    name='akshatx15',  # Replace with your package name
    version='2.1.0',  # Start with an initial version
    description='Project & Project Path Management library.',
    long_description=open('README.md').read(),  # Use your README for this
    long_description_content_type='text/plain',
    author='Akshat Gupta',
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