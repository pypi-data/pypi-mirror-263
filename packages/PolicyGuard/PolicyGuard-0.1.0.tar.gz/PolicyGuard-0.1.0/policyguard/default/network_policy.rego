package policyguard.network

# Define the set of allowed IP addresses to include only localhost.
allowed_ips := {"127.0.0.1", "::1"}

# Define required headers in requests.
required_headers := {"Authorization", "Content-Type"}

# Allowed HTTP methods for requests.
allowed_methods := {"GET", "POST"}

# Policy to check if the source IP is allowed.
allow_source_ip {
    input.source_ip
    allowed_ips[input.source_ip]
}

# Policy to check if all required headers are present in the request.
allow_headers {
    # Ensure every required header is included in the input headers.
    required_headers == {header | header := input.headers[_][0]}
}

# Policy to check if the HTTP method is allowed.
allow_method {
    input.method
    allowed_methods[input.method]
}

# Default decision for allow_request.
default network_enforced = false

# Combined policy to allow a request only if it passes all checks.
network_enforced {
    allow_source_ip
    allow_headers
    allow_method
}