import math
from typing import Union

class UnitConverter:
    """Converter for various units and mathematical operations"""
    
    # Conversion factors to base units
    LENGTH_CONVERSIONS = {
        'meter': 1.0, 'meters': 1.0, 'm': 1.0,
        'kilometer': 1000.0, 'kilometers': 1000.0, 'km': 1000.0,
        'centimeter': 0.01, 'centimeters': 0.01, 'cm': 0.01,
        'millimeter': 0.001, 'millimeters': 0.001, 'mm': 0.001,
        'mile': 1609.34, 'miles': 1609.34, 'mi': 1609.34,
        'yard': 0.9144, 'yards': 0.9144, 'yd': 0.9144,
        'foot': 0.3048, 'feet': 0.3048, 'ft': 0.3048,
        'inch': 0.0254, 'inches': 0.0254, 'in': 0.0254,
    }
    
    WEIGHT_CONVERSIONS = {
        'kilogram': 1.0, 'kilograms': 1.0, 'kg': 1.0,
        'gram': 0.001, 'grams': 0.001, 'g': 0.001,
        'milligram': 0.000001, 'milligrams': 0.000001, 'mg': 0.000001,
        'pound': 0.453592, 'pounds': 0.453592, 'lb': 0.453592, 'lbs': 0.453592,
        'ounce': 0.0283495, 'ounces': 0.0283495, 'oz': 0.0283495,
        'ton': 1000.0, 'tons': 1000.0, 't': 1000.0,
    }
    
    TEMPERATURE_UNITS = ['celsius', 'fahrenheit', 'kelvin', 'c', 'f', 'k']
    
    VOLUME_CONVERSIONS = {
        'liter': 1.0, 'liters': 1.0, 'l': 1.0,
        'milliliter': 0.001, 'milliliters': 0.001, 'ml': 0.001,
        'gallon': 3.78541, 'gallons': 3.78541, 'gal': 3.78541,
        'quart': 0.946353, 'quarts': 0.946353, 'qt': 0.946353,
        'pint': 0.473176, 'pints': 0.473176, 'pt': 0.473176,
        'cup': 0.236588, 'cups': 0.236588,
        'fluid_ounce': 0.0295735, 'fluid_ounces': 0.0295735, 'fl_oz': 0.0295735,
    }
    
    TIME_CONVERSIONS = {
        'second': 1.0, 'seconds': 1.0, 's': 1.0, 'sec': 1.0,
        'minute': 60.0, 'minutes': 60.0, 'min': 60.0,
        'hour': 3600.0, 'hours': 3600.0, 'h': 3600.0, 'hr': 3600.0,
        'day': 86400.0, 'days': 86400.0, 'd': 86400.0,
        'week': 604800.0, 'weeks': 604800.0, 'wk': 604800.0,
    }
    
    @staticmethod
    def convert_length(value: float, from_unit: str, to_unit: str) -> float:
        """Convert between length units"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in UnitConverter.LENGTH_CONVERSIONS:
            raise ValueError(f"Unknown length unit: {from_unit}")
        if to_unit not in UnitConverter.LENGTH_CONVERSIONS:
            raise ValueError(f"Unknown length unit: {to_unit}")
        
        # Convert to base unit (meters) then to target unit
        meters = value * UnitConverter.LENGTH_CONVERSIONS[from_unit]
        result = meters / UnitConverter.LENGTH_CONVERSIONS[to_unit]
        return round(result, 6)
    
    @staticmethod
    def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
        """Convert between weight units"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in UnitConverter.WEIGHT_CONVERSIONS:
            raise ValueError(f"Unknown weight unit: {from_unit}")
        if to_unit not in UnitConverter.WEIGHT_CONVERSIONS:
            raise ValueError(f"Unknown weight unit: {to_unit}")
        
        # Convert to base unit (kilograms) then to target unit
        kg = value * UnitConverter.WEIGHT_CONVERSIONS[from_unit]
        result = kg / UnitConverter.WEIGHT_CONVERSIONS[to_unit]
        return round(result, 6)
    
    @staticmethod
    def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
        """Convert between temperature units"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        # Normalize unit names
        unit_map = {'c': 'celsius', 'f': 'fahrenheit', 'k': 'kelvin'}
        from_unit = unit_map.get(from_unit, from_unit)
        to_unit = unit_map.get(to_unit, to_unit)
        
        if from_unit not in ['celsius', 'fahrenheit', 'kelvin']:
            raise ValueError(f"Unknown temperature unit: {from_unit}")
        if to_unit not in ['celsius', 'fahrenheit', 'kelvin']:
            raise ValueError(f"Unknown temperature unit: {to_unit}")
        
        # Convert to Celsius first
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        else:
            celsius = value
        
        # Convert from Celsius to target unit
        if to_unit == 'fahrenheit':
            result = celsius * 9/5 + 32
        elif to_unit == 'kelvin':
            result = celsius + 273.15
        else:
            result = celsius
        
        return round(result, 2)
    
    @staticmethod
    def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
        """Convert between volume units"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in UnitConverter.VOLUME_CONVERSIONS:
            raise ValueError(f"Unknown volume unit: {from_unit}")
        if to_unit not in UnitConverter.VOLUME_CONVERSIONS:
            raise ValueError(f"Unknown volume unit: {to_unit}")
        
        # Convert to base unit (liters) then to target unit
        liters = value * UnitConverter.VOLUME_CONVERSIONS[from_unit]
        result = liters / UnitConverter.VOLUME_CONVERSIONS[to_unit]
        return round(result, 6)
    
    @staticmethod
    def convert_time(value: float, from_unit: str, to_unit: str) -> float:
        """Convert between time units"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in UnitConverter.TIME_CONVERSIONS:
            raise ValueError(f"Unknown time unit: {from_unit}")
        if to_unit not in UnitConverter.TIME_CONVERSIONS:
            raise ValueError(f"Unknown time unit: {to_unit}")
        
        # Convert to base unit (seconds) then to target unit
        seconds = value * UnitConverter.TIME_CONVERSIONS[from_unit]
        result = seconds / UnitConverter.TIME_CONVERSIONS[to_unit]
        return round(result, 6)
    
    @staticmethod
    def calculate(expression: str) -> Union[float, str]:
        """
        Safely evaluate a mathematical expression
        
        Args:
            expression: Mathematical expression as string
        
        Returns:
            Result of calculation
        """
        # Define safe mathematical functions
        safe_dict = {
            'abs': abs,
            'round': round,
            'min': min,
            'max': max,
            'sum': sum,
            'pow': pow,
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'log10': math.log10,
            'exp': math.exp,
            'pi': math.pi,
            'e': math.e,
            'ceil': math.ceil,
            'floor': math.floor,
        }
        
        try:
            # Remove any potentially dangerous characters/functions
            forbidden = ['__', 'import', 'eval', 'exec', 'open', 'file', 'compile']
            if any(word in expression.lower() for word in forbidden):
                return "❌ Expression contains forbidden operations"
            
            # Evaluate the expression in a restricted namespace
            result = eval(expression, {"__builtins__": {}}, safe_dict)
            return round(result, 10) if isinstance(result, float) else result
        except Exception as e:
            return f"❌ Calculation error: {str(e)}"


def convert_unit(value: float, from_unit: str, to_unit: str, unit_type: str = None) -> str:
    """
    Convert a value from one unit to another
    
    Args:
        value: The value to convert
        from_unit: Source unit
        to_unit: Target unit
        unit_type: Type of unit (length, weight, temperature, volume, time)
                   If None, will try to auto-detect
    
    Returns:
        Formatted conversion result
    """
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    try:
        # Auto-detect unit type if not specified
        if unit_type is None:
            if from_unit_lower in UnitConverter.LENGTH_CONVERSIONS:
                unit_type = 'length'
            elif from_unit_lower in UnitConverter.WEIGHT_CONVERSIONS:
                unit_type = 'weight'
            elif from_unit_lower in UnitConverter.TEMPERATURE_UNITS:
                unit_type = 'temperature'
            elif from_unit_lower in UnitConverter.VOLUME_CONVERSIONS:
                unit_type = 'volume'
            elif from_unit_lower in UnitConverter.TIME_CONVERSIONS:
                unit_type = 'time'
            else:
                return f"❌ Could not detect unit type for '{from_unit}'"
        
        # Perform conversion based on type
        converters = {
            'length': UnitConverter.convert_length,
            'weight': UnitConverter.convert_weight,
            'temperature': UnitConverter.convert_temperature,
            'volume': UnitConverter.convert_volume,
            'time': UnitConverter.convert_time,
        }
        
        if unit_type not in converters:
            return f"❌ Unknown unit type: {unit_type}"
        
        result = converters[unit_type](value, from_unit, to_unit)
        
        icon_map = {
            'length': '📏',
            'weight': '⚖️',
            'temperature': '🌡️',
            'volume': '🧪',
            'time': '⏱️'
        }
        
        icon = icon_map.get(unit_type, '🔄')
        return f"{icon} {value} {from_unit} = {result} {to_unit}"
        
    except ValueError as e:
        return f"❌ {str(e)}"
    except Exception as e:
        return f"❌ Conversion error: {str(e)}"


if __name__ == "__main__":
    print("=== Unit Converter Demo ===\n")
    
    print("1. Length Conversion:")
    print(convert_unit(100, "meters", "feet"))
    
    print("\n2. Weight Conversion:")
    print(convert_unit(150, "pounds", "kg"))
    
    print("\n3. Temperature Conversion:")
    print(convert_unit(100, "celsius", "fahrenheit"))
    
    print("\n4. Volume Conversion:")
    print(convert_unit(5, "gallons", "liters"))
    
    print("\n5. Time Conversion:")
    print(convert_unit(2.5, "hours", "minutes"))
    
    print("\n6. Mathematical Calculation:")
    calc = UnitConverter.calculate("sqrt(144) + pow(2, 3)")
    print(f"🧮 sqrt(144) + pow(2, 3) = {calc}")

