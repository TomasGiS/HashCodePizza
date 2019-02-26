
pizza = []

def readHeader(fileInput):
	rowsPizza = fileInput.read(1)
	fileInput.read(1) #Space
	colsPizza = fileInput.read(1)
	fileInput.read(1) #Space
	
	minIngredientsPerSlice = fileInput.read(1)
	fileInput.read(1) #Space
	maxSizeSlice = fileInput.read(1)
	fileInput.read(1) #Space

	print("Size pizza({} ,{}) and the slices with min {} ingredients and max slice size {}".format(rowsPizza,colsPizza,minIngredientsPerSlice,maxSizeSlice))

	header = {'rowsPizza':int(rowsPizza), 'colsPizza':int(colsPizza), 'minIngredientsPerSlice':int(minIngredientsPerSlice), 'maxSizeSlice':int(maxSizeSlice) }
	print(header)
	return header

def readData(fileInput,header):

	print("header: ", header)
	print("Rows: ",header['rowsPizza'])
	row=[]
	#print("Size pizza({} ,{}) and the slices with min {} ingredients and max slice size {}".format(header.rowsPizza,header.colsPizza,header.minIngredientsPerSlice,header.maxSizeSlice))
	for rowIndex in range(0, header['rowsPizza']):
		for colIndex in range(0, header['colsPizza']):
			ingredient=fileInput.read(1)			
			row.append(ingredient)
		fileInput.read(1) #Line carry return	
		pizza.append(row)
		row=[]
		

	print (pizza)

def inputData(fileName="a_example.in"):
	fileInput = open(fileName,"r") 
	header=readHeader(fileInput)
	readData(fileInput,header)




inputData("a_example.in")