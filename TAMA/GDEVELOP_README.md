# Medical Language Learning Game - GDevelop 5 Project

## 📋 Project Overview
This is a GDevelop 5 conversion of the HTML5 medical language learning game. The game teaches medical vocabulary in English, Finnish, and Tagalog through interactive gameplay.

## 🎮 Game Features
- **Multiple Rooms**: Kitchen, Patient Room, and Bed Components showcase
- **Interactive Objects**: Click on objects to learn medical vocabulary
- **NPCs**: Patient characters that wander and share symptoms
- **Multi-language Support**: English, Finnish, and Tagalog
- **Text-to-Speech**: Audio pronunciation for vocabulary
- **Character Movement**: WASD or Arrow Keys
- **Walking Animations**: Player and NPC movement animations

## 📦 How to Import into GDevelop 5

### Step 1: Install GDevelop 5
1. Download GDevelop 5 from: https://gdevelop.io/download
2. Install and launch GDevelop 5

### Step 2: Import Project
1. Open GDevelop 5
2. Click "Open a project"
3. Navigate to and select the `game.json` file
4. The project will load with all scenes and objects pre-configured

### Step 3: Add Your Image Assets
Copy all your image files to the project directory:
```
project-folder/
├── game.json
├── room_kitchen.png
├── room_patient.png
├── npc_patient1.png
├── npc_patient2.png
├── npc_patient3.png
├── npc_patient4.png
└── images/
    ├── mario_idle_right.png
    ├── mario_walk1_right.png
    ├── mario_walk2_right.png
    ├── mario_walk3_right.png
    ├── mario_idle_left.png
    ├── mario_walk1_left.png
    ├── mario_walk2_left.png
    ├── mario_walk3_left.png
    ├── mario_idle_up.png
    ├── mario_walk1_up.png
    ├── mario_walk2_up.png
    ├── mario_walk3_up.png
    ├── mario_idle_down.png
    ├── mario_walk1_down.png
    ├── mario_walk2_down.png
    ├── mario_walk3_down.png
    ├── refrigerator.png
    ├── sink.png
    ├── stove.png
    ├── microwave.png
    ├── cabinet.png
    ├── table.png
    ├── chair.png
    ├── bed.png
    ├── monitor.png
    ├── iv_stand.png
    ├── mattress.png
    ├── bedsheet.png
    ├── pillow.png
    ├── pillowcase.png
    ├── blanket.png
    ├── fitted_sheet.png
    ├── bed_pad.png
    ├── bed_rail.png
    ├── headboard.png
    └── footboard.png
```

## 🏗️ Project Structure

### Scenes (Layouts)
1. **LanguageSelection** - Choose 2 languages to learn
2. **Kitchen** - Kitchen room with interactive objects
3. **PatientRoom** - Patient room with NPCs and medical equipment
4. **BedComponents** - Showcase of bed parts

### Game Objects

#### Player
- Type: Sprite
- Behavior: TopDownMovement
- Animations: idle_right, walk_right, idle_left, walk_left, idle_up, walk_up, idle_down, walk_down
- Speed: Adjustable via variable (default: 0.5)

#### InteractiveObject
- Variables for multi-language names, descriptions, and examples
- Each object stores English, Finnish, and Tagalog data
- HasDetailView boolean for special objects (like bed)

#### NPC
- Patient characters with complaints in 3 languages
- Random wandering behavior (needs event implementation)
- Collision detection
- Size: Adjustable via global variable NPCSize (default: 48px)

### Global Variables
- `CurrentRoom` (string) - Tracks which room player is in
- `SelectedLanguage1` (string) - First chosen language
- `SelectedLanguage2` (string) - Second chosen language
- `NPCSize` (number) - NPC sprite size (default: 48)

## 🔧 What's Already Configured

✅ Project structure with 4 scenes
✅ Player object with TopDownMovement behavior
✅ Interactive object template with multi-language variables
✅ NPC object template with patient complaint data
✅ Room backgrounds configured
✅ Grid system (20x20 pixels)
✅ Camera setup
✅ Resource references for all images

## ⚠️ What You Need to Implement

The following features need to be built using GDevelop's event system:

### 1. Language Selection Screen
- [ ] Create clickable language buttons (English, Finnish, Tagalog)
- [ ] Track selected languages in global variables
- [ ] Validate that exactly 2 languages are selected
- [ ] Transition to Kitchen scene when "Start" is clicked

### 2. Player Controls & Animation
- [ ] Add event: When moving right → Play "walk_right" animation
- [ ] Add event: When moving left → Play "walk_left" animation
- [ ] Add event: When moving up → Play "walk_up" animation
- [ ] Add event: When moving down → Play "walk_down" animation
- [ ] Add event: When stopped → Play appropriate "idle" animation

### 3. Object Interaction System
- [ ] Create popup panel (use Panel Sprite or BBText extension)
- [ ] Event: On click on InteractiveObject → Show popup
- [ ] Display object name, description, example in selected languages
- [ ] Add "Listen" buttons for text-to-speech
- [ ] Add close button for popup

### 4. NPC Wandering AI
- [ ] Add PathfindingBehavior to NPCs
- [ ] Create random movement timer
- [ ] Event: Every 0.8 seconds → Pick random direction
- [ ] Move NPC with walking animation
- [ ] Add collision detection with player and objects
- [ ] Implement walkable area boundaries (diamond shape for patient room)

### 5. NPC Interaction
- [ ] Event: On click on NPC → Show complaint popup
- [ ] Display patient name and symptoms in selected languages
- [ ] Add text-to-speech for complaints

### 6. Room Switching
- [ ] Create room navigation buttons (Kitchen, Patient Room)
- [ ] Event: On button click → Change scene
- [ ] Reset player position when changing rooms
- [ ] Load appropriate background for each room

### 7. Bed Detail View
- [ ] Create clickable bed object
- [ ] Add "View Bed Components" button to bed popup
- [ ] Transition to BedComponents scene
- [ ] Display all 10 bed parts as clickable objects

### 8. Text-to-Speech Integration
- [ ] Use JavaScript events to call Web Speech API
- [ ] Create TTS function with language parameter
- [ ] Implement audio playback controls

### 9. Canvas Drawing (for Bed Textures)
If you want to recreate the textured bed components from the HTML version:
- [ ] Use Extension: "Drawing" or "Canvas"
- [ ] Implement texture patterns for each bed component
- [ ] Or create the textures as PNG images instead

## 💡 GDevelop Tips

### Using Extensions
You may need these extensions:
- **BBText** - For better text formatting in popups
- **Panel Sprite** - For popup windows
- **Tween** - For smooth animations
- **Drawing** - For custom textures (optional)

To add extensions:
1. Click "Functions/Behaviors" in the left panel
2. Click "Search for new extensions"
3. Search and install the extensions you need

### Creating the Popup System
1. Create a Panel Sprite object for the background
2. Add BBText objects for displaying text
3. Create Button objects for "Listen" and "Close"
4. Use layers to show/hide the popup (UI layer)
5. Use events to populate text based on clicked object variables

### Implementing Click Detection
```
Conditions:
  - Mouse button released
  - Cursor is on InteractiveObject

Actions:
  - Show popup layer
  - Set popup text to InteractiveObject.Variable(NameEnglish)
```

### NPC Movement Pattern
```
Conditions:
  - Repeat every 0.8 seconds
  - For each NPC

Actions:
  - Add to variable NPC.MoveTimer: 1
  - If MoveTimer >= RandomInRange(1, 3):
    - Set MoveTimer = 0
    - Generate random direction (0-3)
    - Move NPC in that direction
    - Set animation based on direction
```

## 🎨 Customization

### Adjusting NPC Size
Change the global variable `NPCSize` to resize all NPCs:
- Default: 48 pixels
- Recommended range: 32-64 pixels

### Changing Movement Speed
Modify the Player object's TopDownMovement behavior:
- Max Speed: Controls how fast the player moves
- Acceleration/Deceleration: Controls responsiveness

### Grid Size
The game uses a 20x20 pixel grid. To change:
1. Open scene editor
2. Click grid settings
3. Adjust grid width/height
4. Reposition all objects accordingly

## 📚 Additional Resources

- **GDevelop Documentation**: https://wiki.gdevelop.io/
- **GDevelop Forums**: https://forum.gdevelop.io/
- **GDevelop Discord**: https://discord.gg/gdevelop
- **Tutorial Videos**: https://www.youtube.com/c/GDevelopApp

## 🐛 Troubleshooting

### Images not showing
1. Check that image files are in the correct directory
2. Right-click on Resources → Refresh resources
3. Verify image paths in resource manager

### Objects not clickable
1. Ensure object has collision mask enabled
2. Check that object is on a visible layer
3. Verify click events are on the correct object

### Animations not playing
1. Check that all animation frames are loaded
2. Verify animation names match event conditions
3. Ensure time between frames is appropriate (0.08-0.15)

## 📝 Next Steps

1. Import the project into GDevelop 5
2. Add all image assets
3. Start with the language selection screen
4. Build the object interaction system
5. Implement NPC AI
6. Add text-to-speech functionality
7. Test and refine gameplay

## 🤝 Support

If you need help with GDevelop:
- Check the official wiki: https://wiki.gdevelop.io/
- Ask on forums: https://forum.gdevelop.io/
- Join Discord community: https://discord.gg/gdevelop

Good luck with your GDevelop project! 🎮
