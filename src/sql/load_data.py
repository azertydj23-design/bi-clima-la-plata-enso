from src.db.connection import DuckDBConnection

con = DuckDBConnection()

for script in [
    "schema.sql",
    "load_dim_enso.sql",
    "load_dim_tiempo.sql",
    "load_fact_clima.sql",
]:
    con.execute(open(f"src/sql/{script}").read())
