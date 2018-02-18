# SimpleApiTest
一个简单的接口测试框架

##我想要这样的功能：
1.纯python实现，方便打断点调试。可与robot、pytest、unittest等库集成
2.用原生json定义接口测试数据，同时支持模板功能。通过模板功能来控制测试数据中的变量。
3.每一个针对单个接口的测试用例都要有：
name：测试名
description：测试描述
url：url，url里也可以带变量
headers：header里的值，可选。
method：HTTP方法
input；
    input_template：输入数据模板
    input_var:输入数据中的可变化部分
output：
    output_template:返回结果模板
    output_var：返回结果中的可变化部分
4.支持端到端接口测试：也就是多个接口按顺序调用下来。接口1的返回值传递给接口2做输入值。
5.要简单


##我做了什么：
###Feature 1 （总代码量不算注释一共15行）：json文件模板下的测试数据功能：
很多测试框架选择把数据放在：Excel里，CSV里，YAML里，源代码里。
但这些都不是我想要的，Excel太笨重，CSV很土，YAML里太难调，源代码里太难读。

ok，如果要发送的是json数据，要测的是rest API，那么数据我就直接放在json里。
但同样有和YAML或者CSV, EXCEL里一样的问题，放进去之后这些数据就写死了，很不灵活。
然后我解决了这个问题。

数据我划分成可变部分和不变部分。


比如一个HTTP请求要发送{"username"："xxxx"，"password"："xxxx"}
这个数据里除了xxxx以外，全是不变部分。至少不会经常不停的变。那么不变部分直接写死在json文件里。
而可变部分在json文件里用模板语法代替，什么是模板？先跳过这个，这个json文件看上会是这样的：
{"username"：{{user.username}}，"password"：{{user.password}}}
这里{{user.username}}和{{user.password}}就是可变部分。不直接写死他们的值。而是，用模板的变量代替。
这个变量就是{{user}}，这个变量有两个属性，一个username一个password，之后我们再在测试用例里把这个变量
传递给模板，就可以渲染出真正的测试数据。也就是说，这个可变部分，真正写，我写在测试用例里面。

比如这样：

@xxxxx(data=[("user1,"password1"),("user2","password2")])
def test_user_login(data):
    login(data)


上面这个是示意的伪代码，相信用过pytest或者其他测试框架的你大概能明白我的意思吧。
这个功能总共花了15行代码，python就是这么神奇。嗯，当然在json文件里你不但可以用变量，还可以用if else，可以
用循环。总之一句话，灵活而可读。





