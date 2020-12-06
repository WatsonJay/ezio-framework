package com.ezio.framework.web.exception;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RestControllerAdvice;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName GlobalExceptionHandler.java
 * @Description TODO
 * @createTime 2020年12月06日 11:46:00
 */

@RestControllerAdvice
public class GlobalExceptionHandler {
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
}
