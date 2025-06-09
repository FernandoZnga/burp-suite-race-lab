# Example Configurations

This directory contains example configurations for different types of Burp Suite laboratory exercises.

## Available Examples

### Race Condition Labs

1. **Shopping Cart Race Condition**
   - File: `cart_race_condition.py`
   - Target: Cart quantity manipulation
   - Technique: Concurrent POST requests

2. **Coupon Code Race Condition**
   - File: `coupon_race_condition.py`
   - Target: Discount code application
   - Technique: Parallel coupon usage

3. **User Registration Race Condition**
   - File: `registration_race_condition.py`
   - Target: Account creation limits
   - Technique: Simultaneous registrations

## Usage Instructions

1. **Choose the appropriate example** for your lab
2. **Copy the example** to the main directory
3. **Rename** to `cart_script.py` (or modify imports)
4. **Update configuration** with your lab-specific values
5. **Run the script** using the standard execution method

## Example Structure

Each example includes:

- **Configuration section** - Headers, cookies, data
- **Attack logic** - Specific to the vulnerability type
- **Validation** - Checks for proper configuration
- **Documentation** - Explanation of the attack vector

## Creating New Examples

When creating new examples:

1. **Follow the naming convention**: `vulnerability_type_target.py`
2. **Include comprehensive documentation**
3. **Add configuration validation**
4. **Ensure educational value**
5. **Test with actual lab instances**

## Educational Notes

These examples are designed to:

- **Demonstrate different attack vectors**
- **Show proper tool usage**
- **Provide learning templates**
- **Illustrate security concepts**

⚠️ **Remember**: Only use these examples on authorized laboratory environments.

