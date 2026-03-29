import sys
import os
import subprocess
from collections import Counter

# Ensure pillow is installed
try:
    from PIL import Image
    import colorsys
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image
    import colorsys

dir_path = './public/'
files = [f for f in os.listdir(dir_path) if f.endswith('.png')]

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def get_dominant_colors(image_path, num_colors=3):
    image = Image.open(image_path)
    image = image.resize((100, 100))
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    pixels = list(image.getdata())
    
    # Quantize to 6 bits per channel to find broad dominant themes
    quantized = [ (r//10*10, g//10*10, b//10*10) for r,g,b in pixels ]
    counts = Counter(quantized)
    
    most_common = counts.most_common(num_colors)
    return [rgb_to_hex(color[0]) for color in most_common]

for f in files:
    full_path = os.path.join(dir_path, f)
    try:
        colors = get_dominant_colors(full_path, 5)
        
        # Calculate approximate perceived lightness to categorize if image is dark or light primarily
        # Simplistic approach based on first dominant color
        r, g, b = Image.open(full_path).resize((1,1)).convert('RGB').getpixel((0,0))
        luminance = (0.299*r + 0.587*g + 0.114*b)
        category = "LIGHT" if luminance > 128 else "DARK"
        
        print(f'{f} ({category}): {colors}')
    except Exception as e:
        pass
