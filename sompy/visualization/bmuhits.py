from collections import Counter

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from .mapview import MapView


class BmuHitsView(MapView):
    def _set_labels(self, cents, ax, labels, onlyzeros, fontsize):
        for i, txt in enumerate(labels):
            if onlyzeros == True:
                if txt > 0:
                    txt = ""
            ax.annotate(txt, (cents[i, 1] + 0.5, cents[-(i+1), 0] + 0.5), va="center", ha="center", size=fontsize)

    def show(self, som, anotate=True, onlyzeros=False, labelsize=7, cmap="jet", logaritmic = False):
        (self.width, self.height, indtoshow, no_row_in_plot, no_col_in_plot,
         axis_num) = self._calculate_figure_params(som, 1, 1)

        #self.prepare()
        #ax = plt.gca()
        counts = Counter(som._bmu[0])
        counts = [counts.get(x, 0) for x in range(som.codebook.mapsize[0] * som.codebook.mapsize[1])]
        #print "counts.shape: ", len(counts)
        mp = np.array(counts).reshape(som.codebook.mapsize[0],
                                      som.codebook.mapsize[1])
        #print "mp.shape: ", mp.shape
        if not logaritmic:
            norm = matplotlib.colors.Normalize(
                vmin=0,
                vmax=np.max(mp.flatten()),
                clip=True)
        else:
            norm = matplotlib.colors.LogNorm(
                vmin=1,
                vmax=np.max(mp.flatten()))

        msz = som.codebook.mapsize
        #print "msz= ", msz

        cents = som.bmu_ind_to_xy(np.arange(0, msz[0] * msz[1]))

        #if anotate:
         #   self._set_labels(cents, ax, counts, onlyzeros, labelsize)

        #print mp[::-1]
        #print mp
        #pl = plt.pcolor(mp[::-1], norm=norm, cmap=cmap)
	#print mp
	#print mp[::-1]
        #plt.axis([0, som.codebook.mapsize[1], 0, som.codebook.mapsize[0]])
        #ax.set_yticklabels([])
        #ax.set_xticklabels([])
        #plt.colorbar(pl)
	return mp
        #plt.show()
        #return mp[::-1]
