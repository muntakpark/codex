import numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt

mpl.rc('font', family='Pretendard')
mpl.rc('axes', unicode_minus=False)

exim = pd.read_csv('D:\codes\sts\exim_krcn.csv')
exim['EXCN_RATIO'] = exim['EXPORT_CN']/exim['EXPORT']
exim_dates = pd.Series(pd.date_range('2021-01-01', periods=24, freq='M')).dt.strftime('%y/%m')

fig, axk = plt.subplots(figsize=(15, 5))
axc = axk.twinx()

axk.set_title('한국 수출입과 대중국 수출 비중')
axk.plot(exim_dates, exim['EXPORT'], lw=2, marker='o', ms=4, label='KR_EX')
axk.plot(exim_dates, exim['IMPORT'], lw=2, marker='o', ms=4, label='KR_IM')
axc.plot(exim_dates, exim['EXCN_RATIO'], '--r', marker='x', lw=1, ms=2, label='CN_RATIO')
axc.set_ylabel('중국 수출이 차지하는 비율 (%)')
fig.legend()
plt.xticks(exim_dates)

plt.grid()
plt.show()