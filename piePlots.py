import numpy as np
import matplotlib.pyplot as plt

# data is put into Python lists here
f_openings = ['White:Karo-Cann', 'Black: Kings Indian Defense', 'White: Kings Indian Defense']   #  X labels
f_won = [3.3, 5, 2]
f_lost = [2, 4, 1.3]
f_draw = [1, 1, 1]

def graph(openings=f_openings,won=f_won, lost=f_lost,draw=f_draw):
	# set up some values for the bars
	bar_width = 0.1 # set the width of the bars
	x = np.arange(len(openings))  # need an array of x values
	opacity = 1  # not so dark

	# setup the plots: both points and smooth curve
	plt.bar(x, won, bar_width, color='green', label='Won', alpha=opacity)
	# notice the shift

	plt.bar(x+bar_width, lost, bar_width, color='red',
				label='Lost', alpha=opacity)

	plt.bar(x+bar_width+bar_width, draw, bar_width, color='blue',
				label='Draw', alpha=.4)



	plt.legend()
	plt.xlabel('Openings')
	plt.ylabel('Percentages')
	plt.title('Player stats')
	plt.xticks(x + bar_width, openings) # override the xlabels with our custom labels

	# okay, I think we are all ready...
	plt.tight_layout() # this helps spread things - easier to read
	plt.show()