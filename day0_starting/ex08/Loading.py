import os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating over lst."""
    total = len(lst)
    bar_size = 129
    green = "\033[32m"
    reset = "\033[0m"

    for index, elem in enumerate(lst):
        progress = index + 1
        percent = int(progress / total * 100)
        filled = int(bar_size * progress / total)

        bar = "█" * filled

        line = f"\r{percent}%|{green}{bar}{reset}| {progress}/{total}"
        # os.write only accept bytes, so we use .encode() method
        os.write(1, line.encode())

        # this transform the function into a Generator
        yield elem

    # os.write(1, b"\n")