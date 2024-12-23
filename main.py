from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from api.registrasi.skema import AnggotaRespon, AnggotaForm
from api.cfg.database import SessionLocal, Base, engine
from api.registrasi.Form import Create_Anggota

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create", response_model=AnggotaRespon)
def Tambah_Anggota(data: AnggotaForm ,db: Session = Depends(get_db)):
    return Create_Anggota(db, data)