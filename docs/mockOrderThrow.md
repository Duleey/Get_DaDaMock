    
**简要描述：** 

- 操作订单拣货

**请求URL：** 
- ` http://xx.com/api/mockOrderThrow `
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|orderNo |是  |string | 订单编号    |
|env |否  |string |环境（不传则默认qa环境）   |
|pid |否  |string |商家id（不传则根据env判断，dev为17，qa为1）   |
|pickNum |否  |string |商品发货数量列表，逗号为英文逗号，数量必须与订单商品数量一致   |


**请求参数示例**

|参数名|数据|
|:----    |:-------    |
|orderNo |125160117 |
|env	  |qa     |
|pid |189017|
|pickNum |1,2,3 |


 **返回示例**

``` 
  {
    "code": 1,
    "msg": "请求成功",
    "请求场景": "操作订单拣货",
    "操作模式": "当前模式为整单发货模式",
    "data": {
        "logBizData": "568442010118",
        "monitorTrackId": "ad99358b-40d3-4914-9aba-d345117e24bb",
        "processResult": true,
        "responseVo": {},
        "returnCode": "000000",
        "returnMsg": "处理成功",
        "successForMornitor": true,
        "timestamp": "1567994645199"
    }
}
```



