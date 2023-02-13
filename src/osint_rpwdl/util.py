import progressbar
import sys

def pbar(query, count=None, label="Progres...", disable_progress_bar=False):
    if sys.stdout.isatty() and not disable_progress_bar:
        if count is None:
            if hasattr(query, "count"):
                try:
                    count = query.count()
                except TypeError:
                    count = len(query)
            elif hasattr(query, "__len__"):
                count = len(query)

        return progressbar.progressbar(
            query,
            max_value=count,
            widgets=[
                progressbar.FormatLabel(label),
                " ",
                progressbar.AnimatedMarker(),
                " ",
                progressbar.SimpleProgress(),
                " ",
                progressbar.Timer(),
                " ",
                progressbar.ETA(),
            ],
        )
    else:
        # You're being piped or redirected
        return query

