# Medical Language Learning Game - Version 2

## What's New in V2? 🎨

### 1. Room Background Images (No More Repeating Tiles!)
- **Kitchen Room**: `room_kitchen.png` - Full room background image
- **Patient Room**: `room_patient.png` - Full room background image
- Objects are now placed ON TOP of the room backgrounds
- Much easier to customize - just swap the PNG files!

### 2. Ultra-Minimalistic Popups
- **Clean white background** instead of dark theme
- **Simple typography** with better readability
- **Removed unnecessary styling** - pure content focus
- **Subtle borders** between language sections
- **Minimal close button** that doesn't distract
- **Clean audio buttons** with simple hover states

### 3. Easier Customization

## How to Customize 🛠️

### Change Room Backgrounds (Easy!)

**Kitchen Room:**
1. Create or find your kitchen room image (640x480 pixels recommended)
2. Replace `room_kitchen.png` with your image
3. Keep the same filename OR update line 636 in HTML:
   ```javascript
   room_kitchen: 'YOUR-KITCHEN-IMAGE.png',
   ```

**Patient Room:**
1. Create or find your patient room image (640x480 pixels recommended)
2. Replace `room_patient.png` with your image
3. Keep the same filename OR update line 637 in HTML:
   ```javascript
   room_patient: 'YOUR-PATIENT-ROOM-IMAGE.png',
   ```

### Change Main Background
Replace `background.png` (see line 27 in CSS)

### Customize Popup Colors
The popup is now ultra-minimal with a white background. To customize:

**Background Color** (line 158):
```css
background: rgba(255, 255, 255, 0.98);
```

**Text Color** (line 189):
```css
color: #1a1a1a;
```

**Button Color** (line 233):
```css
background: #1a1a1a;
```

## File Structure 📁

```
├── educational-room-game-v2.html    (Updated game with room backgrounds)
├── background.png                   (Main app background)
├── room_kitchen.png                 (🏠 Kitchen room background - SWAP THIS!)
├── room_patient.png                 (🏥 Patient room background - SWAP THIS!)
└── images/                          (All game object images)
    ├── refrigerator.png
    ├── bed.png
    ├── mario_idle_right.png
    └── ... (all other objects)
```

## Key Improvements Over V1

### Room Backgrounds
✅ Single image per room instead of repeating tiles
✅ Easier to customize - just replace the PNG
✅ Better visual consistency
✅ Can use detailed room artwork or photos

### Popup Design
✅ White background for better readability
✅ Removed all unnecessary styling
✅ Clean, professional appearance
✅ Better contrast with dark game UI
✅ Minimal borders and spacing
✅ Simple, unobtrusive close button

### Code Organization
✅ Clear comments showing where to swap room images
✅ Simplified rendering code
✅ Better separation of concerns
✅ Easier to understand and modify

## Tips for Creating Room Backgrounds 💡

**Recommended Specifications:**
- **Size**: 640x480 pixels (matches canvas size)
- **Format**: PNG with transparency support
- **Style**: Match your objects' art style
- **Lighting**: Consider where objects will be placed

**Design Tips:**
- Keep backgrounds subtle so objects stand out
- Use appropriate colors (warm for kitchen, clean for patient room)
- Add texture but avoid busy patterns
- Consider perspective and depth
- Leave clear areas for object placement

**Quick Creation Methods:**
1. **Photo + Editing**: Take a real room photo and simplify it
2. **Digital Art**: Draw/paint a room scene
3. **3D Render**: Create and render a 3D room
4. **AI Generation**: Use AI tools to generate room backgrounds
5. **Illustration**: Hand-draw a stylized room

## What to Swap

| File | Purpose | When to Change |
|------|---------|----------------|
| `background.png` | Main app background | Want different app theme |
| `room_kitchen.png` | Kitchen game area | Want custom kitchen design |
| `room_patient.png` | Patient room game area | Want custom patient room design |
| `images/*.png` | Game objects | Want different object graphics |

## Popup Customization Guide

The popup is now **ultra-minimalistic**. Here's what each part does:

### Header (line 189-196)
- Simple title with minimal styling
- Left-aligned for cleaner look
- No emojis or distracting elements

### Language Sections (line 199-206)
- Separated by subtle borders
- No background colors or boxes
- Maximum focus on content

### Text Elements
- **Language Label**: Small, uppercase, gray
- **Name**: Large, bold, black
- **Description**: Medium, gray
- **Example**: Italic, lighter gray

### Audio Button (line 233-245)
- Simple black button
- Minimal hover effect
- Changes to blue when playing

## How to Use

1. Open `educational-room-game-v2.html` in a browser
2. Select 2 languages
3. Move with WASD or Arrow Keys
4. Click objects to see their information in clean, minimal popups
5. Enjoy your custom room backgrounds!

## Need Help?

Look for these markers in the code:
- `🎨` = Customization point
- `🏠` = Room background related
- Section headers with `====` = Major code sections

Enjoy your improved game with room backgrounds and minimal popups! 🎮
