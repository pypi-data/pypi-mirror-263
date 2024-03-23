import setuptools

requires = [
    "flake8 > 3.0.0",
]


setuptools.setup(
    name="flake8_max_lines",
    license="MIT",
    version="0.0.2",
    description="flake8 plugin to check max lines per files",
    author="misogihagi",
    author_email="hagimiso@gmail.com",
    url="https://github.com/misogihagi/flake8_max_lines",
    install_requires=requires,
    py_modules=["flake8_max_lines"],
    entry_points={
        'flake8.extension': [
            'MXL = flake8_max_lines:MaxLinesPlugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
