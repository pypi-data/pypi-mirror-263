# shangjian_api

## 安装
```shell
python -m pip install shangjian_api
```

## 用法
### AirWorks Api

#### 基础用法

```python
import json
from shangjian_api.airworks.package_api import AirWorksApi

awp = AirWorksApi(
    base_url="api.airworks.shangjian.tech:30000",
    access_key="xxx",
    access_secret="xxx",
    default_app_id=1,
    default_api_method="GET",
    default_page_num=1,
    default_page_size=100
)

res = awp.call(
    app_url="api_gateway/api/1/daily",
    port_code='',
    date='',
    api_method="GET"
)
print(json.dumps(res, indent=2, ensure_ascii=False))
```


#### 使用本地配置文件时

```python
import json
from shangjian_api.airworks.package_api import AirWorksApi

awp = AirWorksApi(
    default_app_id=1,
    default_api_method="GET",
    default_page_num=1,
    default_page_size=100
)
```

#### 使用api别名作为函数名来调用
```python
res = awp.daily(
    app_id=1,
    port_code='',
    date='',
    api_method="GET"
)
print(json.dumps(res, indent=2, ensure_ascii=False))
```

### KM Api

```python
from shangjian_api.km.base_api import get_indicator_values

indicator_ids = ["all_indexpv_chain_rank_app_by_week_all"]
result = get_indicator_values(indicator_ids)
print(result)
```

### 配置文件内容
> 文件路径: 包安装路径下名为 sdk_config.toml 的文件, 例如
> /usr/lib/python3.8/site-packages/shangjian_api-0.0.2-py3.8.egg/shangjian_api/sdk_config.toml
> 内容如下
```toml
title = "sdk config"

[km]
[km.indicator]
#host = "localhost:8888"
host = ""
username = ""
password = ""

# airworks
[airworks]
[airworks.api]
#host = "localhost:8888"
host = ""
access_key = ""
access_secret = ""
```
## 开发
> 可将包内代码复制,并修改顶级包名,可新增功能,但需要在理解逻辑的前提下修改现有代码

## release log
### 20211028
- km get_indicator_values 接口返回值有序
### 20210826
- 添加支持本地配置文件功能
- 支持顶级包名可变