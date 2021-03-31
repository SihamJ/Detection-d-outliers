# File name: node.py
# Author: Addison Sears-Collins
# Date created: 7/6/2019
# Python version: 3.7
# Description: Used for constructing nodes for a tree



class Node:
    def __init__(self, label):

        self.attribute = None # attribute (e.g 'x')
        self.attribute_value = []   # valeurs
        self.label = label  # class label for the node (e.g 'Play') inlier
        self.children = {}  # keep track of the node's children

        #References to the parent node
        self.parent_attribute = None
        self.parent_attribute_value = None

        # Used for pruned trees
        self.pruned = False  # Is this tree pruned?
        self.instances_labeled = []