from hydrodb import *

db = HydroDB("tests")

db.create_table(table_name="Test_1", columns=["name", "age", "birth"])

