    
**简要描述：** 

- 修改商品价格

**请求URL：** 
- ` http://xx.com/api/updateGoodsPrice`
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|env |否  |string |环境（不传则默认qa环境）   |
|pid |否  |string |商家id（不传则根据env判断，dev为17，qa为1）   |
|storeId |是  |string | 门店id|
|goodsId     |是  |string | 商品id    |
|originalPrice     |否  |string | 市场价    |
|salePrice     |是  |string | 商家统一价（门店id为商家店时，此字段代表商家统一价；门店id为门店时，此字段代表门店售价）   |

**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env	  |qa     |
|storeId |189017 |
|goodsId |125160117 |
|originalPrice |0.04|
|salePrice |2 |

- 备注：originalPrice需要大于salePrice

 **返回示例**

``` 
{
    "code": 1,
    "msg": "请求成功",
    "请求场景": "修改商品价格",
    "data": {
        "code": {
            "errcode": "0",
            "errmsg": "处理成功"
        },
        "data": {
            "failSkuIdList": [],
            "result": true,
            "outerGoodsIdList": null,
            "goodsId": null,
            "goodsDetailResultVoList": null,
            "skuList": null,
            "errorMsg": null,
            "distributorId": null,
            "distributorResponse": null
        }
    }
}
```


