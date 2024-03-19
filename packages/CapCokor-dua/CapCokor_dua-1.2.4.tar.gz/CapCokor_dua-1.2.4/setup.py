import pathlib
import setuptools


setuptools.setup(
        name="CapCokor_dua",
        version="1.2.4",
        description="cap cokor dua adalah kakak dari cap_cokor_tiga...",
        long_description=pathlib.Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        url="https://github.com/IrfanDect/CapCokor_dua",
        author="bsbdrack",
        author_email="bsbdrack@gmail.com",
        license="MIT",
        install_requires=["baso-kontol","CapCokor-tiga"],
        extras_require={
            "excel": ["openpyxl"],
            },
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"console_script": ["CapCokor_dua = CapCokor_dua.cli:main"]}
        )
