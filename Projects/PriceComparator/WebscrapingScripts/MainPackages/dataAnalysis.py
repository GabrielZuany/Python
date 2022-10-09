from itertools import filterfalse
import matplotlib.pyplot as plt
import statistics as st
from os import getcwd
from math import sqrt
import numpy as np

def BuildJoinedPlot(column, store, color, meancolor, mediancolor, edgelinecolor):
    """
    Build an unique histogram with the price column. (Overlaps the first plot always the function is called).

    Args:
        column (list): list with all product prices. 
        store (str): website name.
        color (str): bar color.
        meancolor (str): mean line color.
        mediancolor (str): median line color.
        edgelinecolor (str): edge line color.
    """
    x = column
    x = list(filterfalse(np.isnan, x)) # remove the NaN values.
    
    interval = (max(x) - min(x))/sqrt(len(x)) # size of each range of values.
     
    bins = np.arange(min(x), max(x), interval) # X axis from lower value to higher by interval.
    mean_x = st.mean(x)
    median_x = st.median(x)
    
    plt.style.use('ggplot')
    plt.grid(True)
    plt.title(f'Product Price')
    plt.xlabel('Value Range')
    plt.ylabel('Frequency')
    plt.axvline(mean_x, color=meancolor, linewidth=1, label= f'{store} Mean = {mean_x:.2f}')
    plt.axvline(median_x, color=mediancolor, linewidth=1, label= f'{store} Median = {median_x:.2f}')
    
    plt.hist(x, bins = bins, color=color, edgecolor=edgelinecolor, label='Value Range', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    path = getcwd()
    
    plt.savefig(f'{path}/DataAnalysis/JoinedPlots.png', dpi=200)
    
    
def BuildSeparatedPlot(df1,df2):
    """
    Build two graph side by side about the data extracted from web.

    Args:
        df1 (dataframe): 1st dataframe.
        df2 (dataframe): 2nd dataframe.
    """
    fig, axes = plt.subplots(1, 2)
    path = getcwd()
    
    df1.hist('ML Price (R$)',color='r', edgecolor='black', alpha=0.5, ax=axes[0])
    df2.hist('AMZ Price (R$)',color='g', edgecolor='black', alpha=0.5, ax=axes[1])
    plt.savefig(f'{path}/DataAnalysis/SeparatedPlots.png', dpi=200)
 

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