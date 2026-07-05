# Secrets Rotation Agent Architecture

Automated secrets lifecycle agent that manages credential rotation schedules, detects leaked secrets in code and logs, enforces secret hygiene policies, integrates with vault systems, and provides emergency rotation capabilities for compromised credentials.

## Domain Tools

- **rotate_secret**: Rotate a secret according to its rotation policy
- **scan_for_leaks**: Scan repositories and logs for exposed secrets
- **audit_secret_age**: Audit secrets approaching or exceeding rotation deadline
- **emergency_rotate**: Emergency rotation of potentially compromised credentials
- **check_rotation_status**: Check rotation status and history for a secret