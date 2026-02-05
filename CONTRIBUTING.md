# Contributing to Sarvam AI Skills

Thank you for your interest in contributing! This document provides guidelines for contributing examples, templates, and improvements to this repository.

## How to Contribute

### 1. Code Examples
Add new working examples demonstrating Sarvam AI APIs:

- Place examples in the `examples/` directory
- Include comprehensive documentation
- Add error handling
- Test thoroughly before submitting

### 2. Templates
Create new skill templates for common use cases:

- Place templates in the `templates/` directory
- Follow the existing template structure
- Include API documentation
- Provide code examples

### 3. Improvements
Enhance existing examples or templates:

- Fix bugs
- Improve documentation
- Add new features
- Optimize performance

### 4. Documentation
Improve README files and documentation:

- Fix typos
- Clarify explanations
- Add missing information
- Update outdated content

## Submission Guidelines

### Before Submitting

1. **Test your code**: Ensure all examples work correctly
2. **Follow style guidelines**: Match the existing code style
3. **Add documentation**: Include clear comments and docstrings
4. **Update README**: Add your contribution to relevant README files

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Markdown**: Use consistent formatting
- **Comments**: Write clear, concise comments
- **Naming**: Use descriptive variable and function names

### Example Code Template

```python
"""
Brief description of what this example does.

Module/API: Specific Sarvam AI API used
Author: Your name (optional)
"""

import os
from sarvamai import SarvamAI

def descriptive_function_name(param1: type, param2: type) -> return_type:
    """
    Detailed function description.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ErrorType: When this error occurs
    """
    # Implementation
    pass

def main():
    """Example usage of the function."""
    # Example code
    pass

if __name__ == "__main__":
    main()
```

### Template Document Structure

```markdown
# Template Name

## Overview
Brief overview of the template

## API Information
- Endpoint
- Method
- Model

## Parameters
Table of parameters

## Examples
Code examples

## Use Cases
Common use cases

## Best Practices
Recommended practices

## Resources
Links to documentation
```

## Pull Request Process

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**: `git commit -m "Add: Brief description"`
6. **Push to your fork**: `git push origin feature/your-feature-name`
7. **Open a pull request** with a detailed description

### Commit Message Format

```
Type: Brief description

Detailed explanation if needed

- List of changes
- Another change
```

**Types:**
- `Add:` New feature or example
- `Fix:` Bug fix
- `Update:` Update existing content
- `Docs:` Documentation changes
- `Refactor:` Code refactoring

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers
- Focus on collaboration

## Getting Help

- Open an issue for questions
- Join the [Discord community](https://discord.com/invite/5rAsykttcs)
- Check existing issues and PRs

## License

By contributing, you agree that your contributions will be licensed under the same license as this project (MIT License).

## Recognition

Contributors will be acknowledged in the README and documentation.

Thank you for contributing! 🎉
