import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dados dos pontos 3D
data = [
    [0.0040106999, 0.0015723430, -0.0030787174],
    [0.0013577836, 1.4664854805, -0.0002735983],
    [0.7795888759, 1.4656860934, 0.0018643970],
    [0.7783916484, -0.0011725950, 0.0016910910],
    [-0.0015136248, -0.0004110288, 0.4560298087],
    [-0.0009480126, 1.4654112552, 0.4498028609],
    [0.7801485176, 1.4676494054, 0.4457739916],
    [0.7823768551, -0.0016201118, 0.4491580505],
    [0.0002223853, 0.0008604155, 0.9077355917],
    [-0.0032767154, 1.4643818642, 0.9040679833],
    [0.7859380907, 1.4664276940, 0.9016854725],
    [0.7797204682, 0.0007359357, 0.9015623184]
]

# Separando os dados em coordenadas x, y e z
x = [point[0] for point in data]
y = [point[1] for point in data]
z = [point[2] for point in data]

# Criação da figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotagem dos pontos
ax.scatter(x, y, z, c='b', marker='o')

# Rótulos dos eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibição do gráfico 3D
plt.show()
