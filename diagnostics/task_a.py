"""Task A (cap 15 minutes). Plain Python, no pandas, no imports. Spec: DIAGNOSTIC_TASKS.md."""


def sessionize(timestamps: list[int], gap: int) -> list[tuple[int, int]]:
    """
    timestamps: event times in seconds for ONE user. Not sorted. May contain duplicates.
    A new session starts whenever an event comes MORE than `gap` seconds
    after the event before it in time order.
    Return one (start, end) tuple per session, earliest session first.
    """
    raise NotImplementedError("Task A: write sessionize yourself")
