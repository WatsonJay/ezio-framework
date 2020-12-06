package com.ezio.admin;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "com.ezio")
public class EzioAdminApplication {

    public static void main(String[] args) {
        SpringApplication.run(EzioAdminApplication.class, args);
    }

}
