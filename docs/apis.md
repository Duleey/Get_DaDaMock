    
**简要描述：** 

- 获取接口list接口

**请求URL：** 
- ` http://xx.com/apis`
  
**请求方式：**
- GET 

**参数：** 

无

 **返回示例**

``` 
  {
    "code": 1,
    "msg": "请求成功",
    "请求场景": "接口列表",
    "prefix": "/api",
    "data": [
        {
            "mock订单状态": {
                "path": "/getDaDaMock",
                "params": {
                    "env": "环境",
                    "type": "模拟类型",
                    "paramterInput": "订单编号"
                }
            },
            "新增商品": {
                "path": "/addGoods",
                "params": {
                    "env": "环境",
                    "storeId": "门店id",
                    "outerGoodsCode": "spu编码",
                    "title": "商品标题",
                    "salePrice": "售价",
                    "originalPrice": "市场价",
                    "adviseSalePriceMin": "门店售价范围开始值",
                    "adviseSalePriceMax": "门店售价范围结束值",
                    "goodsImageUrl": "商品图片"
                }
            },
            "获取商品详情": {
                "path": "/getGoodsDetail",
                "params": {
                    "env": "环境",
                    "goodsId": "商品id",
                    "storeId": "门店id"
                }
            },
            "修改商品价格": {
                "path": "/updateGoodsPrice",
                "params": {
                    "env": "环境",
                    "storeId": "门店id",
                    "goodsId": "商品id",
                    "originalPrice": "市场价",
                    "salePrice": "商家统一价"
                }
            },
            "修改商品上下架状态": {
                "path": "/updateGoodsShelfStatus",
                "params": {
                    "env": "环境",
                    "goodsIdList": "商品id（多个商品id时，请用，号隔开）",
                    "isPutAway": "商品上、下架（0：上架 1:下架）",
                    "storeId": "门店id"
                }
            },
            "修改商品库存": {
                "path": "/updateGoodsStock",
                "params": {
                    "env": "环境",
                    "storeId": "门店id",
                    "goodsId": "商品id",
                    "editStockNum": "需要修改的库存"
                }
            }
        }
    ]
}
```

 **备注** 



