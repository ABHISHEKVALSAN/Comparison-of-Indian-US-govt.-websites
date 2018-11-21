import numpy as np
import matplotlib.pyplot as plt
import sys
from pylab import *

ind	=[	490.01477436968, 0.124501348964188, 0.271342155130882, 1.33145977196082, 58.476955195118, 44.9596916653284,\
		2923.75988167656, 84.4220031797013, 37.4881965633531, 11.2018628553075, 10.6650072265939]

eind=[	1207.35721835792, 0.933810357100132, 0.745291972954829, 3.87418306426826, 164.27071425647, 69.0802441289281,\
 		8678.44616464139, 22.3640534779479, 59.68863675176, 4.57842498331033, 53.112072630305]

usa	=[	544.8088235294117, 0.1613031836106031, 0.168198305208443, 0.5245098039215687, 30.95098039215686, 62.28186274509804,\
		1898.0973785998774, 80.88276651931785, 25.730392156862745, 5.044117647058823, 5.0245098039215685]

eusa=[	372.5016551096119, 0.2240744236445323, 0.101846073397447, 1.4516343915623589, 50.6830070627344, 34.42128651223879,\
		3000.011082193864, 21.243980475197443, 23.810338375833794, 3.0715351443572847, 16.12920828974023]

b18	=[	597.961325966851, 1.20941463305307, 0.263530270897063, 0.519337016574586, 22.2430939226519, 29.5359116022099,\
		3234.79961045407, 74.9498683548821, 30.8839779005525, 7.97790055248619,	4.19889502762431]

eb18=[	1093.00357000861, 13.1064831934754, 0.369497128439535, 4.03813923074724, 37.6512729508433, 41.7942723730434,\
		6608.11853235636, 26.6774076382953, 50.2731739563354, 4.13784136034583, 12.6180734088065]

Country = ['INDIA', 'US', 'BEST OF 2018']

x_pos = np.arange(len(Country))

for mno in range(11):
	col='red'
	if mno in [1,4,6,9,10]:
		col='blue'
	CTEs = [ind[mno],usa[mno],b18[mno]]
	error = [[min(ind[mno],eind[mno]),min(usa[mno],eusa[mno]),min(b18[mno],eb18[mno])],[eind[mno],eusa[mno],eb18[mno]]]
	fig, ax = plt.subplots()
	ax.bar(x_pos, CTEs, yerr=error, align='center', color=col,alpha=0.5, ecolor='black', capsize=20)
	ax.set_xticks(x_pos)
	lprop = {'fontsize':20,'weight':'bold'}
	ax.set_xticklabels(Country,fontdict=lprop)
	ax.yaxis.set_tick_params(labelsize=20)
	ax.yaxis.grid(True)
	plt.tight_layout()
	plt.savefig(str(mno)+'.png')
	plt.show()
