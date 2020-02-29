import xlrd

def parseXML():
  xml_path = r'C:\Users\Administrator\Desktop\ALNS\data\data.xlsx'
  wb = xlrd.open_workbook(xml_path)
  sheet1 = wb.sheet_by_index(0)

  # column number
  col_nodeid = 0
  col_Customer_Opening_time = 1
  col_Customer_Closing_Time = 2
  col_Customer_demand = 3
  col_Customer_pickup = 4
  col_Customer_Latitude = 5
  col_Customer_Longitude = 6


  # {node_id: {...}}
  data = {}
  for row in range(1, sheet1.nrows):
    node_id = int(sheet1.cell(row, col_nodeid).value)
    data[node_id] = {}
    data[node_id]['Customer_Opening_time'] = int(sheet1.cell(row, col_Customer_Opening_time).value)
    data[node_id]['Customer_Closing_Time'] = int(sheet1.cell(row, col_Customer_Closing_Time).value)
    data[node_id]['Customer_demand'] = int(sheet1.cell(row, col_Customer_demand).value)
    data[node_id]['Customer_pickup'] = int(sheet1.cell(row, col_Customer_pickup).value)
    data[node_id]['Customer_Latitude'] = int(sheet1.cell(row, col_Customer_Latitude).value)
    data[node_id]['Customer_Longitude'] = int(sheet1.cell(row, col_Customer_Longitude).value)

  return data
