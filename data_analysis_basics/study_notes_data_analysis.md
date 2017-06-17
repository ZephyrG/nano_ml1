<meta http-equiv="Content-Type" content="text/html; charset=utf-8">


# 数据分析基础

## 配置Anaconda

使用Anaconda来管理Python所用的包和环境，可以轻松安装常使用的包。还可以创建虚拟环境，以便更轻松的处理多个项目。

Anaconda 实际上是一个软件发行版，它附带了 conda、Python 和 150 多个科学包及其依赖项。

conda 是一种只能通过命令行来使用的程序

Anaconda 附带了一大批数据科学包，因此你可以立即开始处理数据。其次，使用 conda 来管理包和环境能减少将来在处理你要使用的各种库时遇到的问题。

### 安装

安装后运行`conda list` 时提示 `-bash: conda: command not found`

查看了`.bash_profile`发现里面是有正确的`PATH`

之前曾家安装过一次Anaconda，把之前的版本卸载后可以用了. 终于可以不用Navigator了，好慢的。

为避免报错，在默认环境下更新所有包。运行 `conda upgrade --all`

### 管理包
要安装包很简单 `conda install package_name`;
还可以安装多个包，比如 `conda install numpy scipy pandas`；
可以指定包的版本，`conda install numpy=1.10`;
如果不知道要找的包的确切名称，可以尝试使用`conda search search_term`进行搜索。

### 管理环境

可以使用 conda 创建环境以隔离项目. 要创建环境，请在终端中使用`conda create -n env_name list of packages`. '-n env_name'设置环境的名称(`-n`是指名称), `list of packages`是要安装在环境中的包的列表. 例如，要创建名为`my_env`的环境并在其中安装 numpy，请键入`conda create -n my_env numpy`.

**创建环境**
创建环境时，可以指定要安装在环境中的 Python 版本。这在你同时使用 Python 2.x 和 Python 3.x 中的代码时很有用。要创建具有特定 Python 版本的环境，请键入类似于 `conda create -n py3 python=3` 或 `conda create -n py2 python=2`的命令。要安装特定版本（例如 Python 3.3），请使用`conda create -n py python=3.3`.

**进入和离开环境**
创建了环境后，在 OSX/Linux 上使用`source activate my_env`进入环境; 要离开环境，请键入`source deactivate`.

**保存和加载环境**

共享环境能让其他人安装你的代码中使用的所有包，并确保这些包的版本正确。可以使用`conda env export > enviroment.yaml`将包保存为 YAML; 要通过环境文件创建环境，使用`conda env create -f environment.yaml`.这会创建一个新环境，而且它具有在 `environment.yaml` 中列出的同样的库。

**列出环境**
如果忘记了环境的名称,可以使用`conda env list`列出你创建的所有环境。你会看到环境的列表，而且你当前所在环境的旁边会有一个星号。默认的环境（即当你不在环境中时使用的环境）名为`root`.

**删除环境**
`conda env remove -n env_name`删除指定的环境.


### 最佳做法

**使用环境**
创建Python 2和Python 3独立环境，分别安装大多数标准的数据科学包，比如numpy, scipy, pandas等。

**共享环境**
在 GitHub 上共享代码时，最好同样创建环境文件并将其包括在代码库中。这能让其他人更轻松地安装你的代码的所有依赖项。对于不使用 conda 的人，我通常还会使用`pip freeze`将一个 pip `requirements.txt`文件包括在内。

[Conda myths and misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)

## 配置Jupyter notebook

Anaconda自动附带了Jupyter notebook，可以在默认环境下使用。要在`conda`环境中安装，`conda install jupyter notebook`; 也可以`pip install jupyter notebook`来安装。

`jupyter notebook`启动 notebook 服务器.

 LaTeX符号创建数学表达式
 `$y = mx + b$`
```
$$
y = \frac{a}{b+c}
$$
```

[Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## 数据分析过程


## Change Log

2017.05.07 创建
2017.05.08 内容更新
