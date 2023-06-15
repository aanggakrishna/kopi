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
import altair as alt

#content-start

st.set_page_config(layout="wide")
st.image("banner.jpg")
st.title('Menjelajahi Potensi Kopi')
st.write('_Proyeksi Produksi dan Peluang Export_')
#st.write('oleh : **I Putu A. Angga Krishna**')
#image = Image.open('udang.JPG')


# sidebar-start
with st.sidebar:
    st.title('Tahun dari 2017-2021')
    start_tahun, end_tahun = st.select_slider(
     'Select a range of color wavelength',options=[2017, 2018, 2019, 2020, 2021,2022]
     ,
     value=(2017, 2022))
    st.write('Kamu Memilih tahun', start_tahun, 'dan', end_tahun)
    
# sidebar-end





data_produksi_kopi = pd.read_excel('data_produksi_kopi.xlsx')
# st.write(data_produksi_kopi)
# Data historis produksi kopi
data_produksi_kopi = data_produksi_kopi.loc[(data_produksi_kopi['tahun']<=end_tahun) & (data_produksi_kopi['tahun']>=start_tahun)]
tahun = data_produksi_kopi['tahun'].to_numpy()
produksi = data_produksi_kopi['value'].to_numpy()
#regresi
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

# with st.container():
# Proyeksi produksi kopi untuk 5 tahun ke depan
tahun_proyeksi = np.array([2023, 2024, 2025])
produksi_proyeksi = regresi_linier(tahun, produksi, tahun_proyeksi)



# Tampilkan data historis produksi kopi
data_historis = {'Tahun': tahun, 'Produksi': produksi}


# Tampilkan proyeksi produksi kopi untuk 5 tahun ke depan
data_proyeksi = {'Tahun': tahun_proyeksi, 'Produksi': produksi_proyeksi}


# Plot data historis dan proyeksi menggunakan Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=tahun, y=produksi, mode='markers', name='Data Historis'))
fig.add_trace(go.Scatter(x=tahun_proyeksi, y=produksi_proyeksi, mode='markers', name='Proyeksi'))

fig.update_layout(
    title='Proyeksi Produksi Kopi di Indonesia',
    xaxis_title='Tahun',
    yaxis_title='Produksi Kopi'
)
# Menggunakan Streamlit untuk membuat tampilan aplikasi
st.title('Proyeksi Produksi Kopi di Indonesia')
st.plotly_chart(fig)


with st.expander("Lihat detail"):
    st.write("""Proyeksi menggunakan regrasi linier menggunakan data histori dari tahun 2017. Untuk proyeksi 3 tahun kedepan terjadi trend positif/ naik.""")
    st.write()

st.markdown('')

export_kopi_dunia_all = pd.read_csv('export_kopi_dunia.csv')

export_kopi_dunia_all = export_kopi_dunia_all.set_index('negara').stack().reset_index()
export_kopi_dunia_all.columns=['negara', 'year', 'export_kopi_dunia']
export_kopi_dunia_all['year'].astype(int)
export_kopi_dunia_all = export_kopi_dunia_all.loc[(export_kopi_dunia_all['year']==str(end_tahun))]
export_kopi_dunia_all = export_kopi_dunia_all.sort_values(by='export_kopi_dunia', ascending=False)

with st.container():
    st.title('TOP 20 Negara Export KOPI')
    st.write('_nilai per ribu USD_')
    jumlah = (int(end_tahun)-int(start_tahun)+1)*10
    
    sorted_data = export_kopi_dunia_all.head(jumlah).sort_values(by='export_kopi_dunia', ascending=False)
    sorted_data['rank'] = sorted_data['export_kopi_dunia'].rank(ascending=False)
    
    c = alt.Chart(sorted_data).mark_bar().encode(
        y=alt.X('export_kopi_dunia:Q', sort='-x'),
        x='negara',
        color='negara',
        tooltip=['year', 'export_kopi_dunia', 'negara']
    )

    st.altair_chart(c, use_container_width=True)
    st.write('')
    st.markdown('')
    with st.expander("Lihat Data Tabel"):
        # table = pd.pivot_table(sorted_data, values='year', index=['negara'], columns=['year'])
        # st.table(table)
        st.write("""Sumber https://trademap.org""")


#regresi
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

# with st.container():
# Proyeksi produksi kopi untuk 5 tahun ke depan
tahun_proyeksi = np.array([2023, 2024, 2025])
produksi_proyeksi = regresi_linier(tahun, produksi, tahun_proyeksi)



# Tampilkan data historis produksi kopi
data_historis = {'Tahun': tahun, 'Produksi': produksi}


# Tampilkan proyeksi produksi kopi untuk 5 tahun ke depan
data_proyeksi = {'Tahun': tahun_proyeksi, 'Produksi': produksi_proyeksi}


# Plot data historis dan proyeksi menggunakan Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=tahun, y=produksi, mode='markers', name='Data Historis'))
fig.add_trace(go.Scatter(x=tahun_proyeksi, y=produksi_proyeksi, mode='markers', name='Proyeksi'))

fig.update_layout(
    title='Proyeksi Produksi Kopi di Indonesia',
    xaxis_title='Tahun',
    yaxis_title='Produksi Kopi'
)
# Menggunakan Streamlit untuk membuat tampilan aplikasi
st.title('Proyeksi Produksi Kopi di Indonesia')
st.plotly_chart(fig)


with st.expander("Lihat detail"):
    st.write("""Proyeksi menggunakan regrasi linier menggunakan data histori dari tahun 2017. Untuk proyeksi 3 tahun kedepan terjadi trend positif/ naik.""")
    st.write()

st.markdown('')





export_kopi_indonesia_all = pd.read_csv('indonesia_export_kopi.csv')

export_kopi_indonesia_all = export_kopi_indonesia_all.set_index('country').stack().reset_index()
export_kopi_indonesia_all.columns=['negara', 'year', 'export_kopi_indonesia']
export_kopi_indonesia_all['year'].astype(int)
export_kopi_indonesia_all = export_kopi_indonesia_all.loc[(export_kopi_indonesia_all['year']<=str(end_tahun))]
export_kopi_indonesia_all = export_kopi_indonesia_all.sort_values(by='export_kopi_indonesia', ascending=False)
with st.container():
    st.title('TOP 10 Negara Import KOPI dari Indonesia')
    st.write('_nilai per ribu USD_')
    jumlah = (int(end_tahun)-int(start_tahun)+1)*10
    
    sorted_data = export_kopi_indonesia_all.head(jumlah).sort_values(by='export_kopi_indonesia', ascending=False)
    sorted_data['rank'] = sorted_data['export_kopi_indonesia'].rank(ascending=False)
    
    c = alt.Chart(sorted_data).mark_bar().encode(
        y=alt.X('export_kopi_indonesia:Q', sort='-x'),
        x='negara',
        color='negara',
        tooltip=['year', 'export_kopi_indonesia', 'negara']
    )

    st.altair_chart(c, use_container_width=True)
    st.write('')
    st.markdown('')
    with st.expander("Lihat Data Tabel"):
        # table = pd.pivot_table(sorted_data, values='year', index=['negara'], columns=['year'])
        # st.table(table)
        st.write("""Sumber https://trademap.org""")


with st.container():
    st.title('TOP 10 Negara Export KOPI per Tahun')
    st.write('_nilai per ribu USD_')
    jumlah = (int(end_tahun)-int(start_tahun)+1)*10
    
    sorted_data = export_kopi_indonesia_all.head(jumlah).sort_values(by='export_kopi_indonesia', ascending=False)
    sorted_data['rank'] = sorted_data['export_kopi_indonesia'].rank(ascending=False)
    
    c = alt.Chart(sorted_data).mark_line().encode(
        y=alt.X('export_kopi_indonesia:Q', sort='-x'),
        x='year',
        color='negara',
        tooltip=['year', 'export_kopi_indonesia', 'negara']
    )

    st.altair_chart(c, use_container_width=True)
    st.write('')
    st.markdown('')
    with st.expander("Lihat Data Tabel"):
        # table = pd.pivot_table(sorted_data, values='year', index=['negara'], columns=['year'])
        # st.table(table)
        st.write("""Sumber https://trademap.org""")

export_indonesia_p = pd.read_excel('export_indonesia_p.xlsx')
# st.write(export_indonesia_p)
# Data historis produksi kopi
export_indonesia_p = export_indonesia_p.loc[(export_indonesia_p['tahun']<=end_tahun)]
tahun = export_indonesia_p['tahun'].to_numpy()
produksi = export_indonesia_p['nilai'].to_numpy()
#regresi
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

# with st.container():
# Proyeksi produksi kopi untuk 5 tahun ke depan
tahun_proyeksi = np.array([2023])
produksi_proyeksi = regresi_linier(tahun, produksi, tahun_proyeksi)
# Tampilkan data historis produksi kopi
data_historis = {'Tahun': tahun, 'Produksi': produksi}
# Tampilkan proyeksi produksi kopi untuk 5 tahun ke depan
data_proyeksi = {'Tahun': tahun_proyeksi, 'Produksi': produksi_proyeksi}
# Plot data historis dan proyeksi menggunakan Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=tahun, y=produksi, mode='markers', name='Data Historis'))
fig.add_trace(go.Scatter(x=tahun_proyeksi, y=produksi_proyeksi, mode='markers', name='Proyeksi'))

fig.update_layout(
    title='Proyeksi Export Kopi di Indonesia',
    xaxis_title='Tahun',
    yaxis_title='Produksi Kopi'
)
# Menggunakan Streamlit untuk membuat tampilan aplikasi
st.title('Proyeksi Export Kopi di Indonesia')
st.plotly_chart(fig)

st.title('Index Spesialisasi Perdagangan')
#isp
isp_all = pd.read_csv('isp.csv')
isp_all = isp_all.set_index('country').stack().reset_index()
isp_all.columns=['negara', 'year', 'isp']

isp_all = isp_all.loc[(isp_all['year']==str(end_tahun))]
isp_all_world = isp_all.loc[isp_all['negara'] == 'World', 'isp']
isp_all_indonesia = isp_all.loc[isp_all['negara'] == 'Indonesia', 'isp']

# st.write(isp_all_indonesia['isp']-isp_all_world['isp'])
hasil_isp = (isp_all_indonesia.sum() - isp_all_world.sum())/(isp_all_indonesia.sum() + isp_all_world.sum())
hasil_isp=round(hasil_isp,2)
hasil_isp_label=''
if hasil_isp <=0.5 and hasil_isp>=-1:
    hasil_isp_label='Tahap Pengenalan'
elif hasil_isp >0.5 and hasil_isp<=0:
    hasil_isp_label='Tahap Substitusi Import'
elif hasil_isp >0 and hasil_isp<=0.8:
    hasil_isp_label='Tahap pertumbuhan'
elif hasil_isp >0.8 and hasil_isp<=1:
    hasil_isp_label='Tahap kematangan'

col1, col2, col3 = st.columns(3)

with col1:
    st.image("isp.png")
with col2:
    st.write("Dengan menggunakan pendekatan ini didapat bahwa nilai export kopi indonesia berada pada :")
with col3: 
    st.metric(hasil_isp_label, hasil_isp, delta=None, delta_color="normal", help=None, label_visibility="visible")

with st.container():
    st.title('Komsumsi Kopi di Dalam negeri')
    st.write('_dalam liter_')
    # jumlah = (int(end_tahun)-int(start_tahun)+1)*10
    sorted_data = pd.read_excel('komsumsi_kopi.xlsx')
    # st.table(sorted_data)
    
    c = alt.Chart(sorted_data).mark_line().encode(
        y='value',
        x='year',
        
        tooltip=['year', 'value']
    )

    st.markdown('')

export_indonesia_p = pd.read_excel('komsumsi_kopi.xlsx')
# st.write(export_indonesia_p)
# Data historis produksi kopi
export_indonesia_p = export_indonesia_p.loc[(export_indonesia_p['year']<=end_tahun)]
tahun = export_indonesia_p['year'].to_numpy()
produksi = export_indonesia_p['value'].to_numpy()
#regresi
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

# with st.container():
# Proyeksi produksi kopi untuk 5 tahun ke depan
tahun_proyeksi = np.array([2022])
produksi_proyeksi = regresi_linier(tahun, produksi, tahun_proyeksi)
# Tampilkan data historis produksi kopi
data_historis = {'Tahun': tahun, 'Produksi': produksi}
# Tampilkan proyeksi produksi kopi untuk 5 tahun ke depan
data_proyeksi = {'Tahun': tahun_proyeksi, 'Produksi': produksi_proyeksi}
# Plot data historis dan proyeksi menggunakan Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=tahun, y=produksi, mode='markers', name='Data Historis'))
fig.add_trace(go.Scatter(x=tahun_proyeksi, y=produksi_proyeksi, mode='markers', name='Proyeksi'))

fig.update_layout(
    title='Proyeksi Komsumsi Kopi di Indonesia',
    xaxis_title='Tahun',
    yaxis_title='Produksi Kopi'
)
# Menggunakan Streamlit untuk membuat tampilan aplikasi
col1, col2= st.columns(2)
with col1:
    st.altair_chart(c)
with col2:
    st.plotly_chart(fig)