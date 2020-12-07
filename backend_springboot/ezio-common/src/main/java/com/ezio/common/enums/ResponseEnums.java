package com.ezio.common.enums;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.EnumSet;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName ResponseEnums.java
 * @Description 响应信息枚举类
 * @createTime 2020年12月06日 21:14:00
 */
public enum ResponseEnums {
    /* 成功状态码 */
    SUCCESS("200", "SUCCESS"),

    /* 服务器错误: 00001-09999*/
    /* 参数错误: 10001-19999 */
    /* 登录错误: 20001-29999*/
    /* 业务错误: 30001-39999 */
    /* 系统错误: 40001-49999 */
    UTIL_EXCEPTION("40001", "uitl.exception");
    /* 接口错误: 50001-599999 */

    private String code;
    private String msg;

    private ResponseEnums(String code, String msg) {
        this.code = code;
        this.msg = msg;
    }

    private MessageSource messageSource;

    public ResponseEnums setMessageSource(MessageSource messageSource) {
        this.messageSource = messageSource;
        return this;
    }

    //通过静态内部类的方式注入bean，并赋值到枚举中
    @Component
    public static class ReportTypeServiceInjector {

        @Autowired
        private MessageSource messageSource;

        @PostConstruct
        public void postConstruct() {
            for (ResponseEnums rt : EnumSet.allOf(ResponseEnums.class)) {
                rt.setMessageSource(messageSource);
            }
        }
    }

    public String getCode() {
        return code;
    }
//    public void setCode(String code) {
//        this.code = code;
//    }
    public String getMsg() {
        return messageSource.getMessage(msg,null,msg, LocaleContextHolder.getLocale());
    }
//    public void setMsg(String msg) {
//        this.msg = msg;
//    }
}
