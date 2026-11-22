"""English content. Keep the same keys and the same number of paragraphs in
fr.py and ar.py: build.py refuses to build when they differ.

Markup: **bold**, and a paragraph starting with "- " is a list item."""

T = {
    "name": "English",
    "og_locale": "en_US",
    "skip": "Skip to content",
    "nav_home": "Home",
    "nav_faq": "FAQ",
    "nav_contact": "Contact",
    "nav_privacy": "Privacy Policy",
    "nav_privacy_header": "Privacy Policy",
    "nav_main": "Main menu",
    "nav_language": "Language",
    "placeholder_notice": "Support email not set yet: this address is a placeholder.",
    "footer_note": "Support website for the Muslim Prayer app.",

    "home_title": "Muslim Prayer – Support",
    "home_desc": "Support for the Muslim Prayer app: prayer times, Adhan notifications, Qibla, Quran, Adhkar and Hijri calendar. Answers to common questions and how to contact us.",
    "home_h1": "Muslim Prayer",
    "home_kicker": "Help and support",
    "home_lead": "Prayer times for your city, Adhan reminders, the Quran in Arabic, the Qibla direction, Adhkar, Tasbih and the Hijri calendar, in one calm app. Find answers here, or write to us.",
    "home_btn_faq": "Read the FAQ",
    "home_btn_contact": "Contact support",
    "home_shot_alt": "The Muslim Prayer home screen: the next prayer with a countdown, and today's prayer times for London.",
    "features_title": "What is in the app",
    "features": [
        ("Prayer times", "Today's times with a countdown to the next prayer, and a monthly timetable. 10 calculation methods and a manual adjustment for each prayer."),
        ("Adhan notifications", "For each prayer, choose the Adhan, a short sound or silence. Scheduled on your device."),
        ("Qibla", "The direction from your selected city, with a live compass on devices that have one."),
        ("Quran", "The complete Arabic text, readable offline, with search, bookmarks and reading progress."),
        ("Adhkar and Tasbih", "Morning, evening, after-prayer and other Adhkar in Arabic with their references, and a digital counter."),
        ("Hijri calendar and Ramadan", "A monthly Hijri calendar, Suhoor and Iftar times, a Ramadan timetable and a private fasting tracker."),
    ],
    "topics_title": "Find help by topic",
    "note_title": "Good to know about prayer times",
    "note": [
        "Prayer times and Hijri dates are calculated. They depend on the location, calculation method and settings you choose, and they can differ from your local mosque or authority by some minutes, or by a day or two for Hijri dates.",
        "When they differ, follow the source you trust. You can adjust each prayer and the Hijri date in the app.",
    ],
    "version_title": "Version covered by this site",
    "version": "Muslim Prayer 1.0.0 for iPhone (iOS 15 or later). Free, with no account and no ads in this version. The app is available in English, French, Arabic, Spanish, Italian and German.",
    "contact_card_title": "Still need help?",
    "contact_card": "Write to us and tell us what you see on your screen.",
    "privacy_card_title": "Your privacy",
    "privacy_card": "The Privacy Policy explains what the app processes and the choices you have.",
    "privacy_link": "Read the Privacy Policy",
    "privacy_title": "Privacy Policy – Muslim Prayer",
    "privacy_desc": "Privacy Policy of the Muslim Prayer app: what information may be processed, how it is used, and the choices and rights you have.",
    "privacy_h1": "Privacy Policy",
    "privacy_updated": "Last updated:",
    "privacy_translation": "",

    "faq_title": "FAQ – Muslim Prayer",
    "faq_desc": "Answers about prayer times and calculation methods, location and privacy, notifications and Adhan, Qibla compass, Quran, Adhkar and the Hijri calendar in Muslim Prayer.",
    "faq_h1": "Frequently asked questions",
    "faq_lead": "These answers describe version 1.0.0 on iPhone. Menu names are written as they appear in the app.",
    "faq_toc": "Topics",

    "contact_title": "Contact – Muslim Prayer",
    "contact_desc": "Contact the Muslim Prayer support team by email, and see what to include so that we can help you.",
    "contact_h1": "Contact support",
    "contact_lead": "Questions, problems and suggestions are welcome.",
    "contact_email_label": "Support email",
    "contact_button": "Write an email",
    "mail_subject": "Muslim Prayer – support",
    "contact_include_title": "What to include",
    "contact_include": [
        "- Your iPhone model and iOS version (iPhone **Settings › General › About**).",
        "- The app version (iPhone **Settings › General › iPhone Storage › Muslim Prayer**).",
        "- What you did, what you expected and what happened. A screenshot helps.",
        "- For prayer times: the city, date, calculation method, Asr method and adjustments, and the timetable you compare with.",
        "- For the Quran or an Adhkar text: the surah and ayah, or the reference shown by the app.",
    ],
    "contact_avoid_title": "What to leave out",
    "contact_avoid": "Please do not send passwords, payment details, identity documents or your exact address. A city is enough.",
    "contact_first_title": "Before you write",
    "contact_first": "Many questions are answered in the FAQ.",

    "nf_title": "Page not found",
    "nf_text": "This page does not exist or has moved.",
    "nf_link": "Go to the support home page",

    "cats": {
        "prayer-times": "Prayer times and calculation methods",
        "location-privacy": "Location and privacy",
        "notifications": "Notifications and Adhan",
        "qibla": "Qibla compass",
        "quran": "Quran",
        "adhkar": "Adhkar and Tasbih",
        "hijri": "Hijri calendar and Ramadan",
        "general": "The app in general",
    },
    "faq": {
        "how-calculated": ("How are prayer times calculated?", [
            "On your device, from the position of the sun for the date and the location you selected, with the calculation method and Asr method chosen in the app. No connection is needed.",
            "The result is a calculation, not an official announcement. It does not take your elevation into account, and a difference of a minute or two with another timetable is normal.",
        ]),
        "methods": ("Which calculation methods are available, and which should I choose?", [
            "There are 10: Muslim World League, Islamic Society of North America (ISNA), Umm al-Qura, Egyptian General Authority of Survey, University of Islamic Sciences (Karachi), Institute of Geophysics (Tehran), Dubai, Qatar, Kuwait and Singapore (MUIS).",
            "The first time you open the app, it suggests a method for your country. If your mosque or local authority follows another one, change it in **More › Settings › Calculation method**.",
        ]),
        "mosque": ("Why are the times different from my mosque's?", [
            "Mosques may use another method, their own safety margins, or the time of the congregation (iqama) rather than the start of the prayer time. Check these settings first:",
            "- the selected city, in **More › Settings › Location**;",
            "- **Calculation method** and **Asr method**, in **More › Settings**.",
            "If a difference remains, open **More › Settings › Time adjustments**: each prayer can be moved earlier or later by up to 60 minutes.",
        ]),
        "asr": ("What is the difference between Standard and Hanafi Asr?", [
            "**Standard** follows the Shafi'i, Maliki and Hanbali schools. **Hanafi** gives a later Asr. Choose yours in **More › Settings › Asr method**.",
        ]),
        "estimated": ("What does the ≈ sign mean?", [
            "It marks an estimated time. At high latitudes, on some days the sun does not reach the angle used for Fajr or Isha, or does not rise or set at all. The app then follows a rule and marks the time; on the Home screen, tap it for an explanation.",
            "You can change the rule in **More › Settings › High-latitude rule**. Local practice varies: ask your mosque which rule it follows.",
        ]),
        "umm-al-qura-ramadan": ("With Umm al-Qura, why is Isha different in Ramadan?", [
            "The app uses 90 minutes after Maghrib all year. In Ramadan the official Umm al-Qura timetable uses 120 minutes, which version 1.0.0 does not apply automatically. You can add 30 minutes to Isha in **More › Settings › Time adjustments** during Ramadan.",
        ]),
        "travel": ("I travelled, but the times did not change. Why?", [
            "The app does not follow your position in the background. Open **More › Settings › Location** and update your approximate location or choose the new city. Times are always shown in the time zone of the selected city.",
        ]),
        "timetable": ("Can I see and share a whole month?", [
            "Yes. On the Home screen open **Monthly timetable**. From there you can share the month as text or export it as a CSV file, with the city and method but without coordinates.",
        ]),

        "what-location": ("Which location does the app use?", [
            "Your approximate location only, read once when you tap **Use my approximate location**. The app does not request precise GPS or background location. The position is rounded to about 1 km and kept on your device, and the nearest city is found offline.",
            "An approximate position can be several kilometres away. This usually changes prayer times by about a minute at most.",
        ]),
        "without-permission": ("Can I use the app without sharing my location?", [
            "Yes. Choose **Choose a city manually** during setup or in **More › Settings › Location**, and search for your city. The city list is inside the app and works offline.",
        ]),
        "not-found": ("My location could not be found. What can I do?", [
            "- Check that Location Services are on in iPhone **Settings › Privacy & Security › Location Services**, and that Muslim Prayer is set to **While Using the App**.",
            "- Try again in a place with a better signal.",
            "- Or choose your city manually: the app works the same way.",
        ]),
        "what-is-sent": ("What stays on my device, and what is sent?", [
            "Your selected location, prayer settings, bookmarks and reading progress, Adhkar and Tasbih counters and fasting records are stored on your device. The app does not send them to its analytics, crash report or configuration services.",
            "The app uses Google Firebase. Remote Config, which delivers app settings, processes technical information such as an installation identifier, the app and system version, and the device's country, language and time zone. It works independently of the two options below.",
            "**Usage analytics** and **Crash reports** are off until you turn them on in **More › Settings › Privacy**. The Privacy Policy is the reference document.",
        ]),
        "change-delete": ("How do I change my choices or delete my data?", [
            "Turn usage analytics and crash reports on or off at any time in **More › Settings › Privacy**. Saved locations can be removed in **More › Settings › Location**.",
            "Deleting the app removes the data it stored on your iPhone; a backup you made earlier may still contain a copy. For other requests, see the Privacy Policy or write to us.",
        ]),

        "turn-on": ("How do I turn on prayer notifications?", [
            "Open **More › Settings › Notifications** and turn on **Prayer notifications**. iOS asks for permission at that moment. Notifications are off until you do this, and a location must be selected.",
        ]),
        "choose-sound": ("Can I choose a different sound for each prayer?", [
            "Yes. In **More › Settings › Notifications**, each of the five prayers can be turned on or off and set to **Adhan**, **Short sound** or **Silent**. You can listen to a sound before choosing it. Sunrise is never notified, because it is not a prayer.",
        ]),
        "adhan-30s": ("Why does the Adhan stop after about 30 seconds?", [
            "iOS limits notification sounds to 30 seconds, so the notification plays the opening of the Adhan.",
        ]),
        "no-sound": ("I do not receive notifications, or they have no sound.", [
            "- In **More › Settings › Notifications**, check that notifications and the prayer are on, that the sound is not **Silent**, and that no warning is shown.",
            "- In iPhone **Settings › Notifications › Muslim Prayer**, allow notifications, alerts and sounds.",
            "- Check silent mode, the volume and Focus modes: notification sounds follow them, and Focus may hold notifications back.",
            "- Check that a location is selected.",
        ]),
        "stopped": ("Notifications stopped after about a week.", [
            "iOS limits how many notifications an app can schedule in advance, so the app plans up to 7 days, or a little less when reminders are on. Open the app to schedule the next days. A message reminds you before the planned notifications run out.",
        ]),
        "reminders": ("Can I be reminded before a prayer, or for Suhoor and Iftar?", [
            "Yes. **More › Settings › Notifications** has an optional reminder 5 to 60 minutes before each enabled prayer. Suhoor, Iftar and daily Ramadan reminders are in **More › Ramadan › Ramadan settings**. All of them are off until you turn them on.",
        ]),

        "how-to-use": ("How do I find the Qibla?", [
            "Select a location, open the **Qibla** tab, hold your phone flat with the screen up and turn until the app says **You are facing the Qibla**. The direction is calculated from the selected city, so check that it is the place where you are.",
        ]),
        "wrong": ("The direction looks wrong or moves a lot.", [
            "Phone compasses are disturbed by metal, magnets, cars, electronics and magnetic cases. The app shows the compass accuracy; tap **Calibrate** for guidance:",
            "- move the phone in a figure-eight a few times, tilting it in every direction;",
            "- move away from metal and magnets, and remove magnetic cases or mounts;",
            "- hold the phone flat;",
            "- if it still looks wrong, compare with a known landmark or another compass.",
        ]),
        "north": ("Why is the result different from my ordinary compass?", [
            "An ordinary compass points to magnetic north. The Qibla angle is measured from true north. The app corrects the difference (magnetic declination) for your place and date with the World Magnetic Model, and shows the value used.",
        ]),
        "no-compass": ("What if there is no working compass?", [
            "The app shows a fixed diagram with north at the top. It does not follow your phone. Use the angle from true north, or the value given for a magnetic compass when it is available.",
        ]),
        "near-makkah": ("Does the Qibla work close to Makkah?", [
            "Your location is approximate, so the direction may be inaccurate within about 25 km of the Kaaba. The app shows a warning there.",
        ]),

        "text": ("Which Quran text is used?", [
            "The complete Arabic text published by the Tanzil Project (tanzil.net), Uthmani script, shown as published under the Creative Commons Attribution 3.0 licence. The sources are listed in the **Quran** tab, under **Sources**.",
        ]),
        "offline": ("Can I read the Quran offline?", [
            "Yes. The text is included in the app.",
        ]),
        "translation-audio": ("Are there translations or recitations?", [
            "Not in version 1.0.0. The Quran is shown in Arabic only, whatever the language of the app, and there is no audio recitation.",
        ]),
        "find": ("How do I search, bookmark and continue reading?", [
            "Use the search button to find a surah by name or number, or to search the Arabic text (diacritics are optional). Tap an ayah to bookmark it. **Continue reading** brings you back to your last position, and you can change the text size while reading.",
        ]),
        "share": ("Can I share or copy an ayah?", [
            "Yes. Tap the ayah, then **Share** or **Copy**. The reference and the source of the text are included.",
        ]),

        "adhkar-source": ("Where do the Adhkar come from?", [
            "From the Quran and from narrations graded Sahih or Hasan in the sources listed in the app. Each dhikr shows its reference and grading. The app is not certified by a religious authority; for religious questions, ask a scholar you trust.",
        ]),
        "adhkar-language": ("Why are the Adhkar in Arabic only?", [
            "They are shown as narrated, without translation, transliteration or audio. Menus and category names are translated.",
        ]),
        "counting": ("How are repetitions counted?", [
            "The app uses the number stated in the hadith. When the hadith gives no number, the dhikr is counted once and the app says so. Progress is kept per day on your device.",
        ]),
        "tasbih": ("How does the Tasbih counter work?", [
            "Open **Adhkar › Tasbih** and tap the circle to count. You can use a preset or create a counter with your own Arabic text, choose a target or none, and turn vibration or sound on. Counters you create are marked **Added by you**: the app does not verify their text.",
        ]),

        "calendar": ("Which Hijri calendar is used?", [
            "The Umm al-Qura calendar, calculated offline for the years 1420 to 1500 AH (1999 to 2077). Outside these years no Hijri date is shown.",
        ]),
        "differs": ("The Hijri date differs from my country's.", [
            "The start of a month can depend on local moon sighting. In **More › Settings › Time adjustments**, set **Hijri date adjustment** up to two days earlier or later. It applies to the calendar, Ramadan and Eid dates too.",
        ]),
        "maghrib": ("Why does the Hijri date not change at Maghrib?", [
            "The app shows each Hijri date on its civil day, from midnight to midnight at the selected location. In the Islamic reckoning the day begins at Maghrib the evening before.",
        ]),
        "ramadan": ("How are Suhoor, Iftar, Ramadan and Eid shown?", [
            "Suhoor ends at Fajr and Iftar is at Maghrib: the same times as your prayer times, with your method and adjustments, and with no extra offset.",
            "Ramadan and Eid dates are estimates from the calendar. They may differ from the announcement of your local authority, which the app does not determine.",
        ]),
        "fasting": ("Who can see my fasting tracker?", [
            "It is stored on your device. The app does not send it to a server.",
        ]),

        "language": ("How do I change the language or the theme?", [
            "Open **More › Settings**. The app is available in English, French, Arabic, Spanish, Italian and German, in light or dark theme, with 12 or 24-hour time.",
        ]),
        "account-ads": ("Do I need an account? Are there ads?", [
            "There is no account and no sign-up. Version 1.0.0 is free and shows no ads.",
        ]),
        "internet": ("Does the app work without a connection?", [
            "Prayer times, notifications, Qibla, Quran text, Adhkar and the calendar work offline. A connection is used for the Firebase services described above and to open the Privacy Policy.",
        ]),
    },
}
