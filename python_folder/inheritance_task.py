import numpy as np  #importing numpy

class mainMatrix:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def addition(self):
        result = np.add(self.m1, self.m2)
        print("Addition of matrices: {} ".format(result))
    
    def substraction(self):
        result = np.subtract(self.m1, self.m2)
        print("subtraction of matrices: {} ".format(result))
    
    def multiplication(self):
        result = np.dot(self.m1, self.m2)
        print("Multiplication of matrices: {} ".format(result))

    def transposes(self):
        print("Transpose of m1: {} ".format( self.m1.transpose()))
        print("Transpose of m1: {}".format(self.m2.transpose()))
        print(" ")
        

class subMatrix(mainMatrix):
    def __init__(self, m1, m2):
        super().__init__(m1, m2)
    
    def addition(self):
        result = [([(m1[i][j] + m2[i][j]) for j in range(len(m1[0]))]) for i in range(len(m1))]
        print("Addition of two matrices is: \n"+str(result))
    
    def subtraction(self):
        result = [([(m1[i][j] - m2[i][j]) for j in range(len(m1[0]))]) for i in range(len(m1))]
        print("subtraction of matrices: \n"+str(result))
    
    def multiplication(self):
        result= [[sum(a * b for a, b in zip(row, col)) for col in zip(*m2)] for row in m1]
        print("Multplication of matrices: \n"+str(result))

    def transposes(self):
        result_1 = [([m1[j][i] for j in range(len(m1))]) for i in range(len(m1[0]))]
        print("Transpose of m1: \n"+str(result_1))

        result_2 = [([m2[j][i] for j in range(len(m2))]) for i in range(len(m2[0]))]
        print("Transpose of m2: \n"+str(result_2))   

print("Parent class operations using numpy: ")

m1 = np.array([[1, 2], [3,4]])
m2 = np.array([[5, 6], [7,8]])
obj = mainMatrix(m1, m2)
obj.addition()
obj.substraction()
obj.multiplication()
obj.transposes()

print("Child class operations using method overriding:")
obj1 = subMatrix(m1, m2)
obj1.addition()
obj1.subtraction()
obj1.transposes()
