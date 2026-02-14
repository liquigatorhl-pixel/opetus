# Vocabulary Data Reference

This file contains all the medical vocabulary data that needs to be added to objects in GDevelop.

## How to Use This Data in GDevelop

For each InteractiveObject instance in your scenes:
1. Set the object's variables to match the data below
2. Use the ObjectID to identify which vocabulary to display
3. The variables are already defined in the object template

## Kitchen Objects

### Refrigerator
- **ObjectID**: refrigerator
- **English**
  - Name: Refrigerator
  - Description: A large appliance used to keep food and drinks cold and fresh.
  - Example: Please store the medications in the refrigerator at 4°C.
- **Finnish**
  - Name: Jääkaappi
  - Description: Suuri laite, jota käytetään ruoan ja juomien pitämiseen kylmänä ja tuoreena.
  - Example: Säilytä lääkkeet jääkaapissa 4°C lämpötilassa.
- **Tagalog**
  - Name: Refrigerator
  - Description: Isang malaking aparato na ginagamit upang panatilihing malamig at sariwa ang pagkain at inumin.
  - Example: Pakilagay ang mga gamot sa refrigerator sa 4°C.

### Stove
- **ObjectID**: stove
- **English**
  - Name: Stove
  - Description: A cooking appliance with burners or heating elements used to cook food.
  - Example: Heat the soup on the stove until it reaches serving temperature.
- **Finnish**
  - Name: Liesi
  - Description: Keittolaite, jossa on polttimia tai lämmityselementtejä ruoan valmistamiseen.
  - Example: Lämmitä keitto liedellä, kunnes se saavuttaa tarjoilulämpötilan.
- **Tagalog**
  - Name: Kalan
  - Description: Isang aparato sa pagluluto na may mga burner o heating elements na ginagamit sa pagluluto ng pagkain.
  - Example: Initin ang sopas sa kalan hanggang umabot sa temperatura ng paghahain.

### Sink
- **ObjectID**: sink
- **English**
  - Name: Sink
  - Description: A basin with running water used for washing hands, dishes, and food preparation.
  - Example: Always wash your hands at the sink before handling food.
- **Finnish**
  - Name: Pesuallas
  - Description: Allas juoksevalla vedellä käsien pesemiseen, astioiden ja ruoan valmistukseen.
  - Example: Pese aina kätesi pesualtaassa ennen ruoan käsittelyä.
- **Tagalog**
  - Name: Lababo
  - Description: Isang palanggana na may tumatakbong tubig na ginagamit sa paghuhugas ng kamay, pinggan, at paghahanda ng pagkain.
  - Example: Laging hugasan ang iyong mga kamay sa lababo bago humawak ng pagkain.

## Patient Room Objects

### Hospital Bed
- **ObjectID**: bed
- **HasDetailView**: true
- **English**
  - Name: Hospital Bed
  - Description: An adjustable bed designed for patients to rest and receive medical care.
  - Example: Please help the patient get into the hospital bed carefully.
- **Finnish**
  - Name: Sairaalasänky
  - Description: Säädettävä sänky, joka on suunniteltu potilaiden lepäämiseen ja hoitoon.
  - Example: Auta potilasta nousemaan sairaalasänkyyn varovasti.
- **Tagalog**
  - Name: Hospital Bed
  - Description: Isang adjustable bed na dinisenyo para sa mga pasyente upang magpahinga at makatanggap ng medikal na pag-aalaga.
  - Example: Pakitulungan ang pasyente na makarating sa hospital bed nang maingat.

### IV Stand
- **ObjectID**: iv_stand
- **English**
  - Name: IV Stand
  - Description: A pole with wheels used to hold intravenous fluid bags for patient treatment.
  - Example: Hang the IV bag on the IV stand at the correct height.
- **Finnish**
  - Name: Tiputusteline
  - Description: Pyörillä varustettu tanko, johon kiinnitetään suonensisäiset nestepussit potilaan hoitoa varten.
  - Example: Ripusta tiputuspussi tipustelineeseen oikealle korkeudelle.
- **Tagalog**
  - Name: IV Stand
  - Description: Isang poste na may gulong na ginagamit upang ilagay ang mga intravenous fluid bags para sa paggamot ng pasyente.
  - Example: Isabit ang IV bag sa IV stand sa tamang taas.

### Vital Signs Monitor
- **ObjectID**: monitor
- **English**
  - Name: Vital Signs Monitor
  - Description: A medical device that displays a patient's heart rate, blood pressure, and other vital signs.
  - Example: Check the vital signs monitor every hour to track the patient's condition.
- **Finnish**
  - Name: Elintoimintojen monitori
  - Description: Lääketieteellinen laite, joka näyttää potilaan sykkeen, verenpaineen ja muut elintärkeät mittaukset.
  - Example: Tarkista elintoimintojen monitori tunnin välein potilaan tilan seuraamiseksi.
- **Tagalog**
  - Name: Monitor ng Vital Signs
  - Description: Isang medikal na aparato na nagpapakita ng heart rate, blood pressure, at iba pang vital signs ng pasyente.
  - Example: Suriin ang monitor ng vital signs bawat oras upang subaybayan ang kondisyon ng pasyente.

## Bed Components (BedComponents Scene)

### Mattress
- **ObjectID**: mattress
- **English**
  - Name: Mattress
  - Description: The cushioned part of a bed that provides comfort and support for sleeping.
  - Example: The hospital mattress is designed to prevent pressure sores.
- **Finnish**
  - Name: Patja
  - Description: Sängyn pehmustettu osa, joka tarjoaa mukavuutta ja tukea nukkumiseen.
  - Example: Sairaalan patja on suunniteltu estämään painehaavoja.
- **Tagalog**
  - Name: Mattress
  - Description: Ang malambot na bahagi ng kama na nagbibigay ng kaginhawahan at suporta sa pagtulog.
  - Example: Ang hospital mattress ay dinisenyo upang maiwasan ang pressure sores.

### Pillow
- **ObjectID**: pillow
- **English**
  - Name: Pillow
  - Description: A soft cushion for supporting the head while sleeping or resting.
  - Example: Adjust the pillow to support the patient's head and neck properly.
- **Finnish**
  - Name: Tyyny
  - Description: Pehmeä tyyny pään tukemiseen nukkuessa tai levätessä.
  - Example: Säädä tyyny tukemaan potilaan päätä ja niskaa oikein.
- **Tagalog**
  - Name: Unan
  - Description: Isang malambot na kutson para suportahan ang ulo habang natutulog o nagpapahinga.
  - Example: I-adjust ang unan upang suportahan nang maayos ang ulo at leeg ng pasyente.

### Blanket
- **ObjectID**: blanket
- **English**
  - Name: Blanket
  - Description: A large piece of warm fabric used to keep patients comfortable and warm.
  - Example: Provide an extra blanket if the patient feels cold.
- **Finnish**
  - Name: Peite
  - Description: Suuri lämmin kangaspala, jota käytetään potilaiden pitämiseen mukavana ja lämpimänä.
  - Example: Tarjoa ylimääräinen peite, jos potilas tuntee olonsa kylmäksi.
- **Tagalog**
  - Name: Kumot
  - Description: Isang malaking piraso ng mainit na tela na ginagamit upang panatilihing komportable at mainit ang mga pasyente.
  - Example: Magbigay ng dagdag na kumot kung nag-iinaw ang pasyente.

## NPC Patient Complaints

### Patient 1: Dizzy Patient
- **NPCID**: npc_1
- **English**
  - Name: Dizzy Patient
  - Complaint: I feel so dizzy and lightheaded. The room is spinning and I can't stand up without feeling like I might fall.
- **Finnish**
  - Name: Huimaava potilas
  - Complaint: Minulla on niin huimaa ja kevyttä päässä. Huone pyörii enkä voi nousta seisomaan tuntematta, että saatan kaatua.
- **Tagalog**
  - Name: Nahihilo na Pasyente
  - Complaint: Nahihilo ako at parang lulutang. Umiikot ang silid at hindi ako makatayo nang hindi pakiramdam na baka mahulog.

### Patient 2: Nauseous Patient
- **NPCID**: npc_2
- **English**
  - Name: Nauseous Patient
  - Complaint: I feel very nauseous and my stomach is upset. I've been feeling sick all morning and can't eat anything.
- **Finnish**
  - Name: Pahoinvoiva potilas
  - Complaint: Minua oksettaa kovasti ja vatsa on kipeä. Olen tuntenut oloni sairaaksi koko aamun enkä voi syödä mitään.
- **Tagalog**
  - Name: Nasusukaang Pasyente
  - Complaint: Nasusuka ako at masakit ang tiyan ko. Masama ang pakiramdam ko buong umaga at hindi ako makakain ng anuman.

### Patient 3: Headache Patient
- **NPCID**: npc_3
- **English**
  - Name: Headache Patient
  - Complaint: I have a terrible headache that won't go away. It's throbbing and the light makes it worse.
- **Finnish**
  - Name: Päänsärkypotilas
  - Complaint: Minulla on hirveä päänsärky, joka ei häviä. Se jomottaa ja valo tekee siitä pahemman.
- **Tagalog**
  - Name: May Sakit ng Ulo
  - Complaint: Masakit na masakit ang ulo ko at hindi nawawala. Tumitibok ito at lalong lumala sa liwanag.

### Patient 4: Fever Patient
- **NPCID**: npc_4
- **English**
  - Name: Fever Patient
  - Complaint: I'm burning up with fever and feel so weak. I'm sweating a lot and everything aches.
- **Finnish**
  - Name: Kuumepotilas
  - Complaint: Minulla on kova kuume ja tunnen itseni niin heikoksi. Hikoilen paljon ja kaikki särkee.
- **Tagalog**
  - Name: May Lagnat
  - Complaint: Mainit ako sa lagnat at napakahina ko. Marami akong pawis at masakit ang lahat.

## Implementation Notes

### In GDevelop Event Editor:

1. **For Objects**: When an object is clicked, read its variables and display them in the popup
```
Event: Mouse clicked on InteractiveObject
Action: 
  - If SelectedLanguage1 = "english": Display object.NameEnglish
  - If SelectedLanguage1 = "finnish": Display object.NameFinnish
  - If SelectedLanguage1 = "tagalog": Display object.NameTagalog
```

2. **For NPCs**: Similar approach for patient complaints
```
Event: Mouse clicked on NPC
Action:
  - If SelectedLanguage1 = "english": Display NPC.PatientNameEnglish + NPC.ComplaintEnglish
```

3. **Text-to-Speech**: Use JavaScript code events
```javascript
var utterance = new SpeechSynthesisUtterance(textToSpeak);
utterance.lang = languageCode; // 'en-US', 'fi-FI', 'fil-PH'
window.speechSynthesis.speak(utterance);
```

### Object Positioning Grid (20x20):
- Kitchen objects: See original HTML gridX/gridY values
- Patient room objects: Use diamond walkable area pattern
- Bed components: Arranged horizontally for showcase

### Language Codes for TTS:
- English: 'en-US'
- Finnish: 'fi-FI'
- Tagalog: 'fil-PH'
