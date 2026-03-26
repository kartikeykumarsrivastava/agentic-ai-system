package com.cloudnexustech.gatewayservice.controller;

import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController		
@RequestMapping("/policy")
public class PolicyController {

    private final Map<String, Object> policyData = Map.of(
        "eligibility", Map.of(
            "min_salary", 500000,
            "age_range", List.of(21, 60),
            "max_emi_ratio", 0.4
        ),
        "interest", Map.of(
            "rate_range", "8% - 10%",
            "type", "floating"
        ),
        "documents", List.of(
            "Identity Proof",
            "Income Proof",
            "Bank Statement"
        ),
        "process", List.of(
            "Check eligibility",
            "Submit documents",
            "Verification",
            "Approval"
        )
    );

    @GetMapping
    public Map<String, Object> getFullPolicy() {
        return policyData;
    }

    @PostMapping("/query")
    public Object getPolicyByTopic(@RequestBody Map<String, String> req) {
        String topic = req.getOrDefault("topic", "").toLowerCase();

        for (String key : policyData.keySet()) {
            if (topic.contains(key)) {
                return Map.of(key, policyData.get(key));
            }
        }

        return Map.of("message", "No matching policy found");
    }
}