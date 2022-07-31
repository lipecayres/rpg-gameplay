require(SixSigma)
require(qcc)

# Target do processo
y0 <- 0.136

# Variacao aceitavel do processo
delta <- 0.05

# Custo de perda do processo
L0 <- 0.0051

# Constante K
k= L0/delta

# Inserindo dados para função perda de taguchi
perda_pesos <- c(0.1418, 0.1385, 0.1402, 0.1415, 0.1371, 0.1463, 0.1391, 0.1311, 0.1463, 0.1445, 0.1529, 0.1274, 0.1403, 0.1431, 0.1394, 0.1381, 0.1439, 0.1560, 0.1492, 0.1420, 0.1286, 0.1464, 0.1423, 0.1320, 0.1417, 0.1409, 0.1436, 0.1348, 0.1486, 0.1488, 0.1500, 0.1473, 0.1528, 0.1491, 0.1511, 0.1404, 0.1443, 0.1393, 0.1318, 0.1398, 0.1376, 0.1499, 0.1302, 0.1416, 0.1467, 0.1373, 0.1526, 0.1475, 0.1378, 0.1498, 0.1472, 0.1398, 0.1436, 0.1444, 0.1478, 0.1415, 0.1371, 0.1651, 0.1421, 0.1332, 0.1408, 0.1500, 0.1459, 0.1312, 0.1358, 0.1368, 0.1362, 0.1510, 0.1549, 0.1423, 0.1320, 0.1441, 0.1453, 0.1481, 0.1545, 0.1495, 0.1385, 0.1389, 0.1387, 0.1406, 0.1464, 0.1436, 0.1371, 0.1519, 0.1434, 0.1413, 0.1597, 0.1393, 0.1403, 0.1496, 0.1350, 0.1528, 0.1423, 0.1283, 0.1483, 0.1117, 0.1608, 0.1556, 0.1344, 0.1413, 0.1461, 0.1481, 0.1418, 0.1349, 0.1287, 0.1354, 0.1481, 0.1317, 0.1338, 0.1370, 0.1488, 0.1346, 0.1499, 0.1484, 0.1566, 0.1398, 0.1511, 0.1408)
pesos <- data.frame(perda_pesos)

# Average Loss 
aL <- k *(sum((pesos$perda_pesos-0.136)^2))/length(pesos$perda_pesos)
print(aL)

# Perda Esperada por minuto - pem
prod.m <- 7168  

pem <- prod.m * aL
print(pem)

# Analise SixSigma - Loss Function
ss.lfa(pesos, "perda_pesos", delta, y0, L0,
       lfa.sub = "Função Perda de Taguchi",
       lfa.size = prod.m, lfa.output = "both")

help("ss.lfa")


# Taguchi Function -> L(Y) = k(Y - y0)?


curve(k * (x - y0)^2, 0.105,0.165,
      lty = 1,
      lwd = 2,
      ylab = "Cost of Poor Quality",
      xlab = "Observed value of the characteristic",
      main = expression(L(Y) == 2.04 ~ (Y - 0.136)^2))

abline(v = 0.105, lty = 2)
abline(v = 0.136, lty = 2)
abline(v = 0.165, lty = 2)
abline(h = 0)
text(0.136, 0.0015, "T", adj = 2)
text(0.105, 0.0015, "LSL", adj = 1)
text(0.165, 0.0015, "USL", adj = -0.1)

