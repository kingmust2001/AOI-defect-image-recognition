# AOI-defect-image-recognition

## 專案介紹
自動光學檢查（Automated Optical Inspection，簡稱 AOI），為高速高精度光學影像檢測系統，運用機器視覺做為檢測標準技術，可改良傳統上以人力使用光學儀器進行檢測的缺點，針對所提供的 AOI 影像資料，來判讀瑕疵的分類，藉以提升透過數據科學來加強 AOI 判讀之效能。

## 軟硬體配置
* CPU: Intel(R) Xeon(R) (6-cores)
* GPU: Tesla K80 (11.44GB)
* OS： Window10
* Pytorch: 1.10.0
* keras: 2.7.0
* tensorflow: 2.7.0
* Memory: 12.69GB
## 資料來源
人工智慧共創平台

https://aidea-web.tw/topic/285ef3be-44eb-43dd-85cc-f0388bf85ea4
## 資料基本資訊
* train_images.zip：訓練所需的影像資料（PNG格式），共計 2,528 張。
* train.csv：包含 2 個欄位，ID 和 Label。
    * ID：影像的檔名。
Label：瑕疵分類類別（0 表示 normal，1 表示 void，2 表示 horizontal defect，3 表示 vertical defect，4 表示 edge defect，5 表示 particle）。
* test_images.zip：測試所需的影像資料（PNG格式），共計 10,142 張。
* test.csv：包含 2 個欄位，ID 和 Label。
    * ID：影像的檔名。
    * Label：瑕疵分類類別（其值只能是下列其中之一：0、1、2、3、4、5）。
 ![image](https://user-images.githubusercontent.com/77257138/149629032-74b9e5c6-73cc-4ac8-99ac-3909aea99711.png)


## 前處理
* 影像隨機水平, 垂直平移(range=0.05)
* 影像大小縮放成 224 x 224
## 模型
MobileNet
## Metrics
Accuracy = Number of correct predictions/Number of total predictions

![image](https://user-images.githubusercontent.com/77257138/149628919-77c1820f-edd5-44ce-87b2-715cf5f6c784.png)
## 成果
epoch:5 batch:16

* training accuracy:0.9593 
* validation accuracy: 0.9666

![image](https://user-images.githubusercontent.com/77257138/152546598-0892517a-fb9f-4c13-9512-28f9b6dd05f9.png)

## other
1. data augmentation method:
* tf.keras.preprocessing.image.ImageDataGenerator
* tf.keras.preprocessing.image_dataset_from_directory
* tf.data.Dataset with image files
* tf.data.Dataset with TFRecords

benefit:

* data增強
* feeds the data gradually to the neural network without keeping it into memory.
![image](https://user-images.githubusercontent.com/77257138/152545306-c5e34546-c04c-413b-bca8-2bb26e36dcf7.png)

conclusion:

image_dataset_from_directory should be the new go-to because it is not more complicated that the old method and is clearly faster.

2.值方圖均衡化(Histogram Equalization)與局部均衡化(createCLAHE)
* object: 處理影像是偏亮或偏暗

note:createCLAHE，這種方法是對部分影像分別做均衡化，限制局部明暗對比太大的狀況(使用Histogram Equalization是對全局圖片進行調整，因此也會存在著一些問題，像是因為整體影像的亮度增加，可能有些小地方會變得模糊)

值方圖均衡化(Histogram Equalization)

![image](https://user-images.githubusercontent.com/77257138/152548094-28af436e-4111-4663-98ad-4dac3c6a1d38.png)

局部均衡化(createCLAHE)

![image](https://user-images.githubusercontent.com/77257138/152548138-ba9e4459-561a-4968-9d6c-336b35be35f5.png)

3. GlobalAveragePooling 將權重值做平均, 減少參數

![image](https://user-images.githubusercontent.com/77257138/154809657-fa499f0b-df14-4db7-9f7e-afded8c7f082.png)



## Reference
https://aidea-web.tw/topic/285ef3be-44eb-43dd-85cc-f0388bf85ea4
https://ithelp.ithome.com.tw/articles/10263866
https://github.com/hcygeorge/aoi_defect_detection
https://towardsdatascience.com/what-is-the-best-input-pipeline-to-train-image-classification-models-with-tf-keras-eb3fe26d3cc5
https://ithelp.ithome.com.tw/articles/10276291


