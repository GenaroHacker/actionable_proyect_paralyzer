def add_example_data():
    tasks = [
        # Task 1
        {
            "place": "home",
            "context": "exercise",
            "tag": "yoga",
            "task": "complete a %duration%-minute yoga session",
            "steps": [
                "set up a comfortable space with a yoga mat",
                "choose a %duration%-minute yoga routine video",
                "follow the video instructions carefully",
                "focus on breathing and posture",
                "cool down and relax for a few minutes after finishing"
            ]
        },
        # Task 2
        {
            "place": "home",
            "context": "recreate",
            "tag": "painting",
            "task": "paint a landscape using %color% colors",
            "steps": [
                "gather all painting supplies",
                "choose a landscape reference or use imagination",
                "sketch the basic outline on canvas",
                "start painting with %color% colors from the background to foreground",
                "let the painting dry and clean up the workspace"
            ]
        },
        # Task 3
        {
            "place": "home",
            "context": "create",
            "tag": "cooking",
            "task": "bake %flavor% cookies",
            "steps": [
                "preheat the oven and prepare baking sheets",
                "mix dough ingredients and fold in %flavor% chips",
                "scoop dough onto baking sheets",
                "bake until cookies are golden brown",
                "cool cookies on a rack before serving"
            ]
        },
        # Task 4
        {
            "place": "office",
            "context": "work",
            "tag": "report",
            "task": "compile a %period% sales report",
            "steps": [
                "gather all relevant sales data from %period%",
                "analyze trends and key performance indicators",
                "create charts and graphs to represent data",
                "write a summary of findings",
                "format the report and prepare for presentation"
            ]
        },
        # Task 5
        {
            "place": "gym",
            "context": "exercise",
            "tag": "strength training",
            "task": "complete a strength training circuit with %equipment%",
            "steps": [
                "start with a 5-minute warm-up",
                "perform three sets of weight lifting exercises with %equipment%",
                "include exercises targeting major muscle groups",
                "take short breaks between sets",
                "end with a 5-minute cool down and stretching"
            ]
        },
        # Task 6
        {
            "place": "home",
            "context": "exercise",
            "tag": "cardio",
            "task": "perform a %time%-minute high-intensity workout",
            "steps": [
                "start with a quick warm-up",
                "follow a %time%-minute HIIT video",
                "perform each exercise with high energy",
                "ensure breaks are short to maintain intensity",
                "cool down with light stretching"
            ]
        },
        # Task 7
        {
            "place": "home",
            "context": "sleep",
            "tag": "relaxation",
            "task": "prepare for a restful nights sleep",
            "steps": [
                "turn off all electronic devices %time% minutes before bed",
                "prepare a cup of %herb% tea",
                "read a book or practice meditation",
                "ensure the room is dark and at a comfortable temperature",
                "try to go to bed at the same time each night"
            ]
        },
        # Task 8
        {
            "place": "office",
            "context": "work",
            "tag": "meeting",
            "task": "organize a %duration%-minute team meeting",
            "steps": [
                "prepare the meeting agenda in advance",
                "invite all relevant team members",
                "start the meeting on time and follow the agenda",
                "encourage team interaction and discussion",
                "summarize key points and conclude on time"
            ]
        },
        # Task 9
        {
            "place": "gym",
            "context": "exercise",
            "tag": "cardio",
            "task": "run on the treadmill for %time% minutes",
            "steps": [
                "start with a 5-minute warm-up at a slow pace",
                "increase speed to a comfortable run",
                "maintain steady pace for %time% minutes",
                "cool down with a 5-minute slow walk",
                "stretch after finishing the run"
            ]
        },
        # Task 10
        {
            "place": "home",
            "context": "create",
            "tag": "crafting",
            "task": "create a %item% using %material%",
            "steps": [
                "gather all necessary tools and materials",
                "follow a guide or tutorial for making %item%",
                "carefully measure and cut %material%",
                "assemble and secure all parts of %item%",
                "finalize with painting or decoration as needed"
            ]
        },
        # Task 11
        {
            "place": "home",
            "context": "recreate",
            "tag": "music",
            "task": "practice %instrument% for %time% minutes",
            "steps": [
                "set up your %instrument% in a quiet space",
                "tune the %instrument% before starting",
                "practice scales or specific pieces for %time% minutes",
                "focus on technique and rhythm",
                "store the %instrument% safely after practice"
            ]
        },
        # Task 12
        {
            "place": "office",
            "context": "work",
            "tag": "organization",
            "task": "organize and label %item% files",
            "steps": [
                "gather all %item% files",
                "sort the files by date or relevance",
                "label each file clearly",
                "store the files in designated cabinets or folders",
                "update the digital tracking system if available"
            ]
        },
        # Task 13
        {
            "place": "home",
            "context": "exercise",
            "tag": "fitness",
            "task": "do a %time%-minute full-body workout",
            "steps": [
                "choose a %time%-minute workout routine",
                "set up your workout space with necessary equipment",
                "follow the routine, focusing on form",
                "take brief rests between exercises if needed",
                "stretch and cool down after the workout"
            ]
        },
        # Task 14
        {
            "place": "gym",
            "context": "exercise",
            "tag": "flexibility",
            "task": "attend a %duration%-minute stretching class",
            "steps": [
                "arrive at the gym early to secure a spot",
                "bring a yoga mat and water bottle",
                "participate actively in the class",
                "focus on breathing and stretching each muscle group",
                "hydrate and rest after the class"
            ]
        },
        # Task 15
        {
            "place": "office",
            "context": "work",
            "tag": "research",
            "task": "conduct research on %topic%",
            "steps": [
                "define the scope of research on %topic%",
                "gather resources and materials",
                "take detailed notes and organize information",
                "analyze findings and draw conclusions",
                "compile a report or presentation on the research"
            ]
        },
        # Task 16
        {
            "place": "home",
            "context": "create",
            "tag": "gardening",
            "task": "plant %plant% in the garden",
            "steps": [
                "choose a suitable location for %plant%",
                "prepare the soil and dig holes",
                "plant %plant% and water thoroughly",
                "add mulch around the plant for moisture retention",
                "regularly check and care for %plant%"
            ]
        },
        # Task 17
        {
            "place": "gym",
            "context": "exercise",
            "tag": "cardio",
            "task": "complete a %time%-minute cycling class",
            "steps": [
                "set up the bike to fit your height",
                "start with a light warm-up",
                "follow the instructors routine",
                "maintain a steady pace and intensity",
                "cool down and stretch after the class"
            ]
        },
        # Task 18
        {
            "place": "home",
            "context": "sleep",
            "tag": "relaxation",
            "task": "perform %time% minutes of bedtime yoga",
            "steps": [
                "create a calm atmosphere in your bedroom",
                "choose a gentle %time%-minute yoga routine",
                "focus on relaxing poses and deep breathing",
                "end with a meditation or mindfulness exercise",
                "prepare for a peaceful nights sleep"
            ]
        },
        # Task 19
        {
            "place": "office",
            "context": "work",
            "tag": "planning",
            "task": "plan the agenda for %event%",
            "steps": [
                "define the objectives of %event%",
                "list key topics and speakers",
                "allocate time slots for each session",
                "incorporate breaks and networking opportunities",
                "circulate the agenda to participants in advance"
            ]
        },
        # Task 20
        {
            "place": "gym",
            "context": "exercise",
            "tag": "cardio",
            "task": "complete a %time%-minute swimming session",
            "steps": [
                "warm up with a few laps",
                "choose a swimming stroke and pace",
                "maintain a steady pace for %time% minutes",
                "cool down with a few laps",
                "stretch after finishing the swim"
            ]
        },
    {"place": "alphabet", "context": "a", "tag": "a", "task": "a a a", "steps": ["%duration% %duration% %duration% %duration% %duration% %duration% %duration% %duration%"]},
    {"place": "alphabet", "context": "a", "tag": "a", "task": "b a a", "steps": ["."]},
    {"place": "alphabet", "context": "a", "tag": "a", "task": "c a a", "steps": ["."]},
    {"place": "alphabet", "context": "a", "tag": "b", "task": "a b a", "steps": ["."]},
    {"place": "alphabet", "context": "a", "tag": "b", "task": "b b a", "steps": ["."]},
    {"place": "alphabet", "context": "a", "tag": "b", "task": "c b a", "steps": ["."]},
    {"place": "alphabet", "context": "a", "tag": "c", "task": "a c a", "steps": ["."]},
    {"place": "alphabet", "context": "a", "tag": "c", "task": "b c a", "steps": ["."]},
    {"place": "alphabet", "context": "a", "tag": "c", "task": "c c a", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "a", "task": "a a b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "a", "task": "b a b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "a", "task": "c a b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "b", "task": "a b b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "b", "task": "b b b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "b", "task": "c b b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "c", "task": "a c b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "c", "task": "b c b", "steps": ["."]},
    {"place": "alphabet", "context": "b", "tag": "c", "task": "c c b", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "a", "task": "a a c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "a", "task": "b a c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "a", "task": "c a c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "b", "task": "a b c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "b", "task": "b b c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "b", "task": "c b c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "c", "task": "a c c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "c", "task": "b c c", "steps": ["."]},
    {"place": "alphabet", "context": "c", "tag": "c", "task": "c c c", "steps": ["."]}
    ]

    placeholders = {
        "duration": ["20", "30", "45"],
        "color": ["red", "blue", "green"],
        "flavor": ["chocolate chip", "peanut butter", "oatmeal raisin"],
        "period": ["monthly", "quarterly", "yearly"],
        "equipment": ["dumbbells", "kettlebells", "resistance bands"],
        "time": ["15", "30", "45"],
        "herb": ["chamomile", "lavender", "mint"],
        "item": ["photo frame", "jewelry box", "birdhouse"],
        "material": ["wood", "cardboard", "metal"],
        "instrument": ["guitar", "piano", "violin"],
        "topic": ["market trends", "new technologies", "consumer behavior"],
        "plant": ["tomatoes", "roses", "lavender"],
        "event": ["team meeting", "product launch", "workshop"],
        "book": ["a novel", "a biography", "a self-help guide"]
    }

    return tasks, placeholders
