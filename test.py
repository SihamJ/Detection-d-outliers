
#RESTE A TESTER LES M'IMPLIMENTATION
def mode_class(instances):
    """
    Parameters:
      instances: A list of dictionaries where each dictionary is an instance.
        Each dictionary contains attribute:value pairs
    Returns:
      Name of the most common class (e.g. 'Don't Play')
    """

    classes = []  # Create an empty list named 'classes'

    # For each instance in the list of instances, append the value of the class
    # to the end of the classes list
    for instance in instances:
        classes.append(instance['Class'])

    # The 1 ensures that we get the top most common class
    # The [0][0] ensures we get the name of the class label and not the tally
    # Return the name of the most common class of the instances
    return Counter(classes).most_common(1)[0][0]





# Prédictions
res = [0 for c in range(len(attr))]
for j in range(len(attr)):
    res[j] = predict(tree,attr)

# Plot
color = [0 for c in range(len(attr))]
for j in range(len(attr)):
    if res[j] == 0:
        color[j] = '#10bbcf'
    else:
        color[j] = '#eecc10'

plt.scatter(attr, y, c=color, s=20, cmap='viridis')
plt.axvline(x=seuils[0],linewidth = 1,color="r")
plt.axvline(x=seuils[1],linewidth = 1,color="r")
plt.xlabel('x')
plt.ylabel('y')

print('\nAprès Clustering:\n')
plt.show()

#3-Evaluation du Modèle
tp = 0
tn = 0
fp = 0
fn = 0

for i in range(len(c)):
    if(c[i] == res[i]):
        if(c[i] == 0):
            tn = tn + 1
        else:
            tp = tp + 1
    else:
        if(c[i] == 0):
            fp = fp + 1
        else:
            fn = fn + 1

print('\n_________________________________________________\n\nEvaluation du Modèle:\n_____________________')
print('\nTrue Negative:  '+str(tn)+' - True Positive:  '+str(tp)+'\nFalse Negative: '+str(fn)+' - False Positive: '+str(fp))
exactitude = (tp + tn) / (tp+tn+fp+fn)
exactitude_ponderee = ( (tp/(tp+fn)) + (tn/(tn+fp)) ) / 2
precision = tp/(tp+fp)
rappel = tp/(fn+tp)
print('\nExactitude: '+ str(exactitude) + '\nExactitude_ponderee: ' + str(exactitude_ponderee) + '\nPrécision: '+ str(precision) + '\nRappel: '+ str(rappel) + '\n')
print('_________________________________________________\n\n')



def predict(node, test_instance):
    '''
    Parameters:
        node: A trained tree node
        test_instance: A single test instance
    Returns:
        Class value (e.g. "Play")
    '''
    # Stopping case for the recursive call.
    # If this is a leaf node (i.e. has no children)
    if len(node) == 0:
        return node.outlier  ### pas sur!!!!
    # Otherwise, we are not yet on a leaf node.
    # Call predict method recursively until we get to a leaf node.
    else:
        ##parcour adroite
        # Extract the attribute name (e.g. "Outlook") from the node.
        # Record the value of the attribute for this test instance into
        # attribute_value (e.g. "Sunny")
        attribute_value = test_instance[node.attribut]

        # Follow the branch for this attribute value assuming we have
        # an unpruned tree.
        if attribute_value in node.children and node.children[
            attribute_value].pruned == False:
            # Recursive call
            return predict(node.children[attribute_value], test_instance)

        # Otherwise, return the most common class
        # return the mode label of examples with other attribute values for the current attribute
        else:
            instances = []
            for attr_value in node.attribute_values:
                instances += node.children[attr_value].instances_labeled
            return mode_class(instances)




