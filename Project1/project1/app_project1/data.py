class PestDisease:
    def __init__(self, id, name, scientific_name, short_desc, full_desc, image_url, category, severity, symtoms, monitoring,control_period):
        self.id = id
        self.name = name
        self.scientific_name = scientific_name
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.image_url = image_url
        self.category = category
        self.severity = severity
        self.symtoms = symtoms
        self.monitoring = monitoring
        self.control_period = control_period

pests_list = [
    PestDisease(
        1,
        "Mango Hopper",
        "Idioscopus clypealis",
        "Small jumping insects that damage flowers.",
        "Mango hoppers feed on sap and damage inflorescences, causing flower drop. Their excretion leads to sooty mold growth. Spraying during flowering helps control them.",
        "/static/images/mango-hopper.jpg",
        "Insect",
        "High",
        "Leaf curling, sticky sticky liquid, sooty mould",
        "Monitor before and during flowering",
        "Pre-flowering to flowering stage."
    ),

    PestDisease(
        2,
        "Fruit Flies",
        "Bactrocera dorsalis",
        "They lay eggs inside mango fruit.",
        "Female fruit flies puncture the mango skin to lay eggs. The larvae feed inside the fruit, making it unmarketable. Proper trapping and sanitation reduce the population.",
        "/static/images/mango-fruit-fly.jpg",
        "Insect",
        "High",
        "Sting marks, fruit decay, young insects in flesh",
        "Use lure traps. inspect fruit for sting marks",
        "Ripening and mature fruit stages"
    ),
    PestDisease(
        3,
        "Powdery Mildew",
        "Oidium mangiferae",
        "White powder appears on young leaves and flowers.",
        "Powdery mildew is caused by Oidium mangiferae and thrives in dry climates with high humidity. It affects young tissues and can lead to poor fruit set and reduced yield.",
        "/static/images/powdery-mildew.jpg",
        "Fungus",
        "Medium",
        "White powdery growth on panicles, leaves, and young fruit",
        "Monitor during dry conditions and early flowering",
        "Early flowering to fruit set",

    ),
    PestDisease(
        4,
        "Anthracnose",
        "Colletotrichum gloeosporioides",
        "Black spots caused by a fungal disease.",
        "Anthracnose is a fungal disease that causes dark, sunken lesions on mango leaves, flowers, and fruits. Infected fruit may drop early or rot after harvest.",
        "/static/images/anthracnose.jpg",
        "Fungus",
        "High",
        "Black spots on leaves, flowers, fruit. Post-harvest fruit rot",
        "Inspect during wet conditions and flowering. Monitor harvested fruit",
        "Pre-flowering to post-harvest",
    ),
    PestDisease(
        5,
        "Mealybugs",
        "Drosicha mangiferae",
        "Tiny insects that suck plant sap.",
        "Mealybugs are white, cotton-like pests that feed on sap. They produce honeydew, which attracts ants and promotes mold. They weaken plants and reduce fruit quality.",
        "/static/images/mealybugs.jpg",
        "Insect",
        "Medium",
        "Symtoms",
        "Monitoring",
        "Control period",
    ),

    PestDisease(
        6,
        "Red Rust",
        "Cephaleuros virescens",
        "Orange-red rust spots on leaves and stems.",
        "Red rust is caused by algae. It forms reddish-orange spots on leaves and stems, and may cause twig dieback and fruit drop in severe cases.",
        "/static/images/red_rust.jpg",
        "Algae",
        "Low",
        "Symtoms",
        "Monitoring",
        "Control period",
    ),
    PestDisease(
        7,
        "Bacterial Canker",
        "Xanthomonas campestris",
        "Cracks and oozing on stems and branches.",
        "Bacterial canker results in cankers, cracking bark, and gummy ooze. It affects stems and fruits. Pruning and copper sprays help reduce spread.",
        "/static/images/bacterial_canker.jpg",
        "Bacteria",
        "Medium",
        "Symtoms",
        "Monitoring",
        "Control period",
    )
]
