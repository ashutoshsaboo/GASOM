import pickle
import matplotlib.pyplot as plt
import sys
import matplotlib.ticker as mtick

first_arg = sys.argv[1] #Path to pickle file (containing results) in dataset_folder - Final Dataset results, processed by BestSOM
second_arg = sys.argv[2] #Name of Dataset
filename=first_arg
dataset_name=second_arg

with open(filename, 'rb') as f:
	error_list=pickle.load(f)

#print error_list
error_list = error_list[:-1]
#print error_list

plt.plot(error_list)

# plt.semilogy(list1)
plt.xlabel('Generation Number')
plt.ylabel('Error plot ' + dataset_name + ' dataset')
# plt.draw()
# fig = plt.figure()
# fig.savefig("myfig.png",dpi=600)
# fig = plt.gcf()
# fig.set_size_inches(80, 60)
ax= plt.gca()
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0e'))

# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.savefig(dataset_name+"_min_error_plot.png")
# plt.show()
plt.semilogy(error_list)
plt.xlabel('Generation Number')
plt.ylabel('Semilogy Error plot ' + dataset_name + ' dataset')
ax= plt.gca()
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0e'))

plt.savefig(dataset_name+"_semilogy_min_error_plot.png")
# plt.show()

