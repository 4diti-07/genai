def get_prompt(mode, user_input):

    if mode == "1":
        return f"Explain in simple terms:\n{user_input}"

    elif mode == "2":
        return f"Summarize:\n{user_input}"

    elif mode == "3":
        return f"Generate interview questions:\n{user_input}"

    elif mode == "4":
        return f"Make a study plan:\n{user_input}"
    
    elif mode == "5":
        return f"Rewrite the following text professionally:\n\n{user_input}"

    else:
        return user_input