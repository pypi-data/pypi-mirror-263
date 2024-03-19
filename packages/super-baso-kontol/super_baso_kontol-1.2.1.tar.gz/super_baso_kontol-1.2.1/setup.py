import pathlib
import setuptools


setuptools.setup(
        name="super_baso_kontol",
        version="1.2.1",
        description="resep super baso kontol....",
        long_description=pathlib.Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        url="https://github.com/IrfanDect/super_baso_kontolPY",
        author="IrfanDect",
        author_email="bsbdrack@gmail.com",
        license="MIT",
        install_requires=["rich","requests","prompt-toolkit"],
        extras_require={
            "excel": ["openpyxl"],
            },
        packages=setuptools.find_packages(),
        include_package_data=True,
        classifiers=[
        'Intended Audience :: Developers', 'Topic :: Utilities',
        'License :: Public Domain', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ],
        keywords="super_baso_kontol",
        entry_points={"console_script": ["super_baso_kontol = super_baso_kontol.cli:main"]}
        )
