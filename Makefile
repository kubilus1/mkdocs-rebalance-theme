pkg:
	python3 setup.py sdist bdist_wheel

build:
	python3 setup.py build

clean:
	- rm -rf build
	- rm -rf dist

push:
	twine upload dist/*
