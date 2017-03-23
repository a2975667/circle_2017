import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn import tree



#output
images_and_predictions = list(zip(digits.images[1771:], predictsvm, predictdt, y_test))
for index, (image, predictionsvm, predictiondt, groundtruth) in enumerate(images_and_predictions[:27]):
    plt.subplot(4, 7, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('SVM/DT/GT: \n {0}/{1}/{2}'.format(predictionsvm, predictiondt, groundtruth))
    #plt.suptitle('Groundtruth: %i' % groundtruth)

plt.show()