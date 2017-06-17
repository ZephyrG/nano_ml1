# Machine Learning Basics

## 课程1：从人工智能到机器学习
ML borrows from twe fields, AI & Data Science.

### Biggest problems of AI
1. Intelligent agents have limited resources.
2. Computation is local, but problems have global constraints.
3. Computation logic is deductive, but many problems are abductive or inductive in nature.
4. World world is dynamic, but knowledge is limited. AI agent must always begin with it already knows. How it addresses a new problem?
5. Problem solving, reasoning, and learning are complex, but explanation and justification are even more complex.


### Charactristics of AI promblem
1. Data arrive incrementally.
2. Problems exhibit recurring patterns.
3. Problems have multiple levels of abstraction.
4. Many problems are computationally intractable.
5. World is dynamic, but knowledge of the world is static.
6. The world is open-ended, but knowledge of the world is limited.

## 配置Python环境

### 在 Atom 中运行 Python 代码

- step1 确保使用`.py`保存代码
- step2 安装`script`扩展包
    Atom -> Preference -> Setting -> Install, 搜索`script`然后安装
    安装成功后 Packages -> Script -> Run Script 或者快捷键 `Command` + `i`运行

> 用VPN才可以安装


### 命令行教程
- `pwd`
- `ls` `ls -a`列出所有内容，包括隐藏内容
- `open` 可打开文件或文件夹
- `cd` 只输入`cd`时会回到主目录
- `touch` 可创建多个文件，用空格隔开
- `mkdir` 可批量创建多个目录，用空格隔开（如果目录名中有空格在空格前用转义符`\`)
- `rm` 删除文件（不可逆），可删除多个，用空格隔开
- `rmdir` 删除目录（只能是空目录）
- `rm -r` `r`代表recursive, 删除飞空目录 **慎用**
- `rm -ri` or `rm -r -i` 提示是否确认删除


## 编程导论

自然语言是模糊的(Ambiguous),对同样的句子可能会有不同的理解。程序序言不能有这样的模糊性。

### 巴克斯构造 Backus-Naur Form
<Non-terminal> -> replacement
<非终止符> -> 非终止符或者终止符
逐步替换只到只有终止符

### Python表达式

Expression -> Expression Operator Expression
Expression -> Number
Operator -> +
Operator -> *
Number -> 0, 1, ...

### Grace Hopper
The Amazing Grace
nanosecond


## 变量和字符串

**要关注的问题**
1. 变量是什么？
2. 对变量进行赋值（assign a value）是什么意思？
3. 等于号 `=`，在数学和编程方面的含义有什么区别？

`+`可以将字符串连接起来
`+`不能连接字符串和数值
`*`字符串*数字意味着重复多个字符串

**字符串索引和子序列**

<string>[<expression>:<expression>]

`<string>.find(<string>)` -> 1st position in search string where target string appears
大小写敏感

`<string>.replace(<old>, <new>)`

`<string>.split(<seperator>)` if empty means space


## 输入 -> 函数 -> 输出

`<procedure>(<input>, <input>, ...)` // operants or arguments

`return`后的语句不被执行


## 控制流和循环：if 和 While

```
if / while <TextExpreesion>:
    <Block>
```

`<Expression> or <Expression>`
1. 如果第一个表达式是True, Python不会evaluate第二个表达式
2. 如果第一个表达式是False，or construct的值等价于第二个表达式的值

`break`语句
跳出while loop，运行while loop之后的语句


## 调试

**策略**
1. 当程序崩溃时，查看错误消息
    Python Traceback 的最后一行将告诉你哪里出错了。从这里往前阅读可以帮你找到出现问题的地方。
2. 在示例代码的基础上编写代码
    如果修改后的代码不能运行，注释掉编写的代码，并逐步修改示例代码，直到达到期望的结果。
3. 确保示例代码可以运行
    找到示例代码并不能保证示例代码能够在你的系统里运行。检查正在使用的示例代码，确保能按照你的预期运行。
4. 检查（输出）中间结果
    当你的代码没有崩溃，但是行为没有达到预期效果时，你可以向程序中添加输出语句，看看代码中的哪些部分开始出错了。
5. 保留并对比旧版本
    当你的代码可以运行时，先保存一个版本，然后再向其中添加代码。这样如果你引入了太多新的 bug，还可以返回到该版本。

**良好注释**

1. 不要为“作用明显的代码”添加注释
2. 定义函数时添加注释
    所有函数开始定义时都需要添加注释，描述预期的输入和输出结果，并解释函数的作用。这样可以帮助其他人了解函数的目的。
    可以使用 docstring 为函数添加注释。docstring 是多行字符串，充当函数的描述性注释，但是当代码执行时，计算机会保留这些内容，并且在代码运行时用户可以访问这些内容。
3. 及时更新注释
4. 简明扼要

## 列表和For循环
//web crawler

### mutation vs. aliasing 变更和别名
`s = 'Hello'`
`s = 'Yello'`
对于字符串，不改变`s`的值，只改变指向; `'Yello'`是新生成的字符串
`p = ['H','e','l','l','o']`
`p[0] = 'Y'`
对于列表，改变了`p`的值
```
p = ['H','e','l','l','o']
q = p
q[4] = '!'
```
对`q`的变更也改变了`p`,`p`,`q`指的是同一个列表
如果一个object是可变更的，需要注意其它指向同一个object的变量
Aliasing指的是指向同一个object不同变量。

### List Opertations
`append`
`+` <list> + <list>, produce new list
`len`
`<list>.index(<value>)`
`<value> in <list>` / `<value> not in <list>`

`<list> * <number>` / We can multiply a list construct to create a list with the same elements n number of times.

## 如何解决问题

0. Don't Panic :-)
1. What are the input?
    - are inputs valid? - need to check for programmers - defensive programming
    - how are inputs represented?
2. What are the outputs?
3. Work through some examples by hand.
4. Simple mechanical solution
5. Develop incrementally and test as we go

Don't optimize prematurely

`assert <expression>`


## Project: 休息一下
```Python
import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())

while break_count < total_breaks:
  time.sleep(10)
  webbrowser.open("http://v.youku.com/v_show/id_XMzUyMjY5Nzky.html?from=s1.8-3-1.1&spm=a2h0k.8191407.0.0")
  break_count += 1
```

## Project: 私密消息
```Python

import os

def rename_files():
  # get file names from folder
  file_list = os.listdir(path)
  saved_path = os.getcwd()
  # rename each file
  for file_name in file_list:
    os.rename(file_name, filename.translate(None, "01234566789"))

```

## Turles

```Python

import turtle

def draw_squre(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    for i in range(0, 100):
        draw_squre(brad)
        brad.right(3)

    window.exitonclick()

draw_art()


```

## Project: 脏字检测器
```Python
import urllib

def read_text():
  quotes = open(<filename>)
  contents_of_file = quotes.read()
  quotes.close()
  check_profanity(contents_of_file)

def check_profanity(text_to_check):
  connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shit"
                              + text_to_check)
  output = connection.read()
  connection.close()

  if "true" in output:
    print "Profanity Alert!"
  elif "false" in output:
    print "Safe document"
  else:
    print "Could not scan properly"
```

## Class

一般将定义Class的文件和使用的分开。
self 不是关键字，但是大部分 Python 程序员习惯使用它。使用“self”使你的代码更易于其他程序员阅读，所以建议你也这么做。

**预定义的类变量**

 `__doc__`, `__module__`, `__name__`

**继承**
`class Child(Parent)`
method overriding











## change log
2017.05.04 创建
2017.05.06 增加内容
2017.05.07 增加内容
