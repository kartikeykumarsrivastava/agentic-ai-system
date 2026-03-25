package com.cloudnexustech.gatewayservice.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/chat")
public class ChatController {

    @Autowired
    private RestTemplate restTemplate;

    @PostMapping
    public String chat(@RequestBody Map<String, String> req) {

        return restTemplate.postForObject(
            "http://localhost:8000/ask",
            req,
            String.class
        );
    }

}