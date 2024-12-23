from sqlalchemy import Column, Integer, String, Enum as SQLEnum, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from typing import List

from ..cfg.database import Base

class TingkatPendidikan(Enum):
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    D3 = "D3/4"

class Anggota(Base):
    __tablename__ = 'anggota'
    id_anggota = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    increment = Column(Integer, primary_key=True, autoincrement=True)
    nama = Column(String(225), nullable=False)
    alamat = Column(String(225), nullable=False)
    tempat_lahir = Column(String(225), nullable=False)
    email = Column(String(225), nullable=False)
    # id_specialist = Column(Integer, ForeignKey('specialist.id_specialist'))
    # id_pendidikan = Column(Integer, ForeignKey('pendidikan.id_pendidikan'))
    # id_profesi = Column(Integer, ForeignKey('gelarprofesi.id_profesi'))
    # id_akademik = Column(Integer, ForeignKey('gelarakademi.id_akademik'))
    dibuat = Column(DateTime, server_default=func.now())

    keahlian_profesi = relationship('Specialist', cascade="all, delete-orphan")
    pendidikan = relationship('JenjangPendidikan', cascade="all, delete-orphan")
    gelar_profesi = relationship('GelarProfesi', cascade="all, delete-orphan")
    gelar_akademik = relationship('GelarAkademik', cascade="all, delete-orphan")
    pengalaman_kerja = relationship('PengalamanKerja', cascade="all, delete-orphan")
    keluarga_anggota = relationship('KeluargaAnggota', back_populates='anggota', cascade="all, delete-orphan")


class PengalamanKerja(Base):
    __tablename__ = "pengalaman_kerja"
    id_perusahaan = Column(Integer, primary_key=True, autoincrement=True)
    nama_perusahaan = Column(String(225), nullable=False)
    posisi = Column(String(40), nullable=False)
    tahun_masuk = Column(Integer)
    tahun_keluar = Column(Integer)
    id_anggota = Column(String(36), ForeignKey('anggota.id_anggota'))

class KeluargaAnggota(Base):
    __tablename__ = "keluarga_anggota"
    id_keluarga = Column(Integer, primary_key=True, autoincrement=True)
    hubungan_keluarga = Column(String(20), nullable=False)
    nomor_keluarga = Column(String(20), nullable=False)
    id_anggota = Column(String(36), ForeignKey('anggota.id_anggota'))
    anggota = relationship('Anggota', back_populates='keluarga_anggota')

class Specialist(Base):
    __tablename__ = 'specialist'
    id_specialist = Column(Integer, autoincrement=True, primary_key=True)
    kategori_specialist = Column(String(20), nullable=False)
    id_anggota = Column(String(36), ForeignKey('anggota.id_anggota'))

class JenjangPendidikan(Base):
    __tablename__ = 'pendidikan'
    id_pendidikan = Column(Integer, primary_key=True, autoincrement=True)
    nama_perguruantinggi = Column(String(70), nullable=False)
    tingkat_pendidikan = Column(SQLEnum(TingkatPendidikan), nullable=False)
    id_anggota = Column(String(36), ForeignKey('anggota.id_anggota'))

class GelarProfesi(Base):
    __tablename__ = 'gelarprofesi'
    id_profesi = Column(Integer, primary_key=True, autoincrement=True)
    nama_profesi = Column(String(20), nullable=False)
    id_anggota = Column(String(36), ForeignKey('anggota.id_anggota'))

class GelarAkademik(Base):
    __tablename__ = 'gelarakademi'
    id_akademik = Column(Integer, primary_key=True, autoincrement=True)
    nama_gelarAkm = Column(String(20), nullable=False)
    id_anggota = Column(String(36), ForeignKey('anggota.id_anggota'))


