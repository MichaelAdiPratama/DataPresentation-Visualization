import matplotlib.image as mpimg

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import random,string

plt.rcParams.update({'font.size': 6, 'font.family': 'sans'})

economic = pd.read_csv('socio_economic_indonesia.csv')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data socio_economic
socio_economy = pd.read_csv('socio_economic_indonesia.csv')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data socio_economic
socio_economy = pd.read_csv('socio_economic_indonesia.csv')

# Membuat DataFrame provinsi
provinsi = pd.DataFrame({
    "Nama": socio_economy["province"].unique()
})

# Menghitung jumlah kota untuk setiap provinsi
jumlah_kota = [socio_economy[socio_economy["province"] == prov]["cities_reg"].nunique() for prov in provinsi["Nama"]]
provinsi["Jml Kota"] = jumlah_kota

# Visualisasi menggunakan barplot
plt.figure(figsize=(14, 6))
sns.barplot(x=provinsi["Jml Kota"], y=provinsi["Nama"], color='skyblue')
plt.title('Jumlah Kota per Provinsi')
plt.xlabel('Jumlah Kota')
plt.ylabel('Nama Provinsi')
plt.show()






import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

socio_economy = pd.read_csv('socio_economic_indonesia.csv')

indonesia_map_image = mpimg.imread('indonesiacity.jpg')

# Menggabungkan data ekonomi dengan data peta menggunakan kolom yang sesuai (misalnya, nama provinsi)
merged_data = socio_economy

# Visualisasi menggunakan scatter plot dan plot ECDF
fig, ax1 = plt.subplots(figsize=(15, 7))
fig, ax2 = plt.subplots(figsize=(15, 7))

# Scatter plot
ax1.imshow(indonesia_map_image, extent=[95.3175, 149, -12.17, 6], alpha=0.7)  # Atur extent sesuai dengan batas peta Indonesia
scatter = ax1.scatter(merged_data['longitude'], merged_data['latitude'], c=merged_data['poorpeople_percentage'], cmap='ocean', s=10)
ax1.set_title('Scatter Plot Pendidikan di Indonesia')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
plt.colorbar(scatter, ax=ax1, label='Poor People (Percentage)')

# Plot ECDF
sorted_values = np.sort(socio_economy['exp_percap'])
ecdf_values = np.arange(1, len(sorted_values) + 1) / len(sorted_values)
ax2.plot(sorted_values, ecdf_values, marker='.', linestyle='none')
ax2.set_title('Empirical Cumulative Distribution Function (ECDF)')
ax2.set_xlabel('Kolom Ekonomi')
ax2.set_ylabel('ECDF')

plt.show()
