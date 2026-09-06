subjects = []
while True:
    print("\n===== STUDY PLANNER =====")
    print("1. Add Subject")
    print("2. Add Topic")
    print("3. View Subjects and Topics")
    print("4. Generate Study Plan")
    print("5. Mark Topic Completed")
    print("6. View Progress")
    print("7. Exit")

    choice = input("Enter your choice: ")


    #ADD SUBJECT
    if choice == "1":

        subject_name = input("Enter subject name: ")
        exam_date = input("Enter exam date: ")

        subject = {
            "name": subject_name,
            "exam_date": exam_date,
            "topics": []
        }

        subjects.append(subject)

        print("Subject added successfully!")


    # ---------------- ADD TOPIC ----------------
    elif choice == "2":

        if len(subjects) == 0:
            print("Please add a subject first.")

        else:
            print("\nSubjects:")

            for i in range(len(subjects)):
                print(i + 1, ".", subjects[i]["name"])

            subject_number = int(input("Choose subject number: "))

            if subject_number >= 1 and subject_number <= len(subjects):

                subject = subjects[subject_number - 1]

                topic_name = input("Enter topic name: ")
                difficulty = int(input("Difficulty (1-Easy, 2-Medium, 3-Hard): "))

                topic = {
                    "name": topic_name,
                    "difficulty": difficulty,
                    "completed": False
                }

                subject["topics"].append(topic)

                print("Topic added successfully!")

            else:
                print("Invalid subject number.")


    # VIEW SUBJECTS 
    elif choice == "3":

        if len(subjects) == 0:
            print("No subjects added.")

        else:

            for subject in subjects:

                print("\nSubject:", subject["name"])
                print("Exam Date:", subject["exam_date"])

                if len(subject["topics"]) == 0:
                    print("No topics added.")

                else:

                    for topic in subject["topics"]:

                        if topic["completed"]:
                            status = "Completed"
                        else:
                            status = "Not Completed"

                        print(
                            "-",
                            topic["name"],
                            "| Difficulty:", topic["difficulty"],
                            "|", status
                        )


    # GENERATE STUDY PLAN
    elif choice == "4":

        if len(subjects) == 0:
            print("No subjects available.")

        else:

            print("\n STUDY PLAN ")

            plan_created = False

            # Harder unfinished topics are given priority
            for difficulty_level in [3, 2, 1]:

                for subject in subjects:

                    for topic in subject["topics"]:

                        if (topic["difficulty"] == difficulty_level
                                and topic["completed"] == False):

                            print(
                                subject["name"],
                                "→",
                                topic["name"],
                                "| Difficulty:", topic["difficulty"]
                            )

                            plan_created = True

            if plan_created == False:
                print("Congratulations! All topics are completed.")


    # MARK COMPLETED
    elif choice == "5":

        topic_found = False

        topic_name = input("Enter the topic you completed: ")

        for subject in subjects:

            for topic in subject["topics"]:

                if topic["name"].lower() == topic_name.lower():

                    topic["completed"] = True
                    topic_found = True

                    print("Topic marked as completed!")
                    break

            if topic_found:
                break

        if topic_found == False:
            print("Topic not found.")


    #VIEW PROGRESS
    elif choice == "6":

        if len(subjects) == 0:
            print("No subjects available.")

        else:

            print("\n PROGRESS ")

            for subject in subjects:

                total = len(subject["topics"])
                completed = 0

                for topic in subject["topics"]:

                    if topic["completed"]:
                        completed += 1

                print(
                    subject["name"],
                    ":",
                    completed,
                    "/",
                    total,
                    "topics completed"
                )


    # ---------------- EXIT ----------------
    elif choice == "7":

        print("Thank you for using the Study Planner!")
        break


    else:
        print("Invalid choice. Please try again.")