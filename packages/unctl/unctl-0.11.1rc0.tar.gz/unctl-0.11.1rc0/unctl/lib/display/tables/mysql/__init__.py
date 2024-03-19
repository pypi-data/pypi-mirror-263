import textwrap

from colorama import Fore, Style

from unctl.constants import CheckProviders
from unctl.lib.display.tables.base import BaseTable
from unctl.lib.display.tables.constants import UNSET, TableNames
from unctl.lib.display.tables.decorators import header_processor

__all__ = ["MySQLSortedByObject", "MySQLSortedByChecks"]


class MySQLSortedByObject(
    BaseTable, providers=[CheckProviders.MySQL], name=TableNames.SORTED_BY_OBJECT
):
    HEADERS = [
        "Resource Name",
        "Check Title",
        "Status",
        "Severity",
        "LLM Explanation",
        "Status Extended",
    ]

    @classmethod
    def configure(
        cls, results, display, context=None, initial_table=None, divider=False
    ):
        sorted_results = sorted(results, key=lambda check: check.resource_name)
        return super().configure(
            sorted_results, display, context, initial_table, divider
        )

    @header_processor("Resource Name")
    def get_resource_name(self, check, context):
        return textwrap.fill(check.resource_name, width=20)

    @header_processor("Check Title")
    def get_check_title(self, check, context):
        return textwrap.fill(check.check_metadata.CheckTitle, width=30)

    @header_processor("Status")
    def get_check_status(self, check, context):
        return check.status.center(10)

    @header_processor("Severity")
    def get_check_severity(self, check, context):
        return check.check_metadata.Severity.center(10)

    @header_processor("LLM Explanation")
    def get_llm_explanation(self, check, context):
        # if LLM summary present, that means that the `LLM Explanation`
        # will be available on the table,
        # and we don't need to set `Status Extended` header later,
        # so that step will be skipped
        if not (context["llm_summary"] and check.llm_summary is not None):
            return UNSET
        return textwrap.fill("🧠 " + check.llm_summary, width=60)

    @header_processor("Status Extended")
    def get_check_status_extended(self, check, context):
        # if LLM summary present, that means that the `LLM Explanation`
        # has been already set,
        # and we don't need to set `Status Extended` at this point
        if context["llm_summary"] and check.llm_summary is not None:
            return UNSET
        return textwrap.fill(check.status_extended, width=60)


class MySQLSortedByChecks(
    BaseTable, providers=[CheckProviders.MySQL], name=TableNames.SORTED_BY_CHECKS
):
    HEADERS = [
        "Resource Name",
        "Status",
        "Severity",
        "LLM Explanation",
        "Status Extended",
    ]

    # this is unique to this table, only part that the base table respects is `HEADERS`
    WIDTH_CONFIG = {
        "Resource Name": 30,
        "Status": 10,
        "Severity": 10,
        "Status Extended": 70,
        "LLM Explanation": 70,
    }

    @classmethod
    def configure(
        cls, results, display, context=None, initial_table=None, divider=False
    ):
        instance = super().configure(results, display, context, initial_table, divider)
        instance.initial_table._max_width = cls.WIDTH_CONFIG
        return instance

    @header_processor("Resource Name")
    def get_resource_name(self, check, context):
        resource_name_wrapped = textwrap.fill(
            check.resource_name, width=self.WIDTH_CONFIG.get("Resource Name", 0)
        )
        resource_name_wrapped = self.display.center_content(
            resource_name_wrapped, self.WIDTH_CONFIG.get("Resource Name", 0)
        )
        return resource_name_wrapped

    @header_processor("Status")
    def get_check_status(self, check, context):
        status = Fore.RED + check.status + Style.RESET_ALL
        status = self.display.center_content(status, self.WIDTH_CONFIG.get("Status", 0))
        return status

    @header_processor("Severity")
    def get_check_severity(self, check, context):
        severity_color = (
            Fore.RED
            if check.check_metadata.Severity == "Critical"
            else (
                Fore.YELLOW if check.check_metadata.Severity == "Severe" else Fore.WHITE
            )
        )
        severity = severity_color + check.check_metadata.Severity + Style.RESET_ALL
        severity = self.display.center_content(
            severity, self.WIDTH_CONFIG.get("Severity", 0)
        )
        return severity

    @header_processor("LLM Explanation")
    def get_llm_explanation(self, check, context):
        # if LLM summary present, that means that the `LLM Explanation`
        # will be available on the table,
        # and we don't need to set `Status Extended` header later,
        # so that step will be skipped
        if not (context["llm_summary"] and check.llm_summary is not None):
            return UNSET
        return self._wrap_extended_status("🧠 " + check.llm_summary)

    @header_processor("Status Extended")
    def get_check_status_extended(self, check, context):
        # if LLM summary present, that means that the `LLM Explanation`
        # has been already set,
        # and we don't need to set `Status Extended` at this point
        if context["llm_summary"] and check.llm_summary is not None:
            return UNSET
        return self._wrap_extended_status(check.status_extended)

    def _wrap_extended_status(self, status):
        # Wrap the content based on max widths
        status_extended_wrapped = textwrap.fill(
            status, width=self.WIDTH_CONFIG.get("Status Extended", 0)
        )
        status_extended_wrapped = self.display.center_content(
            status_extended_wrapped, self.WIDTH_CONFIG.get("Status Extended", 0)
        )
        return status_extended_wrapped
