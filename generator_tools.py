import uuid
import secrets
import string
import hashlib

class GeneratorTools:
    """Tools for generating UUIDs, passwords, and other random secure strings"""
    
    @staticmethod
    def generate_uuid(version: int = 4) -> str:
        """
        Generate a UUID
        
        Args:
            version: UUID version (1 or 4), default is 4
        
        Returns:
            String representation of UUID
        """
        if version == 1:
            return str(uuid.uuid1())
        elif version == 4:
            return str(uuid.uuid4())
        else:
            raise ValueError("Only UUID version 1 and 4 are supported")
    
    @staticmethod
    def generate_password(
        length: int = 16,
        include_uppercase: bool = True,
        include_lowercase: bool = True,
        include_digits: bool = True,
        include_symbols: bool = True
    ) -> str:
        """
        Generate a secure random password
        
        Args:
            length: Length of password (minimum 8)
            include_uppercase: Include uppercase letters
            include_lowercase: Include lowercase letters
            include_digits: Include digits
            include_symbols: Include special symbols
        
        Returns:
            Secure random password
        """
        if length < 8:
            raise ValueError("Password length must be at least 8 characters")
        
        # Build character pool
        characters = ""
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not characters:
            raise ValueError("At least one character type must be selected")
        
        # Generate password ensuring at least one of each selected type
        password = []
        
        if include_uppercase:
            password.append(secrets.choice(string.ascii_uppercase))
        if include_lowercase:
            password.append(secrets.choice(string.ascii_lowercase))
        if include_digits:
            password.append(secrets.choice(string.digits))
        if include_symbols:
            password.append(secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
        
        # Fill the rest randomly
        remaining_length = length - len(password)
        password.extend(secrets.choice(characters) for _ in range(remaining_length))
        
        # Shuffle the password
        shuffled = list(password)
        for i in range(len(shuffled) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        
        return ''.join(shuffled)
    
    @staticmethod
    def generate_api_key(length: int = 32) -> str:
        """
        Generate a secure API key (alphanumeric)
        
        Args:
            length: Length of API key (minimum 16)
        
        Returns:
            Secure random API key
        """
        if length < 16:
            raise ValueError("API key length must be at least 16 characters")
        
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))
    
    @staticmethod
    def generate_token(length: int = 32) -> str:
        """
        Generate a secure hex token
        
        Args:
            length: Length of token in bytes (will be doubled in hex)
        
        Returns:
            Secure random hex token
        """
        return secrets.token_hex(length)
    
    @staticmethod
    def generate_pin(length: int = 6) -> str:
        """
        Generate a secure numeric PIN
        
        Args:
            length: Length of PIN (minimum 4)
        
        Returns:
            Secure random PIN
        """
        if length < 4:
            raise ValueError("PIN length must be at least 4 digits")
        
        return ''.join(secrets.choice(string.digits) for _ in range(length))
    
    @staticmethod
    def hash_string(text: str, algorithm: str = "sha256") -> str:
        """
        Hash a string using specified algorithm
        
        Args:
            text: String to hash
            algorithm: Hash algorithm (md5, sha1, sha256, sha512)
        
        Returns:
            Hexadecimal hash
        """
        algorithms = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha256": hashlib.sha256,
            "sha512": hashlib.sha512
        }
        
        if algorithm not in algorithms:
            raise ValueError(f"Unsupported algorithm. Choose from: {', '.join(algorithms.keys())}")
        
        return algorithms[algorithm](text.encode()).hexdigest()


def generate_multiple(generator_type: str, count: int = 1, **kwargs) -> str:
    """
    Generate multiple items of a specific type
    
    Args:
        generator_type: Type of item to generate (uuid, password, api_key, token, pin)
        count: Number of items to generate
        **kwargs: Additional arguments for the specific generator
    
    Returns:
        Formatted string with generated items
    """
    generators = {
        "uuid": GeneratorTools.generate_uuid,
        "password": GeneratorTools.generate_password,
        "api_key": GeneratorTools.generate_api_key,
        "token": GeneratorTools.generate_token,
        "pin": GeneratorTools.generate_pin
    }
    
    if generator_type not in generators:
        return f"❌ Invalid generator type. Choose from: {', '.join(generators.keys())}"
    
    generator = generators[generator_type]
    results = []
    
    for i in range(count):
        try:
            item = generator(**kwargs)
            results.append(f"{i+1}. {item}")
        except Exception as e:
            results.append(f"{i+1}. Error: {str(e)}")
    
    icon_map = {
        "uuid": "🔑",
        "password": "🔐",
        "api_key": "🎫",
        "token": "🎟️",
        "pin": "🔢"
    }
    
    icon = icon_map.get(generator_type, "🔧")
    header = f"{icon} Generated {count} {generator_type.upper()}(s):"
    
    return header + "\n" + "\n".join(results)


if __name__ == "__main__":
    print("=== Generator Tools Demo ===\n")
    
    print("1. UUID v4:")
    print(GeneratorTools.generate_uuid())
    
    print("\n2. Secure Password (16 chars):")
    print(GeneratorTools.generate_password(length=16))
    
    print("\n3. API Key (32 chars):")
    print(GeneratorTools.generate_api_key(length=32))
    
    print("\n4. Hex Token:")
    print(GeneratorTools.generate_token(length=16))
    
    print("\n5. PIN (6 digits):")
    print(GeneratorTools.generate_pin(length=6))
    
    print("\n6. SHA256 Hash:")
    print(GeneratorTools.hash_string("Hello, World!"))

