from id3 import *

class DecisionTreeClassifier:

    def __init__(self, X, feature_names, labels):
        self.X= X     #feature or predictors
        self.feature_names = feature_names   #name of the feature
        self.labels = labels  # categories
        self.labelCategories = list(set(labels)) #unique categories
        #nombre d'instance de chaqua categorie
        self.labelCategoriesCount = [list(labels).count(x) for x in self.labelCategories]
        self.node = None
        #calculate the initail entropy of the system
        self.entropy = self._get_entropy([x for x in range(len(self.labels))])
