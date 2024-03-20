from setuptools import setup, find_namespace_packages

setup(
    name="terminaal",
    version="0.1",
    description="Address Book Assistant Bot",
    url="https://github.com/alexvekh/project-team-8-Personal-assistant",
    author="Vladyslav Babenko, Oleksy Verkhulevskyy, Aliesia Soloviova, Daniel Prokopenko, Marichka Matviiuk, Maks Pryima",
    author_email="vlad_bb@icloud.com, alexvekh@yahoo.com, aliesia.soloviova@gmail.com, megaprokop3578@gmail.com, m.v.matviiuk@gmail.com, makspryima@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["termcolor", "prompt_toolkit", "setuptools"],
    entry_points={"console_scripts": ["terminaal = package.main:main"]},
)
