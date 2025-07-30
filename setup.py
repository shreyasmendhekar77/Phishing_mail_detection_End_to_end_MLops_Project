import setuptools

# with open("Readme.md", "r", encoding="utf-8") as f:
#     long_description = f.read()


__version__ = "1.0.0"

REPO_NAME = "Phishing_mail_detection_end_to_end_Mlops_project"
AUTHOR_USER_NAME = "SDM"
SRC_REPO = "Mlops_Project"
AUTHOR_EMAIL = "shreyasmendhekar7@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    # long_description=long_description,
    # long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)