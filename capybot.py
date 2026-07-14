import smtplib
import random
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =====================================================================
# 1. THE ULTIMATE CAPYBARA FACT DATABASE (205 UNIQUE FACTS)
# =====================================================================
FACTS = [
    # --- Physical Traits & Anatomy (1-40) ---
    "Capybaras are the undisputed world's largest living rodents.",
    "Adult capybaras can grow up to 4.3 feet (130 cm) in length.",
    "They can weigh anywhere between 77 to 150 pounds (35 to 66 kg).",
    "Female capybaras are actually slightly heavier than males on average.",
    "Their scientific name is Hydrochoerus hydrochaeris, which means 'Water Hog.'",
    "They are closely related to guinea pigs and rock cavies.",
    "They are also distantly related to chinchillas and agoutis.",
    "Capybaras have slightly webbed feet, making them incredible swimmers.",
    "They have four toes on their front feet but only three toes on their back feet.",
    "Their vestigial tail is so tiny that they appear completely tailless.",
    "Their eyes, ears, and nostrils are all located on the very top of their heads.",
    "This facial arrangement allows them to breathe and look around while mostly submerged.",
    "Like all rodents, their two front incisors grow continuously throughout their lives.",
    "They constantly wear down their teeth by chewing on tough grasses and bark.",
    "Their fur is coarse, sparse, and dries out incredibly quickly when they leave water.",
    "The color of their long, brittle fur ranges from reddish-brown to dark brown and grey.",
    "They lack a thick undercoat, which makes them susceptible to sunburn.",
    "To protect their sensitive skin from the sun, they wallow in thick mud.",
    "Adult males have a highly prominent, dark, hairless scent gland on their snout called a morrillo.",
    "The word 'morrillo' translates to 'small hill' in Spanish.",
    "The morrillo gland secretes a white, sticky fluid used for marking territory.",
    "While females have a morrillo gland too, it is much smaller and less developed.",
    "They have a second set of scent glands located inside their anuses.",
    "Both males and females use their anal glands to coat nearby plants with scent.",
    "The scent from their glands is unique to each individual capybara.",
    "They have incredibly sharp eyesight, allowing them to spot predators from afar.",
    "Their hearing is highly acute, perfectly tuned to detect rustling in nearby brush.",
    "They have an excellent sense of smell, which they use to identify family members.",
    "Capybaras have a barrel-shaped body that helps them retain core warmth.",
    "Their legs are relatively short compared to the mass of their bodies.",
    "The hind legs of a capybara are slightly longer than their front legs.",
    "Their claws are thick, blunt, and resemble miniature hooves.",
    "They have an unusually large cecum, a digestive pouch used to break down tough plant fiber.",
    "Their digestive system is specially adapted to ferment cellulose.",
    "Because of their facial structure, they look like they are constantly judging you.",
    "Their jaw alignment allows them to chew in a grinding, back-and-forth motion.",
    "A capybara's skull is elongated and remarkably heavy for a rodent.",
    "They possess 20 teeth in total, including their prominent front incisors.",
    "They don't have canine teeth, leaving a large gap called a diastema.",
    "Their skin is packed with sweat glands, which is quite rare for a rodent.",

    # --- Semi-Aquatic Lifestyle (41-80) ---
    "Capybaras are semi-aquatic mammals, meaning they split life between land and water.",
    "They can hold their breath underwater for up to five full minutes.",
    "They often sleep entirely submerged in water with just their nostrils exposed.",
    "They use water to regulate their body temperature during the hottest parts of the day.",
    "They are native to Central and South America, always living near water sources.",
    "You can find them in abundance throughout the Amazon basin.",
    "They happily inhabit swamps, marshes, rivers, lakes, and flooded savannas.",
    "When threatened by a predator, their first instinct is to dive into deep water.",
    "They are incredibly agile swimmers, capable of out-swimming several predators.",
    "They can run surprisingly fast on land, reaching speeds of up to 22 mph (35 km/h).",
    "Their top land speed is comparable to that of a horse over short distances.",
    "In Japan, captive capybaras are famous for relaxing in hot spring baths (onsen).",
    "The tradition of Japanese capybara onsens began entirely by accident in 1982.",
    "A zookeeper at Izu Shaboten Zoo noticed capybaras huddling around a pool of warm water.",
    "During winter, Japanese zoos float yuzu citrus fruits in the capybaras' hot baths.",
    "The yuzu fruits add a pleasant aroma and help soothe the capybaras' dry skin.",
    "Capybaras will happily spend hours soaking in these warm winter baths.",
    "They love water so much that they frequently mate exclusively in the water.",
    "They will even use water as a bathroom to hide their scent from land predators.",
    "They are excellent swimmers and can glide silently just beneath the water's surface.",
    "They are known to navigate complex, muddy underwater root systems with ease.",
    "They prefer slow-moving rivers over fast-flowing rapids.",
    "During the wet season, their territory expands vastly across flooded plains.",
    "During the dry season, they are forced to crowd around the remaining permanent pools.",
    "They rarely venture more than 500 meters away from a reliable water source.",
    "They can easily swim across large, wide rivers to find fresh feeding grounds.",
    "Their webbed toes spread wide to act like natural paddles in the water.",
    "The density of their bones helps them maintain perfect buoyancy while swimming.",
    "They often use floating mats of vegetation as temporary resting docks.",
    "They can sleep on riverbanks, ready to slide into the water at a second's notice.",
    "Water provides them protection from jaguars, pumas, and ocelots.",
    "However, water also introduces predators like green anacondas and caimans.",
    "They have learned to balance the risks of land and water predators perfectly.",
    "They can use tall marsh grasses as camouflage while wading in shallow water.",
    "Their eyes shine a faint red color at night when hit by a flashlight beam.",
    "They are highly adapted to the seasonal flooding of the South American Llanos.",
    "They share their aquatic habitats with giant river otters and pink river dolphins.",
    "They will happily swim through floating lily pads to get to succulent water plants.",
    "They use muddy banks as giant slides to smoothly enter the water.",
    "They are capable of cross-river migrations if food becomes scarce.",

    # --- Diet & Weird Habits (81-120) ---
    "Capybaras are strict herbivores, meaning they eat only plant matter.",
    "An adult capybara can eat 6 to 8 pounds (2.7 to 3.6 kg) of grass per day.",
    "They are highly selective feeders, focusing on specific nutritious grass species.",
    "They regularly eat their own morning poop in a practice called coprophagy.",
    "Eating their own feces helps them extract maximum nutrients from fibrous grass.",
    "This habit allows them to digest the cellulose in grass a second time.",
    "The bacteria in their feces also helps maintain a healthy gut microbiome.",
    "They produce two distinct types of poop: soft/green (eaten) and hard/olive-shaped (not eaten).",
    "They are known to eat water hyacinths, which helps clear choked waterways.",
    "They will happily munch on aquatic plants, reeds, and sedges.",
    "During the dry season, they supplement their diet with grains and melons.",
    "They will occasionally strip and eat the bark off trees when grass is scarce.",
    "They have been caught raiding agricultural fields for sugar cane and corn.",
    "They cannot synthesize Vitamin C on their own, much like humans and guinea pigs.",
    "In captivity, they must be fed supplementary Vitamin C to prevent scurvy.",
    "They tend to feed mostly during the cool hours of dawn and dusk.",
    "If they feel threatened by humans, they will switch to being completely nocturnal.",
    "They use their highly sensitive lips to sort through grass and find the best blades.",
    "They chew their food so thoroughly that it is reduced to a fine paste before swallowing.",
    "They have a symbiotic relationship with several species of birds.",
    "Birds like the cattle tyrant regularly ride on capybaras' backs to eat bugs.",
    "Capybaras will patiently hold still while birds pick ticks and flies off their skin.",
    "This relationship provides the birds with a meal and the capybaras with pest control.",
    "They will also allow birds to pull loose hairs from their coat to use for nests.",
    "They have been observed eating fallen fruits from trees in the rainforest.",
    "They avoid eating certain plants that contain high levels of toxic tannins.",
    "Their grazing habits help keep riverbank vegetation neatly trimmed.",
    "They play a crucial role in seed dispersal across their native ecosystems.",
    "They will graze in large, coordinated lines to keep an eye out for danger.",
    "A feeding capybara stops to look around for predators every few seconds.",
    "They can accidentally swallow small insects while grazing, but it's not intentional.",
    "They drink a substantial amount of fresh water daily alongside their wet diet.",
    "In captivity, they enjoy treats like apples, carrots, sweet potatoes, and broccoli.",
    "They love pumpkins and are often given them as seasonal enrichment in zoos.",
    "They have a very low metabolic rate compared to other rodents of their size.",
    "Their stomach contents can make up a massive percentage of their total body weight.",
    "They will chew on thick sticks specifically to keep their teeth from overgrowing.",
    "Their grazing pattern promotes the growth of fresh, tender new grass shoots.",
    "They have been observed sharing feeding grounds peacefully with cows and horses.",
    "They are highly efficient machines at turning low-quality grass into energy.",

    # --- Social Life & Communication (121-160) ---
    "Capybaras are highly social and live in stable groups called herds.",
    "A typical capybara herd consists of 10 to 20 tightly-knit individuals.",
    "During the dry season, multiple herds merge around pools, forming groups of up to 100.",
    "A herd is traditionally led by a single, dominant alpha male.",
    "The alpha male establishes his dominance through chase displays and scent marking.",
    "Subordinate males live on the periphery of the herd to act as early warning systems.",
    "Herds also contain several adult females and a large group of communal offspring.",
    "Capybaras are incredibly vocal animals with a complex vocabulary.",
    "They emit a loud, dog-like bark when they sense immediate danger.",
    "When a capybara barks, the entire herd immediately rushes into the nearest water.",
    "They make a soft clicking or purring sound to show contentment and happiness.",
    "Whistles and chirps are used by mothers to keep track of their adventurous pups.",
    "They huff and grunt at each other to negotiate personal space within the herd.",
    "They use low-frequency squeaks to maintain contact while moving through tall grass.",
    "Young pups will whine loudly if they get separated from the main group.",
    "They engage in mutual grooming to strengthen social bonds between herd members.",
    "A capybara will happily lie down and roll over if another herd member grooms them.",
    "They are famously gentle and get along with almost every animal species.",
    "They are often photographed chilling with birds, monkeys, rabbits, and ducks.",
    "Even wild caimans (South American alligators) rarely attack adult capybaras.",
    "They frequently use caimans as temporary sunbathing companions on riverbanks.",
    "This bizarre social harmony has earned them the internet title of 'Nature's Chair.'",
    "They have a very strict social hierarchy that prevents internal fighting.",
    "Dominant males will actively prevent subordinate males from mating with females.",
    "However, peripheral males occasionally succeed by mating when the alpha isn't looking.",
    "They are fiercely territorial and will chase away outsiders from other herds.",
    "Territory sizes range from 25 to 50 acres depending on water availability.",
    "They use communal nurseries where all adult females help raise the pups.",
    "A lactating female capybara will willingly nurse any hungry pup in the herd.",
    "This cooperative breeding ensures a much higher survival rate for the babies.",
    "They huddle closely together in large piles to conserve warmth during cold nights.",
    "They are highly empathetic and will visibly comfort distressed group members.",
    "They can recognize the unique vocal calls of every individual in their herd.",
    "When a member returns after a separation, the herd greets them with soft clicks.",
    "They use collective vigilance, meaning more eyes looking out for predators.",
    "A relaxed capybara will emit a low, vibrating purr when scratched behind the ears.",
    "They prefer to avoid conflict and will almost always run away rather than fight.",
    "If cornered, however, they can inflict severe bites with their razor-sharp teeth.",
    "They are deeply affectionate with family members, often resting their heads on one another.",
    "They maintain their social structures for years, passed down through generations.",

    # --- Babies, Culture, & Fun Facts (161-205) ---
    "A capybara's gestation period lasts roughly 130 to 150 days.",
    "A typical capybara litter consists of about 4 cute, fuzzy pups.",
    "However, they can give birth to anywhere from 1 to 8 pups at a single time.",
    "Capybara pups are precocial, meaning they are born fully formed and active.",
    "Newborn pups are born with a full coat of fur and a complete set of teeth.",
    "Within just a few hours of birth, a pup can walk, run, swim, and dive.",
    "Pups will start chewing on grass within their very first week of life.",
    "Despite eating grass early, they continue to nurse for about 16 weeks.",
    "They reach full sexual maturity at around 15 to 18 months of age.",
    "In the wild, capybaras have a relatively short lifespan of 4 to 8 years.",
    "The low wild lifespan is due to heavy predation by big cats and anacondas.",
    "In captivity, with medical care and no predators, they can live up to 12 years.",
    "In the 16th century, the Catholic Church classified the capybara as a 'fish.'",
    "This allowed Venezuelan hunters to eat capybara meat during the period of Lent.",
    "Because they spend their lives in water and have webbed feet, the classification stuck.",
    "Capybara meat is still traditionally eaten during Holy Week in parts of South America.",
    "Their skin is highly prized for making high-quality leather goods like gloves and jackets.",
    "In Argentina, capybara leather is known locally as 'carpincho' leather.",
    "They are currently classified as a species of 'Least Concern' by the IUCN.",
    "Their global population remains incredibly stable and robust.",
    "They adapt surprisingly well to human-altered landscapes, like golf courses.",
    "In 2021, a herd of capybaras 'invaded' Nordelta, an upscale gated community in Argentina.",
    "The Nordelta capybaras built on their historic wetlands, ate manicured lawns and became local heroes.",
    "This incident turned the capybara into a global internet symbol of anti-bourgeois rebellion.",
    "They have experienced a massive surge in internet popularity due to catchy viral songs.",
    "The viral 'Capybara' song by Russian artist-producer StoBeats became a global TikTok meme.",
    "They are frequently featured in memes due to their unbothered, zen-like aura.",
    "Many people consider them to be the ultimate animal symbol of peace and relaxation.",
    "It is illegal to own a pet capybara in many states and countries due to their complex needs.",
    "To keep a capybara happy, you must provide them with a massive, deep swimming pool.",
    "They cannot survive happily as solitary pets; they require constant companionship.",
    "They can accidentally destroy standard household furniture with their constant chewing.",
    "Despite this, some certified sanctuaries have successfully raised incredibly tame capybaras.",
    "A famous pet capybara named Dobby became an internet sensation for his dog-like behavior.",
    "Dobby loved sleeping on the couch and going for walks on a specialized harness.",
    "Capybaras have a uniquely stiff, clumsy-looking trot when walking slowly on land.",
    "When they get excited, they can perform a joyful 'popcorn' hop, just like guinea pigs.",
    "They are known to sunbathe on docks alongside human swimmers without a care in the world.",
    "Their calm disposition makes them excellent therapy animals in specialized zoo programs.",
    "They can tolerate a wide range of temperatures as long as water is available.",
    "They have been successfully introduced into wild populations in Florida, USA.",
    "These Florida capybaras escaped from captivity and bred in the warm, swampy Everglades.",
    "They are highly intelligent and can be trained to respond to their names and do tricks.",
    "They love being scratched under the chin, which often causes them to fall asleep instantly.",
    "Ultimately, the capybara is proof that you can be huge, weird, and still loved by everyone."
]

# =====================================================================
# 2. FILE TRACKING & STATE SETUP
# =====================================================================
STATE_FILE = "sent_facts.json"

# Credentials setup
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

# Receivers setup: Grab comma-separated string from environments and turn into clean list
RECEIVER_EMAILS_RAW = os.environ.get("RECEIVER_EMAIL", "")
RECEIVER_EMAILS_LIST = [email.strip() for email in RECEIVER_EMAILS_RAW.split(",") if email.strip()]

def load_sent_indices():
    """Loads the list of already sent fact indices to prevent duplicates."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_sent_indices(sent_list):
    """Saves the updated list of sent fact indices."""
    with open(STATE_FILE, 'w') as f:
        json.dump(sent_list, f)

def get_next_fact():
    """Finds a fact that hasn't been sent yet, or resets if all have been sent."""
    sent_indices = load_sent_indices()
    
    # If we ran through all 205 facts, reset the cycle!
    if len(sent_indices) >= len(FACTS):
        print("All facts exhausted! Resetting the Capy-cycle.")
        sent_indices = []
        
    # Find all indices we haven't used yet
    available_indices = [i for i in range(len(FACTS)) if i not in sent_indices]
    
    # Pick a random index from the remaining pool
    chosen_index = random.choice(available_indices)
    
    # Add it to the tracking list and save
    sent_indices.append(chosen_index)
    save_sent_indices(sent_indices)
    
    return FACTS[chosen_index]

# =====================================================================
# 3. MAIL DISPATCH LOGIC
# =====================================================================
def send_capybara_fact():
    if not RECEIVER_EMAILS_LIST:
        print("Error: No receiver emails configured. Please set the RECEIVER_EMAIL environment variable.")
        return

    fact = get_next_fact()
    
    msg = MIMEMultipart()
    msg['From'] = f"Capybot Prime 🤖 <{SENDER_EMAIL}>"
    msg['To'] = ", ".join(RECEIVER_EMAILS_LIST)
    msg['Subject'] = "Your Daily Capybara Fact has Arrived!"
    
# 1. This is your template (keep using r""" so the ASCII head stays on!)
    template = r"""
    ===================================================
                     CAPYBOT v1.2
    ===================================================
    
           /|---|\\
          (  -_-  )   <-- "Greetings, humans."
           )     (
          (_.._.._)
    
    Here is your daily dose of absolute tranquility.
    
    DID YOU KNOW?
    👉 {fact} 👈
    
    ---------------------------------------------------
    This email was dispatched with 100% organic zen.
    Have a relaxed day,
    Capybot 🤖
    ===================================================
    """
    
    # 2. THIS IS THE magic line we need to add/fix!
    # It manually replaces "{fact}" in your template with the real fact.
    body = template.replace("{fact}", fact)
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Establish connection to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade connection to secure TLS
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # NOTE: sendmail requires a Python LIST of emails to deliver to
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS_LIST, msg.as_string())
        
        server.quit()
        print(f"Success: Capybara data successfully delivered to {len(RECEIVER_EMAILS_LIST)} fans.")
    except Exception as e:
        print(f"Error: Mission failed. {e}")

if __name__ == "__main__":
    send_capybara_fact()

