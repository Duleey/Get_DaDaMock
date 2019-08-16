    
**简要描述：** 

- 操作订单拣货

**请求URL：** 
- ` http://xx.com/api/mockOrderThrow `
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|env |否  |string |环境（不传则默认qa环境）   |
|pid |否  |string |商家id（不传则根据env判断，dev为17，qa为1）   |
|orderNo |是  |string | 订单编号    |

**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env	  |qa     |
|pid |189017|
|orderNo |125160117 |

 **返回示例**

``` 
  {
    "code": 1,
    "msg": "请求成功",
    "请求场景": "修改商品库存",
    "data": {
        "code": {
            "errcode": "0",
            "errmsg": "处理成功"
        },
        "data": {
            "result": true,
            "failSkuIdList": null,
            "skuList": null,
            "distributorId": null,
            "goodsId": null,
            "goodsDetailResultVoList": null,
            "outerGoodsIdList": null,
            "distributorResponse": null,
            "errorMsg": null
        }
    }
}
```



