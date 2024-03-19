# Define the DOCUMENTS_IN dictionary with regex patterns for various document types
DOCUMENTS_IN = {
    "IS_AADHAAR_NUMBER": r"^[0-9]{12}$",
    "IS_BANK_ACCOUNT_NO": r"^[0-9]{9,18}$",
    "IS_BANK_SWIFT_CODE": r"^[A-Z]{4}[A-Z]{2}[0-9A-Z]{2}[0-9A-Z]{3}$",
    "IS_BIRTH_CERTIFICATE_NO": r"^[A-Z]{2}[0-9]{6}[A-Z]{1}[0-9]{2}$",
    # Add the remaining document patterns here...
    "IS_VOTER_ID": r"^[A-Z]{3}[0-9]{7}$",
}

# Define the STANDARD dictionary with regex patterns for various data types
STANDARD = {
    "IS_ALPHA": r"^[a-zA-Z]+$",
    "IS_ALPHANUMERIC": r"^[a-zA-Z0-9]+$",
    "IS_BOOLEAN": r"(true|false)",
    # Corrected the email regex pattern to a more common Python version
    "IS_EMAIL": r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$",
    # Add the remaining standard patterns here...
    "IS_UPPERCASE": r"^[A-Z]+$",
}

# Merge the DOCUMENTS_IN and STANDARD dictionaries to create a combined patterns dictionary
PATTERNS = {**STANDARD, **DOCUMENTS_IN}

# When importing from this module, one can directly access DOCUMENTS_IN, STANDARD, and PATTERNS
