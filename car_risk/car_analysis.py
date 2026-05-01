"""
symboling 保險風險等級該數值代表車輛的風險程度（相對於其價格）。精算師先根據價格給予初始標記，再根據實際理賠風險調高或調低等級（通常為 -3 到 +3）。
normalized-losses標準化賠付損失代表每台車在保險年度內的相對平均理賠支出。數值已經過標準化處理，方便跨車型比較。
make廠牌 / 品牌指汽車製造商，例如 Toyota, BMW, Mazda 等。
fuel-type燃料類型主要是 gas（汽油）或 diesel（柴油）。
aspiration進氣方式std（自然進氣）或 turbo（渦輪增壓）。
num-of-doors車門數通常為 two（兩門）或 four（四門）。
body-style車身型態例如 sedan（轎車）、hatchback（掀背車）、convertible（敞篷車）、wagon（旅行車）等。
drive-wheels驅動方式fwd（前輪驅動）、rwd（後輪驅動）、4wd（四輪驅動）。
engine-location引擎位置front（前置引擎）或 rear（後置引擎，如保時捷 911）。
wheel-base軸距前輪中心點與後輪中心點之間的距離。通常軸距越長，車室空間越大、高速行駛越穩。
"""
import  pandas as pd
import  matplotlib.pyplot as plt

data = pd.read_csv('Automobile_data.csv')
plt.figure(figsize=( 19 , 10 ))


plt.subplot2grid(( 2 , 4 ), ( 0 , 0 ))
data.symboling[ data['num-of-doors'] == 'two'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('two')

plt.subplot2grid(( 2 , 4 ), ( 0 , 1 ))
data.symboling[ data['num-of-doors'] == 'four'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('four')

plt.subplot2grid(( 2 , 4 ), ( 0 , 2 ))
data.symboling[ data['engine-location'] == 'front'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('front')

plt.subplot2grid(( 2 , 4 ), ( 0 , 3 ))
data.symboling[ data['engine-location'] == 'rear'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('rear')


plt.subplot2grid(( 2 , 4 ), ( 1 , 0 ))
data.symboling[ data['aspiration'] == 'std'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('std')

plt.subplot2grid(( 2 , 4 ), ( 1 , 1 ))
data.symboling[ data['aspiration'] == 'turbo'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('turbo')

plt.subplot2grid(( 2 , 4 ), ( 1 , 2 ))
data.symboling[ data['fuel-type'] == 'gas'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('gas')

plt.subplot2grid(( 2 , 4 ), ( 1 , 3 ))
data.symboling[ data['fuel-type'] == 'diesel'].value_counts( normalize = True ).sort_index().plot( kind='bar')
plt.title('diesel')
plt.show()