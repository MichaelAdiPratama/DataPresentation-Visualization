import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import random,string

plt.rcParams.update({'font.size': 8, 'font.family': 'sans'})

jobs = pd.read_excel('job_performance - Copy.xlsx')
print(jobs)
fig, ax = plt.subplots(nrows=2, ncols=3, sharex=False, sharey=False, constrained_layout = True)  
fig.set_figheight(5)
fig.set_figwidth(5)


# 1.Correlations between GRIP and ARM:
sns.regplot(data= jobs, x='GRIP', y='ARM',color='red', ax=ax[0,0])  
ax[0,0].set_title('1.GRIP and ARM Correlations')
ax[0,0].set_ylabel('ARM')
ax[0,0].set_xlabel('GRIP')

# 2.Correlations between GRIP and RATINGS:
sns.regplot(data= jobs, x='GRIP', y='RATINGS',color='green', ax=ax[0,1])   
ax[0,1].set_title('2.GRIP and RATINGS Correlations')
ax[0,1].set_ylabel('RATINGS')
ax[0,1].set_xlabel('GRIP')

# 3.Correlations between GRIP and RATINGS:
sns.regplot(data= jobs, x='ARM', y='RATINGS', ax=ax[0,2])  
ax[0,2].set_title('3.ARM and RATINGS Correlations')
ax[0,2].set_ylabel('RATINGS')
ax[0,2].set_xlabel('ARM')

# 4.Correlations between GRIP and RATINGS:
sns.regplot(data= jobs, x='ARM', y='SIMS',color='red', ax=ax[1,0])  
ax[1,0].set_title('4.ARM and SIMS Correlations')
ax[1,0].set_ylabel('SIMS')
ax[1,0].set_xlabel('ARM')

# 5.Correlations between GRIP and RATINGS:
sns.regplot(data= jobs, x='GRIP', y='SIMS',color='green', ax=ax[1,1])  
ax[1,1].set_title('5.GRIP and SIMS Correlations')
ax[1,1].set_ylabel('SIMS')
ax[1,1].set_xlabel('GRIP')

# 6.Correlations between GRIP and RATINGS:
sns.regplot(data= jobs, x='RATINGS', y='SIMS', ax=ax[1,2])  
ax[1,2].set_title('6. RATINGS and SIMS Correlations')
ax[1,2].set_ylabel('SIMS')
ax[1,2].set_xlabel('RATINGS')
plt.show()


# ====================
# HEAT MAP
# ====================
# fig, ax = plt.subplots(nrows=2, ncols=3, sharex=False, sharey=False, constrained_layout = True)  
# fig.set_figheight(5)
# fig.set_figwidth(5)





# Visualisasikan matriks korelasi dengan heatmap
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = jobs
korelasi = data.corr()
sns.heatmap(korelasi, annot=True, cmap='icefire')
plt.title('HeatMap Correlations Between Variable:')
plt.show()

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np


df = jobs


def calculate_score(corr_matrix):
  
    weights = {'ARM': 0.25, 'GRID': 0.25, 'SIMS': 0.25, 'RATINGS': 0.25}

    
    score = 0
    for variable, weight in weights.items():
        score += weight * np.abs(corr_matrix['score'][variable])

    return score


corr_matrix = df.corr()


corr_matrix['score'] = corr_matrix.sum(axis=1) - 1 


df['score'] = df.dot(corr_matrix['score'])

sorted_employees = df.sort_values(by='score')


employees_to_terminate = sorted_employees.head(int(0.25 * len(df)))


print(' 25% Employee dengan Scores terendah:')
print(employees_to_terminate)
