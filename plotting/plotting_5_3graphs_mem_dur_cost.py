import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams
import matplotlib.lines as mlines

red_X = mlines.Line2D([], [], color='red', marker='X', label='Result')

values_linear = [[10706.4, 128, 2.2309461000000004e-05], [5745, 256, 2.3942287500000002e-05],

[3788, 384, 2.3679735e-05], [2965, 512, 2.4713275000000004e-05], [2253, 640,

2.3473443750000003e-05], [1984, 768, 2.480496e-05], [1511, 896, 2.2039823750000002e-05], [1336, 1024, 2.2271120000000002e-05], [1351, 1152, 2.533631625e-05], [1202, 1280,

2.5046675e-05], [959, 1408, 2.1981478750000003e-05], [967, 1536, 2.4179835e-05], [919, 1664, 2.4894561250000003e-05], [833, 1792, 2.4300692500000002e-05], [788, 1920,

2.4629925e-05], [775, 2048, 2.58385e-05]]

values_bin = [[11015.2, 128, 2.2952923000000005e-05], [780.6, 5184, 6.587629762500001e-05],

[12173.6, 128, 2.5366739000000002e-05], [747.2, 2656, 3.230729350000001e-05], [12300.400000000001, 128, 2.5630958500000006e-05], [1117.4, 1392, 2.532115696875e-05], [1068.2, 1392, 2.4206246531250003e-05], [773.4000000000001, 2024,

2.5482986203125e-05], [1081.6, 1392, 2.4509901e-05], [893.0, 1708, 2.48298998828125e-05], [1078.0, 1392, 2.44283221875e-05], [952.6, 1550, 2.4036870214843752e-05], [898.0, 1550,

2.2659153320312505e-05], [876.5999999999999, 1629, 2.3246533142578127e-05], [1016.6000000000001, 1550, 2.5651776464843755e-05], [878.5999999999999, 1589,

2.2727451482421877e-05], [859.2, 1589, 2.2225616109375003e-05], [851.5999999999999, 1609, 2.230628979296875e-05], [865.3999999999999, 1589, 2.2385996486328125e-05], [997.0, 1599, 2.5952503916015626e-05], [857.0, 1589, 2.2168706943359377e-05], [928.8, 1594, 2.4101616234375003e-05], [995.4000000000001, 1589, 2.5748810841796878e-05], [869.4, 1591, 2.2517774138671876e-05], [869.5999999999999, 1591,

2.2522954210937498e-05], [931.4000000000001, 1592, 2.4138759078125e-05], [929.0, 1591,

2.406143567382813e-05], [922.4000000000001, 1591, 2.3890493289062504e-05], [936.5999999999999, 1591, 2.4258278419921877e-05], [929.8000000000001, 1591,

2.408215596289063e-05], [932.5999999999999, 1591, 2.4154676974609376e-05], [926.2, 1591, 2.398891466210938e-05], [942.2, 1591, 2.440332044335938e-05], [926.0, 1591,

2.3983734589843755e-05], [924.6, 1591, 2.3947474083984377e-05], [936.0, 1591,

2.4242738203125004e-05]]

value_gd = [[1507.2, 1024, 2.5125024000000003e-05], [1572.4, 896, 2.2935419500000004e-05], [1823.8000000000002, 791, 2.3484933677734378e-05], [2354.0, 663,

2.5407131191406252e-05], [1545.8, 994, 2.501354988671875e-05], [1644.0, 866, 2.3176900078125005e-05], [1860.6, 797, 2.4140540033203125e-05], [2225.2, 669,

2.4234318550781248e-05], [1481.6, 944, 2.27687195e-05], [1721.1999999999998, 816,

2.28642594375e-05]]


values_linear_dur = [[11593.0, 128, 2.4156913750000002e-05], [5164, 256, 2.152097e-05], [3777, 384,

2.361097125e-05], [2755, 512, 2.2962925000000002e-05], [2089, 640,

2.1764768750000005e-05], [2080, 768, 2.6005200000000003e-05], [1697, 896,

2.475286625e-05], [1516, 1024, 2.5271720000000002e-05], [1356, 1152, 2.5430085e-05], [1064, 1280, 2.2171100000000002e-05], [1076, 1408, 2.4663265000000002e-05], [991, 1536,

2.4779955000000004e-05], [961, 1664, 2.6032288750000002e-05], [874, 1792,

2.5496765e-05], [833, 1920, 2.6036456250000003e-05], [778, 2048,

2.5938520000000004e-05], [816, 2176, 2.8905780000000002e-05]]

values_bin_dur = [[844.6, 5184, 7.127737762500001e-05], [11491.8, 128, 2.394603825e-05], [810.8,

7712, 0.000101792646125], [793.4000000000001, 5184, 6.695651362500002e-05], [824.8, 6448, 8.6578353875e-05], [850.6, 5184, 7.1783728875e-05], [847.8, 7080,

9.7715242265625e-05], [768.8, 6448, 8.0700095125e-05], [819.6, 6764,

9.024874926562502e-05], [872.0, 6448, 9.153288625e-05], [772.6, 6922,

8.706065734765627e-05], [817.2, 6764, 8.998447767187502e-05], [833.8, 7001,

9.502931781835939e-05], [879.0, 6922, 9.905037251953126e-05], [835.8, 7040,

9.578790375000002e-05], [802.5999999999999, 7001, 9.147341146679687e-05], [865.8, 7020, 9.89441989453125e-05], [848.2, 7001, 9.667050536523438e-05], [791.0, 7010,

9.026723603515626e-05], [867.8, 7001, 9.890434397070313e-05], [768.0, 7015,

8.770503750000001e-05], [851.8, 7010, 9.720560259765626e-05], [851.8, 7017,

9.730266953320313e-05], [829.4000000000001, 7015, 9.47168725292969e-05], [772.6, 7016, 8.824293151562501e-05], [851.8, 7015, 9.727493612304688e-05], [833.4000000000001, 7016, 9.518723676562502e-05], [782.5999999999999, 7016, 8.9385086984375e-05]]


values_gd_dur = [[1458.4, 1024, 2.4311528000000003e-05], [1690.8000000000002, 896,

2.4662431500000006e-05], [1187.6, 1196, 2.3122618390625e-05], [1270.2, 1068,

2.2084064367187504e-05], [1370.0, 1023, 2.281559736328125e-05], [1661.2, 895,

2.420363533203125e-05], [1115.0, 1199, 2.1763547802734376e-05], [1406.1999999999998, 1071, 2.451727552148437e-05], [954.4000000000001, 1452, 2.2559667281250002e-05], [1153.4, 1324, 2.4860140304687504e-05], [901.8, 1657, 2.4325870060546876e-05], [962.2, 1529, 2.395016342382813e-05], [1048.2, 1438, 2.4537973019531252e-05], [1031.6, 1310,

2.19997766796875e-05], [1067.4, 1285, 2.232883010742188e-05], [1303.4, 1157,

2.454972992773438e-05], [977.0, 1433, 2.2791683076171878e-05], [1083.8, 1305,

2.3024770048828127e-05], [1224.4, 1220, 2.4317492734375e-05], [1391.1999999999998, 1092, 2.4731351531250002e-05], [1038.6, 1364, 2.30620724296875e-05], [1220.8000000000002, 1236, 2.456397431250001e-05], [903.0, 1507,

2.2153209052734375e-05], [1109.8, 1379, 2.4914067103515624e-05], [980.4, 1706,

2.72281398515625e-05], [959.0, 1578, 2.4635492519531253e-05]]

values_optimal = [[10774, 128, 2.2450322500000002e-05, 0.5826226993865031], [5419, 256,

2.25836825e-05, 0.3345985535502989], [3573, 384, 2.2335716250000003e-05,

0.2480167732247936], [2933, 512, 2.4446555e-05, 0.226084045777098], [2070, 640,

2.1566812500000002e-05, 0.17543576560704538], [1947, 768, 2.4342367500000004e-05,

0.1799423031588202], [1692, 896, 2.4679935000000003e-05, 0.16935058952420107], [1483, 1024, 2.472161e-05, 0.15980468772243106], [1362, 1152, 2.5542607500000002e-05,

0.15721078977907504], [1259, 1280, 2.62344125e-05, 0.1549767760605229], [1093, 1408,

2.5052926250000002e-05, 0.14292488534656828], [925, 1536, 2.3129625e-05,

0.1280501172443089], [942, 1664, 2.5517602500000005e-05, 0.13762739713078861], [906, 1792, 2.6430285000000002e-05, 0.1393156041413036], [896, 1920,

2.8005600000000002e-05, 0.14464906996051619], [848, 2048, 2.8272320000000005e-05,

0.1434030801258654], [840, 2176, 2.9755950000000004e-05, 0.148491938670806]]

values_dur_change =[[11908.400000000001, 128, 2.4814128500000005e-05], [5570, 256, 2.3212975e-05], [3923, 384, 2.4523653750000002e-05], [2976, 512, 2.480496e-05], [2221, 640,

2.3140043750000003e-05], [1767, 768, 2.2091917500000002e-05], [1674, 896,

2.44173825e-05], [1343, 1024, 2.238781e-05], [1282, 1152, 2.4042307500000002e-05], [1147, 1280, 2.39006125e-05], [995, 1408, 2.280664375e-05], [897, 1536, 2.2429485e-05]]

df_linear = pd.DataFrame(np.array(values_linear), columns=['duration', 'memory', 'cost'])
df_bin = pd.DataFrame(np.array(values_bin), columns=['duration', 'memory', 'cost'])
df_gd = pd.DataFrame(np.array(value_gd), columns=['duration', 'memory', 'cost'])

df_linear_dur = pd.DataFrame(np.array(values_linear_dur), columns=['duration', 'memory', 'cost'])
df_bin_dur = pd.DataFrame(np.array(values_bin_dur), columns=['duration', 'memory', 'cost'])
df_gd_dur = pd.DataFrame(np.array(values_gd_dur), columns=['duration', 'memory', 'cost'])

df_optimal = pd.DataFrame(np.array(values_optimal), columns=['duration', 'memory', 'cost', 'test'])
df_dur_chage = pd.DataFrame(np.array(values_dur_change), columns=['duration', 'memory', 'cost'])


fig = plt.figure()

rcParams['figure.figsize'] = 5, 3
rcParams['axes.labelsize'] = 12
rcParams['axes.titlesize'] = 20
rcParams["font.size"] = 10

# plt.plot( df["memory"], "-x", color="#0065bd", label='Memory', linewidth=3.0)
# plt.ylabel('Memory(MB)', color='#0065bd')
# plt.plot( df["duration"], "-x", color="#e37222", label='Duration', linewidth=3.0)
# plt.ylabel('Duration(ms)', color='#e37222')
# plt.plot( df_linear["duration"], "--", color="darkorange", label='Linear', linewidth=2.0)
# plt.plot( df_bin["duration"], "-.", color="royalblue", label='Binary', linewidth=2.0)
# plt.plot( df_gd["duration"], "-1", color="darkgreen", label='Gradient decent', linewidth=2.0)
# plt.ylabel('Duration (ms)', color='black')
# plt.plot(10, df_linear["duration"][10], 'rX', markersize=6)
# plt.plot(24, df_bin["duration"][24], 'rX', markersize=6)
# plt.plot(8, df_gd["duration"][8], 'rX', markersize=6)
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_bin)+1, 1.0), rotation=90, ha='center')
# #plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_duration_cost_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')


# plt.plot( df_linear["memory"], "--", color="darkorange", label='Linear', linewidth=2.0)
# plt.plot( df_bin["memory"], "-.", color="royalblue", label='Binary', linewidth=2.0)
# plt.plot( df_gd["memory"], "-1", color="darkgreen", label='Gradient decent', linewidth=2.0)
# plt.plot(10, df_linear["memory"][10], 'rX', markersize=6)
# plt.plot(24, df_bin["memory"][24], 'rX', markersize=6)
# plt.plot(8, df_gd["memory"][8], 'rX', markersize=6)
# plt.ylabel('Memory (in MB)', color='black')
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_bin)+1, 1.0), rotation=90, ha='center')
# #plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_memory_cost_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')

#
# plt.plot( df_linear["cost"], "--", color="darkorange", label='Linear', linewidth=2.0)
# plt.plot( df_bin["cost"], "-.", color="royalblue", label='Binary', linewidth=2.0)
# plt.plot( df_gd["cost"], "-1", color="darkgreen", label='Gradient decent', linewidth=2.0)
# plt.plot(10, df_linear["cost"][10], 'rX', markersize=6)
# plt.plot(24, df_bin["cost"][24], 'rX', markersize=6)
# plt.plot(8, df_gd["cost"][8], 'rX', markersize=6)
# plt.ylabel('Cost (in $)', color='black')
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_bin)+1, 1.0), rotation=90, ha='center')
# #plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_cost_cost_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')

#
#
#
#
#
# plt.plot( df_linear_dur["duration"], "--", color="darkorange", label='Linear', linewidth=2.0)
# plt.plot( df_bin_dur["duration"], "-.", color="royalblue", label='Binary', linewidth=2.0)
# plt.plot( df_gd_dur["duration"], "-1", color="darkgreen", label='Gradient decent', linewidth=2.0)
# plt.ylabel('Duration (ms)', color='black')
# plt.plot(15, df_linear_dur["duration"][15], 'rX', markersize=6)
# plt.plot(24, df_bin_dur["duration"][24], 'rX', markersize=6)
# plt.plot(10, df_gd_dur["duration"][10], 'rX', markersize=6)
# plt.legend()
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_bin_dur)+1, 1.0), rotation=90, ha='center')
# #plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_duration_dur_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')

#
# plt.plot( df_linear_dur["memory"], "--", color="darkorange", label='Linear', linewidth=2.0)
# plt.plot( df_bin_dur["memory"], "-.", color="royalblue", label='Binary', linewidth=2.0)
# plt.plot( df_gd_dur["memory"], "-1", color="darkgreen", label='Gradient decent', linewidth=2.0)
# plt.plot(15, df_linear_dur["memory"][15], 'rX', markersize=6)
# plt.plot(24, df_bin_dur["memory"][24], 'rX', markersize=6)
# plt.plot(10, df_gd_dur["memory"][10], 'rX', markersize=6)
# plt.ylabel('Memory (in MB)', color='black')
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_bin_dur)+1, 1.0), rotation=90, ha='center')
# #plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_memory_dur_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')

#
# plt.plot( df_linear_dur["cost"], "--", color="darkorange", label='Linear', linewidth=2.0)
# plt.plot( df_bin_dur["cost"], "-.", color="royalblue", label='Binary', linewidth=2.0)
# plt.plot( df_gd_dur["cost"], "-1", color="darkgreen", label='Gradient decent', linewidth=2.0)
# plt.plot(15, df_linear_dur["cost"][15], 'rX', markersize=6)
# plt.plot(24, df_bin_dur["cost"][24], 'rX', markersize=6)
# plt.plot(10, df_gd_dur["cost"][10], 'rX', markersize=6)
# plt.ylabel('Cost (in $)', color='black')
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_bin_dur)+1, 1.0), rotation=90, ha='center')
# #plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_cost_dur_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')

#
#

# plt.plot( df_optimal["duration"], "--", color="darkorange", label='OptimalValues', linewidth=2.0)
# plt.plot( df_dur_chage["duration"], "-.", color="royalblue", label='Duration Change', linewidth=2.0)
# plt.ylabel('Duration (ms)', color='black')
# plt.plot(11, df_optimal["duration"][11], 'rX', markersize=6)
# plt.plot(5, df_dur_chage["duration"][5], 'rX', markersize=6)
# plt.legend()
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_optimal)+1, 1.0), rotation=90, ha='center')
# plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_duration_bal_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')


plt.plot( df_optimal["memory"], "--", color="darkorange", label='OptimalValues', linewidth=2.0)
plt.plot( df_dur_chage["memory"], "-.", color="royalblue", label='Duration Change', linewidth=2.0)
plt.plot(11, df_optimal["memory"][11], 'rX', markersize=6)
plt.plot(5, df_dur_chage["memory"][5], 'rX', markersize=6)
plt.ylabel('Memory (in MB)', color='black')
plt.legend()
plt.xlabel('Iterations')
plt.xticks(np.arange(0, len(values_optimal)+1, 1.0), rotation=90, ha='center')
#plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
plt.show()
fig.savefig("../images/5_combined_memory_bal_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')


# plt.plot( df_optimal["cost"], "--", color="darkorange", label='OptimalValues', linewidth=2.0)
# plt.plot( df_dur_chage["cost"], "-.", color="royalblue", label='Duration Change', linewidth=2.0)
# plt.plot(11, df_optimal["cost"][11], 'rX', markersize=6)
# plt.plot(5, df_dur_chage["cost"][5], 'rX', markersize=6)
# plt.ylabel('Cost (in $)', color='black')
# plt.legend()
# plt.xlabel('Iterations')
# plt.xticks(np.arange(0, len(values_optimal)+1, 1.0), rotation=90, ha='center')
# #plt.grid(axis="both", color="0.9", linestyle='-', linewidth=0.6)
# plt.show()
# fig.savefig("../images/5_combined_cost_bal_obj.pdf", format='pdf', dpi=300, bbox_inches='tight')
#
#
