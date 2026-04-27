"""Disease descriptions, severity, and recommendations for all 38 PlantVillage classes."""

DISEASE_INFO: dict[str, dict] = {
    "Apple___Apple_scab": {
        "description": "Apple scab is caused by the fungus Venturia inaequalis. It appears as olive-green to brown lesions on leaves and fruit, reducing marketability and yield.",
        "severity": "moderate",
        "recommendations": [
            "Apply protective fungicide sprays (e.g., captan or myclobutanil) during early spring.",
            "Remove and destroy fallen leaves to reduce fungal spore load.",
            "Improve air circulation by pruning crowded branches.",
            "Plant scab-resistant apple varieties where possible."
        ]
    },
    "Apple___Black_rot": {
        "description": "Black rot is caused by the fungus Botryosphaeria obtusa. It causes circular brown lesions on leaves and mummified, blackened fruit.",
        "severity": "high",
        "recommendations": [
            "Prune out and destroy all infected wood and mummified fruit.",
            "Apply copper-based fungicides from bud break through harvest.",
            "Ensure good sanitation by removing plant debris promptly."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "description": "Caused by Gymnosporangium juniperi-virginianae, this rust disease requires both apple and cedar/juniper trees to complete its life cycle, causing yellow spots on apple leaves.",
        "severity": "moderate",
        "recommendations": [
            "Remove nearby juniper or cedar hosts if feasible.",
            "Apply fungicide sprays (myclobutanil or propiconazole) at pink bud stage.",
            "Plant rust-resistant apple varieties."
        ]
    },
    "Apple___healthy": {
        "description": "The apple plant appears healthy with no visible signs of disease. Continue regular monitoring and preventive care.",
        "severity": "none",
        "recommendations": [
            "Maintain regular watering and fertilisation schedules.",
            "Conduct periodic scouting for early pest and disease signs."
        ]
    },
    "Blueberry___healthy": {
        "description": "The blueberry plant appears healthy. No intervention required at this time.",
        "severity": "none",
        "recommendations": [
            "Maintain soil pH between 4.5 and 5.5 for optimal blueberry growth.",
            "Monitor for spotted wing drosophila and other common pests."
        ]
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "description": "Powdery mildew on cherry is caused by Podosphaera clandestina. It appears as white, powdery fungal growth on young leaves and shoots.",
        "severity": "moderate",
        "recommendations": [
            "Apply sulfur-based or systemic fungicides (e.g., myclobutanil) at first sign.",
            "Avoid overhead irrigation to reduce leaf wetness.",
            "Prune to improve air circulation within the canopy."
        ]
    },
    "Cherry___healthy": {
        "description": "The cherry plant appears healthy with no signs of disease.",
        "severity": "none",
        "recommendations": [
            "Monitor regularly during humid weather when fungal diseases are most likely."
        ]
    },
    "Corn___Cercospora_leaf_spot_Gray_leaf_spot": {
        "description": "Gray leaf spot, caused by Cercospora zeae-maydis, produces rectangular tan to gray lesions running parallel to leaf veins, reducing photosynthesis and yield.",
        "severity": "high",
        "recommendations": [
            "Plant resistant corn hybrids.",
            "Rotate crops to break disease cycles.",
            "Apply foliar fungicides (strobilurin or triazole) at early tassel stage.",
            "Avoid continuous corn monoculture."
        ]
    },
    "Corn___Common_rust": {
        "description": "Common rust is caused by Puccinia sorghi, producing brick-red powdery pustules on both leaf surfaces, reducing photosynthetic capacity.",
        "severity": "moderate",
        "recommendations": [
            "Plant resistant hybrids as the primary management strategy.",
            "Apply fungicides early in the season if rust is detected before tasselling."
        ]
    },
    "Corn___Northern_Leaf_Blight": {
        "description": "Northern leaf blight, caused by Exserohilum turcicum, produces large, cigar-shaped, grayish-green to tan lesions on corn leaves.",
        "severity": "high",
        "recommendations": [
            "Use resistant hybrids with Ht1, Ht2, or Ht3 resistance genes.",
            "Apply fungicide sprays at early disease onset.",
            "Rotate with non-host crops to reduce inoculum."
        ]
    },
    "Corn___healthy": {
        "description": "The corn plant appears healthy. No disease detected.",
        "severity": "none",
        "recommendations": ["Continue scouting regularly, especially during humid weather."]
    },
    "Grape___Black_rot": {
        "description": "Grape black rot, caused by Guignardia bidwellii, produces tan lesions with dark borders on leaves and causes berries to shrivel into hard, black mummies.",
        "severity": "high",
        "recommendations": [
            "Remove and destroy mummified berries and infected plant material.",
            "Apply fungicides (mancozeb, myclobutanil) from early shoot growth through veraison.",
            "Improve canopy airflow through proper pruning."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "description": "Esca, also called Black Measles, is a complex wood disease caused by several fungi. It causes tiger-stripe leaf patterns, berry spotting, and can lead to vine death.",
        "severity": "severe",
        "recommendations": [
            "Remove and destroy severely infected vines.",
            "Apply wound protectants after pruning.",
            "Avoid large pruning wounds; use double-pruning technique."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "description": "Caused by Pseudocercospora vitis, leaf blight produces dark brown angular spots on leaves that can coalesce and cause early defoliation.",
        "severity": "moderate",
        "recommendations": [
            "Apply copper-based fungicides at shoot emergence.",
            "Remove and burn infected leaves during the growing season.",
            "Ensure adequate row spacing for air circulation."
        ]
    },
    "Grape___healthy": {
        "description": "The grape vine appears healthy with no visible disease symptoms.",
        "severity": "none",
        "recommendations": ["Continue preventive fungicide programme during wet seasons."]
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "description": "Huanglongbing (HLB), or citrus greening, is one of the most devastating citrus diseases caused by Candidatus Liberibacter bacteria, spread by Asian citrus psyllid. It causes asymmetric yellowing ('blotchy mottle') and misshapen, bitter fruit.",
        "severity": "severe",
        "recommendations": [
            "There is no cure; remove and destroy infected trees to prevent spread.",
            "Control Asian citrus psyllid populations with insecticides.",
            "Plant certified disease-free nursery stock.",
            "Report suspected HLB to local agricultural authorities."
        ]
    },
    "Peach___Bacterial_spot": {
        "description": "Bacterial spot, caused by Xanthomonas arboricola pv. pruni, causes water-soaked lesions on leaves that turn brown and fall out, leaving a 'shot-hole' appearance, and causes fruit blemishes.",
        "severity": "moderate",
        "recommendations": [
            "Apply copper bactericides from bloom through fruit development.",
            "Avoid overhead sprinkler irrigation.",
            "Plant resistant peach varieties."
        ]
    },
    "Peach___healthy": {
        "description": "The peach tree appears healthy with no visible signs of disease.",
        "severity": "none",
        "recommendations": ["Monitor for brown rot and bacterial spot during warm, humid periods."]
    },
    "Pepper,_bell___Bacterial_spot": {
        "description": "Bacterial spot on bell pepper, caused by Xanthomonas spp., produces water-soaked, irregular spots on leaves and fruit that turn brown and necrotic.",
        "severity": "moderate",
        "recommendations": [
            "Use certified disease-free transplants and seeds.",
            "Apply copper-based bactericides preventively.",
            "Avoid working in fields when plants are wet.",
            "Rotate crops on a 2–3 year schedule."
        ]
    },
    "Pepper,_bell___healthy": {
        "description": "The bell pepper plant appears healthy.",
        "severity": "none",
        "recommendations": ["Ensure consistent moisture and scout for early aphid infestations."]
    },
    "Potato___Early_blight": {
        "description": "Early blight, caused by Alternaria solani, produces dark, target-like concentric ring lesions on older leaves, progressing upward through the canopy.",
        "severity": "moderate",
        "recommendations": [
            "Apply fungicides (chlorothalonil, mancozeb) at first symptom appearance.",
            "Ensure adequate potassium nutrition to improve plant vigor.",
            "Destroy volunteer potato plants that harbor the pathogen."
        ]
    },
    "Potato___Late_blight": {
        "description": "Late blight, caused by Phytophthora infestans, was responsible for the Irish Potato Famine. It produces water-soaked, greasy-looking lesions that rapidly kill foliage and tubers.",
        "severity": "severe",
        "recommendations": [
            "Apply systemic fungicides (metalaxyl or cymoxanil) at first sign.",
            "Remove and destroy infected plants immediately.",
            "Avoid overhead irrigation; plant in well-drained soil.",
            "Plant certified disease-free seed potatoes."
        ]
    },
    "Potato___healthy": {
        "description": "The potato plant appears healthy with no signs of blight or other disease.",
        "severity": "none",
        "recommendations": ["Scout regularly during cool, wet weather when late blight risk is highest."]
    },
    "Raspberry___healthy": {
        "description": "The raspberry plant appears healthy.",
        "severity": "none",
        "recommendations": ["Prune out old floricanes after fruiting and ensure good drainage."]
    },
    "Soybean___healthy": {
        "description": "The soybean plant appears healthy.",
        "severity": "none",
        "recommendations": ["Monitor for soybean cyst nematode and sudden death syndrome."]
    },
    "Squash___Powdery_mildew": {
        "description": "Powdery mildew on squash, caused by Podosphaera xanthii, appears as white powdery patches on upper leaf surfaces, reducing photosynthesis and causing premature defoliation.",
        "severity": "moderate",
        "recommendations": [
            "Apply potassium bicarbonate or sulfur-based fungicides at first sign.",
            "Plant resistant varieties.",
            "Avoid excessive nitrogen fertilisation which promotes susceptible soft growth."
        ]
    },
    "Strawberry___Leaf_scorch": {
        "description": "Leaf scorch, caused by Diplocarpon earliana, produces irregular dark purple blotches on the upper leaf surface that merge, causing the leaf to appear scorched and reddish-purple.",
        "severity": "moderate",
        "recommendations": [
            "Remove and destroy infected leaves.",
            "Apply fungicides (captan or thiram) preventively.",
            "Avoid overhead irrigation; use drip systems."
        ]
    },
    "Strawberry___healthy": {
        "description": "The strawberry plant appears healthy.",
        "severity": "none",
        "recommendations": ["Renew plantings every 2–3 years to reduce disease buildup."]
    },
    "Tomato___Bacterial_spot": {
        "description": "Bacterial spot on tomato, caused by Xanthomonas spp., produces small, water-soaked, dark lesions with yellow halos on leaves and fruit, reducing quality and yield.",
        "severity": "moderate",
        "recommendations": [
            "Use copper-based bactericides and mancozeb from transplanting.",
            "Avoid working in fields when foliage is wet.",
            "Use disease-free transplants and resistant varieties."
        ]
    },
    "Tomato___Early_blight": {
        "description": "Early blight on tomato, caused by Alternaria solani, causes dark concentric ring lesions surrounded by yellow tissue, starting on older leaves and moving upward.",
        "severity": "moderate",
        "recommendations": [
            "Apply chlorothalonil or mancozeb every 7–10 days during humid periods.",
            "Stake plants to improve air circulation.",
            "Mulch around plants to prevent soil splash."
        ]
    },
    "Tomato___Late_blight": {
        "description": "Tomato late blight, caused by Phytophthora infestans, produces large, irregular, greasy-green water-soaked lesions. White sporulation visible on the underside of leaves under humid conditions.",
        "severity": "severe",
        "recommendations": [
            "Apply systemic fungicides (e.g., Ridomil Gold) immediately upon detection.",
            "Remove and bag all infected plant material immediately.",
            "Avoid overhead irrigation; water in the morning."
        ]
    },
    "Tomato___Leaf_Mold": {
        "description": "Caused by Passalora fulva, tomato leaf mold produces pale green to yellow spots on the upper leaf surface and olive-green velvety mould on the underside.",
        "severity": "moderate",
        "recommendations": [
            "Improve greenhouse ventilation to reduce humidity.",
            "Apply fungicides containing chlorothalonil or thiram.",
            "Plant resistant varieties with Cf resistance genes."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "description": "Septoria leaf spot, caused by Septoria lycopersici, produces numerous small, circular spots with white centres and dark borders on lower leaves first, rapidly defoliating plants.",
        "severity": "high",
        "recommendations": [
            "Apply fungicides (chlorothalonil, copper) every 7 days in wet conditions.",
            "Remove lower infected leaves promptly.",
            "Rotate tomatoes with non-solanaceous crops."
        ]
    },
    "Tomato___Spider_mites_Two-spotted_spider_mite": {
        "description": "Two-spotted spider mites (Tetranychus urticae) cause stippled, bronze-coloured foliage and fine webbing on the undersides of leaves, reducing photosynthesis under hot, dry conditions.",
        "severity": "moderate",
        "recommendations": [
            "Apply miticides (abamectin, bifenazate) and rotate modes of action.",
            "Increase humidity through overhead irrigation to reduce mite populations.",
            "Introduce predatory mites (Phytoseiulus persimilis) for biological control."
        ]
    },
    "Tomato___Target_Spot": {
        "description": "Target spot, caused by Corynespora cassiicola, produces brown, concentric-ringed lesions on leaves, stems, and fruit, resembling a target.",
        "severity": "moderate",
        "recommendations": [
            "Apply fungicides (azoxystrobin or difenoconazole) preventively.",
            "Improve air movement within the canopy."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "description": "TYLCV is a devastating viral disease transmitted by whiteflies (Bemisia tabaci). Symptoms include severe leaf curl upward, yellowing, stunting, and very low or no fruit set.",
        "severity": "severe",
        "recommendations": [
            "Control whitefly populations with insecticides or reflective mulches.",
            "Remove and destroy infected plants immediately.",
            "Plant TYLCV-resistant tomato varieties.",
            "Install insect-proof netting in greenhouse production."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "description": "Tomato mosaic virus (ToMV) causes mosaic patterns of light and dark green on leaves, leaf distortion, and fruit discolouration. It spreads through mechanical contact.",
        "severity": "high",
        "recommendations": [
            "Remove and destroy infected plants.",
            "Disinfect tools with 10% bleach solution between plants.",
            "Wash hands thoroughly after handling tobacco products before entering fields.",
            "Plant ToMV-resistant varieties."
        ]
    },
    "Tomato___healthy": {
        "description": "The tomato plant appears healthy with no visible disease symptoms.",
        "severity": "none",
        "recommendations": [
            "Continue scouting regularly, especially during warm humid periods.",
            "Maintain good nutrition and consistent irrigation."
        ]
    },
}
