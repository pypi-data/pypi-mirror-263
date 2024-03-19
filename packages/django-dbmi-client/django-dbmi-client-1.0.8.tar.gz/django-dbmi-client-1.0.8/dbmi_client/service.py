import dns.resolver
from furl import furl
from dbmi_client.settings import dbmi_settings
import logging
logger = logging.getLogger(dbmi_settings.LOGGER_NAME)

SERVICE_DISCOVERY_NAMESPACE_KEY = "SERVICE_DISCOVERY_NAMESPACE"


class Service(object):
    """
    A class to facilitate service discovery and requests between service
    containers.
    """
    @classmethod
    def resolve(cls, service):
        """
        Resolves the URL for a container running the service using service
        discovery and SRV records.
        :param service: The service discovery name of the service to query for
        :type service: str
        :return: A list of records, sorted by priority then weight
        :rtype: list
        """
        # Fetch service name and service namespace
        service_namespace = dbmi_settings[SERVICE_DISCOVERY_NAMESPACE_KEY]

        # Resolve
        records = []
        for srv in dns.resolver.resolve(f"{service}.{service_namespace}", "SRV"):

            # Get hostname and port and priority
            records.append({
                "host": str(srv.target).rstrip("."),
                "port": srv.port,
                "priority": srv.priority,
                "weight": srv.weight,
            })

        # Sort by priority then weight
        return sorted(records, key=lambda d: (d["priority"], -d["weight"]))

    @classmethod
    def get_service_url(cls, service):
        """
        Resolves service discovery DNS records and returns the top-priority
        URL for the given service.

        :param service: The name of the service to get the URL for
        :type service: str
        :returns: The priority URL for the given service
        :rtype: str
        """
        # Resolve and get the first record
        record = next(iter(Service.resolve(service=service)))

        # Build URL
        if record["port"] == 443:
            url = furl(f"https://{record['host']}")
        elif record["port"] == 80:
            url = furl(f"http://{record['host']}")
        else:
            url = furl(f"http://{record['host']}:{record['port']}")

        return url.url
