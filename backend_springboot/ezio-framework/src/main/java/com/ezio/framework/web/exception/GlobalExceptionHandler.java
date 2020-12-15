package com.ezio.framework.web.exception;

import com.ezio.common.core.domain.ResponseBean;
import com.ezio.common.enums.ResponseEnums;
import com.ezio.common.exception.UtilException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import javax.servlet.http.HttpServletRequest;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName GlobalExceptionHandler.java
 * @Description 全局异常捕获
 * @createTime 2020年12月06日 11:46:00
 */

@RestControllerAdvice
public class GlobalExceptionHandler {
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    /**
     * 运行时异常的捕获
     * 自定义抛出异常。统一的在这里捕获返回JSON格式的友好提示。
     * @param exception
     * @return
     */
    @ExceptionHandler(value={RuntimeException.class})
    @ResponseBody
    @ResponseStatus(value= HttpStatus.INTERNAL_SERVER_ERROR)
    public <T> ResponseBean<T> sendError(RuntimeException exception){
        logger.error("occurs error when execute method ,message {}",exception.getMessage());
        return new ResponseBean<>(false, ResponseEnums.RUNTIME_EXCEPTION);
    }
}
