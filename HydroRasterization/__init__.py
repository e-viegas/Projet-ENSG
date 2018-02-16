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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Hydrology and raster" 
def description():
  return "To rasterize the hydrological data and the land use of a watershed"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load HydroRasterization class from file HydroRasterization
  from HydroRasterization import HydroRasterization 
  return HydroRasterization(iface)
