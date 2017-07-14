##  构建实验环境

### 1  安装python（2.7）  https://www.python.org/

### 2  安装pip：

2.1 下载pip     https://pypi.python.org/pypi/pip/9.0.1 

2.2 解压缩后，安装指令  python setup.py install

2.3 pip升级  python -m pip install --upgrade pip

2.4 pip安装扩展包 pip install jieba （这里以jieba包为例），如果速度较慢，可改为国内的阿里源，
    即 pip install jieba -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com 

### 3  安装pycharm       http://www.jetbrains.com/pycharm/

### 4  使用GitHub获取代码

4.1  安装git    https://git-scm.com/ 

4.2  登陆自己的GitHub账号，找到 https://github.com/Roshanson/TextInfoExp ，点击fork，得到项目的复制。
（如果只是简单的获取代码可直接 git clone https://github.com/Roshanson/TextInfoExp,不需要fork，也可以直接下载zip包放进pycharm）

4.3  打开pycharm，首先设置git的位置及github账号，点击Test都通过后继续，依次在菜单栏点击  VCS  checkout from version control 
 GitHub，登陆自己的账号后选择相应的项目，得到代码。
    
4.4  （更新fork的项目到最新的版本）Syncing a fork  https://help.github.com/articles/syncing-a-fork/

### 5 ipython交互式开发环境

5.1  安装ipython  pip install ipython 

5.2  安装jupyter（即notebook） pip install notebook

5.3  jupyter notebook 启动，打开浏览器即可（默认1224端口）
