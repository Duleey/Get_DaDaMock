    
**简要描述：** 

- 修改商品上下架状态

**请求URL：** 
- ` http://xx.com/api/updateGoodsShelfStatus`
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|env |否  |string |环境（不传则默认qa环境）   |
|pid |否  |string |商家id（不传则根据env判断，dev为17，qa为1）   |
|goodsIdList |是  |string | 商品id（多个商品id时，请用，号隔开）    |
|isPutAway     |是  |string | 商品上、下架（0：上架 1:下架）    |
|storeId     |是  |string | 门店id    |

**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env	  |qa     |
|goodsIdList |12516021 |
|isPutAway |1 |
|storeId |189021|

 **返回示例**

``` 
{
    "code": 1,
    "msg": "请求成功",
    "请求场景": "修改商品上下架状态",
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
            "goodsDetailResultVoList": [
                {
                    "code": 0,
                    "goodsId": 12516021,
                    "message": "操作成功"
                }
            ],
            "outerGoodsIdList": null,
            "distributorResponse": null,
            "errorMsg": null
        }
    }
}
```



