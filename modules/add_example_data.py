from actionable_builder.modules.create_database import add_task
from actionable_builder.modules.create_database import add_placeholders

def add_example_data():
    # Task 1
    task = {
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
    }
    add_task(task)

    # Task 2
    task = {
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
    }
    add_task(task)

    # Task 3
    task = {
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
    }
    add_task(task)

    # Task 4
    task = {
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
    }
    add_task(task)

    # Task 5
    task = {
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
    }
    add_task(task)

    # Task 6
    task = {
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
    }
    add_task(task)

    # Task 7
    task = {
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
    }
    add_task(task)

    # Task 8
    task = {
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
    }
    add_task(task)

    # Task 9
    task = {
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
    }
    add_task(task)

    # Task 10
    task = {
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
    }
    add_task(task)

    # Task 11
    task = {
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
    }
    add_task(task)

    # Task 12
    task = {
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
    }
    add_task(task)

    # Task 13
    task = {
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
    }
    add_task(task)

    # Task 14
    task = {
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
    }
    add_task(task)

    # Task 15
    task = {
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
    }
    add_task(task)

    # Task 16
    task = {
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
    }
    add_task(task)

    # Task 17
    task = {
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
    }
    add_task(task)

    # Task 18
    task = {
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
    }
    add_task(task)

    # Task 19
    task = {
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
    }
    add_task(task)

    # Task 20
    task = {
        "place": "home",
        "context": "recreate",
        "tag": "reading",
        "task": "read %book% for %time% minutes",
        "steps": [
            "find a quiet and comfortable reading spot",
            "set a timer for %time% minutes",
            "focus on reading and understanding %book%",
            "take brief notes if necessary",
            "store the book safely after reading"
        ]
    }
    add_task(task)

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

    add_placeholders(placeholders)
