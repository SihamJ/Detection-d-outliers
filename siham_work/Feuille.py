class Feuille:
    def __init__(self, attribut = None, lower_split = None, higher_split = None):
        self.attribut = attribut
        self.lower_split = lower_split
        self.higher_split = higher_split

    def predir(self,point):
        #remarque à remonter il manque  le signe "égale" de "<= "
        if(point[self.attribut]<self.lower_split or point[self.attribut]>self.higher_split):
            return 1
        else:
            return 0     #outlier


class DecisionLeaf:

    def __init__(self, data, attribIdx):
        self.D = data
        self.attribIdx = attribIdx


def DirectDecision(outlier):
        if outlier == True:
            return 1
        else:
            return 0