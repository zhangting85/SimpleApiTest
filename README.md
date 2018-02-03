# SimpleApiTest
一个简单的接口测试框架

我想要这样的功能：
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