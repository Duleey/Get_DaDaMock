    
**简要描述：** 

- 修改商品库存

**请求URL：** 
- ` http://xx.com/api/updateGoodsStock `
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|env |是  |string |环境（不传则默认qa环境）   |
|storeId |是  |string | 门店id    |
|goodsId     |是  |string | 商品id    |
|editStockNum     |是  |int | 需要修改的库存    |

**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|env	  |qa     |
|storeId |189017|
|goodsId |125160117 |
|editStockNum |9999|

 **返回示例**

``` 
  {
    "error_code": 0,
    "data": {
      "uid": "1",
      "username": "12154545",
      "name": "吴系挂",
      "groupid": 2 ,
      "reg_time": "1436864169",
      "last_login_time": "0",
    }
  }
```



