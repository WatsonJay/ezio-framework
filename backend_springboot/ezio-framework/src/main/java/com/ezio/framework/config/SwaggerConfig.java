package com.ezio.framework.config;

import com.github.xiaoymin.swaggerbootstrapui.annotations.EnableSwaggerBootstrapUI;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import java.util.Collections;

/**
 * @author admin
 * @version 1.0.0
 * @ClassName SwaggerConfig.java
 * @Description TODO
 * @createTime 2020年11月11日 17:02:00
 */

@Configuration
@EnableSwagger2
@EnableSwaggerBootstrapUI
public class SwaggerConfig {

    @Bean(value = "defaultApi")
    public Docket apiSystem() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select() // 选择那些路径和api会生成document
                // 对指定api进行监控
                .apis(RequestHandlerSelectors.basePackage("com.ezio.ezio-system"))
                .paths(PathSelectors.any())
                .build()
                .apiInfo(apiInfo())
                .groupName("系统框架接口");
    }

    private ApiInfo apiInfo(){
        return new ApiInfo(
                "EZIO框架RESTful APIs实例文档",
                "我的博客网站：http://www.nothingistrue.top，欢迎大家访问。",
                "API V1.0",
                " 127.0.0.1:13520",
                new Contact("JayWatson", "https://github.com/WatsonJay", "446725026@qq.com"),
                "Apache", "http://www.apaJayWatsonche.org/", Collections.emptyList());
    }
}
