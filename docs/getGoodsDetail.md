**简要描述：** 

- 获取商品详情

**请求URL：** 
- ` http://xx.com/api/getGoodsDetail `
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|env |否  |string |环境（不传则默认qa环境）   |
|goodsId |是  |string | 商品id    |
|storeId     |否  |string | 门店id    |

**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env	  |qa     |
|goodsId |125160117 |
|storeId |189017 |

 **返回示例**

``` 
  {
    "code": 1,
    "msg": "请求成功",
    "请求场景": "查询商品详情",
    "data": [
        {
            "code": {
                "errcode": "0",
                "errmsg": "处理成功"
            },
            "data": {
                "goods": {
                    "selectedSaleAttrInfoList": null,
                    "initialSales": 0,
                    "goodsId": 121360155,
					......
                ]
}
```


 **备注** 
无


