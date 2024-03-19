import setuptools

setuptools.setup(
    name="ENGR131_Util_2024",
    version="1.0.13",
    author="Joshua C. Agar",
    description="Drexel Midterm Utility Functions",
    packages=["ENGR131_Util_2024"],
    install_requires=["cryptography", "drexel_jupyter_logger>=0.0.15", "ipywidgets"],
)
