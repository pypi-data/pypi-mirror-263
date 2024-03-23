import setuptools

with open("README.md","r") as readmefile:
	readme=readmefile.read()

setuptools.setup(
	name="Pointer-pkg-tkchen",
	version="0.1",
	author="TkChen",
	author_email="cccyyyhhh135@outlook.com",
	description="A Package that can use the pointers just like in C!",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/chen-tk/Pointer-on-Python",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.10"
)