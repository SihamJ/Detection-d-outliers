class Feuille:
    def __init__(self, attribut = None, lower_split = None, higher_split = None):
        self.attribut = attribut
        self.lower_split = lower_split
        self.higher_split = higher_split

    def predir(self,point):
        if(point[self.attribut]<self.lower_split or point[self.attribut]>self.higher_split):
            return 1
        else:
            return 0


class DecisionLeaf:

    def __init__(self, data, attribIdx):
        self.D = data
        self.attribIdx = attribIdx


class DirectDecision:
    def __init__(self,outlier):
        self.outlier = outlier