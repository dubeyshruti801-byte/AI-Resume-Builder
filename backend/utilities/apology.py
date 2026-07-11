from utilities.sanitizer import sanitize_text


def apology_note(name: str | None) -> str:
    friendly = sanitize_text(name) if name else "friend"
    return (
        f"Hey {friendly},\n\n"
        "You’ve reached the limit of 3 free PDF downloads. We totally get how exciting and stressful job hunts can be. "
        "We’re cheering for you! 💼✨\n\n"
        "If our builder saved you time, consider supporting us to unlock unlimited downloads and premium templates. "
        "Either way, we’re grateful you’re here.\n\n"
        "— With appreciation, The Resume Builder Team ❤️"
    )
