pkg:
	python3 setup.py sdist bdist_wheel

clean:
	- rm -rf build
	- rm -rf dist

push:
	twine upload dist/*
