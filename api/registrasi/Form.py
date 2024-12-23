from sqlalchemy.orm import Session
from .models import Anggota, Specialist, GelarProfesi, GelarAkademik, JenjangPendidikan, PengalamanKerja, KeluargaAnggota
from .skema import AnggotaForm

def Create_Anggota(db: Session, anggota: AnggotaForm):
    anggota_data = Anggota(
        nama=anggota.nama,
        alamat=anggota.alamat,
        tempat_lahir=anggota.tempat_lahir,
        email=anggota.email,
    )
    anggota_data.keahlian_profesi = []
    anggota_data.pendidikan = []
    anggota_data.gelar_profesi = []
    anggota_data.gelar_akademik = []
    anggota_data.pengalaman_kerja = []
    anggota_data.keluarga_anggota = []

    # Tambahkan keahlian_profesi
    for keahlian in anggota.keahlian_profesi:
        specialist = Specialist(kategori_specialist=keahlian.kategori_specialist)
        anggota_data.keahlian_profesi.append(specialist)

    # Tambahkan pendidikan
    for pendidikan in anggota.pendidikan:
        jenjang_pendidikan = JenjangPendidikan(
            nama_perguruantinggi=pendidikan.nama_perguruantinggi,
            tingkat_pendidikan=pendidikan.tingkat_pendidikan,
        )
        anggota_data.pendidikan.append(jenjang_pendidikan)

    # Tambahkan gelar_profesi
    for gelar in anggota.gelar_profesi:
        gelar_profesi = GelarProfesi(nama_profesi=gelar.nama_profesi)
        anggota_data.gelar_profesi.append(gelar_profesi)

    # Tambahkan gelar_akademik
    for gelar_akademik in anggota.gelar_akademik:
        gelar_akademik_model = GelarAkademik(nama_gelarAkm=gelar_akademik.nama_gelarAkm)
        anggota_data.gelar_akademik.append(gelar_akademik_model)

    # Tambahkan pengalaman_kerja
    for pengalaman in anggota.pengalaman_kerja:
        pengalaman_kerja = PengalamanKerja(
            nama_perusahaan=pengalaman.nama_perusahaan,
            posisi=pengalaman.posisi,
            tahun_masuk=pengalaman.tahun_masuk,
            tahun_keluar=pengalaman.tahun_keluar,
        )
        anggota_data.pengalaman_kerja.append(pengalaman_kerja)

    # Tambahkan hubungi_keluarga
    for keluarga in anggota.hubungi_keluarga:
        keluarga_anggota = KeluargaAnggota(
            hubungan_keluarga=keluarga.hubungan_keluarga,
            nomor_keluarga=keluarga.nomor_keluarga,
        )
        anggota_data.keluarga_anggota.append(keluarga_anggota)

    # Simpan ke database
    db.add(anggota_data)
    db.commit()
    db.refresh(anggota_data)

    return anggota_data

