import streamlit as st

# Judul aplikasi
st.title("APLIKASI KALKULATOR FISIKA")

# Sub judul aplikasi
st.write("Selamat datang di Aplikasi Kalkulator Fisika!")
st.write("Silahkan pilih menu yang tersedia.")

# Deskripsi
st.write("by : Kelompok 9")
    
# Fungsi untuk menghitung densitas zat
def densitas_zat():
    massa = st.number_input("Masukkan massa (g)", min_value=0.0)
    volume = st.number_input("Masukkan volume (ml)", min_value=0.0)
    if st.button("Hitung Densitas"):
        densitas = massa / volume
        st.write(f"Densitas zat = {densitas} kg/m^3")

# Fungsi untuk menghitung kuat tekan benda
def kuat_tekan_benda():
    gaya = st.number_input("Masukkan gaya (N)", min_value=0.0)
    luas = st.number_input("Masukkan luas (m^2)", min_value=0.0)
    if st.button("Hitung Kuat Tekan Benda"):
        tekanan = gaya / luas
        st.write(f"Kuat tekan benda = {tekanan} N/m^2")

# Fungsi untuk menghitung gaya benda
def gaya_benda():
    massa = st.number_input("Masukkan massa (kg)", min_value=0.0)
    percepatan = st.number_input("Masukkan percepatan (m/s^2)", min_value=0.0)
    if st.button("Hitung Gaya"):
        gaya = massa * percepatan
        st.write(f"Gaya benda = {gaya} N")

# Fungsi untuk menghitung viskositas dinamik
def viskositas_dinamik():
    force = st.number_input("Masukkan gaya gesekan (N)", min_value=0.0)
    area = st.number_input("Masukkan luas permukaan (m^2)", min_value=0.0)
    time = st.number_input("Masukkan waktu (s)", min_value=0.0)
    velocity = st.number_input("Masukkan kecepatan fluida (m/s)", min_value=0.0)
    if st.button("Hitung Viskositas Dinamik"):
        visc_din = (force * time) / (area * velocity)
        st.write(f"Viskositas dinamik = {visc_din} Pa.s")

# Fungsi untuk menghitung viskositas kinematik
def viskositas_kinematik():
    dynamic_viscosity = st.number_input("Masukkan viskositas dinamik (Pa.s)", min_value=0.0)
    density = st.number_input("Masukkan massa jenis fluida (kg/m^3)", min_value=0.0)
    if st.button("Hitung Viskositas Kinematik"):
        visc_kin = dynamic_viscosity / density
        st.write(f"Viskositas kinematik = {visc_kin} m^2/s")

# Sidebar navigation
menu = ["Halaman Utama", "Densitas Zat", "Kuat Tekan Benda", "Gaya Benda", "Viskositas Dinamik", "Viskositas Kinematik"]
choice = st.sidebar.selectbox("Pilih Menu", menu)


# Tampilkan kalkulator yang dipilih
if choice == "Home":
    home()
elif choice == "Densitas Zat":
    densitas_zat()
elif choice == "Kuat Tekan Benda":
    kuat_tekan_benda()
elif choice == "Gaya Benda":
    gaya_benda()
elif choice == "Viskositas Dinamik":
    viskositas_dinamik()
elif choice == "Viskositas Kinematik":
    viskositas_kinematik()