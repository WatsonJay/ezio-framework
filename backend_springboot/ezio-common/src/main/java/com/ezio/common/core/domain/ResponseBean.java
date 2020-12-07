package com.ezio.common.core.domain;

import com.ezio.common.enums.ResponseEnums;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName ResponseBean.java
 * @Description 统一响应类
 * @createTime 2020年12月06日 21:21:00
 */
@ApiModel("统一响应类")
public class ResponseBean<T> {

    @ApiModelProperty(value = "结果编码", name = "code",dataType = "String", example = "200")
    private String code;
    @ApiModelProperty(value = "返回信息", name = "message",dataType = "String", example = "成功")
    private String message;
    @ApiModelProperty(value = "数据集", name = "data",dataType = "T", example = "")
    private T data;

    public String getCode() {
        return code;
    }
    public void setCode(String code) {
        this.code = code;
    }
    public String getMessage() {
        return message;
    }
    public void setMessage(String message) {
        this.message = message;
    }
    public T getData() {
        return data;
    }
    public void setData(T data) {
        this.data = data;
    }

    @Override
    public String toString() {
        return "ResponseBean{" +
                "code='" + code + '\'' +
                ", message='" + message + '\'' +
                ", data=" + data +
                '}';
    }

    public ResponseBean(){}

    public ResponseBean(boolean success, T data) {
        super();
        this.data = data;
    }
    public ResponseBean(boolean success, T data, String code, String message) {
        super();
        this.data = data;
        this.code = code;
        this.message = message;
    }

    public ResponseBean(boolean success, String code, String message) {
        this.code = code;
        this.message = message;
    }
    public ResponseBean(boolean success, ResponseEnums enums){
        this.code=enums.getCode();
        this.message=enums.getMsg();
    }
    public ResponseBean(boolean success,T data,ResponseEnums enums){
        this.data=data;
        this.code=enums.getCode();
        this.message=enums.getMsg();
    }
}
