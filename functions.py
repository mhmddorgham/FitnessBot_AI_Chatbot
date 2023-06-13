# A function that takes weight , height and age, and return BMI category
def calculate_bmi(weight, height, age):
    bmi = weight / (height * height)

    if bmi < 19:
        bmi_category = "Underweight"
        response = "Based on your BMI, it seems like you're underweight. I can help you create a personalized diet plan and workout routine to help you gain weight in a healthy way."
    elif bmi < 25:
        bmi_category = "Healthy Weight"
        response = "Congratulations! Based on your BMI, it seems like you're at a healthy weight. I can help you maintain this weight and improve your overall fitness with a personalized diet and workout plan."
    elif bmi < 30:
        bmi_category = "Overweight"
        response = "Based on your BMI, it seems like you're overweight. I can help you create a personalized diet plan and workout routine to help you achieve your weight loss goals in a healthy way."
    else:
        bmi_category = "Obese"
        response = "Based on your BMI, it seems like you're obese. I can help you create a personalized diet plan and workout routine to help you achieve your weight loss goals in a healthy way. It's important to start making changes as soon as possible to improve your health."

    return [response, bmi_category]

# A function that creates Workout plan based on user BMI and his/ her fitness level


def create_workout_plan_with_BMI(fitness_level, bmi_category):
    print(bmi_category)
    response = ""
    if bmi_category.lower() == "underweight":
        if fitness_level.lower() == 'beginner':
            response = "Based on your BMI, It's important to focus on gaining weight in a healthy way. As a beginner, I recommend you following this workout plan: "

            response += """
            
            1.	Resistance Training: 3 days per week (Monday, Wednesday, and Friday)
                •	Bodyweight squats: 3 sets of 10 reps
                •	Push-ups: 3 sets of 10 reps
                •	Dumbbell curls: 3 sets of 10 reps
                •	Dumbbell shoulder press: 3 sets of 10 reps

            2.	Cardiovascular Exercise: 2-3 days per week (Tuesday, Thursday, and Saturday)
                •	20-30 minutes of low-intensity cardio, such as walking, cycling, or swimming

            """
        elif fitness_level.lower() == 'intermediate':
            response = "Based on your BMI, It's important to focus on gaining weight in a healthy way. As an intermediate, I recommend you following this workout plan: "
            response += """
            
            1.	Resistance Training: 4 days per week (Monday, Tuesday, Thursday, and Friday)
                •	Barbell squats: 3 sets of 8 reps
                •	Barbell bench press: 3 sets of 8 reps
                •	Barbell rows: 3 sets of 8 reps
                •	Barbell shoulder press: 3 sets of 8 reps
                •	Barbell curls: 3 sets of 8 reps
                •	Tricep pushdowns: 3 sets of 8 reps

            2.	Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)
                •	30-40 minutes of moderate-intensity cardio, such as running, cycling, or swimming

            """

        elif fitness_level.lower() == 'advanced':
            response = "Based on your BMI, It's important to focus on gaining weight in a healthy way. As an advanced , I recommend you following this workout plan:"
            response += """
             
            1.	Resistance Training: 5 days per week (Monday, Tuesday, Wednesday, Thursday, and Friday)
                •	Barbell squats: 4 sets of 8 reps
                •	Barbell bench press: 4 sets of 8 reps
                •	Barbell rows: 4 sets of 8 reps
                •	Barbell shoulder press: 4 sets of 8 reps
                •	Barbell curls: 4 sets of 8 reps
                •	Tricep pushdowns: 4 sets of 8 reps

            2.	Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)
                •	40-60 minutes of high-intensity cardio, such as sprinting, cycling, or swimming

            """
    elif bmi_category.lower() == "healthy weight":
        if fitness_level.lower() == 'beginner':
            response = "Based on your BMI, It's important to focus on mainainting your weight to be a healthy person. As a beginner, I recommend you following this workout plan: "
            response += """
            
            1.	Resistance Training: 3 days per week (Monday, Wednesday, and Friday)
                •	Bodyweight squats: 4 sets of 10 reps
                •	Push-ups: 3 sets of 20 reps
                •	Dumbbell curls: 3 sets of 20 reps
                •	Dumbbell shoulder press: 3 sets of 20 reps

            2.	Cardiovascular Exercise: 2-3 days per week (Tuesday, Thursday, and Saturday)
                •	20-30 minutes of low-intensity cardio, such as walking, cycling, or swimming

            """
        elif fitness_level.lower() == 'intermediate':
            response = " Based on your BMI, It's important to focus on mainainting your weight to be a healthy person. As an intermediate, I recommend you following this workout plan: "
            response += """
           
            1.	Resistance Training: 4 days per week (Monday, Tuesday, Thursday, and Friday)
                •	Barbell squats: 4 sets of 8 reps
                •	Barbell bench press: 4 sets of 8 reps
                •	Barbell rows: 4 sets of 8 reps
                •	Barbell shoulder press: 4 sets of 8 reps
                •	Barbell curls: 4 sets of 8 reps
                •	Tricep pushdowns: 4 sets of 8 reps

            2.	Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)
                •	30-40 minutes of moderate-intensity cardio, such as running, cycling, or swimming

            """

        elif fitness_level.lower() == 'advanced':
            response = "Based on your BMI, It's important to focus on mainainting your weight to be a healthy person. As an advanced , I recommend you following this workout plan: "
            response += """
            
            1.	Resistance Training: 5 days per week (Monday, Tuesday, Wednesday, Thursday, and Friday)
                •	Barbell squats: 4 sets of 8 reps
                •	Barbell bench press: 4 sets of 8 reps
                •	Barbell rows: 4 sets of 8 reps
                •	Barbell shoulder press: 4 sets of 8 reps
                •	Barbell curls: 4 sets of 8 reps
                •	Tricep pushdowns: 4 sets of 8 reps
                •	Push-ups: 3 sets of 20 reps


            2.	Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)
                •	40-60 minutes of high-intensity cardio, such as sprinting, cycling, or swimming

            """

    elif bmi_category.lower() == "overweight":
        if fitness_level.lower() == 'beginner':
            response = "Based on your BMI, It's important to focus on losing weight in a healthy way. As a beginner, I recommend you following this workout plan: "
            response += """
            
            1.	Circuit Training: 2-3 days per week (Tuesday, Thursday, and optionally on Saturday)
                •	3 circuits of 10-12 reps each of the following exercises:
                •	Bodyweight squats
                •	Push-ups
                •	Dumbbell rows
                •	Dumbbell shoulder press
                •	Plank

            2.	Cardiovascular Exercise: 3-4 days per week (Tuesday, Thursday, and Saturday)
                •	20-30 minutes of low-intensity cardio, such as walking, cycling, or elliptical machine.

            """
        elif fitness_level.lower() == 'intermediate':
            response = "Based on your BMI, It's important to focus on losing weight in a healthy way. As an intermediate, I recommend you following this workout plan: "
            response += """
            1.	Resistance Training: 3-4 days per week (Monday, Tuesday, Thursday,and optionally on Friday )
                •	Barbell squats: 3 sets of 10 reps
                •	Barbell bench press: 3 sets of 10 reps
                •	Dumbbell rows: 3 sets of 10 reps
                •	Dumbbell shoulder press: 3 sets of 10 reps
                •	Plank: 3 sets of 30 seconds


            2.	Cardiovascular Exercise: 4-5 days per week (Monday, Tuesday, Thursday, Friday, and optionally on Sunday)
                •	30-40 minutes of moderate-intensity cardio, such as jogging on a treadmill, cycling, or using the elliptical machine

            """

        elif fitness_level.lower() == 'advanced':
            response = "Based on your BMI, It's important to focus on losing weight in a healthy way. As an advanced , I recommend you following this workout plan: "
            response += """
            
            1.	Strength Training: 4-5 days per week (Tuesday,Wednesday,Thursday, Saturday, and optionally on Sunday)
                •	Barbell squats: 4 sets of 8 reps
                •	Barbell bench press: 4 sets of 8 reps
                •	Barbell rows: 4 sets of 8 reps
                •	Barbell shoulder press: 4 sets of 8 reps
                •	Barbell curls: 4 sets of 8 reps
                •	Deadlifts: 4 sets of 8 reps


            2.	Cardiovascular Exercise: 5-6 days per week (Monday, Tuesday, Wednesday, Thursday, Friday, and optionally on Sunday)
                •	45-60 minutes of high-intensity cardio, such as running on a treadmill, cycling, or using the rowing machine

            """

    elif bmi_category.lower() == "obese":
        if fitness_level.lower() == 'beginner':
            response = " Based on your BMI, It's important to focus on seriously losing weight in a healthy way. As a beginner, I recommend you following this workout plan: "
            response += """
           
            1.	Resistance Training: 2-3 days per week (Tuesday, Thursday, and optionally on Saturday)
                •	3 sets of 12-15 reps each of the following exercises:
                •	Leg press machine
                •	Chest press machine
                •	Lat pulldown machine
                •	Seated row machine
                •	Shoulder press machine


            2.	Cardiovascular Exercise: 3-4 days per week (Tuesday, Thursday, and Saturday)
                •	20-30 minutes of low-intensity cardio, such as walking, cycling, or elliptical machine.

            """
        elif fitness_level.lower() == 'intermediate':
            response = "Based on your BMI, It's important to focus on seriously losing weight in a healthy way. As an intermediate, I recommend you following this workout plan: "
            response += """
            
            1.	Resistance Training: 3-4 days per week (Monday, Tuesday, Thursday,and optionally on Friday )                
                •	Dumbbell squats: 3 sets of 12 reps
                •	Dumbbell bench press: 3 sets of 12 reps
                •	Dumbbell rows: 3 sets of 12 reps
                •	Dumbbell shoulder press: 3 sets of 12 reps
                •	Plank: 3 sets of 30 seconds

            2.	Cardiovascular Exercise: 4-5 days per week (Monday, Tuesday, Thursday, Friday, and optionally on Sunday)
                •	30-40 minutes of moderate-intensity cardio, such as jogging on a treadmill, cycling, or using the elliptical machine

            """

        elif fitness_level.lower() == 'advanced':
            response = "Based on your BMI, It's important to focus on seriously losing weight in a healthy way. As an advanced , I recommend you following this workout plan: "
            response += """
            
            1.	Resistance Training: 4-5 days per week (Monday, Tuesday, Wednesday, Thursday, and optionally on Friday)
                •	Barbell squats: 4 sets of 8 reps
                •	Barbell bench press: 4 sets of 8 reps
                •	Barbell rows: 4 sets of 8 reps
                •	Barbell shoulder press: 4 sets of 8 reps
                •	Crunches: 3 sets of 1 minute

            2.	Cardiovascular Exercise: 5-6 days per week (Monday, Tuesday, Wednesday, Thursday, Friday, and optionally on Sunday)
                •	45-60 minutes of high-intensity cardio, such as running on a treadmill, cycling, or using the rowing machine

            """

    return response

# A function that creates diet plan based on user BMI and his/ her fitness level


def create_diet_plan_with_BMI(fitness_level, bmi_category):
    if bmi_category.lower() == "underweight":
        if fitness_level.lower() == "beginner":
            # Sample diet plan to gain weight for a beginner person who is underweight
            return "Here is a sample diet plan to gain weight for a beginner person who is underweight:\n\n Breakfast: Oatmeal with milk, banana, and walnuts. \n Snack: Greek yogurt with mixed berries and honey. \n Lunch: Grilled chicken wrap with avocado, tomato, and spinach. \n Snack: Hummus with carrots and whole-grain crackers. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as broccoli and sweet potato). \n Snack: Apple slices with almond butter."
        elif fitness_level.lower() == "intermediate":
            # Sample diet plan to gain weight for an intermediate person who is underweight
            return "Here is a sample diet plan to gain weight for an intermediate person who is underweight:\n\n Breakfast: Whole-grain toast with avocado and a boiled egg. \n Snack: Mixed nuts and dried fruit. \n Lunch: Grilled chicken breast with brown rice and roasted vegetables (such as carrots and zucchini). \n Snack: Greek yogurt with mixed berries and honey. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as broccoli and sweet potato). \n Snack: Apple slices with almond butter."
        elif fitness_level.lower() == "advanced":
            # Sample diet plan to gain weight for an advanced person who is underweight
            return "Here is a sample diet plan to gain weight for an advanced person who is underweight:\n\n Breakfast: Avocado toast with smoked salmon and a poached egg. \n Snack: Protein shake with mixed berries and almond milk. \n Lunch: Grilled chicken breast with quinoa and roasted vegetables (such as broccoli, cauliflower, and sweet potato). \n Snack: Greek yogurt with mixed nuts and honey. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as broccoli, cauliflower, and sweet potato). \n Snack: Apple slices with almond butter."
    elif bmi_category.lower() == "healthy weight":
        if fitness_level.lower() == "beginner":
            # Sample diet plan to maintain weight for a beginner person who has a healthy weight
            return "Here is a sample diet plan to maintain weight for a beginner person who has a healthy weight:\n\n Breakfast: Greek yogurt with mixed berries and honey. \n Snack: Apple slices with almond butter. \n Lunch: Grilled chicken breast with roasted vegetables (such as broccoli, carrots, and zucchini) and brown rice. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with roasted sweet potatoes and green beans. \n Snack: Mixed nuts and dried fruit."
        elif fitness_level.lower() == "intermediate":
            # Sample diet plan to maintain weight for an intermediate person who has a healthy weight
            return "Here is a sample diet plan to maintain weight for an intermediate person who has a healthy weight:\n\n Breakfast: Scrambled eggs with spinach and whole-grain toast. \n Snack: Greek yogurt with mixed nuts and honey. \n Lunch: Grilled chicken salad with mixed greens, tomatoes, and vinaigrette dressing. \n Snack: Apple slices with almond butter. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers). \n Snack: Carrots and hummus."
        elif fitness_level.lower() == "advanced":
            # Sample diet plan to maintain weight for an advanced person who has a healthy weight
            return "Here is a sample diet plan to maintain weight for an advanced person who has a healthy weight:\n\n Breakfast: Quinoa breakfast bowl with avocado, poached egg, and mixed greens. \n Snack: Protein shake with mixed berries and almond milk. \n Lunch: Grilled chicken breast with mixed vegetables (such as bell peppers, onions, and mushrooms) and sweet potato. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers). \n Snack: Mixed nuts and dried fruit."
    elif bmi_category.lower() == "overweight":
        if fitness_level.lower() == "beginner":
            # Sample diet plan to lose weight for a beginner person who is overweight
            return "Here is a sample diet plan to lose weight for a beginner person who is overweight:\n\n Breakfast: Greek yogurt with mixed berries and honey. \n Snack: Apple slices with almond butter. \n Lunch: Grilled chicken breast with roasted vegetables (such as broccoli, carrots, and zucchini) and brown rice. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with roasted sweet potatoes and green beans. \n Snack: Mixed nuts and dried fruit."
        elif fitness_level.lower() == "intermediate":
            # Sample diet plan to lose weight for an intermediate person who is overweight
            return "Here is a sample diet plan to lose weight for an intermediate person who is overweight:\n\n Breakfast: Scrambled eggs with spinach and whole-grain toast. \n Snack: Greek yogurt with mixed nuts and honey. \n Lunch: Grilled chicken salad with mixed greens, tomatoes, and vinaigrette dressing. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers). \n Snack: Apple slices with almond butter."
        elif fitness_level.lower() == "advanced":
            # Sample diet plan to lose weight for an advanced person who is overweight
            return "Here is a sample diet plan to lose weight for an advanced person who is overweight:\n\n Breakfast: Quinoa breakfast bowl with avocado, poached egg, and mixed greens. \n Snack: Protein shake with mixed berries and almond milk. \n Lunch: Grilled chicken breast with mixed vegetables (such as bell peppers, onions, and mushrooms) and sweet potato. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers). \n Snack: Mixed nuts and dried fruit."
    elif bmi_category.lower() == "obese":
        if fitness_level.lower() == "beginner":
            # Sample diet plan to seriously lose weight for a beginner person who is obese
            return "Here is a sample diet plan to seriously lose weight for a beginner person who is obese:\n\n Breakfast: Greek yogurt with mixed berries and honey. \n Snack: Apple slices with almond butter. \n Lunch: Grilled chicken breast with mixed vegetables (such as broccoli, carrots, and zucchini) and brown rice. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with roasted sweet potatoes and green beans. \n Snack: Mixed nuts and dried fruit."
        elif fitness_level.lower() == "intermediate":
            # Sample diet plan to seriously lose weight for an intermediate person who is obese
            return "Here is a sample diet plan to seriously lose weight for an intermediate person who is obese:\n\n Breakfast: Scrambled eggs with spinach and whole-grain toast. \n Snack: Greek yogurt with mixed nuts and honey. \n Lunch: Grilled chicken salad with mixed greens, tomatoes, and vinaigrette dressing. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers). \n Snack: Apple slices with almond butter."
        elif fitness_level.lower() == "advanced":
            # Sample diet plan to seriously lose weight for an advanced person who is obese
            return "Here is a sample diet plan to seriously lose weight for an advanced person who is obese:\n\n Breakfast: Quinoa breakfast bowl with avocado, poached egg, and mixed greens. \n Snack: Protein shake with mixed berries and almond milk. \n Lunch: Grilled chicken breast with mixed vegetables (such as bell peppers, onions, and mushrooms) and sweet potato. \n Snack: Carrots and hummus. \n Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers). \n Snack: Mixed nuts and dried fruit."


#  A function that creates general workoout plan without calculating BMI
def create_workout_plan(fitness_level):
    if fitness_level.lower() == 'beginner':
        response = "Great! As a beginner, it's important to start with simple exercises and gradually build up your strength and endurance.  \n Remember, it is best to calculate your BMI and know your body condition so that I can give you the right exercise plan for you. \n For now, I recommend starting with bodyweight exercises such as push-ups, squats, and lunges, and doing a combination of cardio and strength training for at least 30 minutes a day, five days a week. Here's a sample workout plan you can follow:\n\nMonday: 10 push-ups, 10 squats, 10 lunges (each leg), 10 minutes of jogging\nTuesday: Rest day\nWednesday: 15 push-ups, 15 squats, 15 lunges (each leg), 15 minutes of jumping jacks\nThursday: Rest day\nFriday: 20 push-ups, 20 squats, 20 lunges (each leg), 20 minutes of cycling\nSaturday: Rest day\nSunday: 30 minutes of walking or hiking\n\nRemember to listen to your body and take rest days as needed. As you get stronger, you can gradually increase the intensity and duration of your workouts."
    elif fitness_level.lower() == 'intermediate':
        response = "Awesome! As an intermediate exerciser, you've already built a foundation of strength and endurance. \n Remember, it is best to calculate your BMI and know your body condition so that I can give you the right exercise plan for you. \n I recommend continuing with a combination of cardio and strength training, and gradually increasing the intensity and duration of your workouts. Here's a sample workout plan you can follow:\n\nMonday: 20 push-ups, 20 squats, 20 lunges (each leg), 20 minutes of jogging\nTuesday: Rest day\nWednesday: 30 push-ups, 30 squats, 30 lunges (each leg), 30 minutes of jumping jacks\nThursday: Rest day\nFriday: 40 push-ups, 40 squats, 40 lunges (each leg), 40 minutes of cycling\nSaturday: Rest day\nSunday: 60 minutes of walking or hiking\n\nRemember to challenge yourself but also listen to your body and take rest days as needed. You can also consider adding new exercises or activities to keep your workouts interesting and varied."
    elif fitness_level.lower() == 'advanced':
        response = "Impressive! As an advanced exerciser, you have a high level of fitness and strength. \n Remember, it is best to calculate your BMI and know your body condition so that I can give you the right exercise plan for you. \n I recommend continuing to challenge yourself with a combination of high-intensity cardio and strength training, and incorporating new exercises or activities to keep your workouts varied. Here's a sample workout plan you can follow:\n\nMonday: 30 push-ups, 30 squats, 30 lunges (each leg), 30 minutes of high-intensity interval training (HIIT)\nTuesday: Rest day\nWednesday: 40 push-ups, 40 squats, 40 lunges (each leg), 40 minutes of cycling or running\nThursday: Rest day\nFriday: 50 push-ups, 50 squats, 50 lunges (each leg), 50 minutes of swimming or rowing\nSaturday: Rest day\nSunday: 60 minutes of hiking or rock climbing\n\nRemember to always warm up before exercising and cool down after, and to listen to your body and take rest days as needed. You can also consider working with a personal trainer to help you set and achieve new fitness goals."
    else:
        response = "I'm sorry, I didn't understand. Can you please enter beginner, intermediate, or advanced to indicate your fitness level?"

    return response


#  A function that creates general diet plan without calculating BMI
def create_diet_plan(fitness_level):
    if fitness_level.lower() == 'beginner':
        response = "Great! As a beginner, it's important to start with small, manageable changes to your diet. \n Remember, it is best to calculate your BMI and know your body condition so that I can give you the right diet plan for you. \n Here are some tips to get you started:\n\n1. Focus on whole, nutrient-dense foods such as fruits, vegetables, whole grains, lean protein, and healthy fats.\n2. Drink plenty of water throughout the day to stay hydrated.\n3. Avoid processed foods and sugary drinks.\n4. Plan your meals and snacks ahead of time to avoid impulsive eating.\n5. Consider working with a registered dietitian to help you set and achieve your goals.\n\nHere's a sample meal plan you can follow:\n\nBreakfast: Greek yogurt with berries and honey\nSnack: Apple slices with almond butter\nLunch: Grilled chicken salad with mixed greens, tomatoes, and avocado\nSnack: Carrot sticks with hummus\nDinner: Baked salmon with roasted vegetables\n\nRemember to listen to your body and make changes as needed. Small, sustainable changes are more effective than drastic ones that are difficult to maintain."
    elif fitness_level.lower() == 'intermediate':
        response = "Great! As an intermediate dieter, you already have some experience with healthy eating habits. \n Remember, it is best to calculate your BMI and know your body condition so that I can give you the right diet plan for you. \n Here are some tips to take your diet to the next level:\n\n1. Focus on whole, nutrient-dense foods such as fruits, vegetables, whole grains, lean protein, and healthy fats.\n2. Consider tracking your food intake to ensure you're meeting your macronutrient and calorie goals.\n3. Plan your meals and snacks ahead of time to avoid impulsive eating.\n4. Try new healthy recipes to keep your meals interesting and varied.\n5. Consider working with a registered dietitian to help you set and achieve your goals.\n\nHere's a sample meal plan you can follow based on your goals:\n\nGoal: Weight loss\nBreakfast: Oatmeal with berries and almond milk\nSnack: Greek yogurt with chopped nuts\nLunch: Grilled chicken breast with roasted vegetables\nSnack: Apple slices with peanut butter\nDinner: Baked salmon with quinoa and steamed broccoli\n\nGoal: Muscle gain\nBreakfast: Scrambled eggs with whole wheat toast and avocado\nSnack: Protein shake with banana\nLunch: Grilled chicken breast with sweet potato and green beans\nSnack: Cottage cheese with pineapple chunks\nDinner: Beef stir-fry with brown rice and mixed vegetables\n\nRemember to listen to your body and make changes as needed. Consistency and balance are key to achieving your goals."
    elif fitness_level.lower() == 'advanced':
        response = "Impressive! As an advanced dieter, you've already developed healthy eating habits. \n Remember, it is best to calculate your BMI and know your body condition so that I can give you the right diet plan for you. \n Here are some tips to maintain your progress and continue achieving your goals:\n\n1. Focus on whole, nutrient-dense foods such as fruits, vegetables, whole grains, lean protein, and healthy fats.\n2. Consider tracking your food intake to ensure you're meeting your macronutrient and calorie goals.\n3. Plan your meals and snacks ahead of time to avoid impulsive eating.\n4. Try new healthy recipes to keep your meals interesting and varied.\n5. Consider periodic refeeds or cheat meals to help you stay on track and avoid feeling deprived.\n\nRemember to listen to your body and make changes as needed. Consistency and balance are key to maintaining your progress and achieving your goals."
    else:
        response = "I'm sorry, I didn't understand. Can you please enter beginner, intermediate, or advanced to indicate your fitness level?"

    return response
