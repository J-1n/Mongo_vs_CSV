# Mongo_vs_CSV
## 这是一个CSV数据、MongoDB数据、Quantaxis数据的读取速度测试。
## 由于可能不太专业，最后的结果让人震惊。还请大佬们慷慨相助为谢！

----------------事件概述----------------
对比电脑读取CSV数据、MongoDB数据及QA本地数据（其实也是存在MongoDB中）的速度。
理论上来说读取数据库肯定比比读取CSV文件快。
然而。。。请继续往下看

----------------电脑概况----------------
系统：Win10 64位 专业版
内存：16G
硬盘：固态硬盘

----------------数据来源----------------
CSV数据：自行抓取的A股市场所有股票从2017-06-15到2020-01-23的日线数据；
MongoDB数据：就是把上面的CSV数据文件存入到MongoDB中；
QA本地数据：进入client后，先save all，然后在策略中选取2017-06-15到2020-01-23的股票日线数据。

----------------策略思路----------------
就是一个非常简单的测试，可能都谈不上策略。
遍历每支股票，计算出其五日均线，找到五日均线中的最大值，然后把结果存到excel表中。

----------------跑分结果----------------
在数据和代码几乎完全相同的情况下，分别把三种不同的数据格式转换成pandas.DataFrame，
然后挨个单独跑策略，耗时情况如下：
QA(QA.DataStruct→pd.DataFrame)：255秒
MongoDB(json→pd.DataFrame)：48秒
CSV(csv→pd.DataFrame)：29秒

看到这个结果，我也只能用[黑人问号脸.jpg]来表达当时的感受了。

----------------作者疑问----------------
是否属于操作不当？还望大佬慷慨解答为谢！

----------------相关附件----------------
由于论坛好像不能上传附件，所以源代码请到我github去查看吧https://github.com/J-1n/Mongo_vs_CSV
或者从网盘中下载完整的代码+数据文件链https://pan.baidu.com/s/1RfWXIJG2kHuAZnCkOqqhGw 提取码: gv7j
