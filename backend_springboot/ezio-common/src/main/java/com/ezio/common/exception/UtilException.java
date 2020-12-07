package com.ezio.common.exception;

import io.swagger.annotations.ApiModel;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName UtilException.java
 * @Description 工具类异常
 * @createTime 2020年12月06日 12:03:00
 */

@ApiModel("工具类异常")
public class UtilException extends RuntimeException {

    private static final long serialVersionUID = -2821941270019104196L;

    public UtilException(Throwable e)
    {
        super(e.getMessage(), e);
    }

    public UtilException(String message)
    {
        super(message);
    }

    public UtilException(String message, Throwable throwable)
    {
        super(message, throwable);
    }
}
