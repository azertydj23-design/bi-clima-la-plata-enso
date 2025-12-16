from src.db.connection import DuckDBConnection

con = DuckDBConnection()

print("Total días")
print(con.execute("SELECT COUNT(*) FROM dw.dim_fecha").fetchall())

print("\nTotal hechos")
print(con.execute("SELECT COUNT(*) FROM dw.fact_clima").fetchall())

print("\nENSO por fase")
print(
    con.execute("""
        SELECT fase, COUNT(*)
        FROM dw.dim_enso
        GROUP BY fase
    """).fetchdf()
)

print("\nHechos con ENSO asociado")
print(
    con.execute("""
        SELECT e.fase, COUNT(*)
        FROM dw.fact_clima fc
        JOIN dw.dim_fecha f ON fc.fecha_id = f.fecha_id
        JOIN dw.dim_enso e ON f.enso_id = e.enso_id
        GROUP BY e.fase
    """).fetchdf()
)
