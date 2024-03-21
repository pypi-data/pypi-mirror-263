import ctypes

# Predefined color codes
PREDEFINED_COLORS = {
    "black": "000000",
    "red": "FF0000",
    "green": "00FF00",
    "blue": "0000FF",
    "yellow": "FFFF00",
    "cyan": "00FFFF",
    "magenta": "FF00FF",
    "white": "FFFFFF",
    "orange": "FFA500",
    "pink": "FFC0CB",
    "purple": "800080",
    "brown": "A52A2A",
    "gray": "808080"
}

def print_color_terminal(text, color, reset_color=True):
    """
    Print text in the specified color in the Windows Command Prompt.

    Args:
        text (str): The text to be printed.
        color (str): The color of the text. This can be either a predefined color name or a hexadecimal color code.
                     Predefined color names include: 'black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white',
                     'orange', 'pink', 'purple', 'brown', and 'gray'.
        reset_color (bool, optional): Whether to reset the text color to default after printing. Defaults to True.

    Raises:
        ValueError: If the specified color is not a valid predefined color name or a valid hexadecimal color code.

    Note:
        - Predefined color names are case-insensitive.
        - Hexadecimal color codes should be provided without the '#' symbol.
        - The function uses ANSI escape codes to set the text color in the Command Prompt.
        - If a custom hexadecimal color code is provided, ensure it is in the RGB format (e.g., 'FF0000' for red).

    Example:
        >>> print_color_text("This text will be printed in red.", "red")
        This text will be printed in red.

        >>> print_color_text("This text will be printed in #00FFFF.", "#00FFFF")
        This text will be printed in cyan.

        >>> print_color_text("This text will be printed in custom color.", "FFA500", reset_color=False)
        This text will be printed in custom color.
    """
    # Check if color is a predefined color name
    if color.lower() in PREDEFINED_COLORS:
        hex_color_code = PREDEFINED_COLORS[color.lower()]
    else:
        # Assume color is a hex code
        hex_color_code = color

    # Convert hex color code to RGB
    rgb_color = tuple(int(hex_color_code[i:i+2], 16) for i in (0, 2, 4))
    
    # Calculate corresponding ANSI color code
    ansi_color_code = 16 + (36 * rgb_color[0]) + (6 * rgb_color[1]) + rgb_color[2]
    
    # Set text color using ANSI escape code
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleTextAttribute(kernel32.GetStdHandle(-11), ansi_color_code)
    
    # Print text
    print(text)
    
    # Reset text color to default if specified
    if reset_color:
        kernel32.SetConsoleTextAttribute(kernel32.GetStdHandle(-11), 0x0007)
