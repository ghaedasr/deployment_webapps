import streamlit as st

# Judul aplikasi
st.title("APLIKASI KALKULATOR FISIKA")

# Tampilkan konten terkait dengan menu yang dipilih
def halaman_utama():
    # Konten untuk HALAMAN UTAMA
    st.write("Jangan lupa bilang cakeppp:D")
    st.write("------------------------------")
    st.write("Jalan-jalan ke Antartika")
    st.write("Selamat datang di Aplikasi Kalkulator Fisika!") 
    st.write("------------------------------")
    st.write('<b>by: KELOMPOK 9</b>', unsafe_allow_html=True)
    link_google_drive = "https://drive.google.com/uc?id=1K1rP7_f8pDsYlgCZ__cnLgZsKubHuLtF"
    st.image(link_google_drive, use_column_width=True)
    st.write('<b>ANGGOTA TIM:</b>', unsafe_allow_html=True)
    st.write('<span style="color: blue;">Ghaeda Auliyas Adidnur (2219074)</span>', unsafe_allow_html=True)
    st.write('<span style="color: red;">Nayyara Lizardi (2219131)</span>', unsafe_allow_html=True)
    st.write('<span style="color: purple;">Raisa Nur Afiani (2219149)</span>', unsafe_allow_html=True)
    st.write('<span style="color: orange;">Rosita Widyastuti (2219161)</span>', unsafe_allow_html=True)
    st.write('<span style="color: green;">Verina Aprida Putri (2219179)</span>', unsafe_allow_html=True)
    

def informasi():
    # Konten untuk INFORMASI
    st.write('<b>DENSITAS ZAT</b>', unsafe_allow_html=True)
    st.write("Densitas zat adalah massa per satuan volume dari suatu zat. Satuan umum untuk densitas adalah kg/m³ (kilogram per meter kubik) atau g/cm³ (gram per sentimeter kubik).Dalam fisika, densitas digunakan untuk mengukur seberapa padat suatu zat. Densitas zat dapat ditemukan dengan mengukur massa zat dan volume yang ditempatinya. Dalam banyak kasus, densitas zat bergantung pada suhu dan tekanan, sehingga nilai densitas harus diketahui pada suhu dan tekanan tertentu. Densitas juga dapat digunakan untuk menghitung massa atau volume suatu zat. Misalnya, massa sebuah benda dapat dihitung dengan mengalikan densitasnya dengan volumenya, sedangkan volume sebuah benda dapat dihitung dengan membagi massanya dengan densitasnya.")
    link_google_drive = "https://drive.google.com/uc?id=1K0wM_qpWPFJ4VMLdetVz0iH_aa1zOqTh"
    st.image(link_google_drive, use_column_width=True)
    
    st.write('<b>KUAT TEKAN BENDA</b>', unsafe_allow_html=True)
    st.write("Kuat tekan benda atau kekuatan tekan benda adalah kemampuan suatu benda untuk menahan tekanan atau gaya yang diberikan pada permukaannya tanpa mengalami perubahan bentuk atau kerusakan. Kuat tekan benda dalam fisika dapat diukur melalui beberapa metode pengujian, seperti uji tekan kompresi, uji tarik, dan uji lentur. Pada uji tekan kompresi, benda diletakkan di antara dua pelat pengujian dan diberikan beban secara perlahan-lahan hingga terjadi kerusakan pada benda atau terjadi perubahan bentuk permanen pada benda. Kuat tekan benda dapat dinyatakan dalam satuan Newton per meter persegi (N/m²) atau Pascal (Pa).")
    link_google_drive = "https://drive.google.com/uc?id=1K0UiKg-qNE3iTBgVyBls2bW6SEGizeEW"
    st.image(link_google_drive, use_column_width=True)
    
    st.write('<b>GAYA BENDA</b>', unsafe_allow_html=True)
    st.write("Gaya pada benda adalah pengaruh fisika yang dapat merubah kecepatan, arah gerak, atau bentuk suatu benda. Gaya dapat berasal dari berbagai sumber, seperti gravitasi, elektromagnetik, nuklir, dan lain-lain. Dalam fisika, gaya didefinisikan sebagai besaran vektor yang memiliki arah, besaran, dan satuan tertentu.")
    link_google_drive = "https://drive.google.com/uc?id=1JyWTSPIk8pKeC9J_zBdS5nLqo8gWYAyV"
    st.image(link_google_drive, use_column_width=True)
    
    st.write('<b>VISKOSITAS DINAMIK</b>', unsafe_allow_html=True)
    st.write("Viskositas dinamik (μ) didefinisikan sebagai gaya gesekan per satuan luas (Newton per meter persegi atau N/m²) yang diperlukan untuk membuat dua lapisan fluida dengan perbedaan kecepatan tertentu saling bergeser satu sama lain. Viskositas dinamik dinyatakan dalam satuan Pa·s (Pascal-sekon) atau N·s/m².")
    link_google_drive = "https://drive.google.com/uc?id=1Jv4oEYVKpYox94owAwtrDKJStvVplg6x"
    st.image(link_google_drive, use_column_width=True)
    
    st.write('<b>VISKOSITAS KINEMATIK</b>', unsafe_allow_html=True)
    st.write("Viskositas kinematik (ν) adalah rasio antara viskositas dinamik (μ) dan massa jenis fluida (ρ). Viskositas kinematik dinyatakan dalam satuan m²/s.")
    link_google_drive = "https://drive.google.com/uc?id=1Jv19UvDyMCSx3wzLJglDkwM0oklA6Qkm"
    st.image(link_google_drive, use_column_width=True)
    st.write("Viskositas dinamik dan kinematik sering digunakan dalam penghitungan aliran fluida dan transfer panas, seperti dalam perencanaan sistem pipa dan pemrosesan makanan. Semakin tinggi nilai viskositas suatu fluida, semakin sulit fluida tersebut mengalir, sehingga dibutuhkan gaya yang lebih besar untuk memindahkan fluida tersebut.")


def densitas_zat():
    link_google_drive = "https://drive.google.com/uc?id=1K0wM_qpWPFJ4VMLdetVz0iH_aa1zOqTh"
    st.image(link_google_drive, use_column_width=True)

    massa = st.number_input("Masukkan massa (g)", min_value=0.0)
    volume = st.number_input("Masukkan volume (ml)", min_value=0.0)
    if st.button("Hitung Densitas"):
        densitas = massa / volume
        st.write(f"Nilai densitas zat sebesar = {densitas} kg/m^3")

def kuat_tekan_benda():
    link_google_drive = "https://drive.google.com/uc?id=1K0UiKg-qNE3iTBgVyBls2bW6SEGizeEW"
    st.image(link_google_drive, use_column_width=True)
    
    gaya = st.number_input("Masukkan gaya (N)", min_value=0.0)
    luas = st.number_input("Masukkan luas (m^2)", min_value=0.0)
    if st.button("Hitung Kuat Tekan Benda"):
        tekanan = gaya / luas
        st.write(f"Nilai kuat tekan benda sebesar = {tekanan} N/m^2")
        
def gaya_benda():
    link_google_drive = "https://drive.google.com/uc?id=1JyWTSPIk8pKeC9J_zBdS5nLqo8gWYAyV"
    st.image(link_google_drive, use_column_width=True)
    
    massa = st.number_input("Masukkan massa (kg)", min_value=0.0)
    percepatan = st.number_input("Masukkan percepatan (m/s^2)", min_value=0.0)
    if st.button("Hitung Gaya"):
        gaya = massa * percepatan
        st.write(f"Nilai gaya benda sebesar = {gaya} N")    
        
def viskositas_dinamik():
    link_google_drive = "https://drive.google.com/uc?id=1Jv4oEYVKpYox94owAwtrDKJStvVplg6x"
    st.image(link_google_drive, use_column_width=True)
    
    force = st.number_input("Masukkan gaya gesekan (N)", min_value=0.0)
    area = st.number_input("Masukkan luas permukaan (m^2)", min_value=0.0)
    time = st.number_input("Masukkan waktu (s)", min_value=0.0)
    velocity = st.number_input("Masukkan kecepatan fluida (m/s)", min_value=0.0)
    if st.button("Hitung Viskositas Dinamik"):
        visc_din = (force * time) / (area * velocity)
        st.write(f"Nilai viskositas dinamik sebesar = {visc_din} Pa.s")

def viskositas_kinematik():
    link_google_drive = "https://drive.google.com/uc?id=1Jv19UvDyMCSx3wzLJglDkwM0oklA6Qkm"
    st.image(link_google_drive, use_column_width=True)
    
    dynamic_viscosity = st.number_input("Masukkan viskositas dinamik (Pa.s)", min_value=0.0)
    density = st.number_input("Masukkan massa jenis fluida (kg/m^3)", min_value=0.0)
    if st.button("Hitung Viskositas Kinematik"):
        visc_kin = dynamic_viscosity / density
        st.write(f"Nilai viskositas kinematik sebesar = {visc_kin} m^2/s")

# Membuat sidebar menu
menu_options = ["HALAMAN UTAMA","INFORMASI", "DENSITAS ZAT", "KUAT TEKAN BENDA", "GAYA BENDA", "VISKOSITAS DINAMIK", "VISKOSITAS KINEMATIK"]
selected_menu = st.sidebar.radio("Menu", menu_options)

# Tampilan kalkulator yang dipilih
if selected_menu == "HALAMAN UTAMA":
    halaman_utama()
elif selected_menu == "INFORMASI":
    informasi()
elif selected_menu == "DENSITAS ZAT":
    densitas_zat()
elif selected_menu == "KUAT TEKAN BENDA":
    kuat_tekan_benda()
elif selected_menu == "GAYA BENDA":
    gaya_benda()
elif selected_menu == "VISKOSITAS DINAMIK":
    viskositas_dinamik()
elif selected_menu == "VISKOSITAS KINEMATIK":
    viskositas_kinematik()