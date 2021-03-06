# -*- coding: utf-8 -*-
"""side_Project3_AOI defect.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ic1sgIWuHENDDeRG_hod6lacOjwKn7jQ


import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import Sequential
from tensorflow.keras.models import Model #Model groups layers into an object with training and inference features.
from tensorflow.keras import models
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras import layers, callbacks
from sklearn.metrics import confusion_matrix
from tensorflow.keras.applications import imagenet_utils

"""### **Data augumentation**"""

train_datagen = ImageDataGenerator(
    rotation_range = 0,
    horizontal_flip = False,
    vertical_flip = False,
    width_shift_range = 0.05,
    height_shift_range = 0.05,
    preprocessing_function = tf.keras.applications.mobilenet.preprocess_input 
) #use mobilenet's preprocessing function -> will compress all values to [0,1] 其他的前處理功能，可自行寫def定義或是使用套件提供的
valid_datagen = ImageDataGenerator(preprocessing_function = tf.keras.applications.mobilenet.preprocess_input)

"""#### apply data augumentation to data

two ways that could apply data augumentation on data

* flow_from_directory: 需要將不同標籤的圖片進行分類，安插在同一個資料夾下
* flow_from_dataframe: 不必將圖片分類，全部放置在一個資料夾即可，但須額為製作一份DataFrame，裡頭要包含圖片的名稱以及標籤
"""

image_shape = (224,224)
batch_size = 16
train_generator = train_datagen.flow_from_dataframe(
    dataframe = train,
    directory = data_file_image,
    x_col = "ID",
    y_col = "Label",
    target_size = image_shape,
    batch_size = batch_size,
    calss_mode = "categorical",
    shuffle = True
)
valid_generator = valid_datagen.flow_from_dataframe(
    dataframe = valid,
    directory = data_file_image,
    x_col = "ID",
    y_col = "Label",
    target_size = image_shape,
    batch_size = batch_size,
    calss_mode = "categorical",
    shuffle = True
)


"""### **start training**"""

class_weights = {i:value for i, value in enumerate(class_weights)}
class_weights

def num_steps_per_epoch(data_generator, batch_size):
    if data_generator.n % batch_size==0:
        return data_generator.n//batch_size
    else:
        return data_generator.n//batch_size + 1

train_steps = num_steps_per_epoch(train_generator, batch_size)
valid_steps = num_steps_per_epoch(valid_generator, batch_size)

train_steps

tf.config.list_physical_devices("GPU")

history = model.fit_generator(train_generator, steps_per_epoch=train_steps, epochs = 5, validation_data = valid_generator, validation_steps=valid_steps, class_weight = class_weights, callbacks=callback_list)

import matplotlib.pyplot as plt
#print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left') 
plt.show()

# summarize history for loss 
plt.plot(history.history['loss']) 
plt.plot(history.history['val_loss']) 
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left') 
plt.show()

# Commented out IPython magic to ensure Python compatibility.
#tensorboard
# %load_ext tensorboard
# %tensorboard --logdir logs

"""### **prediction**"""

testing_list = pd.read_csv(os.path.join(data_file, "test.csv"), index_col = False)
testing_list = testing_list[:100]
#testing_list

testing_list.Label = testing_list.Label.astype(str)
testing_list.Label

data_file_image_test = ("/content/drive/MyDrive/Colab Notebooks/side_Project3_AOI defect /aoi.zip (Unzipped Files)/test_images")
test_datagen = ImageDataGenerator(
    preprocessing_function = tf.keras.applications.mobilenet.preprocess_input
)
test_generator = test_datagen.flow_from_dataframe(
    dataframe = testing_list,
    directory = data_file_image_test,
    x_col = "ID",
    y_col = "Label",
    target_size = image_shape,
    batch_size = batch_size,
    class_mode='categorical',
    shuffle = False
)
test_step = num_steps_per_epoch(test_generator, batch_size)

y_pred = model.predict(test_generator, steps = test_step).argmax(-1)
#y_pred = np.argmax(model.predict(valid_generator, steps = valid_steps), axis = 1)
y_pred

"""#### confusion matrix

from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

print(f"accuracy_score: {accuracy_score(y_test, y_test_pred):.3f}")

confusion = confusion_matrix(y_test, y_test_pred)

plt.figure(figsize=(5, 5))
sns.heatmap(confusion_matrix(y_test, y_test_pred), 
            cmap="Blues", annot=True, fmt="d", cbar=False,
            xticklabels=[0, 1], yticklabels=[0, 1])
plt.title("Confusion Matrix")
plt.show()

## referance
https://ithelp.ithome.com.tw/articles/10263866
"""