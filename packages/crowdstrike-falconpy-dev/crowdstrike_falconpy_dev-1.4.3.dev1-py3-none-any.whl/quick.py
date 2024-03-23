"""Simple debug logging example."""
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from logging import Logger, getLogger, basicConfig, DEBUG
from falconpy import APIHarness, Detects, Hosts


def consume_arguments() -> Namespace:
    parser = ArgumentParser(description="A quick test harness")
    parser.add_argument("-u",
                        "--debug_uber",
                        help="Enable debug logging for the Uber Class",
                        required=False,
                        default=False,
                        action="store_true"
                        )
    parser.add_argument("-c",
                        "--debug_service_class",
                        help="Enable debug logging for the Service Class",
                        required=False,
                        default=False,
                        action="store_true"
                        )
    parser.add_argument("-m",
                        "--max_records",
                        help="Limit the number of debug records returned in the log",
                        required=False,
                        default=100
                        )
    parser.add_argument("-d",
                        "--dont_sanitize",
                        help="Disable log sanitization (!!! WARNING !!! API keys will be shown)",
                        required=False,
                        default=None,
                        action="store_false", 
                        )
    require = parser.add_argument_group("required arguments")
    require.add_argument("-k",
                        "--falcon_client_id",
                        help="CrowdStrike API client ID",
                        required=True
                        )
    require.add_argument("-s",
                        "--falcon_client_secret",
                        help="CrowdStrike API client secret",
                        required=True
                        )

    return parser.parse_args()

def setup_logging() -> Logger:
    log_util = getLogger("log_testing")
    basicConfig(level=DEBUG, format="%(asctime)s %(levelname)s %(name)s %(message)s")

    return log_util

def uber_auth(cid: str, sec: str, dbg: bool, cnt: int, san: bool) -> APIHarness:
    """Create an instance of the Uber Class and authenticate."""
    return APIHarness(client_id=cid, client_secret=sec, debug=dbg, debug_record_count=cnt, sanitize_log=san)

def detects_auth(auth: APIHarness, rmax: int) -> Detects:
    """Connect to the Detects Service Class using Credential Authentication.

    Allow for a custom debug record maximum count.
    """
    return Detects(auth_object=auth, debug_record_count=int(rmax)/2)

def hosts_auth(auth: APIHarness, dbg: bool, san: bool) -> Hosts:
    """Connect to the Hosts Service Class using Credential Authentication with a custom timeout."""
    return Hosts(auth_object=auth, timeout=30, debug=dbg, sanitize_log=san)

def run_logging_test(arguments: Namespace, logger: Logger):

    logger.debug("Start debug run")
    uber = uber_auth(arguments.falcon_client_id,
                    arguments.falcon_client_secret,
                    arguments.debug_uber,
                    arguments.max_records,
                    arguments.dont_sanitize
                    )
    # Query for detections
    uber.command("QueryDetects", limit=5000)
    # Retrieve the details for one device
    uber.command("GetDeviceDetails",
                 ids=uber.command("QueryDevicesByFilterScroll", limit=1)["body"]["resources"]
                 )
    logger.debug("Starting Service Class testing")
    # Since the Uber Class inherits from the FalconInterface class we can
    # use Credential Authentication to access different Service Classes.

    detects = detects_auth(uber, arguments.max_records)
    # Query for detections
    print(type(detects.auth_object))
    detects.query_detects(limit=5000)
#    hosts = hosts_auth(uber, arguments.debug_service_class, arguments.dont_sanitize)
    hosts = Hosts(client_id=arguments.falcon_client_id, client_secret=arguments.falcon_client_secret, debug=arguments.debug_service_class, sanitize_log=arguments.dont_sanitize)
    # Retrieve the details for one device
    hosts.get_device_details(hosts.query_devices_by_filter_scroll(limit=1)["body"]["resources"])
    # Trigger a logout. Since our Service Class shares the auth_object with
    # all objects created, this will effectively log us out entirely.
    hosts.logout()
    logger.debug("End debug run")


if __name__ == "__main__":
    run_logging_test(consume_arguments(), setup_logging())