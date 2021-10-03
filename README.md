# qgis-street-address-parser-api

Simple API that runs deepparse.org's address parser model. Intended for use in the QGIS Plugin [Street Address Parser.](https://github.com/tamos/qgis-street-address-parser)


## Setup

1. Create a virtual environment for the API.

  `python3 -m venv env_api `

  `source env_api/bin/activate`

  `pip install torch deeparse`

2. Run the api locally.

  `python3 wsgi.py`
