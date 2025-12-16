import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_RAW = BASE_DIR / "data" / "raw"
DATA_METEO = DATA_RAW / "estaciones"
DATA_CURATED = BASE_DIR / "data" / "curated"
DATA_ENSO = DATA_RAW / "enso"
DUCKDB_PATH = BASE_DIR / "data" / "duckdb" / "clima.duckdb"
