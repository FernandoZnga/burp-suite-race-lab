# Contributing to Burp Suite Laboratory Exercise

## Overview

This repository contains educational materials for a Master's Degree in Cybersecurity program. Contributions that enhance the learning experience are welcome.

## Types of Contributions

### ✅ Welcome Contributions

- **Documentation improvements**
- **Code optimization and best practices**
- **Error handling enhancements**
- **Cross-platform compatibility fixes**
- **Educational content additions**
- **Security best practices updates**

### ❌ Unwelcome Contributions

- **Malicious code or exploits for unauthorized use**
- **Features that could facilitate illegal activities**
- **Code that targets real-world systems without permission**

## Contributing Guidelines

### 1. Educational Focus

All contributions must maintain the educational nature of this project:

- Include clear documentation explaining the purpose
- Add comments explaining security concepts
- Provide safe, laboratory-focused examples

### 2. Code Quality

- Follow Python PEP 8 style guidelines
- Include type hints where appropriate
- Add docstrings for functions and classes
- Ensure cross-platform compatibility

### 3. Security Considerations

- Never include real credentials or session tokens
- Ensure examples only target PortSwigger Academy labs
- Include appropriate warnings about ethical use

## Development Setup

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # OR
   venv\Scripts\activate  # Windows
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Submission Process

### 1. Before Submitting

- [ ] Test your changes thoroughly
- [ ] Update documentation if needed
- [ ] Ensure code follows project standards
- [ ] Verify educational value of changes

### 2. Pull Request Requirements

**Title Format**: `[TYPE] Brief description`

Types:
- `[DOCS]` - Documentation updates
- `[FEAT]` - New features
- `[FIX]` - Bug fixes
- `[REFACTOR]` - Code improvements
- `[SECURITY]` - Security-related changes

**Description Template**:
```markdown
## Description
Brief description of changes

## Educational Value
How this improves the learning experience

## Testing
How you tested the changes

## Checklist
- [ ] Code follows project standards
- [ ] Documentation updated
- [ ] Educational focus maintained
- [ ] No real credentials included
```

### 3. Review Process

1. **Automated checks** - Code style and basic validation
2. **Educational review** - Ensuring academic value
3. **Security review** - Verifying ethical use guidelines
4. **Technical review** - Code quality and functionality

## Specific Contribution Areas

### Documentation

- **README improvements** - Clearer instructions, better formatting
- **Setup guides** - Platform-specific installation help
- **Troubleshooting** - Common issues and solutions
- **Educational context** - Background on security concepts

### Code Enhancements

- **Error handling** - Better exception management
- **Logging** - Improved output and debugging
- **Configuration** - Easier setup and customization
- **Performance** - Optimization for better learning experience

### Educational Content

- **Examples** - Additional lab scenarios
- **Explanations** - Security concept clarifications
- **Best practices** - Ethical hacking guidelines
- **Related resources** - Links to learning materials

## Code Style Guidelines

### Python Style

```python
# Good: Clear, documented, typed
async def send_request(session: aiohttp.ClientSession, url: str) -> dict:
    """
    Send HTTP request and return parsed response.
    
    Args:
        session: aiohttp session instance
        url: Target URL for request
        
    Returns:
        Dictionary containing response data
    """
    try:
        async with session.get(url) as response:
            return await response.json()
    except Exception as e:
        logger.error(f"Request failed: {e}")
        return {}
```

### Documentation Style

- Use clear, concise language
- Include code examples
- Explain security concepts
- Provide step-by-step instructions
- Add warnings for ethical considerations

## Questions and Support

For questions about contributing:

1. **Check existing issues** - Your question might be answered
2. **Create a discussion** - For general questions
3. **Open an issue** - For bugs or feature requests

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes for significant contributions
- Academic citations where appropriate

## License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

*This project is part of academic research in cybersecurity education. All contributions should maintain the educational and ethical focus of the work.*

