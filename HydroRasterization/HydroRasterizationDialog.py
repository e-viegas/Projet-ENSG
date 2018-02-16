"""
/***************************************************************************
Name			 	 : Hydrology and raster
Description          : To rasterize the hydrological data and the land use of a watershed
Date                 : 16/Feb/18 
copyright            : (C) 2018 by M. Méchu, P. Roux and E. Viegas
email                : erwan.vigas@ensg.eu 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_HydroRasterization import Ui_HydroRasterization
# create the dialog for HydroRasterization
class HydroRasterizationDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_HydroRasterization ()
    self.ui.setupUi(self)