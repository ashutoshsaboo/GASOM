# GASOM
GASOM: Genetic Algorithm assisted Architecture Learning in Self Organizing Maps

## Dependencies-:

  1. Pyevolve==0.6rc1
  2. matplotlib==2.0.0
  3. numpy==1.12.1
  4. pandas==0.18.1

## Setup-:

	1. pip install -r requirements.txt
	2. Edit the params : datasetpath, number_of_columns_csv, features, dataset_name, type_of_problem, data
	(Change data numpy array, so that, data contains only the relevant features, without the tags and indices)
	3. python train.py > dataset.log (This gives the best possible SOM Map Size for your dataset)
	4. Results will be present in dataset_name folder in cwd, along with final stats in dataset.log file. 
	5. python generate_error_plot.py <pickle file in dataset_name folder> <dataset_name> (Error plot is generated)
	6. Visualise the results 

## Data sets used for testing our Model-:

* Commercial Data sets used-:
	 
   1. Wine
   2. Iris
   3. Abalone
   4. Car Evaluation
   5. Glass Identification
   6. Sonar

* Synthetic (Self-Made) Data sets used-:
 
   1. Corner
   2. CrescentFullMoon
   3. Ginger Breadman
   4. Half Kernal
   5. Outliers
   6. Two Spirals 
   

