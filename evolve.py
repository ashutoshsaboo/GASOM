from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Statistics
from pyevolve import DBAdapters, Consts
import pyevolve
import random, numpy as np
from time import time
import sompy
from sompy.visualization.hitmap import *
import pandas as pd
import pickle
from multiprocessing import Pool
from sompy.visualization.bmuhits import BmuHitsView
from sompyfinal import final_run
from Weight_file import Generate_file
import os

errors = []
data = 0
len_train_rough = 0
len_train_finetune = 0
def evolve_callback(ga_engine):
   global errors
   generation = ga_engine.getCurrentGeneration()
   # if generation % 100 == 0:
   print "Current generation: %d" % (generation,)
   stats= ga_engine.getStatistics() 
   print "%e" % stats["rawMin"]
   errors.append(stats["rawMin"])
   # vhts  = BmuHitsView(4,4,"Hits Map",text_size=12)
   # vhts.show(som, anotate=True, onlyzeros=False, labelsize=12, cmap="Greys", logaritmic=False)
   return False

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
def eval_func(chromosome):
   global data,len_train_rough,len_train_finetune
   mapsize = [chromosome[0], chromosome[1]]
   som = sompy.SOMFactory.build(data, mapsize, mask=None, mapshape='planar', lattice='rect', normalization='var', initialization='random', neighborhood='gaussian', training='batch', name='sompy')  # this will use the default parameters, but i can change the initialization and neighborhood methods
   som.train(n_job=1, verbose=None, train_rough_len=len_train_rough, train_finetune_len=len_train_finetune) #400,100 # verbose='debug' "info"will print more, and verbose=None wont print anything
   quantization_error = np.mean(som._bmu[1])
   topographic_error = som.calculate_topographic_error()
   print mapsize,quantization_error,topographic_error

   return (quantization_error + topographic_error)/(2.0)

def create_folder(dataset_name):
      current_directory = os.path.dirname(os.path.abspath(__file__))
      new_folder_path = os.path.join(current_directory,dataset_name)
      if not os.path.exists(new_folder_path):
         os.makedirs(new_folder_path)
         print(new_folder_path,"folder created")


def train(dataset_name="test_result",no_generation=15,population_size=10,
   dim_rangemin=1,dim_rangemax=100,data1=None,len_train_rough1=800,len_train_finetune1=200,type_of_problem="realWorld",
   final_rough_train=1600,final_fine_train=400):
   
   global errors,data,len_train_finetune,len_train_rough  
   no_generation = no_generation
   population_size = population_size
   dim_rangemax = dim_rangemax
   dim_rangemin = dim_rangemin
   data = data1
   len_train_finetune = len_train_finetune1
   len_train_rough = len_train_rough1
   errors = []
   dataset_name = dataset_name

   create_folder(dataset_name)

   genome = G1DList.G1DList(2)

   # Sets the range max and min of the 1D List
   genome.setParams(rangemin=dim_rangemin, rangemax=dim_rangemax)#, bestrawscore=0.0000, rounddecimal=4

   # The evaluator function (evaluation function)
   genome.evaluator.set(eval_func)

   # Genetic Algorithm Instance
   ga = GSimpleGA.GSimpleGA(genome)
   ga.setMultiProcessing()
   ga.stepCallback.set(evolve_callback)
   ga.setMinimax(Consts.minimaxType["minimize"])
   # Set the Roulette Wheel selector method, the number of generations and
   # the termination criteria
   ga.selector.set(Selectors.GRouletteWheel)#GRankSelectorGTournamentSelectorGUniformSelector
   ga.setPopulationSize(population_size)
   ga.setGenerations(no_generation)#15
   ga.setElitism(True)
   ga.setElitismReplacement(2)
   #print ga.terminationCriteria.funcList
   #ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)#RawScoreCriteria
   #print ga.terminationCriteria.funcList
   ga.evolve()#freq_stats=20
   # Best individual
   pop = ga.getPopulation()
   bestIndividual = pop.bestFitness()
   print bestIndividual
   # print type(bestIndividual)
   # print "best ",type(pop[0].genomeList), len(pop[0].genomeList)

   best= bestIndividual.genomeList
   final_error = final_run(data,best,dataset_name,type_of_problem,final_rough_train,final_fine_train)

   # errors.pop()
   errors.append(final_error)

   with open(os.path.join(dataset_name, dataset_name+"_errorplot.pkl"), 'wb') as f:
      pickle.dump(errors, f)

