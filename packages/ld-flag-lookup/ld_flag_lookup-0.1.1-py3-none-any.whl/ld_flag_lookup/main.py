import sys
import logging
import click
import ldclient as ldclientSDK  # Aliased to avoid scoped name collision

logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s: %(message)s")

logger = logging.getLogger(__name__)
dict_verbose = {0: logging.ERROR, 1: logging.WARNING, 2: logging.INFO, 3: logging.DEBUG}


@click.command()
@click.option(
    "-f",
    "--flag",
    "flags",
    envvar="LAUNCHDARKLY_FLAGS",
    required=True,
    multiple=True,
    help="The flag key to evaluate",
)
@click.option(
    "--sdk-key",
    envvar="LAUNCHDARKLY_SERVER_KEY",
    default=None,
    help="The LaunchDarkly SDK server key",
)
@click.option("-v", "--verbose", count=True, help="Increase logging verbosity")
def main(flags, sdk_key, verbose):
    logger.setLevel(dict_verbose.get(verbose, logging.DEBUG))
    # Invokes context manager to ensure the SDK shuts down cleanly
    # Python module 'ldclient' __enter__ and __exit__ methods are called.
    # In case of an exception, __exit__ is called before propagating the exception.
    # If analytics events are not delivered, the context properties and flag usage
    # statistics will not appear on your dashboard. In a normal long-running
    # application, the SDK would continue running and events would be delivered
    # automatically in the background.
    ldclientSDK.set_config(ldclientSDK.Config(sdk_key))
    with ldclientSDK.get() as ldclient:
        # Set up logging based on verbosity
        logger.debug("Starting LaunchDarkly evaluation")

        # The SDK starts up the first time ldclient.get() is called
        if ldclient.is_initialized():
            logger.info("SDK successfully initialized!")
        else:
            logger.error("SDK failed to initialize")
            sys.exit()

        # Set up the evaluation context. This context should appear on your
        # LaunchDarkly contexts dashboard soon after you run the demo.
        context = ldclientSDK.Context.builder("example-user-key").name("Sandy").build()

        for flag in flags:
            flag_value = ldclient.variation(flag, context, False)
            print(f"Feature flag '{flag}' is {flag_value} for this context")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
