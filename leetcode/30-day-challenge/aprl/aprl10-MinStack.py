"""
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


maintain a list of min; also keep a global min values and keep updating it on an update
once the stack is empty; update min
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minList=[]
        self.min=9999999999


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        ## Equal case is to handle duplicates
        if x<=self.min:
            self.min = x
            self.minList.append(x)

    def pop(self):
        """
        :rtype: None
        """
        ##re-init min once stack is empty
        if len(self.stack)==1:
            self.min=9999999999
            tmp = self.stack.pop()
            self.minList.pop()

        elif len(self.stack)!=0:
            tmp = self.stack.pop()

            if tmp == self.minList[-1]:
                self.minList.pop()
                self.min = self.minList[-1]

            return tmp
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        #if len()
        if len(self.minList)>0:
            return self.minList[-1]
        else:
            return None

    def printStack(self):
        print self.stack,self.minList,self.min





#["MinStack","push","getMin","top","getMin","push","push","getMin","push","getMin","pop","push","push","getMin","push","top","push","pop","pop","getMin","pop","getMin","getMin","pop","getMin","push","push","pop","push","getMin","getMin","push","getMin","getMin","push","getMin","getMin","getMin","push","getMin","pop","top","push","top","push","getMin","getMin","push","pop","getMin","getMin","pop","pop","getMin","push","getMin","getMin","push","getMin","top","getMin","push","getMin","push","top","getMin","push","getMin","top","getMin","push","getMin","getMin","push","pop","push","push","getMin","push","push","push","top","getMin","push","getMin","push","push","push","getMin","push","push","push","pop","push","getMin","top","getMin","getMin","push","top","push","push","top","push","getMin","push","top","getMin","getMin","getMin","getMin","getMin","push","getMin","push","push","getMin","getMin","getMin","top","getMin","push","pop","getMin","getMin","push","getMin","getMin","getMin","getMin","push","top","top","push","push","push","top","top","push","getMin","push","push","push","getMin","getMin","push","push","push","push","getMin","getMin","getMin","push","top","pop","getMin","push","top","pop","push","getMin","pop","getMin","pop","getMin","push","top","push","getMin","getMin","top","pop","top","getMin","getMin","push","push","push","pop","push","getMin","getMin","push","push","push","top","getMin","top","getMin","getMin","top","top","pop","pop","getMin","getMin","push","getMin","push","getMin","push","push","push","getMin","pop","pop","push","pop","top","push","top","top","pop","top","push","push","top","top","getMin","getMin","getMin","push","getMin","getMin","push","getMin","pop","top","push","push","push","push","push","getMin","getMin","push","getMin","getMin","getMin","push","getMin","getMin","getMin","top","getMin","getMin","push","top","getMin","push","getMin","push","getMin","getMin","getMin","push","pop","push","pop","push","top","getMin","getMin","push","getMin","getMin","getMin","push","push","push","getMin","push","top","push","getMin","push","top","getMin","getMin","getMin","pop","getMin","top","getMin","push","getMin","getMin","getMin","getMin","getMin","pop","getMin","getMin","push","getMin","pop","push","top","push","push","getMin","pop","pop","push","pop","getMin","push","push","getMin","getMin","pop","pop","pop","push","pop","push","push","push","push","getMin","top","getMin","getMin","getMin","top","push","getMin","push","push","getMin","pop","getMin","push","pop","pop","push","push","push","pop","getMin","getMin","pop","push","push","getMin","top","getMin","pop","push","push","push","getMin","getMin","push","push","push","getMin","pop","getMin","push","push","getMin","getMin","getMin","push","getMin","getMin","getMin","getMin","getMin","getMin","push","getMin","pop","getMin","getMin","push","pop","pop","pop","push","top","push","push","getMin","getMin","getMin","getMin","getMin","push","push","top","push","top","push","top","pop","push","getMin","push","push","getMin","getMin","getMin","getMin","pop","getMin","push","top","pop","push","getMin","push","push","push","push","pop","getMin","push","push","top","getMin","getMin","top","getMin","getMin","push","getMin","push","getMin","top","getMin","getMin","push","push","getMin","push","push","push","push","getMin","getMin","pop","push","top","push","pop","getMin","push","push","getMin","getMin","push","getMin","push","push","getMin","getMin","getMin","top","getMin","getMin","push","top","push","top","pop","push","push","getMin","push","pop","pop","push","getMin","push","getMin","getMin","getMin","top","top","pop","pop","pop","getMin","push","top","push","getMin","getMin","getMin","push","getMin","top","getMin","push","push","getMin","pop","getMin"]

#[[],[395],[],[],[],[276],[29],[],[-482],[],[],[-108],[-251],[],[-439],[],[370],[],[],[],[],[],[],[],[],[-158],[82],[],[-176],[],[],[-90],[],[],[411],[],[],[],[-494],[],[],[],[155],[],[-370],[],[],[273],[],[],[],[],[],[],[173],[],[],[0],[],[],[],[-266],[],[-359],[],[],[189],[],[],[],[375],[],[],[-188],[],[-275],[-223],[],[294],[380],[-42],[],[],[33],[],[457],[422],[-352],[],[326],[-378],[231],[],[416],[],[],[],[],[277],[],[472],[205],[],[-443],[],[-5],[],[],[],[],[],[],[-312],[],[-249],[-209],[],[],[],[],[],[196],[],[],[],[-347],[],[],[],[],[400],[],[],[269],[434],[-213],[],[],[-58],[],[-353],[-426],[-335],[],[],[-188],[-388],[369],[319],[],[],[],[121],[],[],[],[155],[],[],[155],[],[],[],[],[],[495],[],[-53],[],[],[],[],[],[],[],[465],[162],[-334],[],[282],[],[],[432],[-418],[195],[],[],[],[],[],[],[],[],[],[],[],[374],[],[202],[],[181],[173],[-323],[],[],[],[-430],[],[],[346],[],[],[],[],[244],[-467],[],[],[],[],[],[279],[],[],[-30],[],[],[],[264],[-217],[-418],[12],[-439],[],[],[7],[],[],[],[-189],[],[],[],[],[],[],[303],[],[],[-297],[],[-21],[],[],[],[461],[],[-303],[],[-338],[],[],[],[-42],[],[],[],[85],[132],[57],[],[-17],[],[-10],[],[-500],[],[],[],[],[],[],[],[],[-7],[],[],[],[],[],[],[],[],[346],[],[],[16],[],[472],[-211],[],[],[],[-381],[],[],[214],[169],[],[],[],[],[],[33],[],[115],[-346],[-309],[130],[],[],[],[],[],[],[335],[],[-92],[-16],[],[],[],[-470],[],[],[250],[327],[144],[],[],[],[],[359],[138],[],[],[],[],[272],[-241],[-362],[],[],[-83],[195],[-208],[],[],[],[-500],[5],[],[],[],[284],[],[],[],[],[],[],[477],[],[],[],[],[30],[],[],[],[-269],[],[-413],[-323],[],[],[],[],[],[217],[-408],[],[-353],[],[-142],[],[],[-321],[],[-33],[382],[],[],[],[],[],[],[298],[],[],[495],[],[195],[-147],[-85],[195],[],[],[154],[-311],[],[],[],[],[],[],[-390],[],[323],[],[],[],[],[338],[263],[],[160],[148],[142],[427],[],[],[],[-153],[],[-384],[],[],[159],[419],[],[],[-385],[],[461],[-346],[],[],[],[],[],[],[343],[],[-269],[],[],[-401],[81],[],[130],[],[],[-428],[],[454],[],[],[],[],[],[],[],[],[],[59],[],[143],[],[],[],[-154],[],[],[],[114],[-346],[],[],[]]

minStack = MinStack()
minStack.push(395)
minStack.getMin()
minStack.top()
minStack.getMin()
minStack.push(276)
minStack.push(29)
minStack.getMin()
minStack.push(-482)
minStack.getMin()
minStack.pop()
minStack.push(-108)
minStack.push(-251)
minStack.getMin()
minStack.printStack()
