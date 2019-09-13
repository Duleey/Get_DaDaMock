    
**简要描述：** 

- 修改商品配送属性

**请求URL：** 
- ` http://xx.com/api/updateStoreGoodsDeliveryType `
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|env |否  |string | 环境（不传则默认qa环境）    |
|pid |是  |string |商家id   |
|storeId |是  |string |门店id   |
|goodsId |是  |string |商品id，逗号为英文逗号，最多100个商品id   |
|deliveryType |是  |string |配送类型（1：同城限时达，2：全城配）   |



**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env |qa |
|pid	  |1     |
|storeId |2001|
|goodsId |172610101,172610102,172610103 |
|deliveryType |1 |


 **返回示例**

``` 
{
    "code": 1,
    "msg": "请求成功",
    "请求场景": "修改商品配送类型",
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



