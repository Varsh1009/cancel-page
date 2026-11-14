# GainTrain Fitness: The Cancel Screen (Boss Fight)

Keytos Hack · Mini-challenge 01 · *Worst Cancel Screen Ever*

Try cancelling your membership at **GainTrain Fitness**, a made-up gym with the most user-hostile cancellation flow I could design. Gyms are famous for being impossible to quit, so this one leans in. Every screen breaks a real usability rule on purpose. It is hostile, not broken: a determined member can always cancel.

**Play:** open `index.html` in a browser (keep `devil.gif` next to it). No build, no dependencies. Press **J** to turn off the session-timeout reset (for judges).

## The boss fight
It opens with a boss-encounter title screen: *"Level 99 Membership Retention Coach. Nobody has ever cancelled. PRESS START."* The cancel screen has an HP bar, and each screen you survive knocks one bar off.

1. **Lights off + confirmshaming.** The gym is pitch black except for a flashlight around your cursor. Only the guilt text ("You came 3 times. We believed in you anyway.") and the glowing KEEP button are lit; the exit, the pre-ticked "3 years of Platinum Plus personal training" box (it re-ticks itself) and the fake countdown are hidden in the dark. The headline rewrites itself every time you go for the exit, and KEEP grows.
2. **Retention offers.** Every cancellation reason leads to an offer ("I'm moving to another city": your membership works at both of our locations, both in this city). You must decline three.
3. **Cookie-banner preferences.** Seven toggles worded as double negatives ("Freeze instead of cancel", "Auto-renew me every January 1st"), with ON shown grey and OFF shown green.
4. **Certainty slider.** You must be exactly 100% sure. Dragging past 95% bounces you back down; arrow keys work.
5. **Cancel in person.** "Cancellations must be done in person, with two forms of ID and a doctor's note." The front desk is open Tuesdays, 3:00–3:02 AM. The small "send a certified letter" link is the way forward.
6. **Brenda, Membership Advisor.** A chatbot that hears every "cancel" as "upgrade" ("Did you mean: can-CARDIO?").
7. **Typed confirmation.** "I am giving up on my fitness goals", with paste blocked and autocorrect changing *goals* to *goats*.
8. **Runaway button.** Cancel dodges the cursor 12 times, then needs a protein bar.
9. **The treadmill maze.** Walk into the squat rack and you're offered a personal trainer and sent back to the start.
10. **Coach Chad.** High-five him goodbye 10 times while he cries into his towel.
11. **Fake loading.** "Emptying your locker… Asking the regional manager…"
12. **Victory (sort of).** You're cancelled, with a scorecard of time spent, clicks, offers declined and squat racks bumped. The fine print says it takes effect in 30 days or after your next annual maintenance fee, whichever is later, and Coach Chad walks off-screen with his gym bag.

## Always-on hostility
- Anything that leads toward cancelling summons a laughing devil (an animated GIF, `devil.gif`) in flames, a red flash, a low "dun-dun" sound and a whispered guilt line ("Your quads felt that."), and Coach Chad shouts "COACH SAW THAT".
- Coach Chad's eyes follow your cursor on every screen, and he texts you phone-style notifications ("who's gonna spot me now").
- A whispering voice reads the guilt lines aloud (there's a SOUND toggle).
- A red heartbeat vignette grows stronger the closer you get to leaving, the window tilts more on every screen, headlines glitch, and pop-up ads have a close button that dodges.
- 25 seconds of no input: "Session expired for your security", and you're back at screen 1.

## Usability rules broken on purpose
Fitts's law, Hick's law, Jakob's law, Nielsen's heuristics (consistency, visibility of system status, user control, error prevention, recognition over recall), Norman's signifiers, Gestalt proximity, the Doherty threshold, the peak-end rule, sunk cost, and WCAG contrast.

`tools/make_devil_gif.py` regenerates the devil GIF with Pillow.

*GainTrain Fitness is fictional. No real accounts, payments, personal data or coaches.*
