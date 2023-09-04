#! python3
#resScaler.py - Calculates proportional output resolution of a source resolution

from fractions import Fraction
import console

#these lines accept initial user input of source resolution
print('What is horizontal (x) resolution of your content?')
iResW = int(input())
print ('What is the vertical (y) resolution of your content')
iResH = int(input())

#asks for the width to scale to (leave blank to scale to height)
print('What is the output width you are scaling to? (Leave blank to scale to height)')
oResW = input()
#defines initial value for variable that is then updated by the function
oResH = ''

#iRatio calculates the input width/height ratio
iRatio = iResW/iResH

def scaledPercent(iResW, oResW):
	x = float(oResW/iResW) * 100
	return(int(x))

def entToExit():
	print()
	print('press return to exit')
	x = input()
	if x == '':
		console.hide_output()

#defines the function
def scaledRes(oResW, oResH):
	#calculates to fit height if a width is entered
	if oResW != '':
		oResW = int(oResW)
		CalcOutResH = int(oResW/iRatio)
		fractionV = Fraction(int(oResW), int(CalcOutResH))
		# scaledPercent = int(iResW/oResW) * 100
		print('Your scaled output (fit to width) is ' + str(oResW) + ' wide x ' + str(CalcOutResH) + ' high')
		print('The aspect ratio is ' + str(iRatio))
		print('The output ratio is ' + str(fractionV))
		print(f'The vertical scaled percentage is {scaledPercent(iResW, oResW)}%')
		

	#asks for scaled height if no width is entered
	else:
		while True:
			try:
				print('What is the output height you are scaling to?')
				#calculates to fit width if a height is entered
				oResH = int(input())
				break
			except ValueError:
				print('Error - You must enter an output height.')
		CalcOutResW = int(oResH * iRatio)
		fractionH = Fraction(int(CalcOutResW), int(oResH))
		print('Your scaled output (fit to height) is ' + str(CalcOutResW) + ' wide x ' + str(oResH) + ' high')
		print('The aspect ratio is ' + str(iRatio))
		print('The output ratio is ' + str(fractionH))
		print(f'The horizontal scaled percentage is {scaledPercent(iResH, oResH)}%')

	
#calls the function
scaledRes(oResW, oResH)
entToExit()

