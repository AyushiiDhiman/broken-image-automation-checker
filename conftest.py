def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default=None,
        help="Target URL to test for broken images."
    )
