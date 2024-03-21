# Rasa Pro placeholder
This is an empty package. 

Please make sure to install the `rasa-pro` package from Rasa's internal
python package registry.

You can find the instructions to setup the internal registry at
https://rasa.com/docs/rasa-pro/installation/python/installation/ 

## Create a release
prerequisite:
* make sure to install `twine`

commands to create and upload a release:
```python
OVERRIDE=true python setup.py sdist
twine upload dist/*
```

