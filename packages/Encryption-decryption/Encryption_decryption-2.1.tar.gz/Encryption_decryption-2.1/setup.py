import setuptools

with open("text.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Encryption_decryption",
    version="2.1",
    description="A Python package for simple encryption and decryption of messages using an algorithm.",
    long_description=long_description,
    long_description_content_type="text/plain",
    author="Wahid Hussain",
    author_email="wahidhussain643@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Development Status :: 6 - Mature",
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Environment :: Console",
    ],
    python_requires=">=3.10,<3.12",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"": ["text.txt"]}  # Include the "text.txt" file in the distribution
)


