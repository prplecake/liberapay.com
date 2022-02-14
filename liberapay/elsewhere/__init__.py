"""This subpackage contains functionality for working with accounts elsewhere.
"""

def _import():
    from .bitbucket import Bitbucket  # noqa
    from .facebook import Facebook  # noqa
    from .github import GitHub  # noqa
    from .gitlab import GitLab  # noqa
    from .google import Google  # noqa
    from .linuxfr import LinuxFr  # noqa
    from .mastodon import Mastodon  # noqa
    from .openstreetmap import OpenStreetMap  # noqa
    from .pleroma import Pleroma  # noqa
    from .sourcehut import Sourcehut #noqa
    from .twitch import Twitch  # noqa
    from .twitter import Twitter  # noqa
    from .youtube import Youtube  # noqa
    return list(locals().values())

CLASSES = _import()
