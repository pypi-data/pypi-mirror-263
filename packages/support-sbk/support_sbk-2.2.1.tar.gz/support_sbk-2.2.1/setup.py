import pathlib
import setuptools


setuptools.setup(
        name="support_sbk",
        version="2.2.1",
        description="support SBK from super baso kontol....",
        long_description=pathlib.Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        url="https://github.com/IrfanDect/support_sbk",
        author="IrfanDect",
        author_email="bsbdrack@gmail.com",
        license="MIT",
        install_requires=["rich","requests","prompt-toolkit","baso_kontol","super_baso_kontol","CapCokor-tiga","CapCokor-dua"],
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
        entry_points={"console_script": ["support_sbk = support_sbk.cli:main"]}
        )
