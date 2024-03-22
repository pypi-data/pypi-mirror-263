package policyguard.encryption

# Define a minimum standard for encryption algorithms
allowed_encryption_algorithms = {"AES256", "RSA-OAEP", "ChaCha20"}

# Define a policy for encrypting data at rest.
default password_encrypted = false

password_encrypted {
    encryption_method := input.password_encryption_method
    allowed_encryption_algorithms[encryption_method]
}

# Define a policy for encrypting data in transit.
default data_in_transit_encrypted = false

data_in_transit_encrypted {
    input.transit.encryption.algorithm == allowed_encryption_algorithms[_]
}

# Define a policy for using HTTPS for all login forms.
default use_https = false

use_https {
    input.protocol == "HTTPS"
}

# Overall policy to check if all conditions are met for a secure login.
default encryption_enforced = false

encryption_enforced {
    password_encrypted
    data_in_transit_encrypted
    use_https
}
