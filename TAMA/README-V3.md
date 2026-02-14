# Medical Language Learning Game - Version 3

## What's New in V3? 🎮

### 1. Bigger Character (48x48 pixels)
- **Was**: 32x32 pixels
- **Now**: 48x48 pixels - 50% larger!
- More visible and easier to see on screen
- Better presence in the game world

### 2. Logical Object Placement 🏥
Objects are now placed exactly where you'd find them in real life!

**Kitchen:**
- **Left Wall**: Refrigerator (top), Pantry (bottom)
- **Back Wall**: Cabinets, Sink, Dishwasher (in logical counter order)
- **Right Wall**: Stove, Microwave, Counter (cooking area)
- **Center**: Dining table with chairs around it
- **Corner**: Trash bin

**Patient Room:**
- **Center**: Hospital bed (main focus)
- **Beside Bed**: IV stand, bedside table (where they should be)
- **Left Wall**: Medical equipment (monitor, blood pressure, medicine cabinet)
- **Back Wall**: Medical sink and call button
- **Front Area**: Visitor chair and overbed table
- **Corner**: Oxygen tank and medical waste bin

### 3. Wandering NPCs with Symptoms 🤒
**4 patients that wander around the patient room!**

Each NPC has their own complaint:
1. **Dizzy Patient** 🔵 (Blue) - "I feel so dizzy and lightheaded..."
2. **Nauseous Patient** 🔴 (Red) - "I feel very nauseous and my stomach is upset..."
3. **Headache Patient** 🟢 (Green) - "I have a terrible headache that won't go away..."
4. **Fever Patient** 🟠 (Orange) - "I'm burning up with fever and feel so weak..."

**NPC Features:**
- Wander randomly around the patient room every 2 seconds
- Avoid colliding with objects and each other
- Highlight in RED when you hover over them
- Click them to hear their symptoms in your chosen languages!
- Speak their complaints with text-to-speech

**Additional Symptoms Available:**
- Coughing Patient
- Tired Patient
- Anxious Patient
- Sore Throat Patient

### 4. Special NPC Popup Design
When you click a patient, you get a special popup:
- **Patient name** in both languages
- **Red symptom box** highlighting their complaint
- **Audio button** to hear them describe their symptoms
- Clean, empathetic design

## Files Included 📁

```
├── educational-room-game-v3.html    (Updated game)
├── npc_patient1.png                 (Blue patient - dizzy)
├── npc_patient2.png                 (Red patient - nauseous)
├── npc_patient3.png                 (Green patient - headache)
├── npc_patient4.png                 (Orange patient - fever)
├── room_kitchen.png                 (Kitchen background)
├── room_patient.png                 (Patient room background)
└── images/                          (All object images)
```

## How NPCs Work 🤖

### Movement System
- NPCs move randomly every 2 seconds
- They move 2 grid squares at a time in random directions
- They avoid:
  - Room boundaries
  - Game objects (beds, tables, etc.)
  - Other NPCs (won't walk through each other)
  - Your character

### Interaction
- **Hover**: NPCs glow RED when you move your mouse over them
- **Click**: Opens a popup with their symptoms
- **Listen**: Click the audio button to hear them speak in your selected languages

### Adding More NPCs
Want more patients? Edit the code:

1. Find the `initNPCs()` function (around line 715)
2. Change `npcCount` to add more NPCs
3. More complaints are already defined in `npcComplaints` array

Example:
```javascript
const npcCount = 6; // Instead of 4 - adds 2 more patients!
```

## Customization Guide 🛠️

### Change NPC Sprites
Replace the PNG files:
- `npc_patient1.png` - Blue patient
- `npc_patient2.png` - Red patient
- `npc_patient3.png` - Green patient
- `npc_patient4.png` - Orange patient

Recommended size: 48x48 pixels

### Add New Complaints
Edit the `npcComplaints` array (around line 600):

```javascript
{
  english: { 
    name: "Your Patient Name", 
    complaint: "Your symptom description here..." 
  },
  finnish: { 
    name: "Potilaan nimi", 
    complaint: "Oireen kuvaus..." 
  },
  tagalog: { 
    name: "Pangalan ng Pasyente", 
    complaint: "Paglalarawan ng sintomas..." 
  }
}
```

### Adjust NPC Speed
Find this line (around line 765):
```javascript
setInterval(updateNPCs, 2000); // 2000 = 2 seconds
```

Change to:
- `1000` = Faster (move every 1 second)
- `3000` = Slower (move every 3 seconds)

### Change NPC Movement Distance
Find this section in `updateNPCs()` (around line 775):
```javascript
case 0: newY -= 2; break; // Change 2 to different number
```

## Educational Benefits 📚

### For Healthcare Workers:
- Learn medical vocabulary in multiple languages
- Practice patient communication scenarios
- Familiarize with medical equipment names
- Understand common patient complaints

### For Language Learners:
- Context-based vocabulary learning
- Real-world medical scenarios
- Audio pronunciation practice
- Interactive, engaging format

## Tips for Best Experience 💡

1. **Start in Kitchen** - Learn basic vocabulary first
2. **Switch to Patient Room** - Interact with NPCs
3. **Click Everything** - Objects AND patients
4. **Use Audio** - Practice pronunciation
5. **Watch NPCs Move** - They'll come to different areas

## What's Different from V2?

| Feature | V2 | V3 |
|---------|----|----|
| Character Size | 32x32 | **48x48** |
| Object Placement | Random | **Logical/Realistic** |
| NPCs | None | **4 wandering patients** |
| NPC Symptoms | N/A | **8 different complaints** |
| NPC Popup | N/A | **Special red design** |
| Interactivity | Objects only | **Objects + NPCs** |

## Technical Notes 🔧

- NPCs only appear in **Patient Room**
- NPCs avoid all collisions (objects, walls, each other)
- Character is now 50% larger (better visibility)
- All object positions follow real-world logic
- Shadow effects added to NPCs for depth

Enjoy your enhanced medical learning experience with wandering patients! 🏥✨
