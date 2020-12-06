package com.ezio.framework.datasource;

import com.alibaba.druid.util.DruidPasswordCallback;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.util.StringUtils;

import java.util.Properties;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName AesDruidPasswordCallback.java
 * @Description TODO
 * @createTime 2020年11月26日 18:05:00
 */
public class AesDruidPasswordCallback extends DruidPasswordCallback {

    @Value("${ezio.aesKey}")
    private String aesKey;

    /**
     * 做个缓存，防止一直请求
     */
    private String password = null;

    @Override
    public void setProperties(Properties properties){
        if (!StringUtils.isEmpty(password)) {
            // 程序应只在启动时调用密码解密，之后保存在内存中，不能每次使用都调用接口获取密码
            setPassword(password.toCharArray());
            return;
        }
        super.setProperties(properties);
        password = properties.getProperty("password");
        try {

        }
        catch (Exception e){

        }
    }
}
