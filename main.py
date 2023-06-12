import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from scipy import stats
from PIL import Image

#content-start
st.set_page_config(layout="wide")
st.title('judul 1')
st.write('_deskripsi_')
#st.write('oleh : **I Putu A. Angga Krishna**')
#image = Image.open('udang.JPG')


# sidebar-start
with st.sidebar:
    st.title('Tahun dari 2017-2021')
    start_tahun, end_tahun = st.select_slider(
     'Select a range of color wavelength',options=['2017', '2018', '2019', '2020', '2021']
     ,
     value=('2017', '2021'))
    st.write('Kamu Memilih tahun', start_tahun, 'dan', end_tahun)
    
# sidebar-end

with st.container():
    st.title('')
    st.write('_nilai per ribu USD_')
    jumlah = (int(end_tahun)-int(start_tahun)+1)*5
    
    
    
    
    st.write('')
    st.markdown('')
    with st.expander("Lihat Data Tabel"):
       
        st.write("""Sumber https://trademap.org""")


data_produksi_kopi = pd.read_excel('data_produksi_kopi.xlsx')
st.write(data_produksi_kopi)
# Data historis produksi kopi

tahun = data_produksi_kopi['tahun'].to_numpy()
produksi = data_produksi_kopi['value'].to_numpy()

# Fungsi regresi linier
def regresi_linier(x, y, x_pred):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numer = np.sum((x - x_mean) * (y - y_mean))
    denom = np.sum((x - x_mean) ** 2)
    
    b1 = numer / denom
    b0 = y_mean - (b1 * x_mean)
    
    y_pred = b0 + (b1 * x_pred)
    
    return y_pred

# Proyeksi produksi kopi untuk tahun depan (2022)
tahun_depan = 2023
tahun_depan = int(tahun_depan)
produksi_proyeksi = regresi_linier(tahun, produksi, tahun_depan)

# Menggunakan Streamlit untuk membuat tampilan aplikasi
st.title('Proyeksi Produksi Kopi di Indonesia')
st.markdown('Data Historis Produksi Kopi:')
data = {'Tahun': tahun, 'Produksi': produksi}
st.table(data)

st.markdown(f'Proyeksi produksi kopi di Indonesia untuk tahun {tahun_depan}: **{produksi_proyeksi} ton**')

# Plot data historis dan proyeksi
fig, ax = plt.subplots()
ax.scatter(tahun, produksi, color='blue', label='Data Historis')
ax.plot(tahun_depan, produksi_proyeksi, color='red', marker='o', markersize=5, label='Proyeksi')
ax.set_xlabel('Tahun')
ax.set_ylabel('Produksi Kopi')
ax.set_title('Proyeksi Produksi Kopi di Indonesia')
ax.legend()
# Mengatur posisi dan label sumbu x
ax.set_xticks(tahun)  # Menggunakan tahun sebagai posisi sumbu x
ax.set_xticklabels(tahun.astype(int))  # Menggunakan tahun sebagai label sumbu x (dikonversi ke integer)

st.pyplot(fig)

# Menggunakan Streamlit untuk membuat tampilan aplikasi
st.title('Proyeksi Produksi Kopi di Indonesia')
st.markdown('Data Historis Produksi Kopi:')
data = {'Tahun': tahun, 'Produksi': produksi}
st.table(data)

st.markdown(f'Proyeksi produksi kopi di Indonesia untuk tahun {tahun_depan}: **{produksi_proyeksi:.0f} ton**')  # Menggunakan :.0f untuk memformat tampilan menjadi bilangan bulat

# Plot data historis dan proyeksi menggunakan Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=tahun, y=produksi, mode='markers', name='Data Historis'))
fig.add_trace(go.Scatter(x=[tahun_depan], y=[produksi_proyeksi], mode='markers', name='Proyeksi'))

fig.update_layout(
    title='Proyeksi Produksi Kopi di Indonesia',
    xaxis_title='Tahun',
    yaxis_title='Produksi Kopi'
)

st.plotly_chart(fig)