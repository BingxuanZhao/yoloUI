# labelGo

#### 一个基于LabelImg的目标检测、密度计算工具

## 环境配置
```
conda create -n yolo python=3.8
```

```
conda activate yolo
```

```
pip install -r requirements.txt
```


## 使用方法

<p>1.克隆仓库到本地</p>

```
git clone git@github.com:BingxuanZhao/yoloUI.git
or
git clone https://github.com/BingxuanZhao/yoloUI.git
```

<p>2.启动应用程序</p>

```
python main.py
```
<p>3.点击“打开目录”按钮选择存放图片的文件夹</p>

<p>4.点击“目标检测”按钮确认信息无误后选择已训练的yolov5 pytorch模型完成目标检测，并将结果（yolo数据格式）保存到图片文件夹下</p>

<p>5.点击YOLO(TO VOC)将yolo数据格式转化为VOC数据格式（.xml文件），并将结果保存到图片文件夹下,便于之后密度的计算（yolo数据格式转化为VOC数据格式是必须的）。</p>
<p>6.点击创建区块选择需计算物体分别密度区域，并将标签命名为实际场景与图片像素之间的大小比例，这一步操作可同时创建多个区域，以及对已创建区域进行修改。</p>
<p>7.点击保存按钮（不可忽略）。</p>
<p>8.点击计算密度按钮，之后图片对应的.xml文件会进行更新，从而得到各区域密度。</p>

### 注意事项
密度计算结束之后，.xml文件得到更新，但是ui界面的更新会稍显迟钝，这时我们仅需切换图片，再将图片切回即可（下面操作选其一即可，点击上一个图像按钮，然后点击下一个图像按钮；点击下一个图像按钮，然后点击上一个图像按钮），这样就可以使得ui界面的标签得到快速更新。

## 参考
[labelGO](https://github.com/cnyvfang/labelGo-Yolov5AutoLabelImg)
[yolov5](https://github.com/ultralytics/yolov5)