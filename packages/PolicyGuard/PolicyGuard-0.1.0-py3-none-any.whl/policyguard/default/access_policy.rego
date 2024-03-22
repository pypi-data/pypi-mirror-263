package policyguard.access

# Default decision for login
default allow_login = false

# Define a set of allowed roles
allowed_roles = {"admin", "standard", "guest"}

# Allow login if the user's role and account status are valid,
# the login attempts are within the limit, and any other specified conditions are met.
allow_login {
    is_role_valid(input.user.role)
    input.user.status == "active"
}

# Check if the user's role is valid for login
is_role_valid(role) {
    allowed_roles[role]
}

# A sample list of blacklisted IPs for illustration purposes.
blacklisted_ips = {
    "192.168.1.100",
    "10.10.10.10",
    "172.16.0.1"
}

# Checks if the user's IP address is not in the blacklisted IPs list.
is_access_location_valid {
    not blacklisted_ips[input.user.ip]
}

default is_user_active = false
# Check if the user is active based on login attempts
is_user_active {
    input.user.login_attempts <= 3
}

password_policy = 90

is_password_expired {
    # Get the current time in seconds since the epoch
    now := time.now_ns() / 1000000000
    # Parse the last password change time to seconds since the epoch
    last_changed := time.parse_rfc3339_ns(input.user.password_last_changed) / 1000000000
    # Calculate the max age in seconds
    max_age_seconds := input.password_policy.max_age * 24 * 60 * 60
    # Check if the time since the last password change is within the allowed max age
    not (now - last_changed > max_age_seconds)
}

default access_enforced = false

access_enforced {
    allow_login
    is_access_location_valid
    is_user_active
    not is_password_expired
}