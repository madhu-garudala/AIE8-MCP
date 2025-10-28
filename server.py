from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import os
from dice_roller import DiceRoller
from text_analyzer import TextAnalyzer
from generator_tools import GeneratorTools, generate_multiple
from unit_converter import UnitConverter, convert_unit

load_dotenv()

mcp = FastMCP("mcp-server")
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

@mcp.tool()
def web_search(query: str) -> str:
    """Search the web for information about the given query"""
    search_results = client.get_search_context(query=query)
    return search_results

@mcp.tool()
def roll_dice(notation: str, num_rolls: int = 1) -> str:
    """Roll the dice with the given notation (e.g., '2d20k1' for roll 2 d20 dice and keep highest 1)"""
    roller = DiceRoller(notation, num_rolls)
    return str(roller)

# ============================================
# CUSTOM TOOLS - Text Analysis, Generators, Unit Conversion
# ============================================

@mcp.tool()
def analyze_text(text: str) -> str:
    """
    Analyze text for various metrics including word count, character count, 
    sentiment analysis, readability score, and most common words.
    """
    analyzer = TextAnalyzer(text)
    return str(analyzer)

@mcp.tool()
def generate_uuid(version: int = 4, count: int = 1) -> str:
    """
    Generate UUID(s). Version can be 1 or 4 (default: 4).
    Set count > 1 to generate multiple UUIDs.
    """
    if count == 1:
        return f"🔑 UUID: {GeneratorTools.generate_uuid(version)}"
    return generate_multiple("uuid", count, version=version)

@mcp.tool()
def generate_password(
    length: int = 16,
    count: int = 1,
    include_uppercase: bool = True,
    include_lowercase: bool = True,
    include_digits: bool = True,
    include_symbols: bool = True
) -> str:
    """
    Generate secure password(s). Customize with length and character types.
    Set count > 1 to generate multiple passwords.
    """
    if count == 1:
        pwd = GeneratorTools.generate_password(
            length, include_uppercase, include_lowercase, 
            include_digits, include_symbols
        )
        return f"🔐 Password: {pwd}"
    return generate_multiple(
        "password", count, length=length,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
        include_digits=include_digits,
        include_symbols=include_symbols
    )

@mcp.tool()
def generate_api_key(length: int = 32, count: int = 1) -> str:
    """
    Generate secure API key(s) (alphanumeric only).
    Set count > 1 to generate multiple API keys.
    """
    if count == 1:
        return f"🎫 API Key: {GeneratorTools.generate_api_key(length)}"
    return generate_multiple("api_key", count, length=length)

@mcp.tool()
def generate_token(length: int = 32, count: int = 1) -> str:
    """
    Generate secure hex token(s). Length is in bytes (output will be 2x in hex).
    Set count > 1 to generate multiple tokens.
    """
    if count == 1:
        return f"🎟️ Token: {GeneratorTools.generate_token(length)}"
    return generate_multiple("token", count, length=length)

@mcp.tool()
def generate_pin(length: int = 6, count: int = 1) -> str:
    """
    Generate secure numeric PIN(s).
    Set count > 1 to generate multiple PINs.
    """
    if count == 1:
        return f"🔢 PIN: {GeneratorTools.generate_pin(length)}"
    return generate_multiple("pin", count, length=length)

@mcp.tool()
def hash_text(text: str, algorithm: str = "sha256") -> str:
    """
    Hash a string using specified algorithm (md5, sha1, sha256, sha512).
    """
    result = GeneratorTools.hash_string(text, algorithm)
    return f"#️⃣ {algorithm.upper()} Hash: {result}"

@mcp.tool()
def convert_units(value: float, from_unit: str, to_unit: str, unit_type: str = None) -> str:
    """
    Convert between units. Supports length, weight, temperature, volume, and time.
    Examples: convert_units(100, "meters", "feet"), convert_units(32, "fahrenheit", "celsius")
    Unit type is auto-detected if not specified.
    """
    return convert_unit(value, from_unit, to_unit, unit_type)

@mcp.tool()
def calculate(expression: str) -> str:
    """
    Perform mathematical calculations. Supports basic operations (+, -, *, /, **) 
    and functions like sqrt, sin, cos, tan, log, exp, abs, round, min, max, etc.
    Example: calculate("sqrt(144) + pow(2, 3)") or calculate("sin(pi/2)")
    """
    result = UnitConverter.calculate(expression)
    if isinstance(result, str):
        return result
    return f"🧮 {expression} = {result}"

if __name__ == "__main__":
    mcp.run(transport="stdio")