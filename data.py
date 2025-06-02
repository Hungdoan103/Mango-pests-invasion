class PestDisease:
    def __init__(self, id, name, severity, type, sci_name, short_des, long_des,
                 egg, larvae, adult, life_cycle, symp, damage, monitor,
                 iterve_thres, ctr_measure, ref, image_url):
        self.id = id
        self.name = name
        self.severity = severity
        self.type = type
        self.sci_name = sci_name
        self.short_des = short_des
        self.long_des = long_des
        self.egg = egg
        self.larvae = larvae
        self.adult = adult
        self.life_cycle = life_cycle
        self.symp = symp
        self.damage = damage
        self.monitor = monitor
        self.iterve_thres = iterve_thres
        self.ctr_measure = ctr_measure
        self.ref = ref
        self.image_url = image_url
        self.category_class = self.type.split()[0].lower()


pests_list = [
    PestDisease(
        "P01", "Mango Seed Weevil",
        "High (Directly damages seeds, severely impacts fruit quality and export potential).",
        "Insect (Beetle, Coleoptera)", "Sternochetus mangiferae", "",
        "The female weevil lays eggs on young fruits (30mm), covering them with wax from her oviposition cuts. Larvae tunnel into seeds, consuming the kernel over 53 days, leaving the fruit externally intact but internally destroyed. This quarantine pest causes significant economic losses by rendering infested fruits unfit for export.",
        "Creamy white, 2mm long.", "Legless, brown head, white body.",
        "Gray-brown with a long snout, 10mm long.",
        "1 generation/year. Eggs laid on young fruits (30mm). Larvae burrow into seeds, develop in 53 days.",
        "Sap exudate on young fruit, seed tunneling.",
        "Seed destruction, reduced fruit quality.",
        "Inspect fallen fruits; cut fruits to examine seeds.",
        "5% infested young fruits.",
        "Pre- and post-fruit set insecticides, orchard sanitation.",
        "Pages 24-25 (PDF).", "/static/images/seed_weevil.jpeg"
    ),
    PestDisease(
        "P02", "Fruitspotting Bug",
        "Moderate-High (Causes fruit drop, reduces yield).",
        "Insect (True Bug, Hemiptera)", "Amblypelta lutescens lutescens, A. nitida", "",
        "Adults suck sap from shoots and fruits, causing necrotic black lesions that lead to fruit cracking and premature drop. They hide under leaves during the day and are active at night, making detection difficult. Scarring on mature fruits reduces market value.",
        "Pale green, 2mm long.", "No", "Light green with brown wings, 15mm long.",
        "4–5 generations/year; egg-to-adult development in 35–42 days.",
        "Black lesions on shoots, cracks on young fruits.",
        "Fruit drop, yield loss.",
        "Weekly checks on new shoots.",
        "10% damaged shoots.",
        "Insecticide sprays during fruit set.",
        "Pages 32-33 (PDF).", "/static/images/fruitspotting_bug.jpg"
    ),
    PestDisease(
        "P03", "Fruit Flies",
        "Very High (Destroys ripe fruit, major economic loss).",
        "Insect (Fly, Diptera)", "Bactrocera tryoni, B. jarvisi", "",
        "Females lay eggs under the skin of ripe fruits, where larvae tunnel through the flesh, causing internal rot. Infested fruits develop small exit holes with oozing sap and are often discarded post-harvest. Adults are attracted to ripening fruits and rapidly spread across orchards.",
        "Creamy white, 1mm long.", "White maggots, 8mm long.",
        "Yellow-brown with patterned wings, 9–10mm long.",
        "Larvae develop in 6–8 days; pupation in soil (10–12 days).",
        "Puncture marks on ripe fruit, internal rot.",
        "Fruit decay, export rejection.",
        "Pheromone traps, ripe fruit inspection.",
        "1 fly/week in traps.",
        "Bait sprays, orchard hygiene.",
        "Pages 56-57 (PDF).", "/static/images/fruit_flies.jpg"
    ),
    PestDisease(
        "P04", "Mango Leafhopper",
        "Moderate (Weakens trees, reduces fruit set).",
        "Insect (Leafhopper, Hemiptera)", "Idioscopus nitidulus, I. clypealis", "",
        "Nymphs and adults feed on young shoots and flowers, excreting honeydew that promotes sooty mold growth. The black mold coats leaves, reducing photosynthesis and causing flower abortion. Their rapid reproduction during dry seasons is signaled by distinctive 'clicking' sounds.",
        "Cigar-shaped, creamy yellow.", "No", "Golden-brown, 4–5mm long.",
        "Egg-to-adult in 12–20 days.",
        "Curled leaves, honeydew, sooty mold.",
        "Reduced fruit set, tree decline.",
        "Listen for 'clicking' sounds from large populations.",
        "20 hoppers/inflorescence.",
        "Imidacloprid sprays, encourage natural enemies.",
        "Pages 38-39 (PDF).", "/static/images/Mango-hopper.jpg"
    ),
    PestDisease(
        "P05", "Mango Fruit Borer",
        "High (Renders fruit unmarketable).",
        "Insect (Moth, Lepidoptera)", "Citripestis eutraphera", "",
        "Larvae bore into fruit near the stem, creating tunnels filled with moist frass, leading to internal rot and fruit drop. Infested fruits are unmarketable due to decay. Nocturnal moths target susceptible mango varieties, laying eggs on developing fruits.",
        "White, turning red after 1 day.", "Pink-brown with black head.",
        "Brown wings, 24mm wingspan.",
        "Egg-to-adult in 30 days.",
        "Boreholes in fruit, frass around stems.",
        "Fruit rot, commercial loss.",
        "Check young and fallen fruits.",
        "5% infested fruits.",
        "Insecticide sprays during early fruit development.",
        "Pages 44-45 (PDF).", "/static/images/fruit_borer.jpg"
    ),
    PestDisease(
        "P06", "Redbanded Thrips",
        "Moderate (Impairs photosynthesis, scars fruit).",
        "Insect (Thrips, Thysanoptera)", "Selenothrips rubrocinctus", "",
        "Thrips scrape leaf surfaces to feed on sap, turning leaves silvery and curling their edges. On fruits, feeding causes brown scars that degrade quality. They thrive in hot, dry conditions and hide on the undersides of leaves.",
        "Kidney-shaped, black when dry.", "No",
        "Dark brown with red abdominal bands.",
        "Egg-to-adult in 14–21 days.",
        "Silvery leaves, brown scars on fruit.",
        "Reduced photosynthesis, cosmetic fruit damage.",
        "Hand lens inspection of leaf undersides.",
        "10 thrips/leaf.",
        "Target larval stages with insecticides.",
        "Pages 82-83 (PDF).", "/static/images/thrips.jpg"
    ),
    PestDisease(
        "P07", "Tea Mosquito Bug",
        "High (Causes flower/fruit abortion).",
        "Insect (Mirid Bug, Hemiptera)", "Helopeltis pernicialis", "",
        "Bugs inject toxins into shoots, flowers, and fruits, causing black necrotic spots and deformed growth. Infested young fruits often abort or drop, while shoots wilt and die. They prefer dense foliage and are challenging to detect due to their small size.",
        "White, embedded in plant tissue.", "No",
        "Black with orange thorax, 6–7mm long.",
        "Egg-to-adult in 15–30 days.",
        "Black necrotic spots on shoots and fruits.",
        "Flower drop, deformed fruits.",
        "Inspect new shoots and fruits.",
        "2 bugs/branch.",
        "Prune dense foliage, insecticide sprays.",
        "Pages 36-37 (PDF).", "/static/images/mosquito_bug.jpg"
    ),
    
    
    
    
    
    
    PestDisease(
    "D06",
    "Anthracnose",
    "Very High (Causes up to 80% yield loss).",
    "Fungus",
    "Colletotrichum gloeosporioides",
    "Fungus spreads via rain-splashed spores and wind. Infects leaves and fruits.",
    "Fungus survives on infected leaves/branches; spreads via rain and wind, spreads via rain-splashed spores, infecting flowers and fruits through stomata or wounds. Post-harvest, infected fruits develop soft rot under humid conditions. Leaf lesions with dark margins weaken trees by reducing photosynthesis.",
    "No",
    "No",
    "No",
    "Spores germinate at >90% humidity, 25–30°C. Thrives in wet seasons.",
    "Black lesions on leaves/flowers; post-harvest fruit rot.",
    "Yield reduction, fruit spoilage.",
    "Check leaves/flowers post-rain; use spore traps.",
    "5% infected leaves/flowers.",
    "Copper-based fungicides, orchard sanitation.",
    "Pages 134–138 (PDF).",
    "/static/images/anthracnose.jpg"
),
PestDisease(
    "D07",
    "Powdery Mildew",
    "High (Triggers flower/fruit drop).",
    "Fungus",
    "Oidium mangiferae",
    "White powdery growth on leaves and flowers. Triggers flower drop.",
    "White powdery growth on leaf surfaces. Blocks sunlight and causes tissue desiccation. Nighttime humidity and daytime dryness trigger outbreaks. Affects flowers and fruitlets.",
    "No",
    "No",
    "No",
    "Spreads in dry, low humidity (50–70%). Active at night.",
    "White powder on leaves/flowers; premature fruit drop.",
    "Reduced fruit set.",
    "Observe humidity, inspect flowers.",
    "10% infected inflorescences.",
    "Sulfur sprays, Triadimefon.",
    "Page 148 (PDF).",
    "/static/images/powdery-mildew.jpg"
),
PestDisease(
    "D01",
    "Mango Malformation Disease",
    "Very High (Destroys shoots, prevents fruiting).",
    "Fungus",
    "Bactrocera tryoni, B. jarvisi",
    "Twisted shoots and malformed flowers due to fungal infection.",
    "Fusarium mangiferae disrupts cell division, causing twisted shoots and dense, sterile flower clusters. Spreads via mites, pruning tools or wind.",
    "No",
    "No",
    "No",
    "Soil-borne spores; thrives at 20–25°C.",
    "Twisted shoots, malformed flowers.",
    "Severe yield loss.",
    "Inspect new shoots in early dry season.",
    "5% malformed shoots.",
    "Prune infected shoots, apply Carbendazim.",
    "Page 142 (PDF).",
    "/static/images/malformation.jpeg"
),
PestDisease(
    "D02",
    "Algal Leaf Spot",
    "Moderate (Reduces photosynthesis).",
    "Algae",
    "Cephaleuros virescens",
    "Orange-gray spots on leaves from algal infection.",
    "Cephaleuros virescens forms raised orange-gray spots on leaves, reducing photosynthesis. Spreads via rain and thrives in prolonged humidity.",
    "No",
    "No",
    "No",
    "Spreads via rain/wind; thrives in high humidity.",
    "Gray-orange spots on leaves/bark.",
    "Weakens trees.",
    "Check leaves after rain or in wet seasons.",
    "5% infected leaves.",
    "Copper sprays, pruning.",
    "Page 132 (PDF).",
    "/static/images/algal_leaf.jpeg"
),
PestDisease(
    "D03",
    "Stem End Rot",
    "High (Post-harvest fruit decay).",
    "Fungus",
    "Lasiodiplodia theobromae",
    "Black rot from stem spreads inward. Post-harvest decay.",
    "Enters through stem wounds or harvest injuries. Causes black rot from the stem inward. Fruits emit fermented odor and become unmarketable. Persists in soil.",
    "No",
    "No",
    "No",
    "Soil-borne; active at 28–32°C.",
    "Black rot from stem end inward.",
    "Post-harvest losses.",
    "Inspect ripe fruits pre-harvest.",
    "5% infected fruits.",
    "Hot water treatment (55°C), cold storage.",
    "Page 154 (PDF).",
    "/static/images/ser.jpeg"
),
PestDisease(
    "D04",
    "Bacterial Black Spot",
    "High (Defoliates trees, scars fruit).",
    "Bacteria",
    "Xanthomonas campestris",
    "Black spots with yellow halos; spread by wind and tools.",
    "Spreads via rain, wind, pruning. Creates black leaf spots with yellow halos and fruit cracks. Cosmetic damage lowers commercial value.",
    "No",
    "No",
    "No",
    "Enters through stomata/wounds; thrives at 25–30°C.",
    "Black spots with yellow halos on leaves; fruit cracks.",
    "Leaf drop, unmarketable fruit.",
    "Inspect after rain or pruning.",
    "10% infected foliage.",
    "Copper-based bactericides, avoid overhead irrigation.",
    "Page 160 (PDF).",
    "/static/images/bacterial_black_spot.jpg"
),
PestDisease(
    "D05",
    "Pink Disease",
    "Moderate (Kills branches, stunts growth).",
    "Fungus ",
    "Erythricium salmonicolor",
    "Pink growth on bark; branch dieback.",
    "Forms pink fungal growth on bark, eventually cracking stems and causing sap oozing. Branches die back. Thrives in shaded orchards.",
    "No",
    "No",
    "No",
    "Spreads via water/insects; thrives at >80% humidity.",
    "Pink powdery coating on branches; oozing sap.",
    "Branch dieback.",
    "Inspect infected branches/trees.",
    "2 bugs/branch.",
    "Lime wash tree bases, apply Hexaconazole.",
    "Page 146 (PDF).",
    "/static/images/pink_disease.jpg"
),

]
