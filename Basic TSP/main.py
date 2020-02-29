import parseXML
import genTSP
import initSolution

data = parseXML.parseXML()
genTSP.genTSP(data)
distance, solution = initSolution.initSolution(data)

print(distance)
print(solution)