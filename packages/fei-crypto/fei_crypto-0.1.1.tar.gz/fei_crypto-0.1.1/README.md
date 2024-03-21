# comm

```shell
pipx install fei-crypto
say -t 'hello world' # cowsay
os # operating system
dt # datetime
ts # timestamp
ms # milliseconds
nano # nanoseconds
e --help
e 'PATH' # 打印环境变量,后面跟名称
  - env_name:环境变量名
uuid # uuid
btc-eth # 从币安获取比特币和以太坊的价格 支持socks5代理设置,设置环境变量->HTTP_PROXY=socks5h://127.0.0.1:7890
rmw "./1.png" --colors 5 # 简单的去水印
tg-login # telegram 获取sessionString
captcha  # 阿里云验证码识别,3个参数,pri_id可选,默认值:dn
  - file_abs_path:图片绝对路径
  - aliyun_ocr_appcode:阿里云appcode [购买地址](https://market.aliyun.com/products/57124001/cmapi030368.html?spm=5176.2020520132.101.3.596972189IxPGX)
  - pri_id:文字类型（dn：纯数字，ne：英文数字，de：纯英文）
```
# dev
```shell
poetry shell
poetry run python --version
poetry run os
poetry run dt
poetry run ts
```

# publish
```shell
poetry build
poetry publish
```