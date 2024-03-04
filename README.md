# Receipt Parser service

The objective of this service, as implied by its name, is to speed up the process of updating products' availability. 
This is achieved by parsing receipts and linking products to the corresponding shops in the database. 
We begin by addressing the more accessible digital receipts, before progressing to handling physical ones.


## Running the service
Make sure to create database and required tables by running `python src/migrations.py` 
with the correct `EnvType`.


## Running tests
`python -m unittest discover -s src/tests`


## Architecture
The code aims at modularity and loose coupling. 
External interfaces like database and endpoint handlers should be easily replaceable.
Schemas aim to add predictability and consistency to the domain objects 
but not at the expense of flexibility.


## Code style
To check the code formatting, run `pylint src function_app.py`
To fix most of the formatting issues, run `black src function_app.py`