import pandas as pd 
import statistics
import csv

df = pd.read_csv("data.csv")

mathlist = df["math score"].to_list()
writinglist = df["writing score"].to_list()
readinglist = df["reading score"].to_list()

mathMean = statistics.mean(mathlist)
writingMean = statistics.mean(writinglist)
readingMean = statistics.mean(readinglist)

mathMedian = statistics.median(mathlist)
readingMedian = statistics.median(readinglist)
writingMedian = statistics.median(writinglist) 

mathMode = statistics.mode(mathlist)
readingMode = statistics.mode(readinglist)
writingMode = statistics.mode(writinglist)

mathstdDeviation = statistics.stdev(mathlist)
writingstdDeviation = statistics.stdev(writinglist)
readingstdDeviation = statistics.stdev(readinglist)

math1stdDevStart, math1stdDevEnd = mathMean - mathstdDeviation, mathMean + mathstdDeviation
math2stdDevStart, math2stdDevEnd = mathMean - (2*mathstdDeviation), mathMean + (2*mathstdDeviation)
math3stdDevStart, math3stdDevEnd = mathMean - (3*mathstdDeviation), mathMean + (3*mathstdDeviation)

writing1stdDevStart, writing1stdDevEnd = writingMean - writingstdDeviation, writingMean + writingstdDeviation
writing2stdDevStart, writing2stdDevEnd = writingMean - (2*writingstdDeviation), writingMean + (2*writingstdDeviation)
writing3stdDevStart, writing3stdDevEnd = writingMean - (3*writingstdDeviation), writingMean + (3*writingstdDeviation)

reading1stdDevStart, reading1stdDevEnd = readingMean - readingstdDeviation, readingMean + readingstdDeviation
reading2stdDevStart, reading2stdDevEnd = readingMean - (2*readingstdDeviation), readingMean + (2*readingstdDeviation)
reading3stdDevStart, reading3stdDevEnd = readingMean - (3*readingstdDeviation), readingMean + (3*readingstdDeviation)

mathDataWithin1std = [result for result in mathlist if result > math1stdDevStart and result < math1stdDevEnd]
mathDataWithin2std = [result for result in mathlist if result > math2stdDevStart and result < math2stdDevEnd]
mathDataWithin3std = [result for result in mathlist if result > math3stdDevStart and result < math3stdDevEnd]

writingDataWithin1std = [result for result in writinglist if result > writing1stdDevStart and writing1stdDevEnd]
writingDataWithin2std = [result for result in writinglist if result > writing2stdDevStart and writing2stdDevEnd]
writingDataWithin3std = [result for result in writinglist if result > writing3stdDevStart and writing3stdDevEnd]

readingDataWithin1std = [result for result in readinglist if result > reading1stdDevStart and reading1stdDevEnd]
readingDataWithin2std = [result for result in readinglist if result > reading2stdDevStart and reading2stdDevEnd]
readingDataWithin3std = [result for result in readinglist if result > reading3stdDevStart and reading3stdDevEnd]