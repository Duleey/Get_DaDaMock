    
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
|pid |否  |string |商家id（不传则根据env判断，dev为17，qa为1）   |
|outerGoodsCode |否  |string |spu编码（不传则默认当前秒级时间戳）   |
|outerSkuCode |否  |string |商家编码（不传则默认当前秒级时间戳）   |
|deliveryTypeIdList |否  |string |配送id（1.同城限时达;2.全城配）   |
|title |是  |string | 商品标题|
|salePrice     |否  |string | 售价（不传则默认0.01）    |
|originalPrice     |否  |string | 市场价（不传则默认空）    |
|adviseSalePriceMin     |否  |string | 门店售价范围开始值（不传则默认0.01）    |
|adviseSalePriceMax     |否  |string | 门店售价范围结束值（不传则默认1）    |
|goodsWeight     |否  |string | 商品重量(如果运费模板是按照重量计算，该字段必填，kg，两位小数；不传则为空)    |
|goodsVolume     |否  |string | 商品体积(如果运费模板是按照体积计算，该字段必填，m3，两位小数；不传则为空)    |
|goodsImageUrl     |否  |string | 商品图片（不传则默认一张图片）    |

**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env	  |qa     |
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


