import math

solution = [0]

def genTour(total_distance, solution):
  file = open(r'C:\Users\Administrator\Desktop\ALNS\output\init_solution.opt.tour','w+')
  file.write('''NAME: Yildiz
COMMENT: Tour length {}
TYPE: TOUR
DIMENSION: {}
TOUR_SECTION
'''.format(str(total_distance), str(len(solution) - 1))
)
  for node_id in solution[0:-1]:
    file.write(str(node_id))
    file.write('\n')

  file.write('-1\n')
  file.write('EOF')
  file.close()


def cal_distance(node1, node2):
  node1_x = node1['Customer_Latitude']
  node1_y = node1['Customer_Longitude']
  node2_x = node2['Customer_Latitude']
  node2_y = node2['Customer_Longitude']

  dis_x = abs(node1_x - node2_x)
  dis_y = abs(node1_y - node2_y)
  distance = math.sqrt(dis_x**2 + dis_y**2)
  return distance


def initSolution(data):
  remain_nodes = []
  for i in range(1, len(data)):
    remain_nodes.append(i)

  total_distance = 0
  for i in range(1, len(remain_nodes) + 1):
    min_node = -1
    min_dis = 100000000
    for node in remain_nodes:
      distance = cal_distance(data[solution[-1]], data[node])
      if distance < min_dis:
        min_node = node
        min_dis = distance

    solution.append(min_node)
    remain_nodes.remove(min_node)
    total_distance += min_dis

  solution.append(0)
  total_distance += cal_distance(data[solution[-2]], data[0])
  genTour(total_distance, solution)

  return total_distance, solution

