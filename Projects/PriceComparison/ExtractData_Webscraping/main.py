import MainPackages.makescrapy as ms
from MainPackages.managerbrowser import OpenGoogleWindow, DefGoogleUrl
from MainPackages.dataAnalysis import BuildSeparatedPlot

#-----Main------
product = input('What do you want to search? ')

browser = OpenGoogleWindow(Show=True) 

ML_dataframe = ms.MLScrap(browser, product)
DefGoogleUrl(browser)

AMZ_dataframe = ms.AmazonScrap(browser, product)
DefGoogleUrl(browser)

BuildSeparatedPlot(ML_dataframe,AMZ_dataframe)

browser.close()


"""
Created by: Gabriel Zuany Duarte Vargas.
Date: 08/10/2022 (Last update).
Protected by GNU V3.0.

Copyright (C) <2022>  <Gabriel Zuany Duarte Varga>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.   
"""