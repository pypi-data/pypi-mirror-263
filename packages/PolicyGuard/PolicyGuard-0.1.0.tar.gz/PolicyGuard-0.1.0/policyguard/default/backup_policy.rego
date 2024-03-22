package policyguard.backup

# Define the backup frequency requirement (days)
backup_frequency_days := 7

# Function to calculate days since the last backup, assuming last_backup_date is a string in "YYYY-MM-DD" format
days_since_last_backup(last_backup_date) = days {
    # Parse the last backup date to time in nanoseconds since the Unix epoch
    last_backup_time_ns := time.parse_rfc3339_ns(sprintf("%sT00:00:00Z", [last_backup_date]))
    # Get the current time in nanoseconds since the Unix epoch
    current_time_ns := time.now_ns()
    # Calculate the difference in nanoseconds, then convert to days
    diff_ns := current_time_ns - last_backup_time_ns
    days := diff_ns / 1e9 / 60 / 60 / 24  # Convert from nanoseconds to days
}

# Check if the backup frequency meets the policy
backup_frequency_met {
    days := days_since_last_backup(input.last_backup_date)
    days <= backup_frequency_days
}

default backup_enforced = false

backup_enforced {
    backup_frequency_met
    input.data_integrity_verified
    input.recovery_process_tested
}