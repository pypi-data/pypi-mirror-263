from setuptools import setup

setup(
    author='CryptoGu',
    author_email='Kriptoairdrop9@gmail.com',
    name='CrypGuge',
    version='0.0.1',
    description='a text tic tac toe game, special game for tea https://app.tea.xyz/',
    url='https://github.com/CryptoGu1/Guge.git',
    project_urls={
        'Homepage': 'https://github.com/CryptoGu1/Guge.git',
        'Source': 'https://github.com/CryptoGu1/Guge.git',
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
        'CryptoGu'
        'CrypDorytea'
    ],
)
