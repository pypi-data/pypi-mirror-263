# xy_string

- zh_CN [简体中文](readme/README_zh_CN.md)
- zh_TW [繁体中文](readme/README_zh_TW.md)
- en [English](readme/README_en.md)


# 说明
字符串工具.

<a href="https://github.com/ShipOfOcean/xy_string.git" target="_blank">Github地址</a>

## 安装

```bash
pip install xy_string
```

## 开始

```python
from xy_string.utils import is_empty_string, empty_string, contains_zh

is_empty_string("")
# true

is_empty_string("empty")
# false

empty_string("empty")
# empty

empty_string(None, default="empty")
# empty

empty_string(None)
# None

contains_zh("中文")
# True

contains_zh("Chinese")
# False

```

## 捐赠

如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢
<br />
![微信](readme/WeChat.png)
![支付宝](readme/Alipay.png)

## 联系方式

```
微信: yuyangitt
邮箱: 845262968@qq.com
```