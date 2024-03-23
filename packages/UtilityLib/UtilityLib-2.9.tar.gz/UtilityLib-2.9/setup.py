from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

LONG_DESCRIPTION = "".join(open("README.md").readlines())

setup(
    packages=find_packages(),
    description='UtilityLib: Lazy Evaluation Saves Time',
    author="VishalKumarSahu",
    author_email='mail@vishalkumarsahu.in',
    url='https://github.com/TheBiomics/UtilityLib',
    install_requires=REQUIREMENTS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
)
