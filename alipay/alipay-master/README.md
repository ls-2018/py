# alipay 支付宝支付

#### 详细信息见：
https://www.cnblogs.com/alice-bj/articles/9399334.html

#### 开发：
###### 1. SDK 依赖 
    
```
pip3 install pycryptodome
```

###### 2. 实例化AliPay()对象时：
需要去阿里官网申请：
https://openhome.alipay.com/platform/appDaily.htm?tab=info
> 正式：需要营业执照

> 测试：沙箱环境
https://docs.open.alipay.com/api_1/alipay.trade.page.pay
```
1. APPID
2. 支付宝得公钥
3. 商家得私钥
4. 支付成功，post请求，处理订单为已支付
5. 支付成功，跳转得页面
```

  
###### 3. 对商品，价格，订单号加密，跳转到支付得页面
 
```
eg:
  query_params = alipay.direct_pay(
    subject="购买得商品，衣服",  # 商品简单描述
    out_trade_no= out_trade_no,  # 商户订单号
    total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
   )
   "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
```
###### 4. 支付成功，跳转到商家页面
###### 5. 支付成功，阿里会发post请求，处理订单得状态，需要校验阿里得签名
  

---
  

##### 原始得

```
s9alipay_src
```

##### 自己练习

```
alipay
```
      
