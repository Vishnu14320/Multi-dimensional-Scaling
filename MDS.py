import zipfile
import cv2
import numpy as np
from sklearn import manifold
import matplotlib.pyplot as plt

imgs = []
ziplocation = "/content/output.zip"
with zipfile.ZipFile(ziplocation) as MZ:
    for s, filename in enumerate(MZ.namelist()):
        if s >= 100:
            break
        if filename.endswith(".png"):
            with MZ.open(filename) as fil:
                dataimg = fil.read()
                arrimg = np.frombuffer(dataimg, np.uint8)
                imag = cv2.imdecode(arrimg, cv2.IMREAD_COLOR)
                imgs.append(imag)

imagefeatures = []
for imag in imgs:
    histos = cv2.calcHist([imag], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    imagefeatures.append(histos.flatten())
dis_mat = np.zeros((len(imgs), len(imgs)))
for l in range(len(imgs)):
    for k in range(len(imgs)):
        dis = np.linalg.norm(imagefeatures[l] - imagefeatures[k])
        dis_mat[l][k] = dis

mdsss = manifold.MDS(n_components=2, dissimilarity="precomputed", normalized_stress=False)
resultformds = mdsss.fit_transform(dis_mat)
plt.scatter(resultformds[:, 0], resultformds[:, 1])
plt.show()
