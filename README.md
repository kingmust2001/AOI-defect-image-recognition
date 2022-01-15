# AOI-defect-image-recognition

## 專案介紹
自動光學檢查（Automated Optical Inspection，簡稱 AOI），為高速高精度光學影像檢測系統，運用機器視覺做為檢測標準技術，可改良傳統上以人力使用光學儀器進行檢測的缺點，本次邀請各界資料科學家共襄盛舉，針對所提供的 AOI 影像資料，來判讀瑕疵的分類，藉以提升透過數據科學來加強 AOI 判讀之效能。

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

## 模型
MobileNet
## Metrics
Accuracy = Number of correct predictions/Number of total predictions

![image](https://user-images.githubusercontent.com/77257138/149628919-77c1820f-edd5-44ce-87b2-715cf5f6c784.png)
## 成果
training loss: 

validation loss: 


## Reference
https://aidea-web.tw/topic/285ef3be-44eb-43dd-85cc-f0388bf85ea4
https://ithelp.ithome.com.tw/articles/10263866
https://github.com/hcygeorge/aoi_defect_detection
