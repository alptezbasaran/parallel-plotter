# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:20:06 2019

@author: atezbas
"""
def main():
  import glob,os
  
  directory="C:/Users/atezbas/Desktop/parallelDecks/parallel-plotter/geometries"
  
  os.chdir(directory)
  files = []

  files = glob.glob("*.master.inp")

  for file in files:
    plotGeom(file,directory)


def plotGeom(inputName,directory):
  # Importing the libraries
  import matplotlib.pyplot as plt
  import pandas as pd
  import os
  inputPath = os.path.join(directory,inputName)
  print(inputName)
  # Importing the dataset
  dataset = pd.read_csv(inputPath ,skiprows = 7,delim_whitespace=True,nrows=1500)
  channelNumber = dataset.iloc[0:-2,0].values
  xCoordinates = dataset.iloc[0:-2, 1].values
  yCoordinates = dataset.iloc[0:-2, 2].values
  xSizes = dataset.iloc[0:-2,3].values
  ySizes = dataset.iloc[0:-2,4].values
  
  fig = plt.figure()
  for i in range(len(channelNumber)):
    plt.vlines(xCoordinates[i] + xSizes[i]/2, yCoordinates[i]-ySizes[i]/2, yCoordinates[i]+ySizes[i]/2)
    plt.vlines(xCoordinates[i] - xSizes[i]/2, yCoordinates[i]-ySizes[i]/2, yCoordinates[i]+ySizes[i]/2)
    plt.hlines(yCoordinates[i] + ySizes[i]/2, xCoordinates[i]-xSizes[i]/2, xCoordinates[i]+xSizes[i]/2)
    plt.hlines(yCoordinates[i] - ySizes[i]/2, xCoordinates[i]-xSizes[i]/2, xCoordinates[i]+xSizes[i]/2)
    plt.text(xCoordinates[i],yCoordinates[i],str(channelNumber[i]), fontsize=5, \
             horizontalalignment='center', verticalalignment='center')
  
  plt.title(inputName)
  plt.xlabel('x location')
  plt.ylabel('y location')
  plt.savefig(inputName+'.png',dpi=500)
  plt.close(fig)
  
if __name__ == '__main__':
  main()
