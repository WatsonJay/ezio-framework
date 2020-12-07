package com.ezio.common.core.domain;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.io.Serializable;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName QueryParam.java
 * @Description 统一分页查询类
 * @createTime 2020年12月07日 22:21:00
 */

@ApiModel("统一分页查询类")
public class QueryParam<T> implements Serializable {

    private static final long serialVersionUID = -6563212813240469234L;

    @ApiModelProperty(value = "每页数量", name = "pageSize",dataType = "int", example = "10")
    private int pageSize;
    @ApiModelProperty(value = "当前页数", name = "pageNum",dataType = "int", example = "1")
    private int pageNum;
    @ApiModelProperty(value = "具体参数", name = "param",dataType = "T", example = "")
    private T param;

    public int getPageSize() {
        return pageSize;
    }
    public void setPageSize(int pageSize) {
        this.pageSize = pageSize;
    }
    public int getPageNum() {
        return pageNum;
    }
    public void setPageNum(int pageNum) {
        this.pageNum = pageNum;
    }
    public T getParam() {
        return param;
    }
    public void setParam(T param) {
        this.param = param;
    }

    public QueryParam(){}

    public QueryParam(int pageSize, int pageNum, T param){
        this.param = param;
        this.pageSize = pageSize;
        this.pageNum = pageNum;
    }
}
