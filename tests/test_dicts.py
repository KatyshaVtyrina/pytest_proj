from utils.dicts import get_val


def test_get_val():
    data = {"vcs": "mercurial"}
    assert get_val(data, "vcs") == "mercurial"
    assert get_val({}, "vcs", "git") == "git"
    assert get_val(data, "key", "git") == "git"
