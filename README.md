
![SourceForge Platform](https://img.shields.io/sourceforge/platform/python?color=python&label=python&logo=python)
[![](https://img.shields.io/badge/知乎-Blog-blue.svg)](https://zhuanlan.zhihu.com/p/634013986)
![](https://img.shields.io/hexpm/l/plug)
# 论文润色
可以根据中文直接输出符合英文论文表达习惯的英文翻译，并在后面给出对应的中文翻译供比较参考。

# 更新日志
2023.06.01 项目上线

2023.06.02 增加翻译功能

2023.06.04 增加网络连接和API密钥debug功能

2023.06.05 史诗级更新，GUI语言全面从PySimpleGUI切换为tkinter，界面设计改版

# 配置
```
pip install openai
```
除此之外注意改一下``` ChatGPT.py```中的代理设置和```api_key```设置

!!!VPN尽量设置到美国而不是香港之类的

# 快速开始
可以将项目下载或者克隆下来，在编译器中打开，运行build文件夹中的```gui.py```文件。


或者命令行中：
```
python ./build/gui.py
```

# 例子
可以实现中英互译（自动识别）和对中文或英文的润色。

**值得注意的是，如果直接从中文翻译到英文，可能会有一些专有名词翻译的不对，需要仔细检查，从英文开始润色则会好一些！**


## 润色：
在上面的框中输入待翻译和润色的中文，再点击润色，等待chatgpt生成一会儿，下面的框中就会生成润色后的英文。


![Image text](https://github.com/XinyuanLiao/PaperPolishing/blob/main/demo.png)


## 翻译：


![Image text](https://github.com/XinyuanLiao/PaperPolishing/blob/main/demo1.png)


## 全新界面:


![Image text](https://github.com/XinyuanLiao/PaperPolishing/blob/main/demo2.png)




