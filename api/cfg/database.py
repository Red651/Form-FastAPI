from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Gantilah dengan kredensial MySQL Anda
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/ikopi"

# Membuat engine untuk koneksi ke MySQL
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})

# Membuat session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base untuk mendefinisikan kelas model
Base = declarative_base()

Base.metadata.create_all(bind=engine)
