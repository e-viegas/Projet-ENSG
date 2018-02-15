import numpy as np
import processing as pcs


class Raster(object):
    def __init__(
            self, name, wshd,
            ncols, nrows, xll, yll,
            size, nodata=-9999, mat=None
    ):
        """
        Constructeur d'un objet de type RASTER
        :param name: nom du raster
        :param wshd: valeur du watershed (en m)
        :param ncols: nombre de colonnes
        :param nrows: nombre de lignes
        :param xll: coordonnee X du coin nord-ouest
        :param yll: coordonnee Y du coin nord-ouest
        :param size: resolution de la rasteurization
        :param nodata: valeur = None
        :param mat: matrice du raster
        """

        self.name = name
        self.watershed = wshd
        self.ncols = ncols
        self.nrows = nrows
        self.xll = xll
        self.yll = yll
        self.cellsize = size
        self.nodata = nodata
        self.mat = mat

    def __str__(self):
        """
        Afficher un raster
        :return: Chaine de caracteres correspondant a un raster
        """

        return "Raster {name=%s dim=(%d, %d) coord=(%d, %d)}" % (
            self.name, self.ncols, self.nrows,
            self.xll, self.yll
        )

    def __repr__(self):
        return str(self)

    def sauvegarder(self, out):
        res = [
            "%s file Watershed %s m" % (self.name, self.watershed),
            "ncols %d" % self.ncols,
            "nrows %d" % self.nrows,
            "xllcorner %f" % self.xll,
            "yllcorner %f" % self.yll,
            "cellsize %d" % self.cellsize,
            "NODATA_value %d" % self.nodata
        ]

        for i in range(self.mat.shape[0]):
            res.append(" ".join([
                "%d" % self.mat[i, j] for j in range(self.mat.shape[1])
            ]))

        with open(out, "w") as fch:
            fch.write("\n".join(res))

def raster_couv_sol(self, shp_couv, out):
    chemin = shp_couv.split("/")
    dossier = chemin[: -1]
    out = "%s/%s" % (dossier, out)

    pcs.runalg(
        "gdalogr:rasterize", shp_couv,
        "ELEV", 0, 1000, 1000, out      # champ, ?, ?, ?, sortie
    )


def lire_raster(chemin):
    try:
        with open(chemin, "r") as fch:
            contenu = fch.readlines()

    except IOError:
        raise IOError("Fichier introuvable !!")

    name, wshd, lst = lire_entete(contenu)
    mat = lire_matrice(lst[1], lst[0], contenu)

    return Raster(
        name, wshd,
        lst[0], lst[1],
        lst[2], lst[3],
        lst[4], lst[5], mat
    )

def lire_entete(contenu):
    entete = contenu[1: 7]
    lst = []

    # Premiere ligne : mask file Watershed 10 m
    first = contenu[0].split()
    k = first.index("file")
    name = " ".join(first[: k])

    # Watershed
    try:
        wshd = float(first[k + 2])
    except IndexError:
        raise IndexError("Argument manquant a la ligne 0 !!")
    except ValueError:
        raise ValueError("Argument invalide a la ligne 0 !!")

    # Le reste de l'entete
    for line in entete:
        try:
            lst.append(int(line[: -1].split()[1]))
        except ValueError:
            try:
                lst.append(float(line[: -1].split()[1]))
            except ValueError:
                raise ValueError("Argument invalide !!")

    return name, wshd, lst

def lire_matrice(n, p, lst):
    mat = np.zeros((n, p))

    for k in range(7, len(lst)):
        line = lst[k].split()

        for j in range(len(line)):
            try:
                mat[k - 7, j] = int(line[j])
            except ValueError:
                raise ValueError("Valeur incorrecte !!")

    return mat


if __name__ == "__main__":
    chemin = "mask.asc"
    raster = lire_raster(chemin)
    print(raster)
    raster.sauvegarder("test.asc")
