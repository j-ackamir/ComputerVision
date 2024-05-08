import matplotlib.pyplot as plt


from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# print( X_train.shape) It should be 60000 images of 28x28 pixels

from keras.utils.np_utils import to_categorical
y_cat_train = to_categorical(y_train, 10)
y_cat_test = to_categorical(y_test, 10)

X_train=X_train/X_train.max()
X_train=X_train.reshape(60000,28,28,1)
X_test=X_test/X_test.max()
X_test=X_test.reshape(10000,28,28,1)

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(4,4),input_shape=(28, 28, 1), activation='relu',))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train,y_cat_train,epochs=2)
print(model.evaluate(X_test,y_cat_test))
print(model.metrics_names)

from sklearn.metrics import classification_report
predictions = model.predict_classes(X_test)
print(classification_report(y_test,predictions))
