# import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({'font.size': 8, 'font.family': 'sans'})
diabetes = pd.read_csv('diabetes.tab.csv')

# ----------------------------------------
# SCATTER PLOT
# ----------------------------------------
# SubPlot --> untuk menampilkan beberapa grafik dalam 1 image/dashboard:
fig, ax = plt.subplots(nrows=3, ncols=3, sharex=False, sharey=False, constrained_layout = True)  # dapat disingkat menjadi plt.subplots(2,2)
fig.set_figheight(8)
fig.set_figwidth(8)

# 1.Correlations between column Y and column BMI:
sns.scatterplot(data= diabetes, x='Y', y='BMI',hue='SEX',size='AGE', palette='vlag',ax=ax[0,0])  # Cari palette lain yang disediakan oleh matplotlib 
ax[0,0].set_title('1.Diabetes and BMI Correlations', fontweight='bold')
ax[0,0].set_ylabel('Diabetes Progress')
ax[0,0].set_xlabel('BMI')
ax[0,0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# 2.Correlations between column Y and column BP:
sns.scatterplot(data= diabetes, x='Y', y='BP',hue='SEX',size='AGE', palette='icefire',ax=ax[0,1])  # Cari palette lain yang disediakan oleh matplotlib 
ax[0,1].set_title('2.Diabetes and BP Correlations', fontweight='bold')
ax[0,1].set_ylabel('Diabetes Progress')
ax[0,1].set_xlabel('BP')
ax[0,1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# 3.Correlations between column Y and column S1:
sns.scatterplot(data= diabetes, x='Y', y='S1',hue='SEX',size='AGE', palette='Spectral',ax=ax[0,2])  # Cari palette lain yang disediakan oleh matplotlib 
ax[0,2].set_title('3.Diabetes and S1 Correlations', fontweight='bold')
ax[0,2].set_ylabel('Diabetes Progress')
ax[0,2].set_xlabel('S1')
ax[0,2].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# 4.Correlations between column Y and column S2:
sns.scatterplot(data= diabetes, x='Y', y='S2',hue='SEX',size='AGE', palette='dark:salmon_r',ax=ax[1,0])  # Cari palette lain yang disediakan oleh matplotlib 
ax[1,0].set_title('4.Diabetes and S2 (LDL) Correlations', fontweight='bold')
ax[1,0].set_ylabel('Diabetes Progress')
ax[1,0].set_xlabel('S2')
ax[1,0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# 5.Correlations between column Y and column S3:
sns.scatterplot(data= diabetes, x='Y', y='S3',hue='SEX',size='AGE', palette='ch:start=2, rot=0, light=.55',ax=ax[1,1])  # Cari palette lain yang disediakan oleh matplotlib 
ax[1,1].set_title('5.Diabetes and S3 (HDL) Correlations', fontweight='bold')
ax[1,1].set_ylabel('Diabetes Progress')
ax[1,1].set_xlabel('S3')
ax[1,1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# 6.Correlations between column Y and column S4:
sns.scatterplot(data= diabetes, x='Y', y='S4',hue='SEX',size='AGE', palette='ch:start=1,rot=0, light=.55',ax=ax[1,2])  # Cari palette lain yang disediakan oleh matplotlib 
ax[1,2].set_title('6.Diabetes and S4 (Total Cholesterol) Correlations', fontweight='bold')
ax[1,2].set_ylabel('Diabetes Progress')
ax[1,2].set_xlabel('S4')
ax[1,2].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# 7.Correlations between column Y and column S5:
sns.scatterplot(data= diabetes, x='Y', y='S5',hue='SEX',size='AGE', palette='ch:start=.2,rot=-.3',ax=ax[2,0])  # Cari palette lain yang disediakan oleh matplotlib 
ax[2,0].set_title('7.Diabetes and S5 (Trigliserida) Correlations', fontweight='bold')
ax[2,0].set_ylabel('Diabetes Progress')
ax[2,0].set_xlabel('S5')
ax[2,0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# 8.Correlations between column Y and column S6:
sns.scatterplot(data= diabetes, x='Y', y='S6',hue='SEX',size='AGE', palette='ch:start=.5, rot=-.75',ax=ax[2,1])  # Cari palette lain yang disediakan oleh matplotlib 
ax[2,1].set_title('8.Diabetes and S6 (Gula Darah) Correlations', fontweight='bold')
ax[2,1].set_ylabel('Diabetes Progress')
ax[2,1].set_xlabel('S6')
ax[2,1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.show()