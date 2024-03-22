from setuptools import setup

setup(
    author='CryptoGu',
    author_email='Kriptoairdrop9@gmail.com',
    name='CrypDorytea',
    version='0.0.1',
    description='A guess number game - is a best game to develop your intuition skills and also your ability to navigate thanks to hints, special game for tea https://app.tea.xyz/',
    url='https://github.com/CryptoGu1/CrypDorytea.git',
    project_urls={
        'Homepage': 'https://github.com/CryptoGu1/CrypDorytea.git',
        'Source': 'https://github.com/CryptoGu1/CrypDorytea.git',
    },
    py_modules=['hi_tea'],
    entry_points={
        'console_scripts': [
            'hi-tea=hi_tea:hello_tea_xyz'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
)
