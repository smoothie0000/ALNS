def genTSP(data):
  file = open(r'C:\Users\Administrator\Desktop\ALNS\output\data.tsp','w+')
  file.write('''NAME : Yildiz
COMMENT : ALNS solution
TYPE : TSP
DIMENSION : {}
EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
'''.format(len(data))
)
  for i in range(0, len(data)):
    wr_str = ''
    wr_str += str(i) + ' ' + str(data[i]['Customer_Latitude']) + ' ' + str(data[i]['Customer_Longitude'])
    file.write(wr_str)
    file.write('\n')

  file.write('EOF')
  file.close()
