#!/usr/bin/env python3
"""
Image Resizer for Medical Language Learning Game
Resizes kitchen background to 1344x768 and NPC sprites to 160x300
"""

from PIL import Image
import os

def resize_kitchen_background(input_path, output_path):
    """
    Resize kitchen room background to 1344x768
    """
    try:
        img = Image.open(input_path)
        print(f"Original kitchen size: {img.size}")
        
        # Resize to 1344x768
        resized = img.resize((1344, 768), Image.Resampling.LANCZOS)
        print(f"Resized kitchen to: {resized.size}")
        
        # Save
        resized.save(output_path, 'PNG', optimize=True)
        print(f"✓ Saved to: {output_path}")
        return True
        
    except FileNotFoundError:
        print(f"✗ Error: File not found: {input_path}")
        return False
    except Exception as e:
        print(f"✗ Error resizing kitchen: {e}")
        return False

def resize_npc_sprite(input_path, output_path):
    """
    Resize NPC sprite to 160x300
    """
    try:
        img = Image.open(input_path)
        print(f"Original NPC size: {img.size}")
        
        # Resize to 160x300
        resized = img.resize((160, 300), Image.Resampling.LANCZOS)
        print(f"Resized NPC to: {resized.size}")
        
        # Save with transparency preserved
        resized.save(output_path, 'PNG', optimize=True)
        print(f"✓ Saved to: {output_path}")
        return True
        
    except FileNotFoundError:
        print(f"✗ Error: File not found: {input_path}")
        return False
    except Exception as e:
        print(f"✗ Error resizing NPC: {e}")
        return False

def main():
    """
    Main function to resize images
    """
    print("=" * 60)
    print("Medical Language Learning Game - Image Resizer")
    print("=" * 60)
    print()
    
    # Define paths (adjust these to match your actual file locations)
    kitchen_input = "room_kitchen.png"
    kitchen_output = "room_kitchen_1344x768.png"
    
    npc_sprites = [
        "npc_patient1.png",
        "npc_patient2.png", 
        "npc_patient3.png",
        "npc_patient4.png"
    ]
    
    # Resize kitchen background
    print("KITCHEN BACKGROUND:")
    print("-" * 60)
    if os.path.exists(kitchen_input):
        resize_kitchen_background(kitchen_input, kitchen_output)
    else:
        print(f"✗ Kitchen background not found: {kitchen_input}")
        print(f"  Please place your kitchen background image here")
    print()
    
    # Resize NPC sprites
    print("NPC SPRITES:")
    print("-" * 60)
    for npc in npc_sprites:
        if os.path.exists(npc):
            output = npc.replace('.png', '_160x300.png')
            resize_npc_sprite(npc, output)
            print()
        else:
            print(f"✗ NPC sprite not found: {npc}")
            print()
    
    print("=" * 60)
    print("DONE!")
    print("=" * 60)
    print()
    print("NEXT STEPS:")
    print("1. Check the resized images in this directory")
    print("2. Replace the original images with the resized ones")
    print("3. Update the game code to use new dimensions")
    print()

if __name__ == "__main__":
    main()
