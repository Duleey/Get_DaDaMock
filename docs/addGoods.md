    
**简要描述：** 

- 新增商品

**请求URL：** 
- ` http://xx.com/api/addGoods`
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|env |否  |string |环境（不传则默认qa环境）   |
|storeId |否  |string |门店id（不传则默认env环境下的商家店）   |
|outerGoodsCode |否  |string |spu编码（不传则默认zd+当前秒级时间戳）   |
|title |是  |string | 商品标题|
|salePrice     |否  |string | 售价（不传则默认0.01）    |
|originalPrice     |否  |string | 市场价（不传则默认1）    |
|adviseSalePriceMin     |否  |string | 门店售价范围开始值（不传则默认0.01）    |
|adviseSalePriceMax     |否  |string | 门店售价范围结束值（不传则默认1）    |
|goodsImageUrl     |否  |string | 商品图片（不传则默认一张图片）    |

**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env	  |qa     |
|storeId |3017 |
|title |商品标题 |
|salePrice |0.01|
|originalPrice |1 |
|adviseSalePriceMin |0.01 |
|adviseSalePriceMax |1 |
|goodsImageUrl |https://www.baidu.com/a016cb2de441406289433fd0c71c56bd.png |

- 备注：originalPrice需要大于salePrice

 **返回示例**

``` 
{
    "code": 1,
    "msg": "请求成功",
    "请求场景": "新增商品",
    "data": [
        {
            "code": {
                "errcode": "0",
                "errmsg": "处理成功"
            },
            "data": {
                "failSkuIdList": null,
                "result": true,
                "outerGoodsIdList": null,
                "goodsId": 125550117,
                "goodsDetailResultVoList": null,
                "skuList": [
                    {
                        "outerSkuCode": null,
                        "goodsSkuId": "125550117_130450117",
                        "imageUrl": null,
                        "skuId": 130450117
                    }
                ],
                "errorMsg": null,
                "distributorId": null,
                "distributorResponse": null
            }
        },
        125550117,
        130450117
    ]
}
```


