import numpy as np
from sklearn import svm

# TODO: pre-processing, shingles, the log. Your problem, Miss Application!

def read_into_feature_dict(file):
    with open(file) as le_file:
        le_dict = {}
        for line in le_file:
            line = line.strip("\n")
            if line not in le_dict:
                # other features besides frequency
                digits = sum(c.isdigit() for c in line)
                spaces = sum(c.isspace() for c in line)
                # initialize an array of [frequency, digits, spaces]. Frequency is initially 1
                le_dict[line] = [1,digits, spaces]
            else:
                # increment frequency if we met this before
                le_dict[line][0] = le_dict[line][0] + 1
        return le_dict

print("Reading training data...")
mfr_feature_dict = read_into_feature_dict("/Users/radu/gits/activate/sklearn/mfrs")
model_feature_dict = read_into_feature_dict("/Users/radu/gits/activate/sklearn/models")

# training data is an array of arrays. Each inner array is the set of features
training = []
for i in mfr_feature_dict:
    training.append(mfr_feature_dict[i])
for i in model_feature_dict:
    training.append(model_feature_dict[i])

X = np.array(training)

# training labels. I know that the first are manufacturers, the last are models
y = []
for i in range(len(mfr_feature_dict)):
    y.append("mfr")
for i in range(len(model_feature_dict)):
    y.append("cat")

print("Initializing and training the model...")
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X, y)

def test_from_file(test_file):
    test_X = []
    test_dict = read_into_feature_dict(test_file)
    for feature_set in test_dict:
        test_X.append(test_dict[feature_set])
    print(test_dict.keys())
    print(test_X)
    print(clf.predict(test_X))

print("\nTrying to label some manufacturers\n===============")
test_from_file("/Users/radu/gits/activate/sklearn/test_mfrs")

print("\nTrying to label some models\n===============")
test_from_file("/Users/radu/gits/activate/sklearn/test_models")