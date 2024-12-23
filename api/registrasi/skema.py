from typing import List
from datetime import datetime
from pydantic import BaseModel, Field

class PengalamanKerja(BaseModel):
    nama_perusahaan: str
    posisi: str
    tahun_masuk: int
    tahun_keluar: int

class HubungiKeluarga(BaseModel):
    hubungan_keluarga: str
    nomor_keluarga: str

class Specialist(BaseModel):
    kategori_specialist: str

class GelarAkademik(BaseModel):
    nama_gelarAkm: str

class GelarProfesi(BaseModel):
    nama_profesi: str

class Pendidikan(BaseModel):
    nama_perguruantinggi: str
    tingkat_pendidikan: str

class AnggotaForm(BaseModel):
    nama: str
    alamat: str
    tempat_lahir: str
    email: str
    keahlian_profesi: List[Specialist] = Field(default_factory=list)
    pendidikan: List[Pendidikan] = Field(default_factory=list)
    gelar_profesi: List[GelarProfesi] = Field(default_factory=list)
    gelar_akademik: List[GelarAkademik] = Field(default_factory=list)
    pengalaman_kerja: List[PengalamanKerja] = Field(default_factory=list)
    hubungi_keluarga: List[HubungiKeluarga] = Field(default_factory=list)

class AnggotaRespon(BaseModel):
    id_anggota: str
    dibuat: datetime
