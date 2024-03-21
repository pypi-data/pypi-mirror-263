# Rasa Pro placeholder
This is an empty placeholder package for pypi.org. 

## Create a release
prerequisite:
* make sure to install `twine`

commands to create and upload a release:
```python
OVERRIDE=true python setup.py sdist
twine upload dist/*
```

