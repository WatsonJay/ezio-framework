package com.ezio.common.utils;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTDecodeException;
import com.auth0.jwt.interfaces.DecodedJWT;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Date;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName JwtUtils.java
 * @Description jwt工具类
 * @createTime 2020年12月05日 10:32:00
 */
public class JwtUtils {
    public static Logger logger= LoggerFactory.getLogger(JwtUtils.class);
    /**
     * 失效时间
     */
    private static final long EXPIRE_TIME = 24 * 60 * 60 * 1000;
    /**
     * 生成签名
     *
     * @param username 用户名
     * @param password   用户的密码
     * @return 加密的token
     */
    public static String sign(String username, String password) {
        Date date = new Date(System.currentTimeMillis() + EXPIRE_TIME);
        Algorithm algorithm = Algorithm.HMAC256(password);
        // 附带username信息
        return JWT.create()
                .withClaim("username", username)
                .withExpiresAt(date)
                .sign(algorithm);
    }

    /**
     * 校验token是否正确
     *
     * @param token  密钥
     * @param password 用户的密码
     * @return 是否正确
     */
    public static boolean verify(String token, String username, String password) {
        try {
            //根据密码生成JWT效验器
            Algorithm algorithm = Algorithm.HMAC256(password);
            JWTVerifier verifier = JWT.require(algorithm)
                    .withClaim("username", username)
                    .build();
            //效验TOKEN
            DecodedJWT jwt = verifier.verify(token);
            return true;
        } catch (Exception exception) {
            logger.error("JWT存在问题，验证失败");
            return false;
        }
    }
    /**
     * 获得token中的信息无需secret解密也能获得
     *
     * @return token中包含的用户名
     */
    public static String getUsername(String token) {
        try {
            DecodedJWT jwt = JWT.decode(token);
            return jwt.getClaim("username").asString();
        } catch (JWTDecodeException e) {
            logger.error("JWT存在问题，提取信息失败");
            return null;
        }
    }
}
